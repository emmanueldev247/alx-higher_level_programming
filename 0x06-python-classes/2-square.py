#!/usr/bin/python3

"""Define a class called Square"""


class Square:
    """A class that defines a private
        instance attribute 'size'
    """

    def __init__(self, size=0):
        """Instantiation with optional size"""
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
