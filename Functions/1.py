"""
"Write a function normalize_name(s: str) -> str that:
Strips extra whitespace,
Converts to title case,
Collapses multiple spaces into single spaces.
If s is empty or contains only spaces, return 
"""
def normalize_names(text : str) -> str:
   if not text or text.split()=="":
       return ""
   return " ".join(text.split()).title()
  
print(normalize_names("   hi   hello  how are you    "))
    
