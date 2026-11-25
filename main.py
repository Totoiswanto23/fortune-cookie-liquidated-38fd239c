#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader.

Writes a single fortune cookie line (at most 20 words, plain text) for a
crypto trader who has just been liquidated, to /output/entry.txt.
"""
import os

FORTUNE = (
    "The stars say your fortune returns soon, but your margin account, "
    "however, has filed for a restraining order."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()
