#!/usr/bin/env python3
"""Check Zoomms effect files against the top-level CSV (Python 3 standard library)."""
from pathlib import Path
import csv, hashlib, struct, sys

root = Path(__file__).resolve().parents[1]
effects = root / "Zoom MultiStomp"
errors = []
with (root / "effects.csv").open(newline="", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))
if len(rows) != 45:
    errors.append(f"Expected 45 entries, found {len(rows)}")

filenames = set()
ids = set()
for row in rows:
    filename = row["zdl file"]
    file = effects / filename
    if filename.lower() in filenames:
        errors.append(f"Duplicate filename: {filename}")
    filenames.add(filename.lower())
    if len(file.stem) > 8 or not file.stem.isascii():
        errors.append(f"Invalid filename alias: {filename}")
    if not file.is_file():
        errors.append(f"Missing effect: {filename}")
        continue
    data = file.read_bytes()
    if hashlib.sha256(data).hexdigest().lower() != row["sha256"].lower():
        errors.append(f"SHA256 mismatch: {filename}")
    if len(data) < 66 or data[4:8] != b"SIZE":
        errors.append(f"Unexpected ZDL format: {filename}")
        continue
    effect_id = (data[60], struct.unpack_from("<H", data, 64)[0])
    expected = (int(row["gid"]), int(row["fxid"]))
    if effect_id != expected:
        errors.append(f"Effect ID mismatch: {filename}")
    if effect_id in ids:
        errors.append(f"Duplicate effect ID: {effect_id}")
    ids.add(effect_id)

extras = set(p.name.lower() for p in effects.glob("*.ZDL")) - filenames
for name in sorted(extras):
    errors.append(f"Not listed in CSV: {name}")
if errors:
    print("FAIL:\n" + "\n".join(errors), file=sys.stderr)
    sys.exit(1)
print(f"PASS: {len(rows)} effects; SHA-256, distinct IDs, and filenames verified")
