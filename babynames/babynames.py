#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
from typing import List

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def read_file(filename: str) -> List[str]:
    with open(filename, encoding="utf-8") as f:
        contents = f.readlines()

    return contents


def read_year(contents: List[str]) -> str:
    for line in contents:
        year_line = re.match(r"<h3 align=\"center\">Popularity in (\d{4})</h3>", line)
        if year_line is not None:
            year = year_line.group(1)
            break
    return year


def read_names(contents: List[str]) -> List[str]:
    print(print("{0:<4} {1:<20} {2:<20}".format("Rank", "Male", "Female")))
    for line in contents:
        name_line = re.match(
            r"<tr align=\"right\"><td>({\d+})</td><td>(\w+)</td><td>(\w+)</td>", line
        )
        if name_line is None:
            continue

        rank = name_line.group(1)
        male = name_line.group(2)
        female = name_line.group(3)

        print("{0:<5} {1:<20} {2:<20}".format(rank, male, female))


def extract_names(filename: str):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    contents = read_file(filename)
    year = read_year(contents)
    read_names(contents)
    # names =
    # +++your code here+++
    return


def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    args.append("/home/powell/google-python-exercises/babynames/baby1990.html")

    if not args:
        print("usage: [--summaryfile] file [file ...]")
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == "--summaryfile":
        summary = True
        del args[0]

    # +++your code here+++
    # For each filename, get the names, then either print the text output
    # or write it to a summary file
    filename = args[0]
    extract_names(filename)


if __name__ == "__main__":
    main()
