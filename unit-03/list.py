ls1 = [1,2,3,4,5,6,7]
print(ls1 + [8,9])

print([8,9]*10)

cities = ['SA', 'NY', 'WDC']

print('NY' in cities)
print('NY' not in cities)
print('LA' in cities)

print(cities[1])

print(len(cities))
# print(cities[4])

print(cities[:])
print(cities[1])
print(cities[:-1])
print(cities[1:])

print(ls1[2:6])
print(ls1[2:6:2])

print(max(ls1))
print(min(ls1))

print(ls1.index(5))

for i in ls1:
    print(i)
    
for i in ls1:
    if i%2 == 2:
        continue
    if i == 5:
        break
    print(i)
    
print(type(ls1))

ls2 = []
ls3 = list()
print(type(ls2))
print(type(ls3))

ls3.append([1,2,3,4])
print(ls3)
ls3.append(5)
print(ls3)

ls3.extend([5,7,8])
print(ls3)

ls3.insert(2,78)
print(ls3)

ls3.remove(78)
print(ls3)
ls3.pop()
print(ls3)
ls3.pop(0)
print(ls3)
ls3.clear()
print(ls3)

tp1 = (3,5,7)
print(type(tp1))

tp2 = 55,66,77,99
print(type(tp2))

print(tp2)

x1, x2, x3, x4 = tp2
print(x3)

(*tmp, y, _) = tp2
print(y)

print(range(8))

for i in range(8):
    print(i)
    
import random

print(random.random())
print(random.randint(500, 50000)) # 18601
