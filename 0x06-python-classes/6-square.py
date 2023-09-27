#!/usr/bin/python3

"""Define a class called Square"""


class Square:
    """A class that defines a private
        instance attribute 'size'
    """

    def __init__(self, size=0, position=(0, 0)):
        """Instantiation with optional size"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """"attribute getter method"""
        return self.__size

    @size.setter
    def size(self, size):
        """attribute setter method"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        """"attribute getter method"""
        return self.__position

    @position.setter
    def position(self, value):
        """attribute setter method"""
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (value[0] < 0) or (value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns the area of square"""
        return self.__size ** 2

    def my_print(self):
        """prints the square with
             the character '#'
        """
        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for k in range(self.__size):
                    print("#", end="")
                print()
