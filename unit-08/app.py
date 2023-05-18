# 
print(lambda s: s[::-1])
# obj()
print(callable(lambda s: s[::-1]))
test = 'Test for callable' # test()
print(callable(test))

print((lambda s: s[::-1])(test))
print((lambda x1, x2, x3: ( x1 + x2 + x3)/3)(9, 7, 3))

print((lambda x: (x, x**2, x**3))(9))

def inner():
    print('I am function inner()')
    
def outer(fn):
    fn()

outer(inner)

def compose1():
    return lambda *args: sum(*args)

add_1 = compose1()
print(add_1([1,2,3]))

def compose2(fn):
    return fn
sum_2 = lambda *args: sum(*args)
add_2 = compose2(sum_2)
print(add_2([2,2,3]))

def compose3(*fns):
    return lambda *args: fns[0](fns[1](*args))

fn_1 = lambda x: x + 100
fn_2 = lambda *args: sum(*args)

add_3 = compose3(fn_1, fn_2)
print(add_3([2,2,3]))
first_list = [[3,2,7],[9,1,3,7,98]]

print(sorted(first_list, key=len, reverse=True))

def rev(l):
    return -len(l)

print(sorted(first_list, key=rev))

numbers = [-2, -1, 0, 3, 9, 7, 3, 1]

print(list(filter(lambda n: n > 0, numbers)))

print(list(filter(lambda x: x % 2 == 0, range(50))))

import math

def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

print(list(filter(prime, range(1, 51))))


import statistics as st 

sample = [10, 0, 10, 8, 2, 7, 9, 3, 333, 9, 5, 9, 321]

mean = st.mean(sample)
print(mean)

stdev = st.stdev(sample)

low = mean - 2 * stdev
high = mean + 2 * stdev

clear_sample = list(filter(lambda x: low <= x <= high, sample))

print(st.mean(clear_sample))


print(list(map(lambda x: (x + 1) * 0.11, clear_sample))) 

from functools import reduce

print(reduce(lambda x, y : x + y, sample)) 

def mult(x, y):
    return x * y

def fac(n):
    return reduce(mult, range(1, n + 1))

print(fac(4))

def my_max(x, y):
    return x if x > y else y
print(reduce(my_max, sample))

print(reduce(lambda x, y: x if x > y else y, sample))

numbs = [1,2,3,4,5]
print(list(map(str, numbs)))

def my_map(fn, itrbl):
    return reduce(lambda items, value: items + [fn(value)], itrbl, [],)

print(list(my_map(str, numbs)))

my_dict = {1: 'a', 2: 'b', 3: 'c'}

print({v: k for k,v in my_dict.items()})

print(dict(zip(my_dict.values(), my_dict)))
print(dict(zip(my_dict.values(), my_dict.keys())))
