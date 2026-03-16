# Given a list of tuples (item, category), create a dictionary grouping items under their category.

def group_items(lst):
    
    dic={}
    for item,category in lst:
        if category not in dic:
            dic[category]=[]
        dic[category].append(item)

    return dic

n=int(input("Enter the number of items"))
items=[]
for _ in range(n):
    item=input("Enter the item name")
    category=input("Enter the category")
    items.append((item,category))
print(group_items(items))
