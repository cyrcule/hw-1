import re


# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y
def first(equation, x):
    m = re.findall(r"([\d\.-]+)\D*([\d\.]+)", equation)

    k = float(m[0][0])
    b = float(m[0][1])

    y = k * x + b
    print(y)


# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
date0 = '01.11.1985'

# Примеры некорректных дат
date1 = '01.22.1001'
date2 = '1.12.1001'
date3 = '-2.10.3001'


def second(string_data):
    def error_message():
        print('Некорректный формат даты')

    if len(string_data) != 10 or string_data.count(".") != 2:
        raise ValueError('Некорректный формат даты')

    day = string_data[:2]
    month = string_data[3:5]
    year = string_data[-4:]

    # проверяем день
    try:
        day = int(day)
    except ValueError:
        error_message()

    if day not in range(1, 32):
        raise ValueError('Некорректный формат даты')

    # проверяем месяц
    try:
        month = int(month)
    except ValueError:
        error_message()

    if month not in range(1, 13):
        raise ValueError('Некорректный формат даты')

    # проверяем год
    try:
        year = int(year)
    except ValueError:
        error_message()

    if year not in range(1, 10000):
        raise ValueError('Некорректный формат даты')

    print('Формат введёной даты правильный')
    return True


# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3
def third(n):
    print('Номер комнаты:', n)
    rooms = [[], ]
    floor_number = 0
    number_of_rooms_per_floor = 0
    groupped_rooms = 1
    for i in range(1, n + 1):
        if len(rooms[-1]) == number_of_rooms_per_floor:
            floor_number += 1
            rooms.append([])
        if i == groupped_rooms:
            groupped_rooms = groupped_rooms + (number_of_rooms_per_floor + 1) ** 2
            number_of_rooms_per_floor += 1
        rooms[-1].append(i)
    print('Комната на {} этаже.'.format(floor_number))
    print('Номер комнаты начиная с левой стороны:', (rooms[floor_number].index(n) + 1))


def console_out():
    first(equation, x)
    print()
    second(date0) # или date1/2/3
    print()
    third(568)
    print()
    third(12)


console_out()