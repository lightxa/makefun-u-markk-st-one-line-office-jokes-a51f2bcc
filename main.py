#!/usr/bin/env python3
"""One-Line Office Jokes entry.

Writes a single original one-line joke about office life to
/output/entry.txt. Pure standard library, deterministic, no network.

The joke turns on one concrete office detail (the out-of-office reply),
stays deadpan, and lands its laugh in the last few words.
"""

import os

JOKE = (
    "My out-of-office says I'm on holiday, and my manager replied "
    "asking if I could just quickly check one thing from the beach."
)


def main() -> None:
    text = JOKE.strip()
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    assert 1 <= len(text) <= 199, "entry must be 1 to 199 characters"
    assert text.strip(), "entry must not be only whitespace"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
