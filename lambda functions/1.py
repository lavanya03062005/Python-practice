"""
You’re given a list of product names with inconsistent casing and extra spaces: 
names = [""  alpha Case  "", ""Beta   unit"", ""gAmMa MODULE  ""]
Use map with a lambda to strip spaces and convert to Title Case (e.g., ""Alpha Case"").
"""
lst=input("enter the list of numbers").split()

result=map(lambda x: x.strip().title(),lst)

print(list(result))