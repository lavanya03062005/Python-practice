#  Return list of (element, count) in order of first appearance.

from collections import OrderedDict
def element_count(lst):
    dic=OrderedDict()
    result=[]
    for el in lst:
        dic[el]=dic.get(el,0)+1
    
    for key,value in dic.items():
        result.append((key,value))
    
    return result
    
lst=list(map(int,input("Enter the elements in the list").split()))
print(element_count(lst))

"""
def element_count(lst):
    dic={}
    result=[]
    for el in lst:
        dic[el]=dic.get(el,0)+1
    
    for el in lst:
        if el in dic.keys():
            result.append((el,dic[el]))
            del dic[el]
    
    return result
    
lst=list(map(int,input("Enter the elements in the list").split()))
print(element_count(lst))"""