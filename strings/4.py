#Receive an amount, apply discount: <1000 → 0%, 1000–4999 → 5%, >=5000 → 10%. Return final payable.
def calculatediscount(price):
    if price < 1000:
        return price
    elif price >= 1000 and price < 5000:
        return price - (price * (5/100))
    else:
        return price - (price * (10/100))
    
print(calculatediscount(500))
print(calculatediscount(2000))