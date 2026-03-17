"""
"Create a base class with a protected attribute _salary and a private attribute __bonus.
Show how subclasses can access _salary but not __bonus directly."
"""
class Employee:
    def __init__(self, salary, bonus):
        self._salary = salary
        self.__bonus = bonus
class Manager(Employee):
    def display_salary(self):
        return f"Salary: {self._salary}"
    def display_bonus(self):
        try:
            return f"Bonus: {self.__bonus}"
        except AttributeError:
            return "Cannot access private attribute __bonus directly."
manager = Manager(50000, 10000)
print(manager.display_salary())
print(manager.display_bonus())
