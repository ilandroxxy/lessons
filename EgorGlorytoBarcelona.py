# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Задание 12 https://education.yandex.ru/ege/task/284b3237-5a54-46f9-87d9-cc13ced58bec

# Какая строка получится в результате применения приведённой ниже программы к
# строке, состоящей из 81 идущей подряд цифры 1? В ответе запишите полученную строку.
#
# ПОКА нашлось (11111) ИЛИ нашлось (888)
#      ЕСЛИ нашлось (11111)
#          ТО заменить (11111, 88)
#      ИНАЧЕ заменить (888, 8)
'''
s = '1' * 81
while '11111' in s or '888' in s:
    if '11111' in s:
        s = s.replace('11111', '88', 1)
    else:
        s = s.replace('888', '8', 1)
print(s)
'''


# Задание 12 https://education.yandex.ru/ege/task/01111836-0d9c-4935-808c-c2fc3acdb738
'''
for n in range(4, 1000):
    s = '2' + '5' * n

    while '25' in s or '355' in s or '555' in s:
        if '25' in s:
             s = s.replace('25', '5', 1)
        if '355' in s:
             s = s.replace('355', '52', 1)
        if '555' in s:
             s = s.replace('555', '3', 1)
    if s.count('3') == 3:
        print(n)
        break
'''


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 4, 6, 12]
# КЕГЭ  = []
# на следующем уроке:
