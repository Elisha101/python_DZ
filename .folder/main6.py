'''
Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
Поскольку разобраться в его кричалках не настолько просто,
насколько легко он их придумывает,
Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв)
в каждой фразе стихотворения одинаковое.
Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
Фразы отделяются друг от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры.
В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
Ввод: пара-ра-рам рам-пам-папам па-ра-па-дам
Вывод: Парам пам-пам
'''

# def rhythm(str):
#     str = str.split()
#     list_1 = []
#     for word in str:
#         sum_w = 0
#         for i in word:
#             if i in '':
#                 sum_w += 1
#         list_1.append(sum_w)
#     return len(list_1) == list_1.count(list_1[0])
#
#
# str_1 = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# if rhythm(str_1):
#     print('Парам пам-пам')
# else:
#     print('Пам парам')
'''
Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
 которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns
указывают число строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы
 (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, 
 как, например, у операции умножения.

*Пример:*

**Ввод:** `print_operation_table(lambda x, y: x * y) ` 
**Вывод:**
1 2 3 4 5 6

2 4 6 8 10 12
3 6 9 12 15 18
4 8 12 16 20 24
5 10 15 20 25 30
6 12 18 24 30 36
'''

# def print_operation_table(operation, num_rows=6, num_columns=6):
#     a = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
#     for i in a:
#         print(*[f"{x:>3}" for x in i])
#
#
# print_operation_table(lambda x, y: x * y)

'''
Задача 38: Дополнить телефонный справочник возможностью 
изменения и удаления данных. Пользователь также может ввести
имя или фамилию, и Вы должны реализовать функционал для 
изменения и удаления данных
'''

# Показывает информацию в файле
def show_data(filename):
    print("\nПП | ФИО | Телефон")
    with open(filename, "r", encoding="utf-8") as data:
        print(data.read())
    print("")

# Записывает информацию в файл
def export_data(filename):
    with open(filename, "r", encoding="utf-8") as data:
        tel_file = data.read()
    num = len(tel_file.split("\n"))
    with open(filename, "a", encoding="utf-8") as data:
        fio = input("Введите ФИО: ")
        phone_number = input("Введите номер телефона: ")
        data.write(f"{num} | {fio} | {phone_number}\n")
        print(f"Добавлена запись : {num} | {fio} | {phone_number}\n")

# Изменяет информацию из файла
def edit_data(filename):
    print("\nПП | ФИО | Телефон")
    with open(filename, "r", encoding='utf-8') as data:
        tel_book = data.read()
    print(tel_book)
    print("")
    index_delete_data = int(input("Введите номер строки для редактирования: ")) - 1
    tel_book_lines = tel_book.split("\n")
    edit_tel_book_lines = tel_book_lines[index_delete_data]
    elements = edit_tel_book_lines.split(" | ")
    fio = input("Введите ФИО: ")
    phone = input("Введите номер телефона: ")
    num = elements[0]
    if len(fio) == 0:
        fio = elements[1]
    if len(phone) == 0:
        phone = elements[2]
    edited_line = f"{num} | {fio} | {phone}"
    tel_book_lines[index_delete_data] = edited_line
    print(f"Запись - {edit_tel_book_lines}, изменена на - {edited_line}\n")
    with open(filename, "w", encoding='utf-8') as f:
        f.write("\n".join(tel_book_lines))

# Удаляет информацию из файла
def delete_data(filename):
    print("\nПП | ФИО | Телефон")
    with open(filename, "r", encoding="utf-8") as data:
        tel_book = data.read()
        print(tel_book)
    print("")
    index_delete_data = int(input("Введите номер строки для удаления: ")) - 1
    tel_book_lines = tel_book.split("\n")
    del_tel_book_lines = tel_book_lines[index_delete_data]
    tel_book_lines.pop(index_delete_data)
    print(f"Удалена запись: {del_tel_book_lines}\n")
    with open(filename, "w", encoding='utf-8') as data:
        data.write("\n".join(tel_book_lines))

def main():
    my_choice = -1
    file_tel = "tel.txt"

    # Создает файл если его нет в папке
    with open(file_tel, "a", encoding="utf-8") as file:
         file.write("")

    while my_choice != 0:
        print("Выберите одно из действий:")
        print("1 - Вывести инфо на экран")
        print("2 - Произвести экпорт данных")
        print("3 - Произвести изменение данных")
        print("4 - Произвести удаление данных")
        print("0 - Выход из программы")
        action = int(input("Действие: "))
        if action == 1:
            show_data(file_tel)
        elif action == 2:
            export_data(file_tel)
        elif action == 3:
            edit_data(file_tel)
        elif action == 4:
            delete_data(file_tel)
        else:
            my_choice = 0

    print("До свидания")

if __name__ == "__main__":
    main()