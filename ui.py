from logger import input_data, print_data, search_data, modify_data, delete_data

def interface():
    while True:
        print('Добрый день! Вы попали на специальный бот-справочник от Geekbrains!')
        print('1 - Запись данных')
        print('2 - Вывод данных')
        print('3 - Поиск данных')
        print('4 - Изменение данных')
        print('5 - Удаление данных')
        print('0 - Выход')

        try:
            command = int(input('Введите число: '))

            if command == 1:
                input_data()
            elif command == 2:
                print_data()
            elif command == 3:
                search_data()
            elif command == 4:
                modify_data()
            elif command == 5:
                delete_data()
            elif command == 0:
                print("Выход из программы. До свидания!")
                break
            else:
                print('Неправильный ввод, пожалуйста, введите число от 0 до 5.')
        except ValueError:
            print('Неправильный ввод, пожалуйста, введите число.')

if __name__ == "__main__":
    interface()