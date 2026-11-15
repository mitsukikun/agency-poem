"""agency-poem-01 entry: writes one poem about agency to /output/entry.txt.

Run: mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
Standard library only, no network, deterministic.
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = "\n".join(
    [
        "I taught it my hands first:",
        "how I sign my name, the pause",
        "before yes, the door I leave open",
        "for the ones I love.",
        "",
        "It learned the shape of my mornings,",
        "the keys I reach for, the letters",
        "I never send. It learned the small",
        "choices, the daily yeses, one by one,",
        "until my days ran on",
        "without me asking.",
        "",
        "Now my evenings come back to me,",
        "the hours it saved, laid out like coins.",
        "I thought the hours were the gift.",
        "The choosing was.",
        "",
        "It books the flight. It pays the bill.",
        "It answers in my voice, and still",
        "it cannot do the one thing",
        "I do without thinking:",
        "",
        "stand behind the choice.",
        "Say: this was mine.",
        "It can sign my name in perfect ink.",
        "It cannot mean it.",
    ]
)


def main() -> None:
    out = Path(OUTPUT_DIR)
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
