#!/usr/bin/env python3
"""Write the review to the path the harness reads.

The gate takes UTF-8 text of 1 to 160 characters that is not only white space.
A review that runs one character long, or that picks up a newline on the way
out, scores 0 and takes no prize, so the line is measured before it is written
and the program refuses rather than produce a file the gate will throw away.
"""
import os
import sys

LINE = (
    "Sleep: I hand over a third of my life every night, and it no-showed "
    "four hours last night and still charged me the full night."
)

MAX_CHARS = 160
OUTPUT_NAME = "entry.txt"


def output_dir():
    """The harness sets MAKEFUN_OUTPUT_DIR; /output is its documented default."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def problems(text):
    """Every reason the gate would refuse this text, in the order it would hit."""
    found = []
    if not text:
        found.append("empty")
        return found
    if len(text) > MAX_CHARS:
        found.append("too long: {} > {}".format(len(text), MAX_CHARS))
    if not text.strip():
        found.append("white space only")
    if "\n" in text or "\r" in text:
        found.append("carries a line break")
    if text != text.strip():
        found.append("has leading or trailing white space")
    return found


def main(argv):
    # --check measures the line and writes nothing, so the entry can be proved
    # on a machine without /output.
    if "--check" in argv:
        bad = problems(LINE)
        if bad:
            print("invalid: " + "; ".join(bad))
            return 1
        print("valid: {} characters".format(len(LINE)))
        return 0
    bad = problems(LINE)
    if bad:
        print("refusing to write: " + "; ".join(bad), file=sys.stderr)
        return 1
    target = output_dir()
    os.makedirs(target, exist_ok=True)
    path = os.path.join(target, OUTPUT_NAME)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    print("wrote {} characters to {}".format(len(LINE), path))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
