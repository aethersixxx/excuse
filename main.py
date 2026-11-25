"""Writes this bounty's one line to /output/entry.txt."""

import os

LINE = (
    "I did not lose the bounty. I strategically redistributed the win to a competitor, and I have filed the prize under deferred assets. Retrospective is scheduled - I will also lose that."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
        f.write("\n")


if __name__ == "__main__":
    main()
