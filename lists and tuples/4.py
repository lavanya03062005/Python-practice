# Rotate List Right by K (No Slicing)

def rotate_list(lst,k):
    k=k%len(lst)

   
    """for i in range(0,k):
        el=lst.pop(0)
        lst.append(el)"""
    for i in range(0,k):
        el=lst.pop()
        lst.insert(0,el)
        
    return lst

lst=list(map(int,input("Enter the list of elements").split()))
k=int(input("Enter the value of k"))
print(rotate_list(lst,k))    
    

