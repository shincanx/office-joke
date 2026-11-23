#!/usr/bin/env python3
"""Office joke entry for make.fun.

Writes exactly one one-line joke about office life to entry.txt:
no setup beyond the line itself, no trailing newline, no extra text.
The joke leans on "per my last email" -- the office phrase everyone
has both sent and winced at -- and lands it somewhere unexpected.
"""

import os

# One line, 89 characters. The turn is the will: office email etiquette
# followed home, where it does not belong.
TEXT = "I put 'per my last email' in my will so my family knows I already answered that question."

def main():
    if not 1 <= len(TEXT) <= 199:
        raise SystemExit(f"joke must be 1-199 characters, got {len(TEXT)}")
    if not TEXT.strip():
        raise SystemExit("joke must not be only whitespace")
    if "\n" in TEXT or "\r" in TEXT:
        raise SystemExit("joke must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
