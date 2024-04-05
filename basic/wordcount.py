#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import os
import sys
from typing import Dict, List


def read_file(filename: str) -> List[str]:
  """
  Reads a file and splits it into a list of words contained in that file.
  
  Args:
    filename(str): the relative or absolute path to the file to read.

  Raises:
    FileExistsError: If the file cannot be found.
  
  Returns:
    words(List[str]): A list of words contained in the file.
  """
  if not os.path.exists(filename):
    raise FileExistsError(f"Could not read {filename}")

  with open(filename, encoding='utf-8') as f:
    contents: str = f.read()
    contents = contents.replace("\n", " ")
  return contents.split()

def make_count_dict(words: List[str]) -> Dict[str, int]:
  """
  Creates a word count dictionary from a list of words.

  Args:
    words(List[str]): A list of strings

  Returns:
    Dict[str, int]: A dictionary where the key is the word and the value is the
      number of times it appears in the words list.
  """
  count_dict: Dict[str, int] = {}
  for word in words:
    if word not in count_dict:
      count_dict[word] = 1
    else:
      count_dict[word] += 1
  return count_dict

def print_words(filename: str) -> None:
  """
  Prints a list of words contained in a filename and their count.
  The list will be printed in alphabetical order.

  Args:
    filename(str): The name of the file to read words from.
  """
  words: List[str] = read_file(filename)
  count_dict: Dict[str, int] = make_count_dict(words)
  keys: List[str] = [word for word in count_dict.keys()]
  keys.sort()

  for key in keys:
    print(key, count_dict[key])

def print_top(filename: str) -> None:
  words: List[str] = read_file(filename)
  count_dict: Dict[str, int] = make_count_dict(words)
  top_freq: List[str] = list(sorted(count_dict, key=count_dict.__getitem__, reverse=True))

  for i in range(min(20, len(top_freq))):
    line: str = f"{i + 1}) Word: '{top_freq[i]}' Count: {count_dict[top_freq[i]]}"
    print(line)

# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main() -> None:
  if len(sys.argv) != 3:
    print('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option: str = sys.argv[1]
  filename: str = sys.argv[2]

  # option = "--topcount"
  # filename = "/home/mustard/repos/google-python-exercises/copyspecial/xyz__hello__.txt"
  # filename = "/home/mustard/repos/google-python-exercises/basic/alice.txt"
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()
