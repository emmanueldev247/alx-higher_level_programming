#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element 2 lists

    Args:
        my_list_1 (list):
        my_list_2 (list):
        my_list_3 (list):
        list_length (int):

    Returns:
        A new list (length = list_length) with all divisions
    """
    new_list = []
    for i in range(list_length):
        try:
            val = my_list_1[i] / my_list_2[i]

        except ZeroDivisionError:
            print("division by 0")
            val = 0

        except TypeError:
            print("wrong type")
            val = 0

        except IndexError:
            print("out of range")
            val = 0

        finally:
            new_list.append(val)

    return new_list
