"""
"Implement python function aggregate(*nums, op=""sum"") supporting:
op=""sum"" → sum of numbers,
op=""avg"" → average (float),
op=""max"" → maximum.
If no numbers provided, return None."
"""
def aggregate(*nums,op="sum"):
    if not nums:
        return None
    if op=="sum":
        return sum(nums)
    elif op=="avg":
        return sum(nums)/len(nums)
    elif op=="max":
        return max(nums)
    else:
        raise ValueError("Unsupported Operation")
    
lst=list(map(int,input("Enter the list of numbers").split()))
op=input("Enter the operation")
print(aggregate(*lst,op=op))