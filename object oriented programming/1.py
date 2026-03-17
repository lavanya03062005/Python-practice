#  "Create a class Student with a class variable school_name and instance variables name and roll_no.Show how changing school_name affects all objects."

class Student:
    school_name="sri chaitanya school"
    
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        
    def show_details(self):
        print("School name=",self.school_name)
        print("Name=",self.name)
        print("Roll no=",self.rollno)
        print()
        
obj1=Student("rohan","588")
obj2 = Student("Rahul", "589")
obj1.show_details()
obj2.show_details()

Student.school_name="Narayana school"
obj1.show_details()
obj2.show_details()
