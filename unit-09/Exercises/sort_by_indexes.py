# Напишіть функцію, що сортує один список на основі іншого списку, що містить потрібні індекси.

# - Використовуйте `zip()` і `sorted()`, щоб об’єднати та відсортувати два списки на основі значень `indexes`.
# - Використовуйте list comprehension, щоб отримати перший елемент кожної пари з результату.
# - Використовуйте параметр `reverse` в `sorted()`, щоб відсортувати словник у зворотному порядку на основі третього аргументу.


def sort_by_indexes(lst, indexes, reverse=False):
  return [val for (_, val) in sorted(zip(indexes, lst), key=lambda x: \
          x[0], reverse=reverse)]

a = ['eggs', 'bread', 'oranges', 'jam', 'apples', 'milk']
b = [3, 2, 6, 4, 1, 5]
sort_by_indexes(a, b) # ['apples', 'bread', 'eggs', 'jam', 'milk', 'oranges']
sort_by_indexes(a, b, True)
# ['oranges', 'milk', 'jam', 'eggs', 'bread', 'apples']