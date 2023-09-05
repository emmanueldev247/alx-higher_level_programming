#!/usr/bin/python3
def uppercase(str):
    result = ""
    for c in str:
        val = ord(c)
        if val >= 97 and val <= 122:
            result += chr(val - 32)
        else:
            result += c
    print("{}".format(result))
