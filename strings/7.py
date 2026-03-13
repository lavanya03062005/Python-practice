# Return squares of even numbers or cubes when odd numbers

def calculate(numbers):
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num**2)
        else:
            result.append(num**3)
    return result

print(calculate([1, 2, 3, 4, 5]))