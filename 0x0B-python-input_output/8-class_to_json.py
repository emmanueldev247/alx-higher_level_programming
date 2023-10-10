#!/usr/bin/python3
"""Returns the dictionary description with simple data
    structure for JSON serialization of an object
"""


def class_to_json(obj):
    """Function that returns the dictionary description with
        simple data structure for JSON serialization of an object
       Args:
        obj(class): Class to be worked on
    """
    return vars(obj)
