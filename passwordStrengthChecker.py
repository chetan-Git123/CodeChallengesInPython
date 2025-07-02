'''
Create a function named check_password_strength that takes one argument:
password (a string) - the password to be checked.

Evaluate the password based on these criteria:
    At least 8 characters long.
    Contains at least one uppercase letter (A-Z).
    Contains at least one lowercase letter (a-z).
    Contains at least one digit (0-9).
    Contains at least one special character (e.g., !, @, #, $, etc.).

Return "Weak" (less than 3 criteria), "Moderate" (3 or 4 criteria), or "Strong" (5 criteria) based on how many criteria it satisfies.
'''

import re

def check_password_strength(password):
    # Write code here
    criteriaCount = 0

    if len(password)>=8:
        criteriaCount = criteriaCount+1
    upperCaseBooleanVal = bool(re.search(r"[A-Z]", password))
    if upperCaseBooleanVal:
        criteriaCount = criteriaCount+1
    lowerCaseBooleanVal = bool(re.search(r"[a-z]", password))
    if lowerCaseBooleanVal:
        criteriaCount = criteriaCount+1
    if re.search('[0-9]', password):
        criteriaCount = criteriaCount+1
    pattern = r'[^\w\s]' 
    specCharBooleanVal =  bool(re.search(pattern, password))
    if specCharBooleanVal:
        criteriaCount = criteriaCount+1
    
    if criteriaCount==5:
        return "Strong"
    elif criteriaCount<5 and criteriaCount>=3:
        return "Moderate"
    else:
        return "Weak"
