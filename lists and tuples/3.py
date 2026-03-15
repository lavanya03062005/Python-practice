# Return the index of the second largest distinct element; if not exists, return -1.

def second_largest_unique(lst):
    
    uniquelst=list(set(lst))
    
    if len(uniquelst) < 2:
        return -1
        
    secondlargest = sorted(uniquelst)[-2]
    return lst.index(secondlargest)

    
lst=list(map(int,input("Enter the list of numbers").split()))
print(second_largest_unique(lst))