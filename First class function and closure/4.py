# Build make_accumulator(start=0) returning add(value) that adds value to an internal total and returns the new total.

def make_accumulator(start=0):
    def add(value):
        nonlocal start
        start+=value
        return start
    return add
    
acc=make_accumulator()
print(acc(5))
print(acc(10))