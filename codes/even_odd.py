""" even and odd """

a = input ("For numbers between 0 and 100, do you want the even numbers or the odd ones? ")
def even ():
    for number in range(101):
        if number % 2 == 0:
            print(number)
def odd ():
    for number in range(101):
        if number % 2 == 1:
            print(number)
if a == "even":
    even()
if a == "odd":
    odd()
