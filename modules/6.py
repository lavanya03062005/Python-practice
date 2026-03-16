""""Write a program that tries to import a non-existent module and handles the ModuleNotFoundError gracefully.
Suggest a fallback mechanism."
"""
try:
    import advancedmath
    print("advancedmath module imported successfully.")
    print("Factorial of 5:", advancedmath.factorial(5))
except ModuleNotFoundError:
    print("advancedmath module not found. Using math module as a fallback.")
    import math
    print("Factorial of 5 using math module:", math.factorial(5))