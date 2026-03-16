# Merge two inventory dicts by summing quantities of same keys.

def merge_inventories(inv1,inv2):
    result=inv1.copy()
    
    for key,value in inv2.items():
        if key in result:
            result[key]+=value
        else:
            result[key]=value
            
    return result
        
inv1={"apple":10,"banana":5,"grapes":2}
inv2={"guava":5,"apple":1,"kiwi":1,"grapes":5}
print(merge_inventories(inv1,inv2))    