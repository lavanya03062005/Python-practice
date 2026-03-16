# Given a dict and a target value, return all keys mapping to that value.

def keys_equal_target(dic,target):
    
    result=[]
    for key,value in dic.items():
        if value==target:
            result.append(key)
            
    return result
    
dic={"a":2,"b":3,"c":5,"d":2}
print(keys_equal_target(dic,2));
    
"""
def keys_equal_target(dic,target):
    
    return [k for k,v in dic.items() if v==target]
    
dic={"a":2,"b":3,"c":5,"d":2}
print(keys_equal_target(dic,2));
"""