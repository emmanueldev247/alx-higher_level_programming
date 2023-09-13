#!/usr/bin/python3
def weight_average(my_list=[]):
    """Function that returns the weighted average of all integers tuple"""
    if len(my_list) == 0:
        return 0

    weight = divisor = 0

    for pair in my_list:
        x, y = pair
        weight += x * y
        divisor += y

    return weight / divisor
