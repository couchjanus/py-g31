# 1. за допомогою list comprehension створити список квадратів всіх чисел у діапазоні від 1 до 9: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 2. за допомогою list comprehension створити список, де всі цифри діляться на 5 без остатку, в диапазоні від 0 до 100: [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
[x for x in range(100) if x%5 == 0]
# [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

# 3. за допомогою list comprehension створити список, де всі цифри діляться на 3 і 6 без остатку, в диапазоні від 0 до 50: [3, 9, 15, 21, 27, 33, 39, 45]
[x for x in range(50) if x%3 == 0 and x%6 != 0]
# [3, 9, 15, 21, 27, 33, 39, 45]

# 4. за допомогою list comprehension створити список, що містить перші літери кожного слова  речення 'The rocket came back from Mars': ['Т', 'с', 'и', 'м', 'P', 'д', 'с']
phrase = 'The rocket came back from Mars'
print([w[0] for w in phrase.split()])
# ['Т', 'с', 'и', 'м', 'P', 'д', 'с']

# 5. за допомогою list comprehension замінити в "all, max, matrix, awesome, appalling, abba" літеру a у кожному слові на #.
phrase = "all, max, matrix, awesome, appalling, abba"
print(''.join([letter if letter != 'a' else '#' for letter in phrase]))


# 6. переписавши код за допомогою list comprehension:
even_numbers = [] 
for x in range(10):
    if x % 2 == 0:
        even_numbers.append(x)
print(even_numbers) # [0, 2, 4, 6, 8]

[x for x in range(10) if x % 2 == 0]
# Out: [0, 2, 4, 6, 8]

# 7. Є список numbers = [121, 544, 111, 99, 77]  
# Вибрати тільки ті числа, що діляться на 11
# [121, 99, 77]
numbers = [121, 544, 111, 99, 77]
number11 = [num for num in numbers if num % 11 == 0]  
print(number11)  # [121, 99, 77]

# 8. створити list comprehension, що містить парні числа від 2 до 9998 включно:
[n for n in range(1, 10000) if n % 2 == 0] 


# 9. Написати фільтр, який відбирає літери у реченні, що не є голосні 
sentence = 'the rocket came back from mars'
# ['e', 'o', 'e', 'a', 'e', 'a', 'o', 'a']
vowels = [i for i in sentence if i in 'aeiou']
print(vowels)
# ['e', 'o', 'e', 'a', 'e', 'a', 'o', 'a']

# 10. знайти квадрат лише парних чисел у діапазоні range(10)
# [0, 4, 16, 36, 64]
final_list = [i**2 for i in range(10) if i%2 is 0]
# [0, 4, 16, 36, 64]

# 11. Зформувати таблицю множення чисел від 1 до 5. 
# [[1, 2, 3, 4, 5],
#  [2, 4, 6, 8, 10],
#  [3, 6, 9, 12, 15],
#  [4, 8, 12, 16, 20],
#  [5, 10, 15, 20, 25]]
table = [[x * y for x in range(1, 6)] for y in range(1, 6)]
print(table)

# 12. Є 2 кортежі a = (1, 3, 5) і b = (2, 4, 6)
# Згенерувати всі пари з a і b
# [(1, 2), (1, 4), (1, 6), (3, 2), (3, 4), (3, 6), (5, 2), (5, 4), (5, 6)]
output = [(a, b) for a in (1, 3, 5) for b in (2, 4, 6)]

# 13. Є 2 кортежі a = (1, 3, 5) і b = (2, 4, 6)
# Згенеруйте всі пари з a і b, за умови  a > b
# [(3, 2), (5, 2), (5, 4)]
output = [(a, b) for a in (1, 3, 5) for b in (2, 4, 6) if a > b]

# 14. Є матриця  matrix = [[1, 2], [3,4], [5,6], [7,8]]
# Транспонувати матрицю за допомогою List Comprehension
[[1, 3, 5, 7], [2, 4, 6, 8]]
matrix = [[1, 2], [3,4], [5,6], [7,8]]
transpose = [[row[i] for row in matrix] for i in range(2)]
print (transpose)
