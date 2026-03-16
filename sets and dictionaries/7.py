# From a dictionary of employee salaries, find the employee with the highest salary.

def highest_salary(dic):
    
    maxsal=0
    empname=""
    for key,value in dic.items():
        if value > maxsal:
            empname=key
            maxsal=value
            
    return empname
    
n=int(input("enter the no of employees"))
dic={}
for i in range(n):
    employee=input("enter the name of employee")
    salary=int(input("enter the salary of employee"))
    dic[employee]=salary
print(highest_salary(dic))