# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Все что необходимо знать про list()
'''
# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
# -i -5   -4   -3   -2   -1

print(M[0])  # Первый элемент списка М
print(M[-1])  # Последний элемент списка М

M[0], M[-1] = 'A', 'E'
print(M)  # ['A', 'b', 'c', 'd', 'E']


# 1. Могут хранить в себе неограниченное кол-во элементов, при чем различных типов данных (в отличие от массивов)
# 2. Каждый элемент списка имеет свой порядковый номер: индекс
# 3. Индексы считаются слева направо начиная с нуля или справа налево начиная с -1
# 4. Элементы списка можно не только брать через индексы, но и изменять их (в отличие от кортеж)


B = (1, 2, 3)  # tuple() - Изменять элементы кортежа нельзя
'''


# Срезы списков
'''
# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
print(M[1:4])  # ['b', 'c', 'd']
print(M[:4])  # ['a', 'b', 'c', 'd'] - все, что слева до 4, не включая.
print(M[2:])  # ['c', 'd', 'e'] - все, что справа начиная с 2 индекса (включительно)
print(M[::])  # ['a', 'b', 'c', 'd', 'e'] - все элементы слева направо с шагом 1
print(M[::2])  # ['a', 'c', 'e'] - все элементы под четными индексами
print(M[1::2])  # ['b', 'd'] - все элементы под нечетными индексами

# особенно полезные

print(M[2:])  # ['c', 'd', 'e'] - Берем все элементы начиная со 2 индекса
print(M[1:-1])  # ['b', 'c', 'd'] - Все элементы кроме первого и последнего
print(M[::-1])   # ['e', 'd', 'c', 'b', 'a'] - Записали список в обратном порядке
'''


# Функции списков
'''
M = [1, 2, 1, 3, 3, 4, 5]

print(len(M))  # 7 - Длина списка М (кол-во элементов в нем)
print(sum(M))  # 19 - Сумма элементов списка
print(max(M), min(M))  # 5 1
print(sorted(M))  # [1, 1, 2, 3, 3, 4, 5] - Сортирует элементы по возрастанию
print(sorted(M, reverse=True))  # [5, 4, 3, 3, 2, 1, 1] - Сортирует элементы по убыванию
print(set(M))  # {1, 2, 3, 4, 5} - Убирает копии элементов 
'''


# 🖥  Все методы списков в Python, которые понадобятся на ЕГЭ


# Метод .append() используется для добавления элемента в конец списка. Пример:
'''
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Вывод: [1, 2, 3, 4]

# Можно реализовать через конкатенацию (склеивание) списков:
my_list = [1, 2, 3]
my_list += [4]
my_list += [5, 6]
my_list += [5, 6]
print(my_list)  # Вывод: [1, 2, 3, 4, 5, 6]


# Метод .reverse() изменяет порядок элементов в списке на обратный. Пример:
my_list = [1, 2, 3, 4]
my_list.reverse()
print(my_list)  # Вывод: [4, 3, 2, 1]

# Можно записать по другому через срез:
my_list = [1, 2, 3, 4]
my_list = my_list[::-1]
print(my_list)  # Вывод: [4, 3, 2, 1]


# Метод .count() возвращает количество вхождений заданного элемента в список. Пример:
my_list = [1, 2, 2, 3, 4, 2]
count_of_twos = my_list.count(2)
print(count_of_twos)  # Вывод: 3


# Метод .remove() удаляет первое вхождение указанного элемента из списка. Пример:
my_list = [1, 2, 3, 2, 4]
my_list.remove(2)  # первая найденная двойка
print(my_list)  # Вывод: [1, 3, 2, 4]

# Можно удалить элемент через его индекс используя del:
my_list = [1, 2, 3, 2, 4]
del my_list[1]  # индекс удаляемого элемента
print(my_list)  # Вывод: [1, 3, 2, 4]


# Метод .index() возвращает индекс первого вхождения заданного элемента в списке. Пример:
my_list = [1, 2, 3, 2, 4]
index_of_two = my_list.index(2)
print(index_of_two)  # Вывод: 1


# Метод .sort() сортирует элементы списка по возрастанию (по умолчанию) 
# или в обратном порядке, если передан аргумент reverse=True. Пример:
my_list = [4, 1, 3, 2]
my_list.sort()
print(my_list)  # Вывод: [1, 2, 3, 4]

my_list.sort(reverse=True)
print(my_list)  # Вывод: [4, 3, 2, 1]

# Скажу честно я не любитель этого метода, считаю, что удобнее будет использовать функцию sorted():
my_list = [4, 1, 3, 2]
my_list = sorted(my_list)
print(my_list)  # Вывод: [1, 2, 3, 4]

my_list = sorted(my_list, reverse=True)
print(my_list)  # Вывод: [4, 3, 2, 1]
'''


# Генераторы списков

# [что кладем | откуда берем | при каком условии]
'''
M = [x for x in range(10)]
print(M)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

M = [x for x in range(10) if x % 2 == 0]
print(M)  # [0, 2, 4, 6, 8]

M = [x**2 for x in range(10) if x % 2 == 0]
print(M)  # [0, 4, 16, 36, 64]

from random import randint
M = [randint(0, 100) for _ in range(10)]
print(M)

chet = [x for x in M if x % 2 == 0]
nechet = [x for x in M if x % 2 != 0]
print(chet, nechet)

not_copied = [x for x in M if M.count(x) == 1]
copied = [x for x in M if M.count(x) > 1]
print(copied, not_copied)


M = [int(x) for x in open('files/17.txt')]
print(M)


for s in open('files/9.txt'):
    M = [int(x) for x in s.split()]
    print(M)
'''
# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 6]
# КЕГЭ  = []
# на следующем уроке:
