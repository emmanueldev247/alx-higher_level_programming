#!/usr/bin/python3

"""Creates 2 classes
    A: a super class BaseGeometry
    B: a sub class Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Instantiation with width and height

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Method for area of Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Magic method for customised output"""
        output = "[{}] {}/{}".format(self.__class__.__name__,
                                     self.__width, self.__height)
        return output
