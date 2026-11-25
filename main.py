#!/usr/bin/env python3
"""The Internet in One Word — entry program.

Writes the winning word to /output/entry.txt.

Winner: "bots" — chosen by a criteria screen of 30 candidates against the
published judge persona (single word describing the whole internet; funny by
itself; true about the whole internet; surprising; lands in one beat), a
self-judged pairwise tournament (quarterfinals -> semifinals -> final), and a
live collision check against the 602-entry field. The tournament winner
"feral" (68/75) and runner-up "unhinged" (68/75) were both already held by
dozens of earlier entries, so the runoff winner is "bots": it beat "wrong"
margin 2 (C1/C3/C5) and "ads" margin 2 (C2). See candidates.md.

The internet is bots — dead-internet theory made literal: roughly half of web
traffic is automated, and with the AI content flood the claim is truer than
ever. One word, 4 letters, no explanation needed.
"""

import os

WORD = "bots"


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
