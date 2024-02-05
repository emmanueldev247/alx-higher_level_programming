#!/usr/bin/python3
"""Find a peak"""


def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers"""
    if list_of_integers == []:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]

    for i in range(len(list_of_integers)):
        if (list_of_integers[i] >= list_of_integers[i-1]):
            if (list_of_integers[i] >= list_of_integers[i+1]):
                break

    return list_of_integers[i]
