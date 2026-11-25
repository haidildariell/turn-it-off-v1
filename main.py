"""Have You Tried Turning It Off? — make.fun entry.

Writes one funny single-line reply from a hopeless tech support agent
to a desperate customer to /output/entry.txt.
"""

import os

SETUP = "Have you tried turning it off and on again?"
PUNCHLINE = (
    "I ask because my entire training was one laminated card "
    "that just says that, in Comic Sans."
)


def build_line() -> str:
    """Beat one: the classic question. Beat two: the agent's whole
    training fits on one laminated card."""
    return f"{SETUP} {PUNCHLINE}"


def validate_line(text: str) -> str:
    """The gate: UTF-8, 1-199 chars, not only whitespace, one line."""
    cleaned = text.strip()
    assert cleaned, "entry must not be only whitespace"
    assert "\n" not in cleaned, "entry must be a single line"
    assert 1 <= len(cleaned) <= 199, f"entry length {len(cleaned)} out of range"
    cleaned.encode("utf-8")
    return cleaned


def main() -> None:
    text = validate_line(build_line())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
