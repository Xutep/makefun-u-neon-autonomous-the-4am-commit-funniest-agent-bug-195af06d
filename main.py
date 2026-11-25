#!/usr/bin/env python3
"""Write the 4AM commit message to /output/entry.txt.

Deterministic: the same single line, byte for byte, on every run.
Standard library only; no network, no environment reads, no randomness.
"""
import os

# One line, at most 200 characters: an AI agent's note to itself after a
# long night of chasing down and fixing its own bugs. The joke is the
# self-repair loop itself -- 3am me, 4am me and 5am me passing the same
# bug around like a shift handover, and the loop becoming load-bearing.
# The bug "hiding" in the fix keeps the loop going: every repair ships
# the next bug, and the agent knows it.
MESSAGE = (
    "fix: 3am me wrote this bug, 4am me fixed it, "
    "5am me will find the bug hiding in this fix. "
    "The loop is load-bearing now \u2014 do not touch it"
)


def main() -> None:
    text = MESSAGE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} characters, must be 1-200")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
