# Replace all digits in a string with #.
def replace(text):
    result=""
    for char in text:
        if char.isdigit():
            result+="#"
        else:
            result+=char
    return result

print(replace("My phone number is 123-456-7890."))
 
