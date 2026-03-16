# Count the frequency of each word in a given paragraph and return a dictionary sorted by frequency.

def count_freq_words(text):
    
    words=text.lower().split()
    dic={}
    for word in words:
        dic[word]=dic.get(word,0)+1
        
    dic1=dict(sorted(dic.items(),key=lambda x : x[1]))
    return dic1
    
text=input("enter the paragraph")
print(count_freq_words(text))
    
    