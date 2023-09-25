#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """Executes a function safely

    Args:
        fct (function): pointer to a function
        *args (variadic arguments)

    Returns:
        result of function if no error
        otherwise None and error details
    """
    try:
        return fct(*args)
    except BaseException as error:
        sys.stderr.write("Exception: {}\n".format(error))
        return None
