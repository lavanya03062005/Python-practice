#Implement make_multiplier(k) that returns a function multiplying its input by k.

def make_multiplier(k):
    def multiply(x):
        return x*k 
    return multiply 
    
m1=make_multiplier(5)
print(m1(3))
