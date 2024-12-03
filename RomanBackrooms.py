# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Задание 12 https://education.yandex.ru/ege/task/b3daa88d-758d-4067-b9c8-542397c4b26d
'''
for n in range(4, 100):
    s = '2' + '5' * n

    while '25' in s or '35' in s or '555' in s:
        if '25' in s:
            s = s.replace('25', '53', 1)
        if '35' in s:
            s = s.replace('35', '2', 1)
        if '555' in s:
            s = s.replace('555', '23', 1)

    summa = sum(map(int, s))
    if summa % 7 == 0:
        print(n)
        break
'''
# Ответ: 21


# Задание 12 https://education.yandex.ru/ege/task/4fefb859-0701-43ee-b1ec-1be11f81e26f
'''
for x in range(50):
    for y in range(50):
        for z in range(50):
            s = '>' + '1' * x + '2' * y + '3' * z

            while '>1' in s or '>2' in s or '>3' in s:
                if '>1' in s:
                    s = s.replace('>1', '21>3', 1)
                if '>2' in s:
                    s = s.replace('>2', '32>', 1)
                if '>3' in s:
                    s = s.replace('>3', '11>2', 1)

            if s.count('1') == 71 and s.count('2') == 54 and s.count('3') == 37:
                print(y)
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
