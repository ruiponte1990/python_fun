import timeit

fibArr = [0,1]

def fib(n):
    if n < 0:
        return 0
    elif n <= len(fibArr):
        return fibArr[n-1]
    else:
        tmp = fib(n-1) + fib(n-2)
        fibArr.append(tmp)
        return tmp



print(timeit.Timer('fib(5);fib(3);fib(10);fib(100)', 'from __main__ import fib').timeit())