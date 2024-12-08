# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 18137 (Уровень: Средний)
'''
s = '1' * 81
while '111' in s or '88' in s:  # ПОКА нашлось (111) ИЛИ нашлось (88)
    if '88' in s:  # ЕСЛИ нашлось (88)
        s = s.replace('88', '1111', 1)  # ТО заменить (88, 1111)
    else:  # ИНАЧЕ
        s = s.replace('111', '8', 1)  # заменить (111, 8)
print(s)  # 811
print(s.count('1'))  # 2
print(len(set(s)))  # 2
'''


# Задание 12 https://education.yandex.ru/ege/task/ca477eb1-a007-4507-af8f-2b8563ac91c6
'''
for m in range(1, 1000):
    s = '4' + '6' * m

    while '46' in s or '666' in s:
        if '46' in s:
            s = s.replace('46', '5', 1)
        if '666' in s:
            s = s.replace('666', '4', 1)
    summa = sum([int(x) for x in s if x.isdigit()])
    if summa > 1000:
        print(m)
'''


# https://education.yandex.ru/ege/task/e693216f-9b91-4bec-9ae0-b023f62d2eda
'''
s = '2' * 400
while '8888' in s or '222' in s:
    if '222' in s:
        s = s.replace('222', '88', 1)
    else:
        s = s.replace('8888', '22', 1)
print(s)
'''


# https://education.yandex.ru/ege/task/507ce5ed-774b-4364-bc31-ce0381aab30c
'''
for n in range(4, 1000):
    s = '2' + '5' * n

    while '25' in s or '355' in s or '555' in s:
        if '25' in s:
            s = s.replace('25', '32', 1)
        if '355' in s:
            s = s.replace('355', '25', 1)
        if '555' in s:
            s = s.replace('555', '3', 1)
    summa = sum([int(x) for x in s])
    # if summa ** 0.5 == int(summa ** 0.5):
    if (summa ** 0.5).is_integer():  # Проверка на полные квадраты
        print(n)
        break
'''


# https://education.yandex.ru/ege/task/cb3913cb-3918-414d-9797-ad7cd3242e6e
'''
for x in range(50):
    for y in range(50):
        for z in range(50):
            s = '0' + '1' * x + '2' * y + '3' * z + '0'

            while '00' not in s:
                s = s.replace('01', '220', 1)
                s = s.replace('02', '1013', 1)
                s = s.replace('03', '120', 1)
            if s.count('1') == 13 and s.count('2') == 18:
                print(2 + x + y + z)
'''

# https://education.yandex.ru/ege/task/c21fb755-a462-4ee3-97b3-4c3be812dd68
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


for n in range(4, 1000):
    s = '2' + '5' * n

    while '25' in s or '355' in s or '555' in s:
        if '25' in s:
            s = s.replace('25', '32', 1)
        if '355' in s:
            s = s.replace('355', '25', 1)
        if '555' in s:
            s = s.replace('555', '3', 1)
    summa = sum([int(x) for x in s])
    # if summa ** 0.5 == int(summa ** 0.5):
    if (summa ** 0.5).is_integer():  # Проверка на полные квадраты
        print(n)
        break

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 12, 14]
# КЕГЭ  = []
# на следующем уроке:
