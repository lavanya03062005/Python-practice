"""
Create check_strength(pwd: str, min_len=8) -> dict returning:
{
  "length_ok": bool,
  "has_upper": bool,
  "has_lower": bool,
  "has_digit": bool,
  "has_special": bool,
  "score": int  # sum of True values
}
Special characters are anything not alphanumeric.
"""

def check_password_strength(pwd:str,min_len=8) -> dict:
    
    length_ok = len(pwd)>=min_len
    has_upper = any(ch.isupper() for ch in pwd)
    has_lower = any(ch.islower() for ch in pwd)
    has_digit = any(ch.isdigit() for ch in pwd)
    has_special = any(not ch.isalnum() for ch in pwd)
    score=sum([length_ok,has_upper,has_lower,has_digit,has_special])
    dic={
         "length_ok": length_ok,
         "has_upper": has_upper,
         "has_lower": has_lower,
         "has_digit": has_digit,
         "has_special": has_special,
         "score": score
    }
    return dic
    
    
print(check_password_strength("Python@123"))