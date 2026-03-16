# Write a generator that yields the first n Fibonacci numbers.

def fib(n):
    a,b=0,1
    
    for i in range(n):
        yield a
        c=a+b
        a=b 
        b=c
        
n=int(input("Enter the value of n"))        
for i in fib(n):
    print(i,end=' ')
    