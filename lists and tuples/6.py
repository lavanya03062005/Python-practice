# Return squares of even numbers from a list.
def squares_of_even_numbers(lst):
    
    result=[]
    result = [x*x for x in lst if x%2==0]
    return result
    
lst=list(map(int,input("Enter the list of numbers").split()))
print(squares_of_even_numbers(lst))