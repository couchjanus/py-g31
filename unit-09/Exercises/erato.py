# Реалізація алгоритму решета Ератосфена

import math

N = 50  # діапазон в якому шукаємо прості числа

prime = [True] * N
prime[0], prime[1] = False, False # 0 та 1 не є простими

for i in range(2, math.ceil(math.sqrt(N))):  # від 2 до квадратного кореня з N 
    if prime[i]:  # якщо просте видаляємо всі числа кратні до нього
        j = i * i   # для j=2 будуть такі значення 4,6,8,10,12... для j=3 — 9,12,15,18,21...
        while j < N:
            prime[j] = False
            j += i

# 
# print(prime)
print([i for i in range(len(prime)) if prime[i]])