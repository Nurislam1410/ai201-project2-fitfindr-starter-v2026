#!/usr/bin/env python3
"""
Send requests to a running FitFindr service and record what came back. ← CAPSTONE

Works against your own machine or the deployed service — only --url changes.
Uses nothing outside the standard library.

    python capstone_client.py --case happy -n 10
    python capstone_client.py --case bad_input
    python capstone_client.py --case fault --fault empty -n 5
    python capstone_client.py --url https://YOUR-APP.onrender.com --case happy -n 10

Each response is printed as one line and also appended to
results/capstone_client_<label>.jsonl, so the record survives even when the
service's own log doesn't (a free host wipes its disk when it sleeps).

Faults (--case fault) need the SERVICE to be started with
FITFINDR_ALLOW_FAULT_HEADER=1; otherwise the header is ignored and you'll see
ordinary successful runs.
"""

import argparse
import json
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent

# Queries that match listings in data/listings.json — the normal path.
HAPPY_QUERIES = [
    "vintage graphic tee under $30",
    "y2k baby tee",
    "cargo pants under $40",
    "denim jacket",
    "graphic tee",
]

# Malformed requests — what a broken or hostile caller sends. (body, content-type)
BAD_INPUTS = [
    ("{}", "application/json"),                         # no query field
    ('{"query": ""}', "application/json"),              # empty query
    ('{"query": "   "}', "application/json"),           # whitespace only
    ('{"query": 42}', "application/json"),              # wrong type
    ("this is not json", "application/json"),           # unparseable body
]


def send(url: str, body: str, content_type: str, fault: str | None, timeout: float):
    headers = {"Content-Type": content_type}
    if fault:
        headers["X-FitFindr-Fault"] = fault
    req = urllib.request.Request(url.rstrip("/") + "/ask", data=body.encode(), headers=headers, method="POST")
    started = time.perf_counter()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            status, raw = resp.status, resp.read().decode()
    except urllib.error.HTTPError as err:
        status, raw = err.code, err.read().decode()
    except Exception as exc:  # noqa: BLE001 — a client timeout is a result too
        return {"status": None, "client_error": f"{type(exc).__name__}: {exc}",
                "client_ms": round((time.perf_counter() - started) * 1000)}
    client_ms = round((time.perf_counter() - started) * 1000)
    try:
        data = json.loads(raw)
    except ValueError:
        data = {"unparsed_body": raw[:300]}
    return {"status": status, "client_ms": client_ms, "body": data}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", default="http://localhost:5000")
    ap.add_argument("--case", choices=["happy", "bad_input", "fault"], required=True)
    ap.add_argument("--fault", help="with --case fault: timeout | server_error | flaky | empty | rate_limit")
    ap.add_argument("-n", type=int, default=None, help="how many requests (default: 10 happy / 5 otherwise)")
    ap.add_argument("--label", default=None, help="name for the results file")
    ap.add_argument("--timeout", type=float, default=180.0, help="client-side timeout, seconds")
    args = ap.parse_args()

    if args.case == "fault" and not args.fault:
        ap.error("--case fault needs --fault")

    n = args.n or (10 if args.case == "happy" else 5)
    label = args.label or (args.case if args.case != "fault" else f"fault_{args.fault}")
    out = ROOT / "results" / f"capstone_client_{label}.jsonl"
    out.parent.mkdir(exist_ok=True)

    for i in range(n):
        if args.case == "bad_input":
            body, ctype = BAD_INPUTS[i % len(BAD_INPUTS)]
            fault = None
        else:
            body = json.dumps({"query": HAPPY_QUERIES[i % len(HAPPY_QUERIES)]})
            ctype = "application/json"
            fault = args.fault if args.case == "fault" else None

        result = send(args.url, body, ctype, fault, args.timeout)
        b = result.get("body") or {}
        meta = b.get("meta") or {}
        line = {
            "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "url": args.url, "case": args.case, "fault": fault, "sent": body,
            "status": result.get("status"), "client_ms": result.get("client_ms"),
            "client_error": result.get("client_error"),
            "error": b.get("error"), "failed_stage": b.get("failed_stage"),
            "fit_card": b.get("fit_card"), "meta": meta,
        }
        with out.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(line, ensure_ascii=False) + "\n")
        shown = (line["error"] or line["fit_card"] or line["client_error"] or "")
        print(f"{i + 1:>2}. {line['status']}  {line['client_ms']:>6} ms  "
              f"tokens={meta.get('prompt_tokens', 0)}+{meta.get('output_tokens', 0)}  "
              f"{shown[:90]!r}")

    print(f"\nwrote {n} lines to {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
