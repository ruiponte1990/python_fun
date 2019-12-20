import timeit

def fib(n):
    first = 0
    second = 1
    i = 2
    while True:
        if (i > n):
            return
        else:
            yield second 
            next_ = second + first
            first = second
            second = next_
            i += 1

print(timeit.Timer('fib(5);fib(3);fib(10);fib(100)', 'from __main__ import fib').timeit())