#!/usr/bin/python3

"""Define a class called MyList"""


class MyList(list):
    """A class MyList that inherits from list"""

    def print_sorted(self):
        """Public instance method that prints the list, but
            sorted (ascending sort). You can assume that all
            the elements of the list will be of type int
        """
        sorted_list = sorted(self)
        print(sorted_list)
