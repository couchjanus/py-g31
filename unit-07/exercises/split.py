# ====================2================================

# У вас є файл із такими реченнями: Peter Piper picked a peck of pickled peppers. A peck of pickled peppers Peter Piper picked. Where's the peck of pickled peppers Peter Piper picked.
# Потрібно вставити нове речення (If Peter Piper picked a peck of pickled peppers) після другого речення  в той самий рядок. 
# Бажаний результат: Peter Piper picked a peck of pickled peppers. A peck of pickled peppers Peter Piper picked. If Peter Piper picked a peck of pickled peppers. Where's the peck of pickled peppers Peter Piper picked.
# Тому найкраща практика:
# Прочитати речення з файлу,
# Внести необхідні зміни,
# Записати його в новий файл. 
# Використовуйте метод splitlines(), який повертає список рядків, розбитих на межі рядків.

with open('text', 'r+') as infile:
    text = infile.read()  # Read the contents of the file into memory.
    print(text)
    content = text.split('.')
    index = 2
    content.insert(index,' If Peter Piper picked a peck of pickled peppers')
    print(content)
    infile.seek(0)
    for item in content:
        infile.writelines(item)