import os
from logger import *
from load_data import load_data

def userinterface():
    os.system('cls')
    print('''1 - Добавить контакт
2 - Поиск
3 - Импорт данных
4 - Вывод в консоль
5 - Удаление записи
6 - Изменение записи
7 - Выход''')
    user_choice = input('Введите номер нужной команды: ')
    while user_choice != '7':
        if user_choice == '1':
            add_person()
        elif user_choice == '2':
            search()
        elif user_choice == '3':
            load_data()
        elif user_choice == '4':
            print_data()
        elif user_choice == '5':
            del_person()
        elif user_choice == '6':
            change_person()
        else:
            print('Вы ввели некорректный вариант, попробуйте еще раз')
        os.system('cls')
        print('''1 - Добавить контакт
2 - Поиск
3 - Импорт данных
4 - Вывод в консоль
5 - Удаление записи
6 - Изменение записи
7 - Выход''')
        user_choice = input('Введите номер нужной команды: ')