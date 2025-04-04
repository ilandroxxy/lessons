# region Домашка: ******************************************************************

# https://education.yandex.ru/ege/task/4361eddf-5383-491c-a4a7-a67acaf27b9a
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = sorted([int(x) for x in s.split(';')])
    flag = 0
    copied = [x for x in M if M.count(x) == 3]
    not_copied = [x for x in M if M.count(x) == 1]
    if len(copied) == 3 and len(not_copied) == 3:
        flag += 1
    chet = [x for x in M if x % 2 == 0]
    nechet = [x for x in M if x % 2 != 0]
    if len(chet) > len(nechet):
        flag += 1
    if (M[-1] + M[-2]) > 2*(M[0] + M[1] + M[2] + M[3]):
        flag += 1
    if flag >= 2:
        cnt += 1
print(cnt)
'''
from zoneinfo import reset_tzpath

'''
R = []
M = [int(x) for x in open('0. files/17.txt')]
U = [x for x in M if abs(x) % 41 == 0 and x > 0]
for i in range(len(M) - 1):
    x, n = M[i], M[i + 1]
    if abs(x - n) % min(U) == 0:
        R.append(x + n)
print(len(R), max(R))
'''
'''
R=[]
M=[int(x)for x in open('0. files/17.txt')]
Q=[x for x in M if abs(x)%10==3 and len(str(abs(x)))==3]
for i in range(len(M)-2):
    a,b,c = M[i],M[i+1],M[i+2]
    if (a in Q) + (b in Q) + (c in Q) >= 1:
        if (a + b + c) < max(Q):  # а сумма всех элементов меньше максимального элемента последовательности, оканчивающегося на 3 и являющегося трёхзначным числом.
            R.append(a+b+c)
print(len(R),max(R))
'''
'''
R=[]
M=[int(x)for x in open('0. files/17.txt')]
A=[x for x in M if abs(x)%32==0]
for i in range(len(M)-1):
    a,b=M[i],M[i+1]
    if (a < 0)+(b < 0) >= 1:
        if (a+b)<len(A):
            R.append(a+b)
print(len(R),max(R))
'''
'''
R=[]
M=[int(x)for x in open('0. files/17.txt')]
for i in range(len(M)-1):
    a,b=M[i],M[i+1]
    if (a % 55 == min(M)) + (b % 55 == min(M)) >= 1:
        R.append(a+b)
print(len(R),min(R))
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 20811 Апробация 05.03.25 (Уровень: Базовый)
# 1 куча: +1, +4, *2 | >= 51,  1 ≤ s ≤ 50
'''
def F(s, n):
    """
    n = 1: Первый шаг Пети
    n = 2: Первый шаг Вани
    n = 3: Второй шаг Пети
    n = 4: Второй шаг Вани

    :param s: - это кол-во камней в куче
    :param n: - это шаг игры
    """
    if s >= 51:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s+1, n-1), F(s+4, n-1), F(s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

print([s for s in range(1, 51) if F(s, 2)])
print([s for s in range(1, 51) if F(s, 3) and not F(s, 1)])
print([s for s in range(1, 51) if F(s, 4) and not F(s, 2)])
'''


# № 17682 Пересдача 04.07.24 (Уровень: Базовый)
'''
def F(s, n):
    if s >= 67:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s+1, n-1), F(s+3, n-1), F(s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

print([s for s in range(1, 67) if F(s, 2)])
print([s for s in range(1, 67) if F(s, 3) and not F(s, 1)])
print([s for s in range(1, 67) if F(s, 4) and not F(s, 2)])
'''

'''
from math import ceil, floor

print(ceil(7 / 2))  # 4 - округляет вверх
print(floor(7 / 2))  # 3 - округляет вниз
'''


# № 17875 Демоверсия 2025 (Уровень: Базовый)
# -2, -5, //3 | <= 19
'''
from math import floor

def F(s, n):
    if s <= 19:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s-2, n-1), F(s-5, n-1), F(floor(s/3), n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

print([s for s in range(20, 1000) if F(s, 2)])
print([s for s in range(20, 1000) if F(s, 3) and not F(s, 1)])
print([s for s in range(20, 1000) if F(s, 4) and not F(s, 2)])
'''


# № 20907 Апробация 05.03.25 (Уровень: Базовый)
# +1, *2 |  a + s >= 81
'''
def F(a, s, n):
    if a+s >= 81:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a+1, s, n-1), F(a, s+1, n-1), F(a*2, s, n-1), F(a, s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

print([s for s in range(1, 74) if F(7, s, 2)])  # [19,
print([s for s in range(1, 74) if F(7, s, 3) and not F(7, s, 1)])
print([s for s in range(1, 74) if F(7, s, 4) and not F(7, s, 2)])
'''


def F(s, n):
    if s <= 116:
        return n%2==0
    if n == 0:
        return 0
    h = [F(s-7, n-1), F(s//3, n-1)]
    return any(h) if (n-1) % 2 ==0 else any(h)

print(max([s for s in range(117, 10001) if F(s, 3)]))
print([s for s in range(117, 10001) if F(s, 3)  and not F(s, 1)])
print([s for s in range(117, 10001) if F(s, 4) and not F(s, 2)])


# endregion Урок: ********************************************************************
# #
# #
# region Разобрать: ********************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25, 26.1]
# КЕГЭ  = [5, 9, 14, 15, 16, 17, 22, 23]
# на следующем уроке:


# Первый пробник 21.12.24:
# Александр 19/25 -> 75 вторичных баллов +[1-5, 7, 9-10, 12, 14-16, 18-22, 24, 25] -[6, 8, 11, 13, 17, 23]

# Второй пробник 28.02.25:
# Александр 24/25 -> 88 вторичных баллов +[1-10, 12-25] -[11]
# Саша 10/25 -> 51 вторичных баллов +[1, 2, 4, 12, 14-16, 19, 23, 25] -[3, 5, 6-10, 11, 13, 17, 18, 20-22, 24]
