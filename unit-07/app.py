src_list = [2, 5, -3, 9]

dest_list = []

for item in src_list:
    dest_list.append(item)
    
print(dest_list)

comp_list = [item for item in src_list]
print(comp_list)

print(list(range(0, 19, 2)))
print([x for x in range(0, 19, 2)])

print([x**2 for x in range(10)])

def price_with_tax(tax, TAX_RATE=.08):
    return tax * (1 + TAX_RATE)

print([price_with_tax(i) for i in [1.09, 33.55, 54.66, 99.44, 7, 1.99]])


print([x for x in range(10) if x%2 == 0])

print([x for x in src_list if x < 0])

sentence = 'the rocket came back from mars'

print([i for i in sentence if i in 'aeiou'])

prices = [1.09, 33.55, -54.66, 99.44, -7, 1.99]
print([i if i > 0 else 0 for i in prices])

print([2 * (x if x % 2 == 0 else -1) + 1 for x in range(10)])

print([x if (x > 2 and x % 2 == 0) else '!' for x in range(10)])

import sys

c = [i for i in range(10000)]
print(sys.getsizeof(c))


d = (i for i in range(10000))
print(sys.getsizeof(d))


print({x:chr(65 + x) for x in range(1, 200)})

dict1 = {'w': 1, 'x': 1}
dict2 = {'x': 2, 'y': 2, 'z':2}
print({k:v for d in [dict1, dict2] for k, v in d.items()})

print({(x**2) for x in [1,1,1,2,2,5,2]})

matrix = [[i for i in range(10)] for _ in range(7)]
print(matrix)


mtr = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
    ]

print([n for row in mtr for n in row])

def fac(n):
    return 1 if n <= 1 else n * fac(n-1)

print(fac(4))

def fib(n):
    if n in {0, 1}:
        return n
    return fib(n - 1) + fib(n -2)

print([fib(n) for n in range(15)])

cache = {0: 0, 1: 1}

def fibc(n):
    
    if n in cache:
        return cache[n]
    cache[n] = fibc(n - 1) + fibc(n -2)
    return cache[n]

print([fibc(n) for n in range(15)])