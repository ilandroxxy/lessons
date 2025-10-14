# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 23752 Демоверсия 2026 (Уровень: Базовый)
'''
def convert(n, b):
    alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

n = 2*2187**2020 + 729**2021 -2*243**2022 + 81**2023 - 2*27**2024 - 6561
s = convert(n, 27)
print(len([x for x in s if x > '9']))


# Варианты условий для первого прототипа
print(s.count('0'))  # Кол-во значащих нулей
print(s.count('0') + s.count('4'))  # Кол-во нулей и четверок
print(len(s) - s.count('0'))  # Кол-во ненулевых значений
print(len(set(s)))  # Кол-во различных значений
print(len([x for x in s if x > '9']))  # Количество цифр с числовым значением, превышающим 9.
'''


# № 23754 Демоверсия 2026 (Уровень: Базовый)
'''
def convert(n, b):
    alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]


RES = []
for x in range(1, 3000+1):
    n = 9*11**210 + 8*11**150 - x
    s = convert(n, 11)
    if s.count('0') == 60:
        RES.append(x)
print(max(RES))
'''


# № 23753 Демоверсия 2026 (Уровень: Базовый)
'''
RES = []
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alp[:29]:
    A = int(f'923{x}874', 29)
    B = int(f'524{x}6152', 29)
    if (A + B) % 28 == 0:
        RES.append((A + B) // 28)
print(max(RES))
'''


# 21413
'''
RES = []
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alp[:21]:
    A = int(f'82934{x}2',21)
    B = int(f'2924{x}{x}7',21)
    C = int(f'67564{x}8',21)
    if (A+B+C) % 20 ==0:
        RES.append((A + B + C) // 20)
print(min(RES))
'''

# № 21709 ЕГКР 19.04.25 (Уровень: Базовый)
'''
RES = []
def convert(n, b):
    alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

for x in range(1, 3000+1):
    n = 4**210+4**110-x
    s = convert(n,4)
    # RES.append(s.count('0'))
    if s.count('0') == 105:
        RES.append(x)
# print(max(RES)) $ 105
print(min(RES))
'''


def convert(n, b):
    alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]


RES = []
for x in range(1, 2030 + 1):
    n = 3 ** 100 - x
    s = convert(n, 3)
    if s.count('0') == 1:
        RES.append(x)
print(max(RES))




#
# № 17870 Демоверсия 2025 (Уровень: Базовый)
'''
def convert(n, b):
    alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

RES = []
for x in range(1, 2030 + 1):
    n = 7 ** 170 + 7 ** 100 - x
    s = convert(n, 7)
    if s.count('0') == 71:
        RES.append(x)
print(max(RES))
'''
# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [5, 14]
# КЕГЭ = []
# на следующем уроке:
