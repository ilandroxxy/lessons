# region Домашка: ******************************************************************


# https://inf-ege.sdamgia.ru/problem?id=55592
'''
k = 0
for n in range(14, 15):
    r = bin(n)[2:]
    for _ in range(3):
        sctt = len([x for x in str(n) if x in '02468'])
        snecht = len([x for x in str(n) if x not in '02468'])

        if sctt > snecht:
            r = r + '1'
        elif snecht > sctt:
            r = r + '0'
        else:
            if n % 2 == 0:
                r = r + '0'
            else:
                r = r + '1'
        n = int(r, 2)

    ans = int(r, 2)
    print(ans)
    if 123_455 <= ans <= 987_654_321:
        k += 1
print(k)
'''


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r

n = 3*3125**8 + 2*625**7 - 4*625**6 +3*125**5 - 2*25**4 - 2025
s = convert(n, 25)
print(s.count('0'))  # 10
print(len(s) - s.count('0'))
'''



# № 23752 Демоверсия 2026 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r


n = 2 * 2187**2020 + 729**2021 - 2*243**2022 + 81**2023 - 2*27**2024 - 6561
s = convert(n, 27)
print(len([x for x in s if x > '9']))
'''


# № 17870 Демоверсия 2025 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r

R = []
for x in range(1, 2030):
    n = 7**170 + 7**100 - x
    s = convert(n, 7)
    if s.count('0') == 71:
        R.append(x)
print(max(R))
'''

'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r

R = []
for x in range(1, 3000):
    n = 4**210 + 4**110 - x
    s = convert(n, 4)
    if s.count('0') == 105:
        print(x)
    R.append(s.count('0'))
print(max(R))  # 105
'''


# № 21413 Досрочная волна 2025 (Уровень: Базовый)
'''
R = []
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alp[:21]:
    A = int(f'82934{x}2', 21)
    B = int(f'2924{x}{x}7', 21)
    C = int(f'67564{x}8', 21)
    if (A + B + C) % 20 == 0:
        R.append((A + B + C) // 20)
print(min(R))
'''


# Тип 14 №48388
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alp[:12]:
    for y in alp[:12]:
        A = int(f'{x}231{y}', 12)
        B = int(f'78{x}98{y}', 14)
        if (A + B) % 99 == 0:
            print((A + B) // 99)
'''


# № 23935 (Уровень: Базовый)
'''
# alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
# print(alp.index('H'))
for p in range(18, 36+1):
    A = int(f'22A12E', p)
    B = int(f'2F1391', p)
    C = int(f'1H05D0', p)
    if (A  + B - C) % 19 == 0:
        print(p, (A  + B - C) // 19)
'''

# № 13246 Открытый курс "Слово пацана" (Уровень: Средний)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for p in range(10, 36+1):
    for x in alp[:p]:
        for y in alp[:p]:
            A = int(f'24{x}9', p)
            B = int(y+x+y+'3', p)
            C = int(f'{x}4{y}0', p)
            if A + B == C:
                print(int(x + y + y, p))
'''


# № 7702 (Уровень: Сложный)
'''
R = []
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for y in range(9, 17+1):
    for x in alp[:y]:
        A = int(f'5{x}{alp[y]}A', 18)
        B = int(f'18{x}7', y)
        R.append(A + B)
print(len(set(R)))
'''

# Тип 9 №76677

cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(',')]
    avg = sum(M) / len(M)
    zam = [x for x in M if x > avg]
    if len([x for x in zam if x % 2 == 0]) > len([x for x in zam if x % 2 != 0]):
        if sum([x for x in M if x % 2 == 0]) < sum([x for x in M if x % 2 != 0]):
            cnt += 1
print(cnt)

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [5, 9, 14, 17]
# КЕГЭ = []
# на следующем уроке:
