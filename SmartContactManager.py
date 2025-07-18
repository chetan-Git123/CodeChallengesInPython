'''
Create a function named organize_contacts that processes a list of contact dictionaries to create a clean contact database.

Each contact dictionary in the input list has these keys:
    name: The person's name
    email: The person's email address
    phone: The person's phone number

Your function should:
    Remove duplicate contacts (contacts with the same email or phone number)
    Standardize all emails to lowercase
    Filter out contacts with invalid email addresses
    Filter out contacts with invalid phone numbers
    Return a list of cleaned contact dictionaries

Validation rules:
    Valid email: Must contain '@' and '.', and must not have spaces
    Valid phone: Must contain exactly 10 digits (ignore non-digit characters like dashes or parentheses)
'''
cleaned_contact_list=[]

#Checks if the email in a contact is valid
def isEmailValid(email):
    validStatus = True
    if '@' not in email:
        return False
    if '.' not in email:
        return False
    if ' ' in email:
        return False
    return validStatus

#Converts email to all lower case letters
def emailToLowerCase(email):
    return email.lower()

#Checks if the phone number in a contact is valid
def isPhoneNumValid(phone):
    phoneWithOnlyNumericChar = filter(lambda char:char.isdigit(),phone)
    if len(list(phoneWithOnlyNumericChar))==10:
        return True
    else:
        return False

def organize_contacts(contact_list):
    #Solution
    # 1. Create helper functions for validation (email and phone)    
    # 2. Process each contact
    # - Clean email (lowercase) and phone (digits only)
    # - Check if email and phone are valid
    # - Check for duplicates
    # 3. Return the clean contact list
    seen_phones = set()  # Set to track unique phone numbers
    seen_emails = set() # Set to to track unique emails
    for contact in contact_list:
        if not isEmailValid(contact['email']):
            continue
        if not isPhoneNumValid(contact['phone']):
            continue
        cleaned_contact = contact.copy()
        phoneWithOnlyNumericChar = filter(lambda char: char.isdigit(), cleaned_contact['phone'])
        phone_digits_only = ''.join(filter(str.isdigit, cleaned_contact['phone']))
        lowercased_email = emailToLowerCase(cleaned_contact['email'])

        # Check for email duplicates
        if lowercased_email in seen_emails:
            continue
        # Check for phone number duplicates
        if phone_digits_only in seen_phones:
            continue  # Skip duplicates

        seen_emails.add(lowercased_email)
        seen_phones.add(phone_digits_only)
        cleaned_contact['phone'] = phone_digits_only
        cleaned_contact['email'] = lowercased_email
        cleaned_contact_list.append(cleaned_contact)
    return cleaned_contact_list

             





       

        
