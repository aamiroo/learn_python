import math
import sys

def mashinhesab():
    try:
        print()
        a = input("enter first number (or exit): ")

        if a.lower() == "exit":
            sys.exit()
        b = input("enter second number: ")
        a = float(a)
        b = float(b)

        act = input("+ - / % * : ")

        if act == "+":
            return a + b
        elif act == "-":
            return a - b
        elif act == "*":
            return a * b
        elif act == "/":
            return a / b
        else:
            return "not information"
    except ValueError:
        print("Please do the right thing.")

while True:
    a = mashinhesab()
    print(a)