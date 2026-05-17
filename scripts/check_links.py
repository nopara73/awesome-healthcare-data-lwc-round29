from __future__ import annotations

import argparse
import sys
import time
from urllib.parse import urlparse

import requests
from common import load_all_datasets

parser = argparse.ArgumentParser()
parser.add_argument("--timeout", type=float, default=15.0)
parser.add_argument("--sleep", type=float, default=0.2)
parser.add_argument("--fail", action="store_true", help="fail on broken links; default reports only")
args = parser.parse_args()

failures = []
seen = set()
for _, e in load_all_datasets():
    urls = [e["owner"]["url"], *[v for v in e["resources"].values() if v], e["access"]["request_url"], e["access"]["download_url"]]
    for url in urls:
        if not url or url in seen:
            continue
        seen.add(url)
        parsed = urlparse(url)
        if parsed.scheme not in {"http", "https"}:
            failures.append((url, "not http(s)"))
            continue
        try:
            resp = requests.head(url, timeout=args.timeout, allow_redirects=True)
            if resp.status_code in {403, 405} or resp.status_code >= 500:
                resp = requests.get(url, timeout=args.timeout, allow_redirects=True, stream=True)
            if resp.status_code >= 400 and resp.status_code not in {403, 429}:
                failures.append((url, f"HTTP {resp.status_code}"))
        except Exception as exc:  # noqa: BLE001
            failures.append((url, str(exc)))
        time.sleep(args.sleep)

if failures:
    for url, reason in failures:
        print(f"LINK CHECK: {url} -> {reason}")
    if args.fail:
        sys.exit(1)
else:
    print(f"Checked {len(seen)} links; no failures.")
