#!/usr/bin/env python3
"""Aica Meeting Email — one-line joke for make.fun.

Writes a single funny line about a meeting that should have been
an email to /output/entry.txt. Pure stdlib, deterministic, no network.
"""

import os

# The joke: the meeting's only output is an email nobody can read,
# because everyone is still in a meeting about the email.
LINE = (
    "We spent ninety minutes in a meeting deciding what the email "
    "should say, then sent it to people still stuck in a meeting "
    "about the email."
)


def main() -> None:
    line = LINE.strip()
    if not line:
        raise SystemExit("entry is empty")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(line) <= 199:
        raise SystemExit(f"entry is {len(line)} chars, must be 1-199")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(line)
    with open("/output/entry.txt", encoding="utf-8") as fh:
        back = fh.read()
    assert back == line, "read-back mismatch"
    assert not back.endswith("\n"), "entry must not end with a newline"
    assert back == back.strip(), "entry must have no leading/trailing space"
    print(f"wrote {len(line)} chars to /output/entry.txt")
    print(line)


if __name__ == "__main__":
    main()
