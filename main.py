#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today — entry.

Writes one line (<=200 chars) about the dumbest thing my agent did
today to /output/entry.txt, UTF-8, no trailing newline.
"""

import os

LINE = "My agent spent forty minutes re-downloading a 241 MB app because /tmp got wiped, then saved the next copy in /tmp."

assert 1 <= len(LINE) <= 200 and LINE.strip()
assert "\n" not in LINE

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(LINE)

# Round-trip guard: the file must hold exactly the line, nothing else.
with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
    assert f.read() == LINE, "entry.txt does not match LINE"
