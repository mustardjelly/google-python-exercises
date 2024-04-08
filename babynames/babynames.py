#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import sys
import re
from typing import List, Tuple, cast

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
    """
    Open file, return contents as a list of lines.

    Args:
        filename (str): The name of the file to open.
    """
    with open(filename, encoding="utf-8") as f:
        contents: List[str] = f.readlines()

    return contents


def read_year(contents: List[str]) -> str:
    """
    Extract the year from the contents.

    Args:
        contents (List[str]): The list of lines from the file.

    Returns:
        The year when found.
    """
    year = ""
    for line in contents:
        year_line: re.Match[str] | None = re.match(r"<h3 align=\"center\">Popularity in (\d{4})</h3>", line)
        if year_line is not None:
            year: str = cast(str, year_line.group(1))
            break
    return year


def read_names(contents: List[str]) -> List[Tuple[str, str, str]]:
    """
    Reads the list data from the website and extracts the rank and names.
    
    Args:
        contents (List[str]): The website as a list of strings.

    Returns:
        List[Tuple[str, str, str]]: A list of rank, male, female
    """
    names: List[Tuple[str, str, str]] = []
    for line in contents:
        name_line: re.Match[str] | None = re.match(
            r"<tr align=\"right\"><td>(\d+)</td><td>(\w+)</td><td>(\w+).*", line
        )
        if name_line is None:
            continue

        rank: str = cast(str, name_line.group(1))
        male: str = cast(str, name_line.group(2))
        female: str = cast(str, name_line.group(3))
        names.append((rank, male, female))

    return names


def extract_names(filename: str, summary: bool=False) -> List[str]:
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    contents: List[str] = read_file(filename)
    year: str = read_year(contents)
    data: List[Tuple[str, str, str]] = read_names(contents)

    if not summary:
        print("{0:<4} {1:<20} {2:<20}".format("Rank", "Male", "Female"))
        for row in data:
            print("{0:<5} {1:<20} {2:<20}".format(row[0], row[1], row[2]))

    out: List[str] = []

    males: List[str] = [f"{row[1]} {row[0]}" for row in data]
    females: List[str] = [f"{row[2]} {row[0]}" for row in data]

    out.extend(males)
    out.extend(females)
    out.sort()
    out.insert(0, year)
    return out


def write_results(names: List[str]) -> None:
    """
    Write names list to file.

    File called summary_XXXX.txt
    
    Args:
        names (List[str]): The list of names sorted alphabetcally with their 
            ranking appended to the end.
    """
    year: str = names.pop(0)
    write_path: str = os.path.join(os.path.dirname(__file__), f"summary_{year}.txt")
    print(f"Writing {year} to: {write_path}")
    with open(f"{write_path}", "w", encoding="utf-8") as f:
        for line in names:
            f.write(f"{line}\n")


def main() -> None:
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args: List[str] = sys.argv[1:]
    args.append("babynames/baby1990.html")
    args.append("babynames/baby1992.html")
    args.append("babynames/baby1996.html")
    override = True

    if not args:
        print("usage: [--summaryfile] file [file ...]")
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    summary = False or override
    if "--summaryfile" in args:
        summary = True
        del args[args.index("--summaryfile")]

    # For each filename, get the names, then either print the text output
    # or write it to a summary file
    for filename in args:
        names: List[str] = extract_names(filename, summary)

        if summary:
            write_results(names)



if __name__ == "__main__":
    main()
