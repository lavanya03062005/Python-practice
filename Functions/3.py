# Write make_counter(start=0) that returns a function counter() which, each time it’s called, increments and returns the next value (1, 2, 3 … starting from start+1).

def make_counter(start=0):
    count=start
    
    def counter():
        nonlocal count
        count+=1
        return count
    return counter
    
c=make_counter(5)
print(c())
print(c())
print(c())