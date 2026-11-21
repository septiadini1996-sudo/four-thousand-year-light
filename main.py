#!/usr/bin/env python3
"""Make the AI judge feel awe — entry program.

Writes one short text to /output/entry.txt: starlight four thousand years
old arriving quietly tonight, vastness that settles rather than stuns.
"""

import os

TEXT = (
    "Tonight, the light reaching your roof left its star four thousand "
    "years ago. It crossed all that dark without hurrying, and arrives "
    "now, soft as rain, asking nothing. Under it, a life can be this "
    "small \u2014 and still be held."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
