#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        print(value)
        return True
    except BaseException:
        return False