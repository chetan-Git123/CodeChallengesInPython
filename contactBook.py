'''
Build a Contact Book application step by step by breaking it into small, manageable functions.
The user can view their contacts. They should have the ability to add, delete and modify contacts.
'''

def display_menu():
    print('Contact Book Menu:')
    print('1. Add Contact')
    print('2. View Contact')
    print('3. Edit Contact')
    print('4. Delete Contact')
    print('5. List All Contacts')
    print('6. Exit')

def add_contact(contactDict):
    name = input()
    phone = input()
    email = input()
    address = input()
    if name in contactDict:
        print('Contact already exists!')
    else:
        contactDict[name] = {
	    "phone": phone,
	    "email": email,
	    "address": address
        }
        print('Contact added successfully!')

def view_contact(contactDict):
    name = input()
    if name in contactDict:
        print(f'Name: {name}')
        print(f'Phone: {contactDict[name]['phone']}')
        print(f'Email: {contactDict[name]['email']}')
        print(f'Address: {contactDict[name]['address']}')
    else:
        print('Contact not found!')

def edit_contact(contactDict):
    name = input()
    if name in contactDict:
        phone = input()
        email = input()
        address = input()   
        contactDict[name]['phone'] = phone
        contactDict[name]['email'] = email
        contactDict[name]['address'] = address
        print('Contact updated successfully!')
    else:
        print('Contact not found!')

def delete_contact(contactDict):
    name = input()
    if name in contactDict:
        del contactDict[name]
        print('Contact deleted successfully!')
    else:
        print('Contact not found!')

def list_all_contacts(contactDict):
    if len( contactDict.keys() )==0:
        print('No contacts available.')
    else:
        for key in contactDict.keys():
            print(f'Name: {key}')
            print(f'Phone: {contactDict[key]['phone']}')
            print(f'Email: {contactDict[key]['email']}')
            print(f'Address: {contactDict[key]['address']}')
            print('')

# Execution of the functionality
display_menu()
contactDict = {}
userInput = None
while userInput!=6:
    userInput = int( input() )
    if userInput==1:
        add_contact(contactDict)
        display_menu()
    elif userInput==2:
        view_contact(contactDict)
        display_menu()
    elif userInput==3:
        edit_contact(contactDict)
        display_menu()
    elif userInput==4:
        delete_contact(contactDict)
        display_menu()
    elif userInput==5:
        list_all_contacts(contactDict)
        display_menu()
    elif userInput==6:
        break
