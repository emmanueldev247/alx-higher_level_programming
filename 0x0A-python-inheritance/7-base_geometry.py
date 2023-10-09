#!/usr/bin/python3

"""Creates a class BaseGeometry"""


class BaseGeometry:
    """Create an instance method"""

    def area(self):
        """Public instance method that raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method that validates value"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
