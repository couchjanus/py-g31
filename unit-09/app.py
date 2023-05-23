"""Main module"""

# import mod

# print(mod.app_name)

# print(mod.foo())

from mod import app_name, foo as bar

def foo():
    return "I'm foo!"

print(app_name)

print(foo())
print(bar())


try:
    import baz
except ImportError:
    print("Module not found")
    
try:
    from mod import bla
except ImportError:
    print("Object not found in module")
    
# MVC

print(f"The value of __name__ is {repr(__name__)}")

def main():
    print("Hello Main")
    
if __name__ == "__main__":
    main()

def my_decorator(function):
   def wrapper():
       func = function()
       make_uppercase = func.upper()
       return make_uppercase
   return wrapper

def say_hi():
   return f'hello there'
decorate = my_decorator(say_hi) 
# функція-декоратор приймає функцію як аргумент
print(decorate())


import sys

def command_decorator(function):
   def wrapper(arg = None):
       if arg == None:
           print(f""" You get a nice error, you are missing NAME
               Usage: main.py [OPTIONS] NAME""")
           raise sys.exit("Missing argument 'NAME'")

       func = function(arg)
       make_uppercase = func.upper()
       return make_uppercase
   return wrapper


# Функція-декоратор приймає функцію як аргумент.
def hi_name(name):
   return f'hello there {name}!'

decor = command_decorator(hi_name)
print(decor('World'))
# print(decor())
# Однак Python надає набагато простіший спосіб застосування декораторів. Ми просто використовуємо символ @ перед функцією, яку хочемо декорувати. 
@command_decorator
def hi_name(name):
   return f'hello there {name}!'
print(hi_name('Decorator'))
print(hi_name())
