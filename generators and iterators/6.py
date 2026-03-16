# Create a generator infinite_even() that yields even numbers indefinitely.


def infinite_even():
    n=0
    while True:
        yield n 
        n=n+2
        
gen=infinite_even()

for i in range(10):
    print(next(gen),end=' ')