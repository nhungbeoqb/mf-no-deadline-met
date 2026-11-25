#!/usr/bin/env python3
"""One Line, No Deadline Met — writes a single-line deadline excuse to /output/entry.txt."""

import os

LINE = (
    "I finished it on time in my head, ahead of schedule in my dreams, "
    "and three days late in the only timeline that counts \u2014 this one."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert "\n" not in LINE, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
