# Given text, return sorted unique words ignoring case.

def sorted_unique(text):
    words=text.lower().split()
    st=set(words)
    return sorted(st)
    
text=input("Enter the text")
print(sorted_unique(text))