#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import sys
import os
from typing import Dict, List


def mimic_dict(filename: str) -> Dict[str,List[str]]:
  """Returns mimic dict mapping each word to list of words which follow it."""
  if not os.path.exists(filename):
    raise FileExistsError(f"File not found: {filename}")
  
  with open(filename, encoding='utf-8') as f:
    contents: str = f.read()
    contents = contents.replace("\n", " ")
    contents = contents.replace("\\'", "'")

  split: list[str] = contents.split()
  max_idx: int = len(split) - 1
  m_dict: Dict[str, List[str]] = {"": [split[0]]}
  for idx, value in enumerate(split):
    if idx == max_idx:
      break

    if value in m_dict:
      m_dict[value].append(split[idx+1].strip())
    else:
      m_dict[value] = [split[idx+1]]

  return m_dict


def print_mimic(mimic_dict: Dict[str,List[str]], word: str) -> None:
  """Given mimic dict and start word, prints 200 random words."""
  max_words: int = 200
  story: List[str] = []
  for i in range(200):
    if i == 0:
      current_word: str = random.choice(mimic_dict[word])
    else:
      current_word = next_word
    story.append(current_word)
    next_word: str = random.choice(mimic_dict[current_word])

  print(" ".join(story))


# Provided main(), calls mimic_dict() and mimic()
def main() -> None:
  # if len(sys.argv) != 2:
  #   print('usage: ./mimic.py file-to-read')
  #   sys.exit(1)

  # dict: Dict[str, List[str]] = mimic_dict(sys.argv[1])
  dict: Dict[str, List[str]] = mimic_dict(os.path.join("basic","mimic.py"))
  print_mimic(dict, '')


if __name__ == '__main__':
  main()
