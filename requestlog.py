"""
The structured request log. ← CAPSTONE

Every request to serve.py writes ONE record here, as one line of JSON, whether
it succeeded, was rejected, or failed. Named fields, not sentences, so a
question about a run that already happened ("how many 503s yesterday, and at
which stage?") is a filter, not a reading exercise.

Each record goes to two places:

    logs/requests.jsonl     a file you can read back (path: FITFINDR_LOG)
    stdout                  prefixed "REQUESTLOG ", because a free host wipes
                            its disk when it sleeps, but keeps stdout in its
                            log viewer — that is the copy that survives on
                            Render until you paste it into the README.

Fields:

    ts              when the request arrived, UTC, ISO 8601
    request_id      short id, also returned to the caller in `meta`
    route           "/ask"
    status          HTTP status returned
    outcome         ok | no_results | model_unavailable | bad_input | crash
    query           what came in (the user's text)
    wardrobe_items  how many wardrobe items came in with it
    fault           the injected fault, if one was on ("" = none)
    selected_item   id of the listing the agent chose, or null
    output          what went out: the fit card, or null
    error           session["error"] or the exception, or null
    failed_stage    which step stopped the run, or null
    duration_ms     wall-clock time inside the handler, including any wait
                    for the one-at-a-time lock
    wait_ms         how much of duration_ms was waiting for that lock
    model_calls     model calls this request made (0 if it never got there)
    prompt_tokens   tokens sent, as reported by the service
    output_tokens   tokens received, as reported by the service
    transient_retries / rate_limit_retries   retries this request needed
"""

import json
import os
import sys
import threading
import uuid
from datetime import datetime, timezone
from pathlib import Path

import config

LOG_PATH = Path(os.getenv("FITFINDR_LOG", str(config.ROOT / "logs" / "requests.jsonl")))
_write_lock = threading.Lock()


def new_request_id() -> str:
    return uuid.uuid4().hex[:8]


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")


def write(record: dict) -> None:
    """Append one record. Logging must never take a request down with it."""
    line = json.dumps(record, ensure_ascii=False, default=str)
    try:
        with _write_lock:
            LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
            with LOG_PATH.open("a", encoding="utf-8") as fh:
                fh.write(line + "\n")
    except Exception as exc:  # noqa: BLE001
        print(f"  [requestlog] couldn't write {LOG_PATH}: {exc}", file=sys.stderr, flush=True)
    print("REQUESTLOG " + line, flush=True)
