#!/usr/bin/python3

"""Creates a class 'Base' which happens to be
the base of other classes in this project"""


class Base:
    """The “base” of all other classes in this project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation with id

            Args:
                id (int): id of class instances

            Private Class Attributes:
                __nb_object (int): Number of instantiated Bases
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
