# unpickled.py
# ============================3========================

# Використовуючи модуль pickle, змініть програму управління контактами таким чином:
# Список контактів має зберігатись у файлі phone.db
# Кожний контакт має бути словником
# Для перегляду списку контактів та пошуку відповідного контакту потрібно звертатись до файлу phone.db
# Після виконання операцій створення, оновлення, видалення потрібно оновлювати файл phone.db


contact_item = {
                   'first_name':'john', 
                   'last_name':'doe', 
                   'home_mobile':'1422155', 
                   'office_mobile':'1563231'
                }

contacts.append(contact_item)


def pickled(contacts):
	with open('phone.db', 'wb') as output:
		pickle.dump(contacts, output)

def unpickled():
	list_unpickled = []
	with open('phone.db', 'rb') as file:
		list_unpickled = pickle.load(file)
	return list_unpickled