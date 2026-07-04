""" Simple calculator """

import math
import sys

def calculator():
    try:
        print ("Type \"exit\" to quit.\nor")
        a = input("Enter first number: ")

        if a.lower() == "exit":
            sys.exit()
        b = input("Enter second number: ")
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
    run = calculator()
    print(run)