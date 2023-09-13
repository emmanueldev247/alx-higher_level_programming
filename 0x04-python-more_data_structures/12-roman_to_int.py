#!/usr/bin/python3
def roman_to_int(roman_string):
    """Converts a Roman numeral to an integer"""
    if not roman_string.isalpha() or roman_string is None or not roman_string:
        return None

    roman_value = {"I": 1, "V": 5, "X": 10,
                   "L": 50, "C": 100, "D": 500, "M": 1000}
    value = 0
    previous = 0
    for i in reversed(roman_string):  # Start from the right and move left
        val = roman_value.get(i, 0)
        if val < previous:
            value -= val
        else:
            value += val
        previous = val

    return value
