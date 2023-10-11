#!/usr/bin/python3

"""Creates a class 'Square' that inherits from f.__class__
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class that inherits from class Rectangle"""

    def __init__(self, size):
        """Instantiation with size

        Args:
            size (int): The size of the Square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Method for area of Square"""
        return self.__size ** 2

    def __str__(self):
        """Magic method for customised output"""
        output = "[{}] {}/{}".format(self.__class__.__name__,
                                     self.__size, self.__size)
        return output
