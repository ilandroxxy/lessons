# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Номер 5
'''
m = []
for n in range(1, 1000):
    s = bin(n)[2:]  # 0b1000
    # s = f'{n:b}'
    if n % 2 == 0:
        s = '10' + s
    else:
        s = '1' + s + '01'
    r = int(s, 2)
    if n <= 12:
        m.append(r)
print(max(m))
'''


# Номер 23
'''
def f(a, b):
    if a <= b:
        return a == b  # a < b (False), a == b (True)
    return f(a - 2, b) + f(a // 2, b)
    # True + True + False + True == 3


print(f(38, 16) * f(16, 2))
'''

# Номер 14
'''
m = []
for x in range(1, 2031):
    n = 7 ** 170 + 7 ** 100 - x
    s = ''
    while n > 0:
        s += str(n % 7)
        n //= 7
    m.append([s.count('0'), x])
print(max(m))


m = []
for x in range(1, 2031):
    n = 7 ** 170 + 7 ** 100 - x
    cnt = 0
    while n > 0:
        if n % 7 == 0:
            cnt += 1
        n //= 7
    m.append([cnt, x])
print(max(m))
'''


# Функция для решения 25 номеров с делителями:
'''
def divisors(x):
    div = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            div.append(j)
            div.append(x // j)
    return sorted(set(div))

# [1, 2, 3, 4]  # 24 // 4 == 6
print(divisors(24))  # [1, 2, 3, 4, 6, 8, 12, 24]
print(divisors(16))  # [1, 2, 4, 8, 16]
'''


# Номер 25 (20814)
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            div.append(j)
            div.append(x // j)
    return sorted(set(div))


cnt = 0
for x in range(500_000+1, 10**10):
    d = divisors(x)
    R = sum(d)
    if R % 10 == 9:
        print(x, R)
        cnt += 1
        if cnt == 5:
            break
'''


# Номер 9 (17863)
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied = [x for x in M if M.count(x) == 3]
    uncopied = [x for x in M if M.count(x) == 1]
    if len(copied) == 3 and len(uncopied) == 3:
        if sum(copied) ** 2 > sum(uncopied) ** 2:
            cnt += 1
print(cnt)
'''


# endregion Урок: ********************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1.1, 2, 5, 6, 8, 9, 12, 13, 14, 15, 16, 18, 23, 25]
# КЕГЭ  = []
# на следующем уроке: 17 номер


# Первый пробник 21.12.24:
# Матвей 10/14 -> 51 вторичных баллов +[1, 3, 4, 6, 7, 10, 11, 14, 18, 25] -[2, 5, 8, 12]

# Второй пробник 28.02.25:
# Матвей 14/29 -> 62 вторичных баллов +[1-4, 6, 7, 10, 11, 14, 15, 16, 18, 23, 25] -[5, 8, 12, 13]
