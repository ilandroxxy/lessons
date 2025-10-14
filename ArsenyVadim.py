# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 23752 Демоверсия 2026 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

n = 2*2187**2020 + 729**2021 - 2*243**2022 + 81**2023 -2*27**2024 - 6561
s = convert(n, 27)

# Варианты условий для этого прототипа:
print(s.count('0'))  # Какое количество значащих нулей
print(s.count('0')  + s.count('4'))  # Количество нулей и четверок
print(len(s) - s.count('0'))  # Количество ненулевых символов
print(len(set(s)))  # Кол-во различных значений
print(len([x for x in s if x > '9']))  # количество цифр с числовым значением, превышающим 9
'''


# № 23754 Демоверсия 2026 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
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

'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
print(alp[:2])  # ['0', '1']
print(alp[:8])  # ['0', '1', '2', '3', '4', '5', '6', '7']
print(alp[:16])  # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
'''

# № 23753 Демоверсия 2026 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
RES = []
for x in alp[:29]:
    A = int(f'923{x}874', 29)
    B = int(f'524{x}6152', 29)
    if (A + B) % 28 == 0:
        RES.append((A + B) // 28)
print(max(RES))
'''

# 19246
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
res = []
for x in alp[:25]:
    A = int(f'11353{x}12', 25)
    B = int(f'135{x}21', 25)
    if (A + B) % 24 == 0:
        res.append((A + B) // 24)
print(max(res))
'''


# 21413
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
S = []
for x in alp[:21]:
    A = int(f'82934{x}2', 21)
    B = int(f'2924{x}{x}7', 21)
    C = int(f'67564{x}8', 21)
    R = A + B + C
    if R % 20 == 0:
        S.append(R // 20)
print(min(S))
'''

# 21900
'''
def convert(n, b):
    alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

list = []
for x in range(1, 2300 + 1):
    a = 7 ** 350 + 7 ** 150 - x
    s = convert(a, 7)
    if s.count('0') == 200:
        list.append(x)
print(max(list))
'''


# 23198
'''
def convert(n, b):
    alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

RES = []
for x in range(1, 3001):
    a = 9**150 + 9**30 - x
    b = convert(a, 9)
    if b.count('0') == 122:
        RES.append(x)
print(min(RES))
'''


# https://inf-ege.sdamgia.ru/problem?id=48388
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
res = []
for x in alp[:12]:
    for y in alp[:12]:
        A = int(f'{x}231{y}', 12)
        B = int(f'78{x}98{y}', 14)
        if (A + B) % 99 == 0:
            res.append((A + B) // 99)
print(min(res))
'''


# № 13246 Открытый курс "Слово пацана" (Уровень: Средний)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for p in range(10, 36+1):
    for x in alp[:p]:
        for y in alp[:p]:
            A = int(f'24{x}9', p)
            B = int(y + x + y + '3', p)
            C = int(f'{x}4{y}0', p)
            if A + B == C:
                print(int(x + y + y, p))
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [5, 14]
# КЕГЭ  = []
# на следующем уроке:
