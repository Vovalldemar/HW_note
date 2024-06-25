from logger import input_data, print_data, search_data, modify_data, delete_data

def interface():
    print('Добрый день! Вы попали на специальный бот-справочник от Geekbrains! \n 1 - запись данных \n 2 - вывод данных \n')
    command = int(input('Введите число'))

    while command != 1 and command != 2:
        print('Неправильный ввод')
        command =  int(input('Введите число '))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()

    print_data