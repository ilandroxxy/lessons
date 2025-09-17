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


# 1. Системы счисления (перевод)
# 2. Срезы строк (списков)
# 3. Основы списков

# Пару слов про срезы
'''
# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
# -i -5   -4   -3   -2   -1

print(M[2:])  # ['c', 'd', 'e']
print(M[-3:])  # ['c', 'd', 'e']
print(M[:-2])  # 'a', 'b', 'c']
'''

# № 23742 Демоверсия 2026 (Уровень: Базовый)
'''
R = []
for n in range(1, 10000):
    s = bin(n)[2:]  # s = f'{n:b}'  # s = convert(n, 2)
    if n % 3 == 0:
        s = s + s[-3:]
    else:
        x = (n % 3) * 3
        s = s + f'{x:b}'
    r = int(s, 2)
    # ValueError: int() base must be >= 2 and <= 36, or 0
    if r >= 200:
        R.append(n)
print(min(R))
'''


# Универсальная функция перевода в различные системы счисления
'''
from string import *
alp = digits + ascii_uppercase  # 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ
alp = '0123456789ABC...'
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r

n = 8
print(convert(n, 2))  # 1000
print(convert(n, 3))  # 22
print(convert(n, 8))  # 10
print(convert(n, 16))  # 8
print(convert(10**8, 16))  # 5F5E100
print(int('5F5E100', 16))  # 10**8
'''


# № 23364 Резервный день 19.06.25 (Уровень: Базовый)
'''
def f(x, b):
    s = ''
    while x > 0:
        s = str(x % b) + s
        x //= b
    return s

for n in range(1, 1000):
    r = f(n, 3)
    if n % 3 == 0:
        r = '1' + r + '02'
    else:
        t = f((n % 3)*4, 3)
        r = r + t
    a = int(r, 3)
    if a < 100:
        print(n)
'''


# № 22272 (Уровень: Средний)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')


def f(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r


R = []
for n in range(1, 10000):
    s = f(n, 9)
    if s[0] == '7':
        s = s.replace('6', '*')
        s = s.replace('3', '6')
        s = s.replace('*', '3')
        s = s + '34'
    else:
        s = '3' + s[1:] + '45'

    r = int(s, 9)
    if r < 2876:
        R.append([r, n])

print(max(R))
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [5, 9, 17]
# КЕГЭ = []
# на следующем уроке:
