#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for y in x:
            if y == x[len(x) - 1]:
                print("{}".format(y))
            else:
                print("{}".format(y), end=" ")
