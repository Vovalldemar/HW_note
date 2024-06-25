from data_create import name_data, surname_data, phone_data, address_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные \n\n"
                    f"1 Вариант: \n"
                    f"{name} \n {surname} \n {phone} \n {address} \n \n"
                    f"2 Вариант: \n"
                    f"{name}{surname}{phone}{address} \n"
                    f"Выберите вариант: "))

    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input('Введите число '))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name} \n {surname} \n {phone} \n {address} \n \n")
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}{surname}{phone} {address} \n\n")

def print_data():
    print("Вывожу данные из 1 файла: \n")
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j = i + 1
        print(''.join(data_first_list))

    print('Вывожу данные из 2 файла: \n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        print(''.join(data_second))

def search_data():
    query = input("Введите имя или фамилию для поиска: ")
    found = False

    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.read()
        if query in data_first:
            print("Запись найдена в первом файле:")
            print(data_first[data_first.index(query):data_first.index(query) + 100])
            found = True

    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.read()
        if query in data_second:
            print("Запись найдена во втором файле:")
            print(data_second[data_second.index(query):data_second.index(query) + 100])
            found = True

    if not found:
        print("Запись не найдена.")

def modify_data():
    query = input("Введите имя или фамилию для изменения: ")
    modified = False

    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()

    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()

    for i, line in enumerate(data_first):
        if query in line:
            print("Запись найдена в первом файле:")
            print(''.join(data_first[i:i+4]))
            name = name_data()
            surname = surname_data()
            phone = phone_data()
            address = address_data()
            data_first[i] = f"{name} \n {surname} \n {phone} \n {address} \n \n"
            modified = True
            break

    for i, line in enumerate(data_second):
        if query in line:
            print("Запись найдена во втором файле:")
            print(data_second[i])
            name = name_data()
            surname = surname_data()
            phone = phone_data()
            address = address_data()
            data_second[i] = f"{name}{surname}{phone}{address} \n"
            modified = True
            break

    if modified:
        with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
            f.writelines(data_first)
        with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
            f.writelines(data_second)
        print("Данные успешно изменены.")
    else:
        print("Запись не найдена.")

def delete_data():
    query = input("Введите имя или фамилию для удаления: ")
    deleted = False

    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()

    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()

    new_data_first = []
    new_data_second = []

    for i in range(0, len(data_first), 5):
        if query in data_first[i]:
            print("Запись найдена и удалена в первом файле:")
            print(''.join(data_first[i:i+5]))
            deleted = True
        else:
            new_data_first.extend(data_first[i:i+5])

    for line in data_second:
        if query in line:
            print("Запись найдена и удалена во втором файле:")
            print(line)
            deleted = True
        else:
            new_data_second.append(line)

    if deleted:
        with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
            f.writelines(new_data_first)
        with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
            f.writelines(new_data_second)
        print("Запись успешно удалена.")
    else:
        print("Запись не найдена.")
