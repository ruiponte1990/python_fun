# Fibonacci  

Here are four different ways to calculate a fibonacci sequence up to the nth digit.  

### fib_iter.py  

The first solution I thought of to solve this problem. There are two variables, first and second, which are initialized to 0 and 1 respectively.  Then you iterate between two and n, setting the next iteration to be the sum of first and second, and then setting first to be second, and finally second equal to the sum to move forward to the next iteration.  

#### performance with timeit: 6.40641999245 seconds

### fib_recursion.py  

The second way to solve this problem is recursively. Since the next iteration in the sequence will be: 

##### Sn = Sn-1 + Sn-2  

You can just call the function multiple times until you get to the smallest two numbers which will be 1 and 2. This solution is impractical however. As n grows large the function calls and variables will need too much memory and might cause a stack overflow.  Also it is inefficient since you are solving the same problem repeatedly instead of only once.  
For example when you solve for:  

##### fib(4) = fib(3) + fib(2)
##### fib(3) = fib(2) + fib(1)
##### fib(2) = fib(1) + fib(1)  

You have one more call to fib(2) than you need, and two unnecessary calls to fib(1).  

#### performance with timeit: Didn't finish 
Even removing the last call ( n = 100 ) it took 13.7212889194 seconds. Clearly this isn't an acceptable solution.

### fib_dynamic.py  

The third solution to this problem uses dynamic programming to maintain the simplicity of the recursive function without the associated memory and redundancy issues. When you have the solution to fib(n), you store the solution in an array so you don't need to calculate it again.

If you look at lines 6 and 7:

elif n <= len(fibArr):  
return fibArr[n-1]

The function checks how far along in the sequence we are by comparing the input of the function to the length of the stored array. If it is less than the array length then it knows it can just return the stored value without calling it itself again.  

#### performance with timeit: 0.575966119766 seconds

# fib_gen.py  

I also thought it might be cool to try this problem using a generator since I knew that was a method to avoid storing values in memory. However since generators essentially allow you to convert a function into an iterator it ends up basically working the same as the first solution. It is a little faster though!

#### performance with timeit: 1.30446720123 seconds