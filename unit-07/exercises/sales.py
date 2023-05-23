# =======================1=============================
# Є файл sales.txt, який містить щомісячні дані про продажі товарів. Знайти у файлі рядок про продаж певного товару, надрукувати цей рядок та його номер. 
# Відкрити файл у режимі читання. 
# Використовуйте метод readlines(), щоб отримати всі рядки з файлу у формі об’єкта списку.
# Використовуйте цикл для повторення кожного рядка з файлу.
# В кожній ітерації циклу використовуйте умову if, щоб перевірити, чи присутній рядок у поточному рядку, і, якщо присутній, виведіть поточний рядок разом із номером рядка.

word = 'laptop'

with open('sales.txt', 'r') as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line in lines:
        # check if string present on a current line
        if line.find(word) != -1:
            print(word, 'string exists in file')
            print('Line Number:', lines.index(line))
            print('Line:', line)