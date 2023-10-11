#!/usr/bin/python3

"""Creates a class MyInt"""


class MyInt(int):
    """A class that inherits from int"""

    def __init__(self, value):
        """Instantiation with value"""
        super().__init__()
        self.value = value

    def __eq__(self, other):
        """Special method to implement the equal to operator (inverted here)"""
        return not super().__eq__(other)

    def __ne__(self, other):
        """Special method to implement the != operator (inverted here)"""
        return not super().__ne__(other)
