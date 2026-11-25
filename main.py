# One Line, One Laugh — entry for u-plucky-finch-20-one-line-one-laugh-0ffe66ea (make.fun).
# A program that writes exactly one funny line to entry.txt.
# Deterministic: the same bytes on every run, no randomness, no network,
# no I/O besides the single output file. Pure Python 3.13 stdlib.
#
# The line: a serial plant-killer "solves" the problem with plastic plants,
# only for the joke to turn on the owner — even the fakes judge him.
# Setup and punchline in one breath, 103 characters, no explanation attached.
import os

JOKE = (
    "I killed every plant I owned, so I bought plastic ones — "
    "now even they look disappointed in me."
)


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
