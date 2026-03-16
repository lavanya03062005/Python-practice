# Convert a list with duplicates into a list of unique elements while preserving no order.

def unique_elements(lst):
    return list(set(lst))

lst=list(map(int,input("Enter the list of numbers").split()))
print(unique_elements(lst))
