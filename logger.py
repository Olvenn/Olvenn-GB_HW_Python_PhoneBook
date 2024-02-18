from data_create import *
import os


def create_contact():
    with open("phonebook.txt", 'r', encoding='utf-8') as file:
        contacts_str = file.read()

    contacts_list = contacts_str.rstrip().split('\n\n')
    id = len(contacts_list) + 1
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    return f'id-{id} {surname} {name} {patronymic}: {phone}\n{address}\n\n'


def add_contact():
    contact_str = create_contact()
    with open("phonebook.txt", 'a', encoding='utf-8') as file:
        file.write(contact_str)


def print_contacts():
    with open("phonebook.txt", 'r', encoding='utf-8') as file:
        contacts_str = file.read()
    contacts_list = contacts_str.rstrip().split('\n\n')
    for n, contact in enumerate(contacts_list, 1):
        print(n, contact)


def search_contact():
    print(
        'Возможные варианты поиска:\n'
        '1. По фамилии\n'
        '2. По имени\n'
        '3. По отчество\n'
        '4. По телефону\n'
        '5. По адресу(город)'
        )
    var = input('выберите вариант поиска: ')
    while var not in ('1', '2', '3', '4', '5'):
        print('некорректный ввод!')
        var = input('выберите вариант поиска: ')
    i_var = int(var) - 1

    search = input('Введите данные для поиска: ').title()
    with open("phonebook.txt", 'r', encoding='utf-8') as file:
        contacts_str = file.read()
    contacts_list = contacts_str.rstrip().split('\n\n')

    for str_contact in contacts_list:
        lst_contact = str_contact.replace(':', '').split()
        if search in lst_contact[i_var + 1]:
            print()
            print("Данные контакта  ", str_contact)


def find_contact():
    print_contacts()
    var = int(input('Выберите порядковый номер контакта: '))
    with open("phonebook.txt", 'r', encoding='utf-8') as file:
        contacts_str = file.read()

    contacts_list = list(contacts_str.rstrip().split('\n\n'))

    while var not in range(len(contacts_list) + 1):
        print('некорректный ввод!')
        var = input('выберите вариант поиска: ')

    i_var = int(var) - 1

    contacts_list_id = list(map(lambda arg: arg.split()[0], contacts_list))
    contact_id = contacts_list_id[i_var].split()[0]

    return [i_var, contact_id]


def transfer_contact():
    contact = find_contact()
    id = contact[1]
    with open("phonebook.txt", 'r', encoding='utf-8') as file:
        contacts_str = file.read()

    contacts_list = list(contacts_str.rstrip().split('\n\n'))

    def exists(path):
        try:
            os.stat(path)
        except OSError:
            return False
        return True

    contacts_list_new_id = []

    if (exists("phonebook_new.txt")):
        contacts_str_new = ""
        with open("phonebook_new.txt", 'r', encoding='utf-8') as file:
            contacts_str_new = file.read()
            print(contacts_str_new)
        if (len(contacts_str_new) != 0):
            contacts_list_new = list(contacts_str_new.rstrip().split('\n\n'))
            contacts_list_new_id = list(map(lambda arg: arg.split()[0],  
                                        contacts_list_new))

    if id in contacts_list_new_id:
        print("Такой элемент уже есть в файле.")
    else:
        with open("phonebook_new.txt", 'a', encoding='utf-8') as file_new:
            contact_str = contacts_list[contact[0]] + '\n\n'
            file_new.write(contact_str)
