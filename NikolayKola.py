# region Домашка: ******************************************************************
'''
print('w x y z F')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                F = ((z == (not x)) <= ((w <= (not y)) and (y <= x)))
                if F == 1:
                    print(w, x, y, z, int(F))


for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                F = ((z == (not x)) <= ((w <= (not y)) and (y <= x)))
                if F == 0:
                    print(w, x, y, z, int(F))
'''
import math

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
import turtle as t
t.screensize(20000, 20000)
t.tracer(0)
t.lt(90)
l = 40

for _ in range(3):
    t.fd(7 * l)
    t.rt(90)
    t.fd(12 * l)
    t.rt(90)
t.up()
t.fd(4*l)
t.rt(90)
t.fd(6*l)
t.lt(90)
t.down()
for _ in range(4):
    t.fd(83*l)
    t.rt(90)
    t.fd(77*l)
    t.rt(90)


t.up()
for x in range(-30, 30):
    for y in range(-30, 30):
        t.goto(x*l, y*l)
        t.dot(2, 'red')

t.done()
'''


'''
# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
# -i -5   -4   -3   -2   -1

for x in M:
    print(x, end=' ')  # a b c d e 
print()

for i in range(len(M)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e
print()


for i in range(len(M)):
    M[i] = M[i] * i
print(M)  # ['', 'b', 'cc', 'ddd', 'eeee']
'''


# Срезы
'''
# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
# -i -5   -4   -3   -2   -1

print(M[1:3])  # ['b', 'c']
print(M[:3])  # ['a', 'b', 'c']
print(M[3:])  # ['d', 'e']
print(M[::])  # ['a', 'b', 'c', 'd', 'e']
print(M[::2])  # ['a', 'c', 'e'] - все четные индексы
print(M[1::2])  # ['b', 'd'] - все нечетные индексы
print(M[::-1])  # ['e', 'd', 'c', 'b', 'a']
'''

# Функции списков
'''
from math import prod

M = [5, 1, 2, 4, 3, 1, 1]
print(min(M))  # 1
print(max(M))  # 5
print(len(M))  # 7
print(sum(M))  # 17
print(prod(M))  # 120
print(sorted(M))  # [1, 1, 1, 2, 3, 4, 5]
print(sorted(M, reverse=True))  # [5, 4, 3, 2, 1, 1, 1]
print(set(M))  # {1, 2, 3, 4, 5}
print(len(set(M)))  # 5 - кол-во различных элементов списка 
'''

# Методы списков (Методы это локальные функции, работающие только с одним типом данных)

'''
# Метод .append() используется для добавления элемента в конец списка. Пример:
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Вывод: [1, 2, 3, 4]

# Можно реализовать через конкатенацию (склеивание) списков:
my_list = [1, 2, 3]
my_list += [4]
my_list = [0] + my_list
print(my_list)  # Вывод: [0, 1, 2, 3, 4]



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
my_list_new = [x for x in my_list if x != 2]
print(my_list_new)  # [1, 3, 4]
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


# Метод .sort() сортирует элементы списка по возрастанию (по умолчанию) или в обратном порядке, если передан аргумент reverse=True. Пример:
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


# Генераторы списка
'''
import random
M = [random.randint(1, 100) for _ in range(20)]
chet = [x for x in M if x % 2 == 0]
nechet = [x for x in M if x % 2 != 0]
copied = [x for x in M if M.count(x) > 1]
print(M)
print(chet)
print(nechet)
print(copied)

s = '23256134125iuerhgj6342156'
chet = [x for x in s if x in '02468']
print(chet)

M = [int(x) for x in open('17.txt')]
'''

'''
x = 4 * 3125**2019 + 3*625**2020 - 2*125**2021 + 25**2022 - 4*5**2023 - 2024
M = []
while x > 0:
    M.append(x % 25)
    x //= 25
M.reverse()
print(len([i for i in M if i > 10]))
print(M.count(0))
'''

# № 17555 Основная волна 08.06.24 (Уровень: Базовый)
'''
for x in range(0, 2030+1):
    n = 7**91 + 7**160 - x
    M = []
    while n > 0:
        M.append(n % 7)
        n //= 7
    if M.count(0) == 70:
        print(x)
'''

'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:27]:
    A = int('123' + x + '24', 27)
    B = int(f'135{x}78', 27)
    if (A + B) % 26 == 0:
        print((A + B) // 26)
'''

'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:7]:
    for y in alphabet[:7]:
        A = int(f'{y}{x}320', 7)
        B = int(f'1{x}3{y}3', 9)
        if (A + B) % 181 == 0:
            print((A + B) // 181)
'''
# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2*, 3, 4, 6, 7, 9*, 10, 11, 18, 19-21]
# КЕГЭ  = [2]
# на следующем уроке:
