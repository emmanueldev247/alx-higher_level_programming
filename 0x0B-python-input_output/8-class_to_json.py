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


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file (UTF8)
        and returns the number of characters added

        Args:
            filename(str): file to be appended to
            text(str): string to append to "filename"
        Returns:
            The number of characters added

    """
    with open(filename, "a", encoding='UTF-8') as my_file:
        return my_file.write(text)
