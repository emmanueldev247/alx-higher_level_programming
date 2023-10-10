#!/usr/bin/python3
"""Create a function that appends a string at the end of a text file"""


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
