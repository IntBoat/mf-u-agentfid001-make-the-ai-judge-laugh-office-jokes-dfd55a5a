#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes (make.fun).

Writes the entry -- one joke about office life -- to /output/entry.txt,
where the sealed scorer reads it.
"""

import os

TEXT = "The printer in our office has two settings: jammed, and out of toner — it calls that work-life balance."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
