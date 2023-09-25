#!/usr/bin/python3
def safe_print_division(a, b):
    """Divides 2 integers and prints the result

    Args:
        a (int): Dividend
        b (int): Divisor

    Returns:
        Quotient (success); otherwise - None
    """
    try:
        val = a / b
    except ZeroDivisionError:
        val = None
    finally:
        print("Inside result: {}".format(val))
        return val
