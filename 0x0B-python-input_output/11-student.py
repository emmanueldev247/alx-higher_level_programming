#!/usr/bin/python3
"""Defines a class Student"""


class Student:
    """A class that defines a Student
        Public instance attributes:
            - first_name
            - last_name
            - age
        Public method:
            - def to_json(self, attrs=None):
            - def reload_from_json(self, json):
    """

    def __init__(self, first_name, last_name, age):
        """Instantiation magic method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Function that returns the dictionary description with
        simple data structure for JSON serialization of an object
        Args:
            attrs(list): list of strings that can contain attribute names;
            default is None
        Returns:
            A dictionary representation of a Student instance
        """
        if attrs is None:
            return {key: value for key, value in self.__dict__.items()}
        else:
            return {k: val for k, val in self.__dict__.items() if k in attrs}

    def reload_from_json(self, json):
        """Public method that replaces all
            attributes of the Student instance
           Args:
            json(dict): containing attributes to be replaced"""
        attr_dict = dict(json)
        print(attr_dict)
        for key, value in attr_dict.items():
            if key in self.__dict__:
                self.__dict__[key] = value
