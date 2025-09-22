# region Домашка: ******************************************************************


# https://stepik.org/lesson/1038432/step/2?unit=1060804
'''
L = []
for n in range(1, 10000):
    s = bin(n)[2:]

    for i in range(2):
        if s.count('1') % 2 == 0:
            s = s + '00'
            s = '11' + s[2:]
        else:
            s = s + '11'
            s = '10' + s[2:]

    r = int(s, 2)
    if n < 100:
        L.append(r)
print(max(L))
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 23752 Демоверсия 2026 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def G(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r

n = 2 * 2187**2020 + 729**2021 -2*243**2022 + 81**2023 - 2*27**2024 - 6561
s = G(n, 27)
print(len([x for x in s if x > '9']))
'''

# № 19880 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def G(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r

n = 15625**16 - 3125**3 * 25**19 + 625**4 - 2005
s = G(n, 25)
print(s.count('0'))  # Сколько значащих нулей содержится
print(len(s) - s.count('0'))  # Сколько не нулевых чисел содержится
'''


# № 23754 Демоверсия 2026 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def G(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r

R = []
for x in range(1, 3000):
    n = 9 * 11**210 + 8*11**150 - x
    s = G(n, 11)
    if s.count('0') == 60:
        R.append(x)
print(max(R))
'''


# № 23560 Пересдача 03.07.25 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def G(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r

R = []
for x in range(1, 2400):
    n = 7 * 9**210 + 6*9**110 - x
    s = G(n, 9)
    if s.count('0') == 100:
        R.append(x)
print(max(R))
'''

# Татьяна
# № 23198 Основная волна 10.06.25 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def G(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r


R = []
for x in range(1, 3000):
    n = 9 ** 150 + 9 ** 30 - x
    s = G(n, 9)
    if s.count('0') == 122:
        R.append(x)
print(min(R))
'''


# Анна
# № 21900 Открытый вариант 2025 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')


def G(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r


R = []
for x in range(1, 2300):
    n = 7 ** 350 + 7 ** 150 - x
    s = G(n, 7)
    if s.count('0') == 200:
        R.append(x)
print(max(R))
'''



# № 23273 Основная волна 11.06.25 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alp[:29]:
    A = int(f'923{x}874', 29)
    B = int(f'524{x}6152', 29)
    if (A + B) % 28 == 0:
        print(x, (A + B) // 28)
'''


# № 21413 Досрочная волна 2025 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alp[:21]:
    A = int(f'82934{x}2', 21)
    B = int(f'2924{x}{x}7', 21)
    C = int(f'67564{x}8', 21)
    if (A + B + C) % 20 == 0:
        print(x, (A + B + C) // 20)
'''


# Татьяна
# № 17868 Демоверсия 2025 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
R = []
for x in alp[:19]:
    A = int(f'98897{x}21', 19)
    B = int(f'2{x}923', 19)
    if (A + B) % 18 == 0:
        R.append((A + B) // 18)
print(max(R))
'''

# Анна
# № 19246 ЕГКР 21.12.24 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
R = []
for x in alp[:25]:
    A = int(f'11353{x}12', 25)
    B = int(f'135{x}21', 25)
    if (A + B) % 24 == 0:
        R.append((A + B) // 24)
print(max(R))
'''


# Тип 14 №48391

# Операнды арифметического выражения записаны в
# системах счисления с основаниями 12 и 14:
#
# yAAx_12 +  x02y_14.
#
# В записи чисел переменными x и y обозначены
# допустимые в данных системах счисления неизвестные
# цифры. Определите значения x и y, при которых
# значение данного арифметического выражения будет
# наименьшим и кратно 80.
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alp[:12]:
    for y in alp[:12]:
        A = int(f'{y}AA{x}', 12)
        B = int(f'{x}02{y}', 14)
        if (A + B) % 80 == 0:
            print((A + B) // 80)
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 14]
# КЕГЭ = []
# на следующем уроке:
