# Use itertools.islice() to take the first 5 elements from an infinite generator of multiples of 3.

import itertools
def multiples_of_three():
    n=1
    while True:
        yield 3*n 
        n+=1
        
gen=multiples_of_three()
for i in itertools.islice(gen,10):
    print(i,end=' ')