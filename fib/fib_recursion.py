import timeit

def fib(n):
    if n < 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return  fib(n-1) + fib(n-2)

print(timeit.Timer('fib(5);fib(3);fib(10)', 'from __main__ import fib').timeit())