#Given income, credit_score, and existing_debt, determine "Eligible", "Review", or "Reject" using sensible thresholds.
def check(income,credit_score,existing_debt):
    if income>= 50000 and credit_score>=700 and existing_debt <= 20000:
        return "Eligible"
    elif income>=30000 and credit_score>=600 and existing_debt<=30000:
        return "Review"
    else:
        return "Reject"

print(check(60000,750,15000))
print(check(35000,650,25000))
print(check(25000,550,35000))