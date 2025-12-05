import math

op = input()

if op in ["+", "-", "*", "/", "%", "**", "//"]:
    a = float(input())
    b = float(input())
    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        print(a / b if b != 0 else "err")
    elif op == "%":
        print(a % b)
    elif op == "**":
        print(a ** b)
    elif op == "//":
        print(a // b)

elif op == "sqrt":
    a = float(input())
    print(math.sqrt(a))

elif op == "cbrt":
    a = float(input())
    print(a ** (1/3))
