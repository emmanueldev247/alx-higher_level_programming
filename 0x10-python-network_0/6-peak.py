#!/usr/bin/python3
"""Find a peak"""


def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers"""
    lenList = len(list_of_integers)

    if lenList == 0:
        return None

    if lenList == 1:
        return list_of_integers[0]

    if lenList == 2:
        return max(list_of_integers)

    low = 0
    high = len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2
        peak = list_of_integers[mid]

        if (peak > list_of_integers[mid + 1]):
            high = mid
        else:
            low = mid + 1
    return list_of_integers[low]
