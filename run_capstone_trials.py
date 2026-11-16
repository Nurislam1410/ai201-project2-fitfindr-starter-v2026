#!/usr/bin/env python3
"""
Run the capstone trial protocol against the deployed service. ← CAPSTONE

    python3 run_capstone_trials.py --label after
    python3 run_capstone_trials.py --url http://localhost:5000 --label local

One trial is the same 24 requests, one at a time, in this order:

    10 normal queries                                  criterion 5
     5 × X-FitFindr-Fault: timeout                     criterion 1
     1 each of timeout / server_error / empty /
       rate_limit                                      criterion 2
     5 malformed bodies                                criterion 4
                                                       (criterion 3: all 24)

It runs three trials back to back, changing nothing in between, and writes
every response to results/capstone_m5_<label>_trials.csv in the same columns as
the before-run. Standard library only. The service has to be running with
FITFINDR_ALLOW_FAULT_HEADER=1. A full run takes about 20 minutes, because a
`timeout` request now waits out the real per-call limit twice.
"""

from __future__ import annotations

import argparse
import csv
import json
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent

HAPPY = [
    "vintage graphic tee under $30",
    "y2k baby tee",
    "cargo pants under $40",
    "denim jacket",
    "graphic tee",
]
FAULT_QUERY = "vintage graphic tee under $30"
BAD = ['{}', '{"query": ""}', '{"query": "   "}', '{"query": 42}', "this is not json"]

COLUMNS = ["trial", "criterion", "fault", "sent", "status", "duration_ms", "client_ms",
           "transient_retries", "rate_limit_retries", "prompt_tokens", "output_tokens",
           "request_id", "message", "at"]


def message_code(err: str | None) -> str:
    if not err:
        return ""
    if "Couldn't reach" in err:
        return "MSG_CONNECTION"
    if "didn't answer" in err or "timed out" in err:
        return "MSG_TIMEOUT"
    if "having trouble" in err:
        return "MSG_TROUBLE"
    if "empty reply" in err:
        return "MSG_EMPTY"
    if "rate limited" in err:
        return "MSG_RATELIMITED"
    if "Send JSON" in err:
        return "MSG_SENDJSON"
    return "OTHER:" + err[:40]


def send(url: str, body: str, fault: str = "") -> dict:
    headers = {"Content-Type": "application/json"}
    if fault:
        headers["X-FitFindr-Fault"] = fault
    req = urllib.request.Request(url.rstrip("/") + "/ask", data=body.encode(), headers=headers, method="POST")
    started = time.perf_counter()
    try:
        with urllib.request.urlopen(req, timeout=240) as resp:
            status, raw = resp.status, resp.read().decode()
    except urllib.error.HTTPError as err:
        status, raw = err.code, err.read().decode()
    except Exception as exc:  # noqa: BLE001 — a client-side failure is a result too
        return {"status": "", "client_ms": round((time.perf_counter() - started) * 1000),
                "body": {"error": f"CLIENT {type(exc).__name__}: {exc}"}}
    try:
        data = json.loads(raw)
    except ValueError:
        data = {"error": "unparsed: " + raw[:80]}
    return {"status": status, "client_ms": round((time.perf_counter() - started) * 1000), "body": data}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", default="https://fitfindr-anl0.onrender.com")
    ap.add_argument("--label", required=True)
    ap.add_argument("--trials", type=int, default=3)
    args = ap.parse_args()

    out = ROOT / "results" / f"capstone_m5_{args.label}_trials.csv"
    out.parent.mkdir(exist_ok=True)

    plan = []
    for q in (HAPPY * 2):
        plan.append((5, "", json.dumps({"query": q})))
    for _ in range(5):
        plan.append((1, "timeout", json.dumps({"query": FAULT_QUERY})))
    for f in ("timeout", "server_error", "empty", "rate_limit"):
        plan.append((2, f, json.dumps({"query": FAULT_QUERY})))
    for raw in BAD:
        plan.append((4, "", raw))

    # Wake it first so the run doesn't start on a sleeping instance.
    try:
        urllib.request.urlopen(args.url.rstrip("/") + "/health", timeout=120).read()
    except Exception as exc:  # noqa: BLE001
        print(f"warning: /health didn't answer: {exc}")

    print(f"started {datetime.now(timezone.utc).isoformat(timespec='seconds')} — writing {out.relative_to(ROOT)}")
    with out.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=COLUMNS)
        w.writeheader()
        for trial in range(1, args.trials + 1):
            for crit, fault, body in plan:
                r = send(args.url, body, fault)
                b = r["body"] if isinstance(r["body"], dict) else {}
                meta = b.get("meta") or {}
                sent = json.loads(body)["query"] if crit != 4 else body
                row = {
                    "trial": trial, "criterion": crit, "fault": fault, "sent": sent,
                    "status": r["status"], "duration_ms": meta.get("duration_ms", ""),
                    "client_ms": r["client_ms"],
                    "transient_retries": meta.get("transient_retries", ""),
                    "rate_limit_retries": meta.get("rate_limit_retries", ""),
                    "prompt_tokens": meta.get("prompt_tokens", ""),
                    "output_tokens": meta.get("output_tokens", ""),
                    "request_id": meta.get("request_id", ""),
                    "message": message_code(b.get("error")),
                    "at": datetime.now(timezone.utc).isoformat(timespec="milliseconds"),
                }
                w.writerow(row)
                fh.flush()
                print(f"trial {trial}  c{crit}  {fault or '-':<12} {row['status']}  "
                      f"{row['duration_ms']:>6} ms  {row['message'] or 'fit card'}")
    print(f"finished {datetime.now(timezone.utc).isoformat(timespec='seconds')}")


if __name__ == "__main__":
    main()
