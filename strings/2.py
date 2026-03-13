#Implement division that returns "NaN" if denominator is zero.
def division(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Nan"
   

a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
print("Division:",division(a,b))

"""def division(a,b):
    if b==0:
        return "Nan"
    else:
        return a/b
    
num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
print("Result of division:", division(num1, num2))
"""