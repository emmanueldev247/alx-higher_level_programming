#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """Print an integer

    Args:
        value (int): The integer to print.

    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return True
    except BaseException as error:
        sys.stderr.write("Exception: {}\n".format(error))
        return False
