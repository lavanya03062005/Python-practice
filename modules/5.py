"""
Create a package utilities with two modules: string_utils.py and math_utils.py. Import functions from both and demonstrate usage.
"""

import utilities.math_utils as math
import utilities.string_utils as string

print(math.add(10, 5))
print(math.subtract(10, 5)) 
print(string.to_uppercase("hello world"))
print(string.title_case("hello world"))
print(string.reverse_string("hello world"))