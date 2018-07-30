# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()
fruit_list = ['яблоко', 'банан', 'киви', 'арбуз']
random_list = ['dfghhfdg', 'dfghkcn', 'dfgh5', 'vbn', 534, 86, 866, 4, 666, 58, 88, 88, 'Python', 'test', 'what']
another_random_list = ['vbn', 'test', 86, 666, 'Python']
initial_list = [3, 66, 7, 45, 25, 6, 88, 143567, 4, 6.8]


def first(fruit_list):
    for fruit_index, fruit_name in enumerate(fruit_list, start=1):
        print(fruit_index, '{:>10}'.format(fruit_name))


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
def second(first_list, second_list):
    print('Первый лист: ', first_list)
    print('Второй лист:', second_list)
    first_list = [x for x in first_list if x not in second_list]
    print('Результат', first_list)


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
def third(initial_list):
    print('\nИсходный лист:', initial_list)
    new_list = []
    for i in initial_list:
        if i % 2 == 0:
            new_list.append(i / 4)
        else:
            new_list.append(2 * i)
    print('Результат:', new_list)


def console_out():
    first(fruit_list)
    print()
    second(random_list, another_random_list)
    print()
    third(initial_list)


console_out()