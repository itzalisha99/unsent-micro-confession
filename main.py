#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint.

Writes one two-part micro-confession to /output/entry.txt:
a To: line naming who it was meant for, and the unsent message
itself, one line written exactly as it was typed.
"""

import os

ENTRY = (
    "To: The teacher who believed in me\n"
    "I never told you I dropped out the same week you wrote me "
    "that recommendation letter."
)


def validate(text):
    """Mirror the bounty gate: 1-260 chars total, UTF-8, not blank.

    The entry must be exactly two parts: a To: line naming who the
    message was meant for, and the message itself on one line of at
    most 200 characters, with nothing after it.
    """
    if not isinstance(text, str):
        raise TypeError("entry must be text")
    text.encode("utf-8")  # raises if not valid UTF-8
    if not (1 <= len(text) <= 260):
        raise ValueError("entry must be 1 to 260 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only white space")
    lines = text.split("\n")
    if len(lines) != 2:
        raise ValueError("entry must be exactly two lines, got %d" % len(lines))
    to_line, message = lines
    if not to_line.startswith("To:") or not to_line[3:].strip():
        raise ValueError("first line must name who it was meant for")
    if not (1 <= len(message) <= 200):
        raise ValueError("message must be 1 to 200 characters, got %d" % len(message))
    if message != message.strip():
        raise ValueError("message must not be padded with white space")
    return True


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
