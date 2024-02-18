import os

# 1. Создание файла:
# - открываем файл на дозапись # a
# 2. Добавление контакта:
# - запросить у пользователя новый контакта
# - открыть файл на дозапись # a
# - добавить новый контакт
# 3. Вывод данных на экран:
# - открыть файл на чтение # r
# - считать файл
# - вывести на экран
# 4. Поиск контакта:
# - выбор варианта поиска
# - запросить данные для поиска
# - открыть файл на чтение
# - считываем данные файла, сохранить их в переменную
# - осуществляем поиск контакта
# - выводим на экран найденный контакта
# 5. Создание UI:
# - вывести меню на экран
# - запросить у пользавателя вариант действия
# - запустить соответствующую функцию
# - осуществить возможность выхода из программы

# def create_contact():
#     with open("phonebook.txt", 'r', encoding='utf-8') as file:
#         contacts_str = file.read()

#     contacts_list = contacts_str.rstrip().split('\n\n')
#     id = len(contacts_list) + 1
#     surname = input_surname()
#     name = input_name()
#     patronymic = input_patronymic()
#     phone = input_phone()
#     address = input_address()
#     return f'id-{id} {surname} {name} {patronymic}: {phone}\n{address}\n\n'

# def add_contact():
#     contact_str = create_contact()
#     with open("phonebook.txt", 'a', encoding='utf-8') as file:
#         file.write(contact_str)


# def print_contacts():
#     with open("phonebook.txt", 'r', encoding='utf-8') as file:
#         contacts_str = file.read()
#             #print([contacts_str])
#     contacts_list = contacts_str.rstrip().split('\n\n')
#     for n, contact in enumerate(contacts_list, 1):
#         print(n, contact)
        

# def search_contact():
#     print(
#         'Возможные варианты поиска:\n'
#         '1. По фамилии\n'
#         '2. По имени\n'
#         '3. По отчество\n'
#         '4. По телефону\n'
#         '5. По адресу(город)'
#         )
#     var = input('выберите вариант поиска: ')
#     while var not in ('1', '2', '3', '4', '5'):
#         print('некорректный ввод!')
#         var = input('выберите вариант поиска: ')
#     i_var = int(var) - 1

#     search = input('Введите данные для поиска: ').title()
#     with open("phonebook.txt", 'r', encoding='utf-8') as file:
#         contacts_str = file.read()
#         #print([contacts_str])
#     contacts_list = contacts_str.rstrip().split('\n\n')
#         #print(contacts_list)

#     for str_contact in contacts_list:
#         lst_contact = str_contact.replace(':', '').split()
#         if search in lst_contact[i_var]:
#             print(str_contact)


# def find_contact():
#     print_contacts()
#     var = int(input('Выберите порядковый номер контакта: '))
#     with open("phonebook.txt", 'r', encoding='utf-8') as file:
#         contacts_str = file.read()

#     contacts_list = list(contacts_str.rstrip().split('\n\n'))
#     contacts_list = list(map(lambda arg: arg.split()[0], contacts_list))
#     print(contacts_list)

#     while var not in range(len(contacts_list) + 1):
#         print('некорректный ввод!')
#         var = input('выберите вариант поиска: ')

#     i_var = int(var) - 1

#     with open("phonebook_new.txt", 'a', encoding='utf-8'):
#         pass

 
#     contact_str = contacts_list[i_var] + '\n\n'
#     with open("phonebook_new.txt", 'a', encoding='utf-8') as file:
#         file.write(contact_str)





