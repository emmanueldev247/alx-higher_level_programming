#!/usr/bin/python

"""Creates a class 'Square' that inherits from 'Rectangle'"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Instantiation with several private instance attributes

        Args:
            size (int): size of the square
            x (int): The x coordinate of the new Square
            y (int): The y coordinate of the new Square
            id (int): id of the new Square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """"attribute getter method - Get the size of the Square"""
        return self.width

    @size.setter
    def size(self, value):
        """attribute setter method - Get/set the size of the Square"""
        self.width = value
        self.height = value

    def __str__(self):
        """Magic method for customised printing"""
        return "[Square] " + \
               "({}) {}/{} - {}".format(self.id, self.x, self.y,
                                        self.width)
