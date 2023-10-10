#!/usr/bin/python3
"""Create a function that reads text file"""


def read_file(filename=""):
    """function that reads a text file and prints it to stdout

        Args:
            filename(obj): file to be read
    """
    with open(filename, encoding='UTF-8') as my_file:
        print(my_file.read())
