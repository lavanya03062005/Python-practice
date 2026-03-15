# Compute cumulative sum; stop when a negative number is encountered.

def cumulative_sum(lst):
    total=0
    
    for x in lst:
        if x < 0:
            break
        total+=x
        
    return total
    
lst=list(map(int,input("Enter the list of numbers").split()))
print(cumulative_sum(lst))
    