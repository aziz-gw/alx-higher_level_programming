#!/usr/bin/python3
"""
 finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Finds a peak element in an unsorted list of integers.

    Args:
        list_of_integers (list): input list of integers.

    Returns:
        int: index of a peak element
    """
    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = left + (right - left) // 2

        # Compare mid with its neighbors
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            # If mid is greater than its right neighbor, search left
            right = mid
        else:
            # Otherwise, search right
            left = mid + 1

    return left
