""" To calculate a prime number """

for number in range(101):
    if number > 1:
        for adad in range(2, number):
            if (number % adad) == 0:
                break
        else:
            print(number)
