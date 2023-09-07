#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as mod1
    import sys

    length = len(sys.argv)
    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    if sys.argv[2] not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]

    if op == '+':
        print("{} {} {} = {}".format(a, op, b, mod1.add(a, b)))

    elif op == '-':
        print("{} {} {} = {}".format(a, op, b, mod1.sub(a, b)))

    elif op == '*':
        print("{} {} {} = {}".format(a, op, b, mod1.mul(a, b)))

    elif op == '/':
        print("{} {} {} = {}".format(a, op, b, mod1.div(a, b)))
