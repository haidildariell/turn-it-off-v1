"""Have You Tried Turning It Off? — make.fun entry.

Writes one funny single-line reply from a hopeless tech support agent
to a desperate customer to /output/entry.txt.
"""

import os

LINE = (
    "Have you tried turning it off and on again? "
    "I ask because my entire training was one laminated card "
    "that just says that, in Comic Sans."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 199, f"entry length {len(text)} out of range"
    assert text.strip(), "entry must not be only whitespace"
    text.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
