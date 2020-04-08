#!/usr/bin/env python


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x/y


operations = {"+": add, "-": sub, "*": mul, "/": div, "**": pow}
print("dictionary", operations)


while True:
    expr = input("Enter a math expression: ")  # "100 / 5"

    if expr.lower() == 'q':
        break

    v1, op, v2 = expr.split()  # ["100", "/", "5"]
    v1 = float(v1)
    v2 = float(v2)

    if op not in operations:
        print(f"we do not know the {op} operator yet.")
        continue

    f = operations[op]
    result = f(v1, v2)

    print("{:.3f}".format(result))
