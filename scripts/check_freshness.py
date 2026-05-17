from __future__ import annotations

import sys
from datetime import date
from common import load_all_datasets

MAX_AGE_DAYS = 180
errors = []
for path, e in load_all_datasets():
    last = date.fromisoformat(e["freshness"]["last_validated"])
    age = (date.today() - last).days
    if age > MAX_AGE_DAYS:
        errors.append(f"{path}: stale last_validated={last} age={age} days")

if errors:
    print("Freshness check failed:\n" + "\n".join(errors), file=sys.stderr)
    sys.exit(1)
print("Freshness check passed.")
