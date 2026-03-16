"""
Write fib(n) that computes the nth Fibonacci number efficiently with memoization. Provide two versions:
Using a dictionary cache inside the function,
Using a custom @memoize decorator that caches by arguments.
"""
# using a dictionary cache inside the function
def fibonocci(n,dp={}):
     if n in dp:
         return dp[n]
     if n<=1:
         return n
         
     result=fibonocci(n-1,dp)+fibonocci(n-2,dp)
     dp[n]=result
     return result
     
print(fibonocci(5))

# using a custom @memoize decorator that caches by arguments.

def memoize(func):
    cache={}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result=func(*args)
        cache[args]=result
        return result
    return wrapper
@memoize
def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
    
print(fib(3))