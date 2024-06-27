# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Условные операторы (ветвление): if, elif, else
'''
n = int(input('n: '))
if n % 2 == 0:  # if - если
    print('Четное')
else:  # else - иначе
    print('Нечетное')
'''


# x, y = int(input('x: ')), int(input('y: '))
'''
x, y = -7, 2

if x > 0 and y > 0:  # if - если
    print('Первая четверть')
elif x < 0 and y > 0:
    print('Вторая четверть')
elif x < 0 and y < 0:  # elif - иначе если
    print('Третья четверть')
elif x > 0 and y < 0:
    print('Четвертая четверть')
else:  # else - иначе
    print('Лежит на осях')
print('Конец')
'''


# Каскадные (вложенные) условные операторы
'''
x, y = int(input('x: ')), int(input('y: '))

if x > 0:
    if y > 0:  # x > 0, y > 0
        print('Первая четверть')
    else:  # x > 0, y <= 0
        print('Четвертая четверть')
else:
    if y > 0:  # x <= 0, y > 0
        print('Вторая четверть')
    else:  # x <= 0, y <= 0
        print('Третья четверть')
'''


# Логические связки: and, or, not, ^, ==, !=
'''
# a = 7
# b = 2
a, b = 7, -5

if a > 0 and b > 0:  # and - гарантирует, что оба (все) условия выполняются
    print('YES 1')
if a > 0 or b > 0:  # or - говорит о том, что хотя бы одно условие выполняется.
    print('YES 2')
if (a > 0) ^ (b > 0):  # ^, != - гарантируют, что только одно условие выполняется
    print('YES 3')
if (a > 0) != (b > 0):
    print('YES 4')

print(a > 0)   # True
print(b > 0)   # False
print(a > b)   # True
print(a == b)  # False
print(a != b)  # True
# = - присваивание (в переменную кладем значение)
# == - сравнение (когда мы сравниваем две переменные)

# Проверьте, что только два элемента положительные
a, b, c = 5, 6, -6
if (a > 0) + (b > 0) + (c > 0) == 2:
    print('Только два элемента положительные')
if (a > 0) + (b > 0) + (c > 0) == 1:
    print('Только один элемент положительный')

print(True + False + True)  # 2

# not - инверсия
flag = True
print(not flag)  # False
print(not(not flag))  # True
'''


'''
M = []
M.append(2)
print(help(M.append))
# append(object, /) method of builtins.list instance
#     Append object to the end of the list.
'''

# Способы взаимодействия с библиотеками:
'''
import useful  # Просто импортируем библиотеку
print(useful.orel_or_reshka())
print(useful.ALPHABET)


import useful as u  # Переименовали библиотеку в более короткую форму
print(u.orel_or_reshka())
print(u.ALPHABET)


from useful import orel_or_reshka, ALPHABET, who_is_name  # Импортируем конкретные функции и константы
print(orel_or_reshka())
print(ALPHABET)


# Не рекомендуется*
from useful import *  # Импортируем сразу все содержимое
print(orel_or_reshka())
print(ALPHABET)
print(who_is_name())

# Сочетание клавиш ctrl + B - ведет к описанию функции (или библиотеки)
print(who_is_name.__doc__)
print(my_convert.__doc__)
print(help(my_convert))
# Универсальная функция для перевода в системы счисления от 2-ой до 36-ой
#     :param number: Переводимое 10-ное число
#     :param system: Система счисления в которую будем переводить
#     :return: Результат вернем в виде строки
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = []
# КЕГЭ  = []
# на следующем уроке: Создать учебный репозиторий через github
