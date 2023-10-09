#!/usr/bin/python3

"""Create a  def lookup(obj):"""


def lookup(obj):
    """returns the list of available attributes and methods of an object

        Args:
        obj(object): object whose attribute is to be returned
    """
    return dir(obj)
