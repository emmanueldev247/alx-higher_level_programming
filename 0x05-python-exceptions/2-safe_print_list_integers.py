#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list and only integers

    Args:
        my_list (list): List to print from
        x (int): the number of elements to print from my_list

    Returns:
        number of elements printed
    """
    num = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            num += 1
        except (TypeError, ValueError):
            continue
    print()
    return num
