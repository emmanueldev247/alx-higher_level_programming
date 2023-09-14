#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """Function that deletes keys with a specific value in a dictionary"""
    to_del = []
    for key, val in a_dictionary.items():
        if val == value:
            to_del.append(key)
    for key in to_del:
        del a_dictionary[key]
    return a_dictionary
