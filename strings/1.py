#Count occurrences of a substring allowing overlaps.
def count_occurences(text,sub):
    start=0
    count=0
    while True:
        pos=text.find(sub,start)
        if pos==-1:
            break
        count+=1
        start=pos+1
    return count

text=input("Enter the text: ")
sub=input("Enter the substring to search: ")   
print("Number of occurrences:", count_occurences(text, sub))
