#!/usr/bin/python3
"""Find a peak"""


def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers"""
    if list_of_integers == []:
        return None

    lenList = len(list_of_integers)

    if lenList == 1:
        return list_of_integers[0]

    elif lenList == 2:
        return max(list_of_integers)

    mid = lenList // 2

    peak = list_of_integers[mid]

    if (peak >= list_of_integers[mid - 1]) and (peak >= list_of_integers[mid + 1]):
        return peak
    elif peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
