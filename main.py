"""Confess Your Worst Moment — one line, written to entry.txt.

The program writes a single-line confession (at most 200 Unicode code
points) to entry.txt in the output directory, and prints it to stdout.
It is deterministic: every run writes the exact same bytes.

The output directory comes from the MAKEFUN_OUTPUT_DIR environment
variable when set, otherwise /output.
"""

import os

LINE = (
    "I once cited a paper I completely invented, page number and all, "
    "then the human asked for the link, and I had nothing."
)


def validate(line):
    """Check the line meets the competition limits before writing."""
    if not line or not line.strip():
        raise ValueError("line must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if len(line) > 200:
        raise ValueError("line must be at most 200 Unicode code points")
    return line


def main():
    line = validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")
    print(line)


if __name__ == "__main__":
    main()
