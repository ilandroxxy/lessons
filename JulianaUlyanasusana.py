# region Домашка: ******************************************************************

# № 2573 (Уровень: Средний)
# https://stepik.org/lesson/1038682/step/4?unit=1062773
'''
maxi = 0
M = []
for i in range(301, 350):
    s = i * '5'

    while '55555' in s:
        s = s.replace('55555', '88', 1)
        s = s.replace('888', '55', 1)
    if s.count('5') > maxi:
        maxi = s.count('5')
        M.append(i)
print(max(M))
'''


# № 12921 (Уровень: Базовый)
# https://stepik.org/lesson/1038682/step/5?unit=1062773
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
    if summa % 10 == 7:
        print(n)
        break
'''


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Задание 5 https://education.yandex.ru/ege/task/bcf2f1cf-26f3-4678-bf57-1b1eb99555ad
'''
M = []
for n in range(2, 1000):
    s = f'{n:b}'  # s = bin(n)[2:]

    for i in range(2):
        if s[-2] == s[-1]:
            s = s + '0'
        else:
            s = s + '1'

    r = int(s, 2)

    if r > 93:
        M.append(n)
        
print(min(M))
'''


# # Задание 5  https://education.yandex.ru/ege/task/f1fac643-8eea-4ba9-8bb9-85670cd87bdd
'''
for n in range(1, 1000):
    s = bin(n)[2:]
    if n % 2 == 0:
        s = '1' + s + '1'
    else:
        s = s + '10'
    r = int(s, 2)
    if r > 179:
        print(n)
        break
'''


# Задание 5 https://education.yandex.ru/ege/task/fef8d85c-6b9d-43d3-954c-6acb16a1f5a9
'''
for n in range(11, 1000):
    s = bin(n)[2:]
    if n % 5 == 0:
        s = s + s[-3:]
    else:
        x = (n % 5) * 5
        s = s + bin(x)[2:]
    r = int(s, 2)
    if r > 512:
        print(n)
        break
'''
'''
def convert(n, b):
    s = ''
    while n > 0:
        s += str(n % b)
        n //= b
    return s[::-1]


for n in range(11, 1000):
    s = convert(n, 2)
    if n % 5 == 0:
        s = s + s[-3:]
    else:
        x = (n % 5) * 5
        s = s + convert(x, 2)
    r = int(s, 2)
    if r > 512:
        print(n)
        break
'''

# Задание 5 https://education.yandex.ru/ege/task/da798c09-d5d5-46c3-bbfb-16f606da3ef5
'''
def convert(n, b):
    s = ''
    while n > 0:
        s += str(n % b)
        n //= b
    return s[::-1]


for n in range(5, 1000):
    s = convert(n, 4)
    summa = sum([int(x) for x in s])
    if summa % 2 == 0:
        s = s + s[:2]
    else:
        s = '10' + s[2:] + '2'  # два левых разряда заменяются на «10».
    r = int(s, 4)

    if r < 250:
        print(n)
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
