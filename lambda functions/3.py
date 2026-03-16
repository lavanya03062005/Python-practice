#Calculate Weighted Score Aggregationusing reduce when given lists of scores and weights.

from functools import reduce
scores=list(map(int,input("enter the prices").split()))
weights=list(map(int,input("enter the prices").split()))

result=reduce(lambda acc,x: acc+x[0]*x[1],zip(scores,weights),0)

print(result)
