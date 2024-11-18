# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Задание 12 https://education.yandex.ru/ege/task/2ada5a06-1d3c-4302-b356-8796eb5fc06f
'''
s = '4' * 50
while '444' in s or '333' in s:
    if '444' in s:
        s = s.replace('444', '3', 1)
    else:
        s = s.replace('333', '3344', 1)
    if '3443' in s:
        s = s.replace('3443', '0', 1)
print(sum(int(x) for x in s))
'''


# Задание 12 https://education.yandex.ru/ege/task/fa6a6353-cd0b-47f3-a927-9dc7c339b34e
'''
for x in range(50):
    for y in range(50):
        for z in range(50):
            s = '0' + '1' * x + '2' * y + '3' * z + '0'

            while '00' not in s:
                s = s.replace('01', '103', 1)
                s = s.replace('02', '2011', 1)
                s = s.replace('03', '130', 1)
            if s.count('1') == 92 and s.count('2') == 16 and s.count('3') == 52:
                print(z)
'''


# Задание 12 https://education.yandex.ru/ege/task/0dae60c5-8bfc-40e6-9913-2395abbd6a99
'''
for n in range(4, 10000):
    s = '5' + '2' * n

    while '52' in s or '2222' in s or '1122' in s:
        if '52' in s:
            s = s.replace('52', '11', 1)
        if '2222' in s:
            s = s.replace('2222', '5', 1)
        if '1122' in s:
            s = s.replace('1122', '25', 1)

    summa = sum([int(x) for x in s])
    if summa == 64:
        print(n)
'''


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 12]
# КЕГЭ  = []
# на следующем уроке:
