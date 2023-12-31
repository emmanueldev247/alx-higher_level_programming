#!/usr/bin/python3
"""Pascal's Triangle Program"""


def pascal_triangle(n):
    """function that returns pascal triangle list of lists

        Args:
            n(int): pascal triangle level
        Returns:
            A list of lists of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    elif n == 2:
        return [[1], [1, 1]]
    elif n == 3:
        return [[1], [1, 1], [1, 2, 1]]
    result = [[1], [1, 1], [1, 2, 1]]
    for i in range(0, n-3):
        use_list = result[-1]
        new_list = []
        for index in range(len(use_list)):
            if index == 0:
                new_list.append(use_list[index])
            else:
                new_list.append(use_list[index] + use_list[index - 1])
            if index == len(use_list) - 1:
                new_list.append(use_list[index])
        result.append(new_list)
    return result
