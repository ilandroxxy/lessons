# region Домашка: ******************************************************************

# № 12922 PRO100 ЕГЭ 26.01.24 (Уровень: Базовый)
'''
from ipaddress import *
cnt = 0
net = ip_network('136.36.240.16/255.255.255.248', 0)
for ip in net:
    # b = bin(int(ip))[2:]
    b = f'{ip:b}'
    if '101' not in b:
        cnt += 1
print(cnt)
'''


# № 8503 Апробация 17.05 (Уровень: Базовый)
'''
def F(x, A):
    return ((x & 52 != 0) and (x & 36 == 0)) <= (x & A != 0)


for A in range(1, 100000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
        break
'''

'''
def F(x, a1, a2):
    P = 10 <= x <= 45
    Q = 35 <= x <= 78
    A = a1 <= x <= a2
    return ((not P) <= Q) and (not A)


R = []
M = [x / 4 for x in range(1 * 4, 90 * 4)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) == False for x in M):
            R.append(a2 - a1)
print(min(R))  # 68.0 -> 68
'''

# № 12469 (Уровень: Базовый)
'''
def F(x, a1, a2):
    D = 7 <= x <= 68
    C = 29 <= x <= 100
    A = a1 <= x <= a2
    return D <= (((not C) and (not A)) <= (not D))


R = []
M = [x / 10 for x in range(1 * 10, 110 * 10)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(min(R))  # 21.75 -> 21.8 -> 21.9 -> 22
'''
# Ответ: 22


# № 18930 Новогодний вариант 2025 (Уровень: Базовый)
'''
def F(x, a1, a2):
    P = 10 <= x <= 150
    Q = 160 <= x <= 250
    R = 240 <= x <= 300
    A = a1 <= x <= a2
    return (Q <= P) or ((not A) <= R)

R =[]
M = [x / 2 for x in range(1 * 2, 310 * 2)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
            print(min(R))
'''


# № 18595 (Уровень: Базовый)
'''
def F(x, A1, A2):
    C = 48 <= x <= 94
    J = 83 <= x <= 100
    A = A1 <= x <= A2
    return (not(C or J)) <= (not A)


R = []
M = [x / 5 for x in range(35 * 5, 110 * 5)]
for A1 in M:
    for A2 in M:
        if all(F(x, A1, A2) for x in M):
            R.append(A2 - A1)
print(max(R)) #74.8 -> 75
'''
#Ответ: 75


def F(A, x):
    return (x & 57 == 0) or ((x & 23 == 0) <= (x & A != 0))


for A in range(1, 1000):
    if all(F(A, x) for x in (1, 100000)):
        print(A)
        break



# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 10, 12, 13, 14, 15, 25]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Женя 5/7 -> 34 вторичных баллов +[2, 5, 8, 12, 14] -[6, 10]
# Ярослав 2/7 -> 14 вторичных баллов +[2, 12] -[5, 6, 8, 10, 14]
