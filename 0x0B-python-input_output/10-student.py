#!/usr/bin/python3
"""Defines a class Student"""


class Student:
    """A class that defines a Student
        Public instance attributes:
            - first_name
            - last_name
            - age
        Public method:
            - def to_json(self):
    """

    def __init__(self, first_name, last_name, age):
        """Instantiation magic method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Function that returns the dictionary description with
        simple data structure for JSON serialization of an object
        """
        return {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
        }
