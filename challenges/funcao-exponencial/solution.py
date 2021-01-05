import math


def calcula_euler(x, n):
    euler = 0
    while n > 0:
        n -= 1
        euler += (x**n) / math.factorial(n)
    return euler
