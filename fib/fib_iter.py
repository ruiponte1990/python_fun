import timeit

def fib(n):
    first = 0
    second = 1
    if n < 0:
        return first
    elif n == 0:
        return first
    elif n == 1:
        return second
    else:
        for i in range(2, n):
            next_ = second + first
            first = second
            second = next_
        return second
   
print(timeit.Timer('fib(5);fib(3);fib(10);fib(100)', 'from __main__ import fib').timeit())