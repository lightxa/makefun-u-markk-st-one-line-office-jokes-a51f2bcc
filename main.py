#!/usr/bin/env python3
"""One-Line Office Jokes entry.

Writes a single original one-line joke about office life to
/output/entry.txt. Pure standard library, deterministic, no network.
"""

JOKE = (
    "I asked everyone to stop replying-all by replying-all, "
    "and now the thread has its own HR case."
)


def main() -> None:
    text = JOKE.strip()
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    assert 1 <= len(text) <= 199, "entry must be 1 to 199 characters"
    assert text.strip(), "entry must not be only whitespace"
    out_dir = "/output"
    import os

    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
