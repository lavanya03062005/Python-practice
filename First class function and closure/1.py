#  Write a function apply_twice(func, x) that takes another function func and a value x, then returns func(func(x)).

def add_one(n):
    return n+1
    
def apply_twice(func,x):
    return func(func(x))
    
print(apply_twice(add_one,5))