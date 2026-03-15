# From a list, remove duplicates while keeping the last occurrence of each element.

def remove_duplicates(l1):
    """Function to remove duplicates that keeps last occurence of each element"""
    seen=set()
    uniquelist=[]
    
    for i in reversed(l1):
        if i not in seen:
            uniquelist.append(i)
            seen.add(i)
        
    return list(reversed(uniquelist))

l1=list(map(int,input("enter the list of elements").split()))
print(remove_duplicates(l1))