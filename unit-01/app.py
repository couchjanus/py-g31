# application first 
from colorama import init, Fore

# print("Hello world!")

# 'Hello Python'

# print("""Hello Python
#     Hello Python
# """)

# hell1_string = '''Hello Python String
#     Hello Python Programm
# '''
# print(hell1_string)

# print(hell1_string)

# print(hell1_string)

# Hell1_string = "Hello String !"

# if  Hell1_string >= "Hello String":
#     print(Hell1_string)
#     print(hell1_string)

# print(hell1_string)

x = input(Fore.RED + "Enter x = ")
y = input(Fore.MAGENTA + "Enter y = ")

x = int(x)
y = int(y)

o = input(Fore.YELLOW + "Enter operation = ")

def add(a, b):
    return a + b 

if o == '+':
    print(Fore.GREEN + "Result: ", add(x, y))
elif o == '-':
    print(Fore.GREEN + "Result: ", x - y)
elif o == '*':
    print(Fore.GREEN + "Result: ", x * y)
else:
    print(Fore.RED + "Error")



# >>> import math
# >>> math.sqrt(9)
# 3.0





