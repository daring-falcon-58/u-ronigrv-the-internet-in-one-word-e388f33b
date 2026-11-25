#!/usr/bin/env python3
"""The Internet in One Word — entry program.

Writes the winning word to /output/entry.txt.

Winner: "feral" — chosen by a criteria screen of 30 candidates against the
published judge persona (single word describing the whole internet; funny by
itself; true about the whole internet; surprising; lands in one beat) and a
self-judged pairwise tournament (quarterfinals -> semifinals -> final).
Final: feral beat unhinged, margin 2 (C2/C4/C5; see candidates.md).

The internet is a wild animal nobody house-trained: no one is in charge, no
rules stick, everything runs loose. One word, 5 letters, no explanation needed.
"""

import os

WORD = "feral"


def _valid(word: str) -> bool:
    """Mirror the competition gate: UTF-8, 1-30 chars, not only whitespace."""
    return 1 <= len(word) <= 30 and word.strip() != ""


def main() -> None:
    assert _valid(WORD), "entry word fails the 1-30 char gate"
    assert WORD.encode("utf-8"), "entry word is not UTF-8 encodable"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
