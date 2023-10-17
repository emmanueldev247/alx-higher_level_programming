#!/usr/bin/python3

"""Creates a class 'Base' which happens to be
the base of other classes in this project"""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method that returns the JSON
            representation of list_dictionaries

            Args:
                list_dictionaries(list): list to be converted to JSON
            Returns:
                The JSON representation of the list
        """

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)


    @classmethod
    def save_to_json_file(my_obj, filename):
     def save_to_file(cls, list_objs):
         """function that writes an Object to a text file,
        using a JSON representation

        Args:
            my_obj(object): object to write to "filename"
            filename(str): file to be written to
    """
    with open(filename, "w", encoding='UTF-8') as my_file:
        my_file.write(json.dumps(my_obj))
