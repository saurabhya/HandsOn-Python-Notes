import time
# recusive style implementation of fibonacci sequence

def fib(n):
    if n<=2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

# lookup table implementation of fibonscci using DP with memorization

def dp_fib(n, lookup):
    if n<=2:
        lookup[n]=1
    if lookup[n] is None:
        lookup[n] = dp_fib(n-1, lookup) + dp_fib(n-2, lookup)
    return lookup[n]
'''
A second technique in dynamic programming involves the use of table or matrix in some cases,
to store the results og computations for later use.

This approach solves bigger problem by first working out a route to the final solution.
In that case o fthe fib() function, we develop a table with values of fib(1) and fib(2) predetrminated.
Based on these values we work our way to fib(n)
'''
def dp_fib2(n):
    results = [1,1]

    for i in range(2,n):
        results.append(results[i-1]+results[i-2])
    return results[-1]

map_set = [None]*1000

a = time.time()
print(fib(20))
b = time.time()
print("TIme taken by recursive implementation: {}".format(b-a))
a = time.time()
print(dp_fib(20, map_set))
b= time.time()
print("Time taken by DP implementation : {}".format(b-a))

a = time.time()
print(dp_fib2(20))
b= time.time()
print("Time taken by DP implementation : {}".format(b-a))