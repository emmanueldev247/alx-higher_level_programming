#!/usr/bin/python3
def print_last_digit(number):
    num = number
    if num < 0:
        num *= -1
    last = num % 10

    while num > 9:
        last = num % 10
        num = last
    print(last, end="")
    return (last)
