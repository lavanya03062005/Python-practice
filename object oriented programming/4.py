"""
"Create a class MathUtils with:
A @staticmethod for add(a, b).
A @classmethod that returns the class name.
Show how both are called without creating an object."
"""

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def get_class_name(cls):
        return cls.__name__
result = MathUtils.add(5, 3)    
print(f"Result of add: {result}")
class_name = MathUtils.get_class_name()
print(f"Class name: {class_name}")
