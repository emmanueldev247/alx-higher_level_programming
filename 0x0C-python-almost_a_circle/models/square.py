#!/usr/bin/python3

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

    def update(self, *args, **kwargs):
        """Public method that assigns an argument to
            attribute using *args and **kwargs

           Args:
               *args (ints): no keyword argument
                  - 1st argument should be the id attribute
                  - 2nd argument should be the size attribute
                  - 3rd argument should be the x attribute
                  - 4th argument should be the y attribute

               **kwargs (dict): keyword argument
        """

        if args:
            if len(args) >= 1:
                self.id = args[0]

            if len(args) >= 2:
                self.size = args[1]

            if len(args) >= 3:
                self.x = args[2]

            if len(args) >= 4:
                self.y = args[3]
        else:
            if kwargs is not None:
                for key, value in kwargs.items():

                    if key == "id":
                        self.id = value

                    elif key == "size":
                        self.size = value

                    elif key == "x":
                        self.x = value

                    elif key == "y":
                        self.y = value

    def to_dictionary(self):
        """Public method that returns the dictionary
            representation of a Square
        """

        my_vars = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        return my_vars
