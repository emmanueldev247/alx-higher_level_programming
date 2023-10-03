#!/usr/bin/python3
"""Write a function that prints My name is <first name> <last name>
    - Prototype: def say_my_name(first_name, last_name=""):
    - first_name and last_name must be strings otherwise,
      raise a TypeError exception with the message
      first_name must be a string or last_name must be a string
    - You are not allowed to import any module
 """


def say_my_name(first_name, last_name=""):
    """Prints My name is <first name> <last name>

    Args:
        first_name (str): first name
        last_name (str): last name
    """
    err1 = "{} must be a string"

    if type(first_name) != str:
        raise TypeError(err1.format("first_name"))

    if type(last_name) != str:
        raise TypeError(err1.format("last_name"))

    print(f"My name is {first_name} {last_name}")
