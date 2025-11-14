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

n = 2*2187**2020 + 729**2021 -2*243**2022 + 81**2023 -2*27**2024 - 6561
s = convert(n, 27)
print(s.count('0'))  # Сколько было значащих нулей
print(s.count('0') + s.count('2'))  # Сколько было нулей и двоек
print(len(s) - s.count('0'))  # Сколько ненулевых цифр?
print(len(set(s)))  # Сколько различных цифр?
print(len([x for x in s if x > '9']))
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
for x in range(1, 3000):
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


# № 14345 (Уровень: Базовый)
'''
RES = []
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alp[:14]:
    A = int(f'4B3{x}1', 14)
    B = int(f'5{x}F83', 16)
    if (A + B) % 13 == 0:
        RES.append((A + B) // 13)
print(min(RES))
'''


# № 8418 (Уровень: Средний)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for p in range(7, 36+1):
    for x in alp[:p]:
        for y in alp[:p]:
            for z in alp[:p]:
                if int(f'{y}4{y}', p) + int(f'{y}65', p) == int(f'{x}{z}33', p):
                    print(int(x + y + z, p))
'''

# 21413
'''
RES = []
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alp[:21]:
    A = int(f'82934{x}2', 21)
    B = int(f'2924{x}{x}7', 21)
    C = int(f'67564{x}8', 21)
    if (A + B + C) % 20 == 0:
        RES.append((A + B + C) // 20)
print(min(RES))
'''


# 23273
'''
RES = []
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alp[:29]:
    A = int(f"463{x}7921", 29)
    B = int(f"8241{x}153", 29)
    if (A + B) % 28 == 0:
        RES.append((A + B) // 28)
print(min(RES))
'''

# 21413
'''
def convert(n, b):
    alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

RES = []
for x in range(1, 2300):
    n = 7 ** 350 + 7 ** 150 - x
    s = convert(n, 7)
    if s.count('0') == 200:
        RES.append(x)
print(max(RES))
'''


# 18122
'''
def convert(n, b):
    alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

RES = []
for x in range(1, 5555):
    n = 5 ** 150 + 5 ** 135 - x
    s = convert(n, 5)
    if s.count('4') == 134:
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
# ФИПИ = [2, 4, 5, 14]
# КЕГЭ = []
# на следующем уроке:
