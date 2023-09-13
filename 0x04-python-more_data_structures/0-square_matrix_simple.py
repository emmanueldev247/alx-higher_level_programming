#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Function that computes the square value of all integers of a matrix"""
    squared = []
    for row in matrix:
        squared.append(list(map(lambda x: x**2, row)))
    return squared
