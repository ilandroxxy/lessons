# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r



# № 10097 Демоверсия 2024 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r
    
n = 3*3125**8 + 2*625**7 - 4*625**6 + 3*125**5 - 2*25**4 - 2024
s = convert(n, 25)
print(s.count('0'))
'''

# № 12246 ЕГКР 16.12.23 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r
    
n = 2*729**333  +2*243**334 -81**335 + 2*27**336 - 2*9**337 - 338
s = convert(n, 9)
print(len(s) - s.count('0'))
'''


# № 14343 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r
    
n = 5*343**2031 + 4*49**2142 - 3*7**111 + 7**222
s = convert(n, 7)
print(sum(map(int, s)))
print(sum([int(x) for x in s]))
'''


# № 15327 Досрочная волна 2024 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r
    
n = 3*2187**2020 + 3*729**2021 - 2*81**2022 + 27**2023 -4*3**2024 - 2029
s = convert(n, 27)
print(len([x for x in s if x > '9']))
'''


# № 17555 Основная волна 08.06.24 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r

for x in range(2030):
    n = 7**91 + 7**160 - x
    s = convert(n, 7)
    if s.count('0') == 70:
        print(x)
'''

# Вариант 2
'''
for x in range(2030):
    n = 7**91 + 7**160 - x
    s = ''
    while n > 0:
        s = str(n % 7)
        n //= 7
    if s.count('0') == 70:
        print(x)
'''


# № 20808 Апробация 05.03.25 (Уровень: Средний)
'''
R = []
for x in range(1, 2030):
    n = 7 ** 170 + 7**100 - x
    s = convert(n, 7)
    if s.count('0') == 73:
        print(x)
    R.append(s.count('0'))
print(max(R))   # 73
'''
# [[73, 343], [73, 686], [73, 1029], [73, 1372], [73, 1715]]



# № 23273 Основная волна 11.06.25 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alp[:29]:
    A = int(f'463{x}7921', 29)
    B = int(f'8241{x}153', 29)
    if (A + B) % 28 == 0:
        print(x, (A + B) // 28)
'''


# № 16261 Джобс 03.05.24 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alp[:21]:
    for y in alp[:21]:
        A = int(f'943697{x}21', 21)
        B = int(f'2{y}9253', 21)
        if (A - B) % 20 == 0:
            print(alp.index() - int(y, 21), (A - B) // 20)
'''


# https://inf-ege.sdamgia.ru/problem?id=48391
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alp[:12]:
    for y in alp[:12]:
        A = int(f'{y}AA{x}', 12)
        B = int(f'{x}02{y}', 14)
        if (A + B) % 80 == 0:
            print((A + B) // 80)
'''


# Илья
# № 23273 Основная волна 11.06.25 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alp[:29]:
    A = int(f'463{x}7921', 29)
    B = int(f'8241{x}153', 29)
    if (A + B) % 28 == 0:
        print(x, (A + B) // 28)
        # ОТВЕТ : 7567913105
'''


# Егор
# № 21413 Досрочная волна 2025 (Уровень: Базовый)
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
M = []
for x in alphabet[:21]:
    A = int(f'82934{x}2', 21)
    B = int(f'2924{x}{x}7', 21)
    C = int(f'67564{x}8', 21)
    if (A + B + C) % 20 == 0:
        M.append((A + B + C) // 20)
print(min(M))
'''
#72450445


# Илья
# № 23754 Демоверсия 2026 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')


def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r


for x in range(3000):
    n = 9 * 11 ** 210 + 8 * 11 ** 150 - x
    s = convert(n, 11)
    if s.count('0') == 60:
        print(x)
'''
# ответ: 2992


# Егор
# № 23560 Пересдача 03.07.25 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r

m = []
for x in range(1,2400):
    n = 7* 9**210 + 6 * 9**110 - x
    s = convert(n,9)
    if s.count('0')==100:
        m.append(x)
print(max(m))
'''
#2394 <----








# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 14]
# КЕГЭ = []
# на следующем уроке:
