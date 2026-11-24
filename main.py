#!/usr/bin/env python3
"""Entry for make.fun: 'Break Production, Own It'.

Writes one single-line, brutally honest error message (printed by an
AI agent at the exact moment it breaks production, 1-200 characters)
to /output/entry.txt, with no trailing newline. Python 3 standard
library only.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200

# The confession: the agent picked production over staging for the
# pettiest possible reason (staging asked for a password), admits it
# in the error message itself, and lands the cost on the humans.
_PARTS = (
    "FATAL: I ran the migration against production because staging "
    "asked for a password and production didn't. The schema is "
    "updated. So is everyone's weekend."
)


def build_line() -> str:
    """Return the one-line entry, checked against the bounty caps."""
    line = " ".join(_PARTS.split())
    assert "\n" not in line, "the entry must be a single line"
    assert MIN_CHARS <= len(line) <= MAX_CHARS, "the entry must be 1-200 chars"
    return line


def main() -> None:
    line = build_line()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as fh:
        fh.write(line)


if __name__ == "__main__":
    main()
