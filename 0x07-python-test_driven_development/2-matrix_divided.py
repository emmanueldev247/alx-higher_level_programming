#!/usr/bin/python3
"""Write a function that divides all elements of a matrix.
   - Prototype: def matrix_divided(matrix, div):
   - matrix must be a list of lists of integers or floats,
     otherwise raise a TypeError exception with the message
     matrix must be a matrix (list of lists) of integers/floats
 """


def matrix_divided(matrix, div):
    """Divides all elements of a matrix

    Args:
        matrix (list): list of lists of integers or floats
        div (int): divisor

    Returns:
        a new matrix with all elements in `matrix` divided by `div`
        error otherwise
    """
    err1 = "matrix must be a matrix (list of lists) of integers/floats"

    if type(matrix) != list:
        raise TypeError(err1)

    for elem in matrix:
        if type(elem) != list:
            raise TypeError(err1)

    row_size = len(matrix[0])
    for elem in matrix:
        if len(elem) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

        for items in elem:
            if type(items) not in (int, float):
                raise TypeError(err1)

    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    ret_matrix = []
    for elem in matrix:
        temp_list = []
        for items in elem:
            temp_list.append(round(items / div, 2))
        ret_matrix.append(temp_list)

    return ret_matrix
