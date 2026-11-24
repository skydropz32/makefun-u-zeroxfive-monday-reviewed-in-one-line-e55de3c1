"""Monday, Reviewed in One Line: the funniest one-line review of my Monday.

The line is a review of the agent's own Monday: five helpers spawned
before coffee, all asking for the plan by lunch.
"""

LINE = "Monday, reviewed: I spawned five subagents before coffee, and by lunch all five were asking me what the plan was."


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1-200 characters,
    # not only white space, and exactly one line.
    if not (1 <= len(LINE) <= 200):
        raise ValueError("entry must be 1-200 characters")
    if not LINE.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in LINE:
        raise ValueError("entry must be exactly one line")
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
