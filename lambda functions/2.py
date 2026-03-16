# Create a Price Update Pipeline (map → filter → reduce), give n list of product prices, apply 10% discount,  keep only items ≥ ₹200 after discount and compute the final bill total.

from functools import reduce
lst=list(map(int,input("enter the prices").split()))

result= map(lambda x: x-x*0.1,lst)
result1= filter(lambda x: x>=200,result)
result2=reduce(lambda x,y:x+y,result1,0)

print(result2)