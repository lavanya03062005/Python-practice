# rack running maximum; reset to 0 when value ≤ 0. Output list of running max values.

def running_maximumvalue(lst):
    result=[]
    running_maxvalue=0
    
    for i in lst:
        if i<=0:
            running_maxvalue=0
        else:
            running_maxvalue=max(running_maxvalue,i)
        
        result.append(running_maxvalue)
        
    return result
        
lst=list(map(int,input("Enter the list of numbers").split()))
print(running_maximumvalue(lst))

