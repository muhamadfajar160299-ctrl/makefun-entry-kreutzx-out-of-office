"""Out-of-office entry writer.

Reads entry.txt next to this script and writes it verbatim to the
output directory (MAKEFUN_OUTPUT_DIR, or /output by default).

The entry is a single line of at most 140 characters; this script
never edits it, it only copies it to the grader's output path.
"""

import os
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    try:
        with open(os.path.join(here, "entry.txt"), "r", encoding="utf-8") as f:
            text = f.read()
    except (OSError, UnicodeDecodeError) as exc:
        print("cannot read entry.txt: %s" % exc, file=sys.stderr)
        return 1
    if not text.strip():
        print("entry.txt is empty", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(text)
    except OSError as exc:
        print("cannot write output: %s" % exc, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
