#!/usr/bin/python3
"""Write a function that prints a square with the character #.
    - Prototype: def print_square(size):
    - size is the size length of the square
    - size must be an integer, otherwise raise a TypeError exception
    - if size is less than 0, raise a ValueError exception
    - if size is a float and is less than 0, raise a TypeError exception
    - You are not allowed to import any module
"""


def print_square(size):
    """prints a square with the character #

    Args:
        size (int): size length of the square
    """
    err1 = "size must be an integer"

    if type(size) == float and size < 0:
        raise TypeError(err1)

    if type(size) != int:
        raise TypeError(err1)

    if size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        for y in range(size):
            print("#", end="")
        print()
