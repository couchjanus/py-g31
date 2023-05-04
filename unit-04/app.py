# phone book
from tabulate import tabulate

contacts = []

contact_item = {}

contact_item = {
    'first_name': 'john',
    'last_name': 'doe',
    'home_mobile': 380501234567,
    'office_mobile': 380671234567
}

contacts.append(contact_item)

# print(contact_item['first_name'])
# print(contact_item.get('last_name'))

def helper():
    print('''Awailable:
          h: Help
          v: View
          a: Add New
          d: Delete
          s: Search
          u: Update
          q: Quit
          ''')

def full_name(contact):
    return ' '.join([contact['first_name'].title(), contact['last_name'].title()])

def add_item():
    contact = {}
    contact['first_name'] = input('Enter Your First Name: ').strip().lower()
    contact['last_name'] = input('Enter Your Last Name: ').strip().lower()
    contact['home_mobile'] = input('Enter Your Home Mobile: ').strip()
    contact['office_mobile'] = input('Enter Your Office Mobile: ').strip()
    # print(contact)
    return contact
    # pass
def delete_item():
    pass
def update_item(contact):
    first_name = input('Enter Your First Name: ').strip().lower() or contact['first_name']
    last_name = input('Enter Your Last Name: ').strip().lower() or contact['last_name']
    home_mobile = input('Enter Your Home Mobile: ').strip() or contact['home_mobile']
    office_mobile = input('Enter Your Office Mobile: ').strip() or contact['office_mobile']
    contact.update({'first_name':first_name, 'last_name': last_name, 'home_mobile':home_mobile, 'office_mobile':office_mobile})
    pass
def search_item():
    pass
def view_items(contact):
    print(full_name(contact))
    pass

while True:
    choice = input('Take Your choice (h|v|a|d|s|u|q): ').strip().lower()
    
    match choice:
        case 'h'|'help':
            helper()
        case 'a'|'add':
            contacts.append(add_item())
        case 'v'|'view':
            # view_items(contact_item)
            # print(contacts)
            data = []
            for contact in contacts:
                name = full_name(contact)
                *tmp, hm, om = list(contact.values())
                data.append([name, hm, om])
                    
            if len(data) == 0:
                print('contacts list is ampty')
            else:
                col_names = ['Contact Name', 'Home Mobile', 'Office Mobile']
                
                print(tabulate(data, headers=col_names, tablefmt="fancy_grid", showindex='always')) 
            
        case 'd'| 'del'|'delete':
            c_n = int(input('Enter the number of the contact You wish delete: '))
            if c_n in range(len(contacts)):
                confirm = input('Are You sure You wish to delete this contact? y/n').strip()
                if confirm.lower() in ('yes', 'y'):
                    contacts.pop(c_n)
                
            else: print('That contact does not exist!')
        case 's':
            first_name = input('Enter the name of contact details You wish to view: ').strip().lower()
            data = []
            for contact in contacts:
                if contact['first_name'] == first_name:
                    name = full_name(contact)
                    *tmp, hm, om = list(contact.values())
                    data.append([name, hm, om])
                    
            if len(data) == 0:
                print('That contact does not exist')
            else:
                col_names = ['Contact Name', 'Home Mobile', 'Office Mobile']
                
                print(tabulate(data, headers=col_names, tablefmt="fancy_grid", showindex='always')) 
            
        case 'u':
            c_n = int(input('Enter the number of the contact You wish update: '))
            if c_n in range(len(contacts)):
                update_item(contacts[c_n])
            else: print('That contact does not exist!')
        case 'q':
            print('Thanks for using the Phone Book')
            break
        case other:
            print('No match found. Text help please.')
