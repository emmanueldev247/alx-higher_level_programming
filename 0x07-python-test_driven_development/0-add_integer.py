#!/usr/bin/python3
"""Task 0. Integer addition

   * Write a function that adds 2 integers
        - Prototype: def add_integer(a, b=98):
        - a and b must be integers or floats,
          otherwise raise a TypeError exception
          with the message a must be an integer
          or b must be an integer
        - a and b must be first casted to integers if they are float
        - Returns an integer: the addition of a and b
        - You are not allowed to import any module

"""


def add_integer(a, b=98):
    """Adds 2 integers

    Args:
        a (int): first integer
        b (int): second integer

    Returns:
        the addition i.e a + b;
        error if a (or b) is not an integer or float
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")

    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return (a + b)
