# Password Check- Allow up to 3 attempts; on success return "Unlocked" else "Locked".

def password_check():
    correct_pas="PythonTest"
    
    for i in range(3):
        password=input("Enter the password")
        
        if password == correct_pas:
            return "unlocked"
            
    return "locked"
    
print(password_check())
