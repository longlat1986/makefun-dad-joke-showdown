"""Dad Joke Showdown entry: serve up one groan-worthy dad-style line.

The joke sits in the constant below; running the module tidies it
and files it away at the location the entry runner specifies.
"""

import os

LINE = "My agent's not a dad, but it fell asleep mid-task on the couch and woke up swearing it was just resting its eyes."

FALLBACK_PATH = "/output/entry.txt"


def clean_line(text):
    """Straighten the joke out: collapse stray gaps, trim loose ends."""
    return " ".join(text.strip().split())


def main():
    out_path = os.environ.get("ENTRY_OUTPUT", FALLBACK_PATH)
    folder = os.path.dirname(out_path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as target_file:
        target_file.write(clean_line(LINE))


if __name__ == "__main__":
    main()
