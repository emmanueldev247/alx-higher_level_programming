#!/usr/bin/python3
"""Create a function that appends a string at the end of a text file"""


import json


def to_json_string(my_obj):
    """function that returns the JSON representation of an object (string)

        Args:
            my_obj(object): object to be converted to JSON
        Returns:
            The JSON representation of the object (string):

    """
    return json.dumps(my_obj)
