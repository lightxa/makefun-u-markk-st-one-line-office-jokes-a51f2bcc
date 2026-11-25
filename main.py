#!/usr/bin/env python3
"""One-Line Office Jokes entry.

Writes a single one-line joke about office life to /output/entry.txt.
Deterministic, stdlib only, no network.

The joke turns on one concrete office detail (the "quick sync" calendar
invite that eats the afternoon) and lands its laugh in the last few
words: a meeting scheduled about the meeting itself.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 199

JOKE = (
    "The invite said 'quick sync', so naturally it ran forty-five minutes "
    "and ended by scheduling a meeting about the meeting."
)


def validate(text: str) -> str:
    """Return the entry text, enforcing the gate: 1-199 chars, one line."""
    line = " ".join(text.split())
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"entry must be 1 to {MAX_CHARS} characters")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    return line


def main() -> None:
    entry = validate(JOKE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(entry + "\n")


if __name__ == "__main__":
    main()
