#!/usr/bin/python3
"""Write a function that prints a text with 2 new lines
    after each of these characters: ., ? and :

    - Prototype: def text_indentation(text):
    - text must be a string, otherwise raise a TypeError exception
    - There should be no space at the beginning
      or at the end of each printed line
    - You are not allowed to import any module
"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these
       characters: ., ? and :

    Args:
        text(str): text to be formatted and displayed
    """

    if type(text) != str:
        raise TypeError("text must be a string")

    char = [".", "?", ":"]
    output = ""
    tmp = ""
    previous_char = ""
    for ch in text:
        tmp += ch
        if ch in char:
            tmp = tmp.strip("\t ")
            tmp += "\n\n"
            output += tmp
            tmp = ""
        elif ch == "\n" and previous_char == " ":
            tmp = tmp.strip("\t ")

        elif previous_char == "\n":
            tmp = tmp.strip("\t ")

        previous_char = ch

    tmp = tmp.strip("\t ")
    output += tmp

    print(output, end="")
