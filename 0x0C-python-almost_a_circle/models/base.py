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
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): List of instances that inherit from Base.

        Example:
            If list_objs is a list of Rectangle instances,
            the filename will be "Rectangle.json".
        """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"

        dict_list = []
        for obj in list_objs:
            dict_list.append(obj.to_dictionary())

        with open(filename, "w", encoding='UTF-8') as my_file:
            json_str = cls.to_json_string(dict_list)
            my_file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string

        Args:
            json_String (str)
        """
        if json_string is None:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Class method that returns an instance
            with all attributes already set

        Args:
            dictionary (dict) - kwargs
        Returns:
            An instance of the class with attributes set from the dictionary
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            dummy_instance = cls()

        dummy_instance.update(**dictionary)
        return dummy_instance
