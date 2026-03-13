# Multiplication Table (1..N) 
def multiplication_table(n):
    for i in range(1,n+1):
        print("Table of ",i)
        for j in range(1,11):
            print(i,"x",j,"=",i*j)

n=int(input("Enter the number: "))
multiplication_table(n)