# Interleave two lists element-wise, stopping when one ends.

def interleave(lst1,lst2):
     
    result=list()
    for a,b in zip(lst1,lst2):
        result.extend([a,b])
    
    return result
"""n=min(len(lst1),len(lst2))
    result=[]
    
    for i in range(n):
        result.append(lst1[i])
        result.append(lst2[i])
        
    return result"""
    
lst1=list(map(int,input("Enter the first list of numbers").split()))
lst2=list(map(int,input("Enter the second list of numbers").split()))
print(interleave(lst1,lst2))

    
        
        
    