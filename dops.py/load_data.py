def load_data():
    with open('C:\\Users\\Умка\\Desktop\\Сатанизм\\Python\\dops.py\\phonebook.txt', 'r+', encoding='utf-8') as data:
        text_data = data.read()
        path = input('Введите путь к файлу: ')
        with open(path, 'r', encoding='utf-8') as data_2:
            for i in data_2:
                if i not in text_data:
                    data.write(i)