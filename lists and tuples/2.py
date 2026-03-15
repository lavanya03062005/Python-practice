# Convert [a,b,c,d,e] to [(a,b),(c,d)] and ignore the last if odd length. Use Tuple List

def convert_to_tuples(lst):
    """result=[]
    for i in range(0,len(lst)-1,2):
        result.append((lst[i],lst[i+1]))
    return result"""
    return list(zip(lst[::2],lst[1::2]))
    
lst=list(map(int,input("enter the list of numbers").split()))
print(convert_to_tuples(lst))