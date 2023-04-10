from data_create import *
from time import sleep

def add_person():
    last_name = last_name_data()
    name = name_data()
    surname = surname_data()
    phone = phone_data()

    data = open('C:\\Users\\Умка\\Desktop\\Сатанизм\\Python\\dops.py\\phonebook.txt', 'a', encoding='utf-8')
    data.writelines([last_name + ' ', name + ' ', surname + ' ', phone + '\n'])
    data.close()

def print_data():
    with open('C:\\Users\\Умка\\Desktop\\Сатанизм\\Python\\dops.py\\phonebook.txt', 'r', encoding='utf-8') as data:
        print(data.read())
        sleep(5)

def search():
    search_arg = input('Введите параметр поиска: ')
    with open('C:\\Users\\Умка\\Desktop\\Сатанизм\\Python\\dops.py\\phonebook.txt', 'r', encoding='utf-8') as data:
        for i in data:
            if search_arg in i:
                print(i)
        sleep(10)

def del_person():
    del_name = input('Введите данные контакта, который хотите изменить: ')
    with open('C:\\Users\\Умка\\Desktop\\Сатанизм\\Python\\dops.py\\phonebook.txt', 'r', encoding='utf-8') as data:
        d = data.readlines()
        for i_line in range(len(d)):
            if del_name in d[i_line]:
                del d[i_line]
    with open('C:\\Users\\Умка\\Desktop\\Сатанизм\\Python\\dops.py\\phonebook.txt', 'w', encoding='utf-8') as data:
        print(d)
        for line in d:
            data.write(line)

def change_person():
    change_name = input('Введите данные контакта, который хотите изменить: ')
    last_name = input('Введите новую фамилию: ')
    name = input('Введите новое имя: ')
    surname = input('Введите новое отчество: ')
    phone = input('Введите новый номер телефона: ')

    with open('C:\\Users\\Умка\\Desktop\\Сатанизм\\Python\\dops.py\\phonebook.txt', 'r', encoding='utf-8') as data:
        d = data.readlines()
    for i_line in range(len(d)):
        if change_name in d[i_line]:
            d[i_line] = last_name + ' ' + name + ' ' + surname + ' ' + phone + '\n'

    with open('C:\\Users\\Умка\\Desktop\\Сатанизм\\Python\\dops.py\\phonebook.txt', 'r+', encoding='utf-8') as data:
        for line in d:
            data.write(line)