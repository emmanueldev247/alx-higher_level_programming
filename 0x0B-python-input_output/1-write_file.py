#!/usr/bin/python3
"""Create a function that writes to a text file"""


def write_file(filename="", text=""):
    """function that a writes a string to a text file (UTF8)
        and returns the number of characters written

        Args:
            filename(str): file to be written to
            text(str): string to write to "filename"
        Returns:
            The number of characters written

    """
    with open(filename, "w", encoding='UTF-8') as my_file:
        return my_file.write(text)
