#!/usr/bin/python3
def roman_to_int(roman_string):
    """Converts a Roman numeral to an integer"""
    if not roman_string.isalpha() or roman_string is None:
        return None

    roman_value = {"I": 1, "V": 5, "X": 10,
                   "L": 50, "C": 100, "D": 500, "M": 1000}
    value = 0
    for i in roman_string:
        for key, val in roman_value.items():
            if i == key:
                value += val
    return value
