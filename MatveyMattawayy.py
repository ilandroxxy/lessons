# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
R = []
for x in alphabet[:13]:
    a = int(f'537{x}623', 13) - int(f'6{x}35{x}2', 13)
    if a % 3 == 0:
        R.append(int(x, 13))
print(max(R))
'''

'''
for p in range(6, 36+1):
    a = 7**500 - int('53', p)
    if a % 6 == 0:
        print(p)
        break
'''

'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for p in range(7, 36+1):
    for x in alphabet[:p]:
        for y in alphabet[:p]:
            for z in alphabet[:p]:
                if int(f'{y}4{y}', p) + int(f'{y}65', p) == int(f'{x}{z}33', p):
                    print(int(x+y+z, p))
'''

'''
import sys
sys.setrecursionlimit(10000)

def F(n):
    if n == 1:
        return 1
    if n > 1:
        return 2 * n * F(n-1)

print((F(2024) - 4 * F(2023)) / F(2022))
'''
# Ответ: 16362024


'''
import sys
sys.setrecursionlimit(10000)

def F(n):
    if n == 1:
        return 1
    if n > 1:
        return 2 * n * F(n-1)

print((F(2024) // 16 - F(2023)) / F(2022))
'''
#      print((F(2024) / 16 - F(2023)) / F(2022))
#             ~~~~~~~~^~~~
# OverflowError: integer division result too large for a float


# № 16324 Открытый вариант 2024 (Уровень: Базовый)
'''
from ipaddress import *
net = ip_network('122.159.136.144/255.255.255.248', 0)
cnt = 0
for ip in net:
    b = f'{ip:b}'
    if b.count('1') % 4 !=0 :
        cnt += 1
print(cnt)
'''

# № 12922 PRO100 ЕГЭ 26.01.24 (Уровень: Базовый)
'''
from ipaddress import *
net = ip_network('136.36.240.16/255.255.255.248', 0)
cnt = 0
for ip in net:
    b = f'{ip:b}'
    if '101' not in b:
        cnt += 1
print(cnt)
'''

'''
R = []
for n in range(4, 10000):
    s = '5' + '7' * n
    while '57' in s or '877' in s or '777' in s:
        if '57' in s:
            s = s.replace('57', '7', 1)
        if '877' in s:
            s = s.replace('877', '75', 1)
        if '777' in s:
            s = s.replace('777', '8', 1)
    summa = sum(map(int, s))
    R.append(summa)
    print(max(R))
'''


# № 12930 PRO100 ЕГЭ 26.01.24 (Уровень: Базовый)
# У исполнителя есть три команды, которые обозначены латинскими буквами:
#     A. Прибавить 1
#     B. Умножить на 2
#     C. Возвести в квадрат
# Сколько существует программ, для которых при исходном числе 2
# результатом является число 40, при этом траектория вычислений
# содержит число 10, не содержит числа 11 и не содержит числа 12?

def F(a, b):
    if a > b or a == 11 or a == 12:
        return 0
    elif a == b:
        return 1
    else:
        return F(a+1, b) + F(a*2, b) + F(a**2, b)

print(F(2, 10) * F(10, 40))


def F(a, b):
    if a >= b or a == 11 or a == 12:
        return a == b
    return F(a+1, b) + F(a*2, b) + F(a**2, b)

print(F(2, 10) * F(10, 40))

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1+, 2+, 3, 4, 5*, 6, 7, 8*, 10+, 12*+, 14*, 16, 18, 19-21+]
# КЕГЭ  = [5, 12, 13, 14, 15, 16, 23]
# на следующем уроке: 9, 11, 25
