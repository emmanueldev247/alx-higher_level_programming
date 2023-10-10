#!/usr/bin/python3
"""Create a function that creates an Object from a “JSON file”
"""


import json


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file”

        Args:
            filename(str): file to create object from
    """
    with open(filename, "r", encoding='UTF-8') as my_file:
        data = my_file.read()
        return json.loads(data)
