#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic list exercises

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
from typing import Any, List, Optional


def remove_adjacent(nums: List[int]) -> List[int]:
    """
    Iterate through the list.
    Store the last processed number, and if the new number is different, store
    it in the list to return.
    """
    last: Optional[int] = None
    new: List[int] = []
    for num in nums:
        if last == num:
            continue
        new.append(num)
        last = num
    return new


# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def linear_merge(list1: List[Any], list2: List[Any]) -> List[Any]:
    """
    Iterate through the lists and pop the smallest head from the list and
    add that to the final list. O(1)

    If either list is empty, then extend the rest of the remaining list to the
    final list and return. O(n)
    """

    final_list: List[Any] = []

    while True:
        if not list1:
            final_list.extend(list2)
            break
        
        if not list2:
            final_list.extend(list1)
            break

        if list1[0] <= list2[0]:
            final_list.append(list1.pop(0))
        else:
            final_list.append(list2.pop(0))

    return final_list

# Note: the solution above is kind of cute, but unforunately list.pop(0)
# is not constant time with the standard python list implementation, so
# the above is not strictly linear time.
# An alternate approach uses pop(-1) to remove the endmost elements
# from each list, building a solution list which is backwards.
# Then use reversed() to put the result back in the correct order. That
# solution works in linear time, but is more ugly.


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got: Any, expected: Any) -> None:
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '    X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Calls the above functions with interesting inputs.
def main():
    print('remove_adjacent')
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([]), [])

    print()
    print('linear_merge')
    test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
             ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
             ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
             ['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == '__main__':
    main()
