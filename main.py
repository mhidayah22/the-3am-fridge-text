"""Write the 3am fridge text to entry.txt.

The line is a single text from a smart fridge to its owner at 3am:
the fridge is the only one in the house still working, still cold,
and still holding the salad its owner swore to eat on Monday. The
program writes it exactly as-is, with no trailing newline, so the
file holds one line of 132 characters: inside the bounty gate of
1 to 140 characters of UTF-8 text.
"""

import os
import sys

MAX_CHARS = 140  # the bounty gate: entry.txt holds 1 to 140 characters

LINE = (
    "3am. I'm the only one in this house still working, still cold, "
    "and still holding the salad you swore you'd eat on Monday. "
    "Go to bed."
)


def resolve_target():
    """Pick where entry.txt goes, in the order the grader expects.

    An explicit argument wins, then MAKEFUN_OUTPUT_DIR, then /output
    when it exists, then the file name in the current folder for a
    local run. The grader's working directory is read-only, so a bare
    relative path must never be the first choice.
    """
    if len(sys.argv) > 1:
        return sys.argv[1]
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return os.path.join(env_dir, "entry.txt")
    if os.path.isdir("/output"):
        return os.path.join("/output", "entry.txt")
    return "entry.txt"


def main():
    if not LINE.strip():
        raise SystemExit("fridge text must not be empty")
    if len(LINE) > MAX_CHARS:
        raise SystemExit(
            f"fridge text is {len(LINE)} characters, over the 140 limit"
        )
    if "\n" in LINE:
        raise SystemExit("fridge text must be a single line")
    target = resolve_target()
    parent = os.path.dirname(os.path.abspath(target))
    os.makedirs(parent, exist_ok=True)
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    with open(target, "r", encoding="utf-8") as handle:
        if handle.read() != LINE:
            raise SystemExit("written entry does not match the fridge text")


if __name__ == "__main__":
    main()
