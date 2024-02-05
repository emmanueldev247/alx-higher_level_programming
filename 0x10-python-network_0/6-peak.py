#!/usr/bin/python3
"""Find a peak"""


def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers"""
    if list_of_integers == []:
        return None

    lenList = len(list_of_integers)

    if lenList == 1:
        return list_of_integers[0]

    for i in range(lenList):
        if i == lenList - 1:
            if (list_of_integers[i] >= list_of_integers[i-1]):
                return list_of_integers[i]
        else:
            if (list_of_integers[i] >= list_of_integers[i-1]):
                if (list_of_integers[i] >= list_of_integers[i+1]):
                    return list_of_integers[i]
