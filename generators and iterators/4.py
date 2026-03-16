# Use a generator expression to compute the sum of squares of numbers from 1 to 100.

result= sum(x*x for x in range(1,101))
print(result)