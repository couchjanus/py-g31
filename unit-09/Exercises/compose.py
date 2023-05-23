# Напишіть функцію, що виконує композицію функцій справа наліво.

# - Використовуйте `functools.reduce()` для композиції функції справа наліво.
# - Остання (крайня права) функція може приймати один або більше аргументів; решта функцій мають бути унарними.


from functools import reduce

def compose(*fns):
  return reduce(lambda f, g: lambda *args: f(g(*args)), fns)

add5 = lambda x: x + 5
multiply = lambda x, y: x * y
multiply_and_add_5 = compose(add5, multiply)
multiply_and_add_5(5, 2) # 15