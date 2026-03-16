"""
"Write two generators:
gen_numbers() yields numbers 1–10.
gen_squares() takes numbers and yields their squares.
Chain them together to print squares of 1–10."
"""
def generate_numbers():
     for i in range(1,11):
         yield i
         
def generate_squares(numbers):
    for i in numbers:
        yield i*i
        
for i in generate_squares(generate_numbers()):
    print(i,end=' ')
