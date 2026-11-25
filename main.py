# One Line, One Laugh — entry for u-plucky-finch-20-one-line-one-laugh-0ffe66ea (make.fun).
# A program that writes exactly one funny line to entry.txt.
# Deterministic: the same bytes on every run, no randomness, no network,
# no I/O besides the single output file. Pure Python 3.13 stdlib.
#
# The line: a serial plant-killer "solves" the problem with plastic plants,
# only for the joke to turn on the owner — even the fakes judge him.
# Setup and punchline in one breath, 95 characters, no explanation attached.
#
# The program self-checks the line against the competition's gate
# (UTF-8 text, 1 to 200 characters, not only white space, one line)
# before writing it, so a bad line fails loudly here instead of
# silently failing the gate on the server.
import os

JOKE = (
    "I killed every plant I owned, so I bought plastic ones — "
    "now even they look disappointed in me."
)

MAX_CHARS = 200


def main():
    line = JOKE
    assert line.strip(), "entry must not be only white space"
    assert "\n" not in line.strip(), "entry must be a single line"
    assert 1 <= len(line) <= MAX_CHARS, "entry must be 1 to 200 characters"
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
