"""
fibonacci program

Golden Ratio

Application of fibo

Serie

0
1
1
2
3
5
8
13
21
34
55 .....



"""


def fib(number: int):
    """find n-th of fibo series"""
    # fib(n)

    if number == 0:
        return 0
    if number == 1:
        return 1
    return fib(number - 2) + fib(number - 1)


for i in range(10):
    print(f"fibo {i}: {fib(i)}")
