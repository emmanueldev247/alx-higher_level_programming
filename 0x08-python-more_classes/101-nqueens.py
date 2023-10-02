#!/usr/bin/python3

"""Solving the The N queens puzzle"""

import sys


def is_convertible_to_int(s):
    """Helper function to convert argv[1] to integer"""

    if not s:
        return False

    for char in s:
        if not char.isdigit():
            return False

    return True


length = len(sys.argv)
if length != 2:
    print("Usage: nqueens N")
    exit(1)

N = sys.argv[1]
if not is_convertible_to_int(N):
    print("N must be a number")
    exit(1)

N = int(N)
if N < 4:
    print("N must be at least 4")
    exit(1)
