# region Домашка: ******************************************************************


# n = int(input())
# numbers = [int(input()) for _ in range(n)]
# print(numbers)

# Вычисли всё! https://stepik.org/lesson/1309452/step/12?unit=1324568
'''
from math import prod
n = int(input())  # 125 -> [1, 2, 5]
numbers = [int(x) for x in str(n)]
print(numbers.count(2))
print(numbers.count(numbers[-1]))
nechet = [x for x in numbers if x % 2 != 0]
print(len(nechet))
numbers7 = [x for x in numbers if x > 7]
print(sum(numbers7))
if len(numbers7) == 0:
    print(11)
elif len(numbers7) == 1:
    print(numbers[0])
else:
    # total = 1
    # for x in numbers7:
    #     total *= x
    # print(total)
    print(prod(numbers7))
print(numbers.count(0) + numbers.count(4))
'''


# Уникальные элементы списка
# https://stepik.org/lesson/1309452/step/13?unit=1324568
'''
n = int(input())
numbers = [int(input()) for _ in range(n)]

cnt = 0
for elem in numbers:
    if numbers.count(elem) == 1:
        print(elem)
        cnt += 1
if cnt == 0:
    print("Уникальных элементов нет")
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
s = '312534214312321312'
s = s.replace('2', '*')  # Сразу все '2' заменяем на '*'
# 31*534*1431*3*131*
s = s.replace('*', '2', 3)  # Заменили только первые три '*' на '2'
# 3125342143123*131*
'''

# Задание 12 https://education.yandex.ru/ege/task/50a1b75e-3829-4e52-96bc-44d8e024790e
'''
s = '3' * 70
while '333' in s or '77777' in s:  # ПОКА нашлось(333) или нашлось(77777)
    if '333' in s:  # ЕСЛИ нашлось(333)
        s = s.replace('333', '77', 1)  # ТО заменить(333,77)
    else:
        s = s.replace('77777', '7', 1)  # ИНАЧЕ заменить(77777,7)
print(s)
print(sum([int(x) for x in s]))
'''


# Задание 12 https://education.yandex.ru/ege/task/a59f3bdb-ccef-4a7f-b2d8-1bf3b3982a40
'''
s = '>' + '1' * 26 + '3' * 14 + '2' * 10
while '>1' in s or '>2' in s or '>3' in s:
    if '>1' in s:
        s = s.replace('>1', '22>', 1)
    if '>2' in s:
        s = s.replace('>2', '2>', 1)
    if '>3' in s:
        s = s.replace('>3', '1>', 1)
print(s)
print(sum([int(x) for x in s if x.isdigit()]))
# ValueError: invalid literal for int() with base 10: '>'
'''

# Задание 12 https://education.yandex.ru/ege/task/507ce5ed-774b-4364-bc31-ce0381aab30c
'''
for n in range(4, 100):
    s = '2' + '5' * n

    while '25' in s or '355' in s or '555' in s:
        if '25' in s:
            s = s.replace('25', '32', 1)
        if '355' in s:
            s = s.replace('355', '25', 1)
        if '555' in s:
            s = s.replace('555', '3', 1)

    summa = sum([int(x) for x in s])
    # if summa**0.5 == int(summa**0.5):
    if (summa**0.5).is_integer():
        print(n)
        break
'''


# Задание 12 https://education.yandex.ru/ege/task/c21fb755-a462-4ee3-97b3-4c3be812dd68
'''
for x in range(50):
    for y in range(50):
        for z in range(50):
            s = '0' + '1' * x + '2' * y + '3' * z

            while '01' in s or '02' in s or '03' in s:
                s = s.replace('01', '30', 1)
                s = s.replace('02', '3103', 1)
                s = s.replace('03', '1201', 1)
            if s.count('1') == 31 and s.count('2') == 24 and s.count('3') == 46:
                print(z)
'''
# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 6, 12]
# КЕГЭ  = []
# на следующем уроке:
