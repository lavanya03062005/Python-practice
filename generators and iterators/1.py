# Write a generator function count_up_to(n) that yields numbers from 1 to n.
 
def generate_n(n):
    for i in range(1,n+1):
        yield i


n=int(input("Enter the value of n"))        
for i in generate_n(n):
    print(i,end=' ')
    