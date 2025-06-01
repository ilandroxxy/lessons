# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
from ipaddress import*
net =ip_network('98.81.154.195/255.252.0.0',0)
for ip in net:
    print(ip)
'''


# 21909 (25)
'''
def divisors(x):
    div = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            div.append(j)
            div.append(x // j)
    return sorted(set(div))


cnt = 0
for x in range(500_001, 10**10):
    d = divisors(x)
    if len(d) > 0:
        R = sum(d)
        if R % 10 == 6:
            print(x, R)
            cnt += 1
            if cnt == 5:
                break
'''
# 500032 1070356
# 500035 606816
# 500039 501456
# 500050 949716
# 500052 1333696


# № 18148 (Уровень: Базовый)
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            div.append(j)
            div.append(x // j)
    return sorted(set(div))


cnt = 0
for x in range(900_001, 10**10):
    d = divisors(x)
    if len(d) > 0:
        M = min(d) + max(d)
        if M % 100 == 46:
            print(x, M)
            cnt += 1
            if cnt == 5:
                break
'''


# № 17642 Основная волна 19.06.24 (Уровень: Базовый)
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            div.append(j)
            div.append(x // j)
    return sorted(set(div))


cnt = 0
for x in range(800_001, 10**10):
    d = [j for j in divisors(x) if j % 10 == 9 and j != 9 and j != x]
    if len(d) > 0:
        print(x, min(d))
        cnt += 1
        if cnt == 5:
            break
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 25]
# КЕГЭ = []
# на следующем уроке: 24, 26, 27
