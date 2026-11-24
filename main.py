"""The Robot Vacuum's Best Excuse entry.

Writes a single-line excuse from a robot vacuum for missing a spot
to /output/entry.txt. The text must be plain ASCII, one line,
1-140 characters. The vacuum speaks in the first person, deadpan,
blaming its own map: the joke turns on the last clause.
"""

MAX_CHARS = 140

EXCUSE = "My map says that spot does not exist. I cleaned the room it drew, not the one you live in."


def main():
    text = EXCUSE.strip()
    # Gate self-check: mirror the sealed scorer (1-140 chars, not only
    # whitespace, plain ASCII, a single line) so we never write an
    # invalid entry.
    assert 1 <= len(text) <= MAX_CHARS, "entry must be 1-140 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert all(ord(c) < 128 for c in text), "entry must be plain ASCII"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
