#!/usr/bin/python3
"""Create a function that writes an Object to a text file,
    using a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """function that that writes an Object to a text file,
        using a JSON representation

        Args:
            my_obj(object): object to write to "filename"
            filename(str): file to be written to
    """
    with open(filename, "w", encoding='UTF-8') as my_file:
        my_file.write(json.dumps(my_obj))
