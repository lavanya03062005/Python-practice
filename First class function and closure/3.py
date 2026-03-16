# Build counter() that returns a function next() which, when called, returns 1, 2, 3, … without using globals.
def counter(start=0):
    count=start
    def next():
        nonlocal count
        count+=1
        return count
    return next
    
m1=counter()
print(m1())
print(m1())