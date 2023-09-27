#!/usr/bin/python3

"""Define 2 classes called Node & SinglyLinkedList"""


class Node:
    """A class that defines a node
        of a singly linked list
    """

    def __init__(self, data, next_node=None):
        """Instantiation with optional node"""
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        if next_node and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")

        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """attribute getter method"""
        return self.__data

    @data.setter
    def data(self, value):
        """attribute setter method"""
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """attribute getter method"""
        return self.__next_node

    @data.setter
    def next_node(self, value):
        """attribute setter method"""
        if value and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """ Class that defines a singly linked list"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """Public instance method that
           inserts a new Node into the
           correct sorted position
           in the list (increasing order)
        """
        new_node = Node(value)
        if self.__head is None or value < self.__head.__data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.__next_node is not Node:
                current = current.__next_node
            new_node.next_node = current.__next_node
            current.__next_node = new_node


def __str__(self):
    result = []
    current = self.head
    while current:
        result.append(str(current.data))
        current = current.next_node
    return "\n".join(result)
