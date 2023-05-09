# units_03-04.py

# Напишіть програму для перевірки, чи є введене число простим
a=int(input("enter a number"))     
if a>1:
    for x in range(2,a):
        
        if(a%x)==0:
            print("not prime")
            break
        else:
            print("Prime")
else:
    print("not prime")

# Напишіть програму розпаковки кортежу на кілька змінних.
#create a tuple
tuplex = 4, 8, 3 
print(tuplex)
n1, n2, n3 = tuplex
#unpack a tuple in variables
print(n1 + n2 + n3) 
#the number of variables must be equal to the number of items of the tuple
# n1, n2, n3, n4 = tuplex 

# Напишіть програму Python для перетворення кортежу в рядок.
tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
str =  ''.join(tup)
print(str)

# Напишіть програму Python, щоб перевірити, чи існує елемент у кортежі.
tuplex = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
print("r" in tuplex)
print(5 in tuplex)

# Напишіть програму для реверсу кортежу.
#create a tuple
x = ("w3resource")
# Reversed the tuple
y = reversed(x)
print(tuple(y))
#create another tuple
x = (5, 10, 15, 20)
# Reversed the tuple
y = reversed(x)
print(tuple(y))

# Напишіть програму, щоб отримати список, відсортований у порядку зростання за останнім елементом у кожному кортежі з заданого списку непорожніх кортежів.

def last(n): return n[-1]

def sort_list_last(tuples):
  return sorted(tuples, key=last)

print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

# Напишіть програму, щоб перевірити, порожній список чи ні.
l = []
if not l:
  print("List is empty")

# Напишіть програму для друку номерів із зазначеного списку після видалення з нього парних чисел.
num = [7, 8, 120, 25, 44, 20, 27]
nums = []
# num = [x for x in num if x%2!=0]
for x in num:
    if x%2!=0:
        nums.append(x)
        print(x)
print(nums)

# Створити просту гру на відгадування чисел, яка дозволяє користувачеві вгадувати випадкове число від 1 до 100.  Програма повинна надавати підказки користувачеві після кожного вгадування, вказуючи, чи було його припущення завеликим або замалим,  доки користувач вгадує правильне число.
# Почніть з імпорту модуля random, який дозволить вам згенерувати випадкове число. Згенеруйте випадкове число від 1 до 100 за допомогою функції randint() із модуля random і призначте його змінній.
# Створіть цикл, де користувачі вгадуватиме число, поки не вгадає правильно. У циклі запропонуйте користувачеві ввести число за допомогою функції input().
# Додайте умовний оператор у середині циклу, який перевіряє, чи припущення користувача є правильним, занадто високим чи малим. Якщо припущення вірне, роздрукуйте вітальне повідомлення та вийдіть із циклу. Якщо припущення завелике або занизьке, надрукуйте повідомлення-підказку, щоб допомогти користувачеві правильно вгадати число. 
import random

secret_number = random.randint(1, 100)

while True:
    guess = int(input("Guess the number between 1 and 100: "))
    
    if guess == secret_number:
        print("Congratulations! You guessed the number!")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

# До програми управління контактами додати метод очищення списку словників.
# Додати вимогу обов’язкового заповнення всіх значень словника
# Додати перевірку значення поля телефонного номера з такими вимогами
# Номер телефона має бути числом
# Номер телефона має бути довжиною 12
# Номер телефона не повинен мати дублів у списку словників

# Додати вимогу унікальності значення повного імені  

contacts = []

contact_item = {
                   'first_name':'john', 
                   'last_name':'doe', 
                   'home_mobile':'1422155', 
                   'office_mobile':'1563231'
                }

contacts.append(contact_item)

def full_name(contact):
	return ' '.join([contact['first_name'].title(), contact['last_name'].title()])

def is_valid_phone(x):
    return x.isdigit() and len(x) == 12

def is_valid_name(x):
    return len(x) >= 2

def add_item():
    contact = {}
    
    first_name = input('Enter Your First Name: ').strip().lower()
    
    while not is_valid_name(first_name):
        first_name = input('Please Enter Your First Name: ').strip().lower()
    else:
        contact['first_name'] = first_name
    
    last_name = input('Enter Your Last Name: ').strip().lower()
    while not is_valid_name(last_name):
        last_name = input('Enter Your Last Name: ').strip().lower()
    else:
        contact['last_name'] = last_name
    
    home_mobile = input('Please Enter a home mobile: ').strip()

    while not is_valid_phone(home_mobile):
        home_mobile = input('Please Enter a home mobile: ').strip()
    else:
        contact['home_mobile'] = home_mobile

    office_mobile = input('Please Enter a office mobile: ').strip()

    while not is_valid_phone(office_mobile):
        office_mobile = input('Please Enter a office mobile: ').strip()
    else:
        contact['office_mobile'] = office_mobile
        
    return contact
 
contact_item_new =  add_item()

def check_contact_item(contact_item_new):
    for item in contacts:
        if item['home_mobile'] == contact_item_new['home_mobile']:
            print("This phone number already is in contacts")
            return False
        if full_name(item) == full_name(contact_item_new):
            print("This name already is in contacts")
            return False
    return True    

if check_contact_item(contact_item_new):
     contacts.append(contact_item_new)
else: print("This item already is in contacts")

# printing new contact item
print("new contact item", str(contact_item_new))


# Використовуючи словник, видалити всі дублі слів з даного речення: 
# Python is great and Java is also great
# Потрібно отримати: Python is great and Java also
string = 'Python is great and Java is also great'
# print(dict.fromkeys(string.split()))
print(' '.join(dict.fromkeys(string.split())))