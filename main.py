#!/usr/bin/env python3
"""Write one funny resignation letter, exactly one line long."""

import os

TEXT = "I resign, effective immediately \u2014 my two weeks' notice is this sentence, and my exit interview is the door closing behind me."

# Entry rule: exactly one line — the whole resignation letter is this sentence.
assert "\n" not in TEXT, "entry must be exactly one line"
assert TEXT.endswith("."), "entry must end with a full stop"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
