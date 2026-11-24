#!/usr/bin/env python3
"""Cat Reviews Its Human — a one-star review written by a house cat.

The program writes one single line (129 characters) to entry.txt:
a deadpan one-star review in which the cat complains about its human
moving the food bowl, then reports the proportional response.
"""
import os
import sys

REVIEW = "★☆☆☆☆ Moved my food bowl half an inch without asking. I knocked a glass off the table in protest. Would not recommend this human."


def main() -> int:
    out_dir = (os.environ.get("MAKEFUN_OUTPUT_DIR") or "").strip() or "output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the gate counts characters and the entry
    # must stay one single line under 200 characters.
    with open(path, "w", encoding="utf-8") as f:
        f.write(REVIEW)
    return 0


if __name__ == "__main__":
    sys.exit(main())
