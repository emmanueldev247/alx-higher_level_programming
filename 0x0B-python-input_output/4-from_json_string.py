#!/usr/bin/python3
"""Create a function that returns an object represented by a JSON string"""


import json


def from_json_string(my_str):
    """function that returns an object (Python data structure)
        represented by a JSON string

        Args:
            my_str(str): JSON string to be converted to Python data structure
        Returns:
            The Python Data Structure representation of the JSON string

    """
    return json.dumps(my_str)
