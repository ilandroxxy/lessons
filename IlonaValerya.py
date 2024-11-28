# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Задание 14 https://education.yandex.ru/ege/task/39bb599c-c811-49fe-84b7-be8dd035d167
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    s = ''
    while n > 0:
        s = s + alphabet[n % b]
        n = n // b
    return s[::-1]


n = 5**23 + 25**12
print(convert(n, 5).count('0'))
'''
# Ответ: 23


# Задание 14 https://education.yandex.ru/ege/task/18a7009f-9d5c-467d-88c4-102e7ed5aca4
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    s = ''
    while n > 0:
        s = s + alphabet[n % b]
        n = n // b
    return s[::-1]


n = 2*729**75 + 2*243**78 + 81**81 + 2*27**84 + 2*9**87 + 58
s = convert(n, 27)
print(s.count('0'))
'''


# Задание 14 https://education.yandex.ru/ege/task/35d1a21d-f415-4666-830a-8028485771a4
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    s = ''
    while n > 0:
        s = s + alphabet[n % b]
        n = n // b
    return s[::-1]


for x in range(2042+1):
    n = 25**61 + 5**178 - x
    s = convert(n, 5)
    if s.count('0') == 60:
        print(x)
'''


# Задание 14 https://education.yandex.ru/ege/task/258db83f-773f-43a0-88da-89f8e3c2ab70

alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

for x in alphabet[:18]:
    A = int(f'77968{x}11', 18)
    B = int(f'4{x}213', 18)
    if (A + B) % 7 == 0:
        print((A + B) // 7)


# https://inf-ege.sdamgia.ru/problem?id=48386

alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

for x in alphabet[:15]:
    for y in alphabet[:15]:
        A = int(f'90{x}4{y}', 15)
        B = int(f'91{x}{y}2', 16)
        if (A + B) % 56 == 0:
            print((A + B) // 56)

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 14]
# КЕГЭ  = []
# на следующем уроке:
