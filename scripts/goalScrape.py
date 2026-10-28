#!/usr/bin/env python3
"""Scrape the CSCI 401 module goals into goals.md."""

from pathlib import Path
from urllib.request import urlopen


BASE_URL = "https://facultyweb.cs.wwu.edu/~wehrwes/courses/csci401_26f/modules"
OUTPUT_FILE = Path(__file__).with_name("goals.md")


def fetch_goals(module_number):
    module = f"m{module_number:02}"
    goal_file = f"G{module_number:02}.md"
    url = f"{BASE_URL}/{module}/{goal_file}"

    with urlopen(url, timeout=20) as response:
        markdown = response.read().decode("utf-8")

    goals = []
    for line in markdown.splitlines():
        line = line.strip()
        if line.startswith("* ") and not line.startswith("**"):
            goals.append(line[2:])
    return goals


def main():
    sections = []
    for module_number in range(1, 18):
        if module_number == 3:
            continue

        goals = fetch_goals(module_number)
        sections.append(
            f"## M{module_number:02}\n\n"
            + "\n".join(f"* {goal}" for goal in goals)
        )

    OUTPUT_FILE.write_text("\n\n".join(sections) + "\n", encoding="utf-8")
    print(f"Saved module goals to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
