# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Задача 2
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = w and (y == (z <= (x or y)))
                if F == 1:
                    print(x, y, z, w)
'''
# Ответ: wxyz


# Задача 5
'''
M = []
for n in range(26, 1000):
    s = bin(n)[2:]  # s = f'{n:b}'
    print(s)
    if n % 2 != 0:
        s = s[:-2] + '10'
    else:
        s = '10' + s[2:] + '1'
    r = int(s, 2)
    M.append(r)
print(min(M))
'''
# Ответ: 26


# Задача 8
'''
s = sorted('ПРОБНИК')
n = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        word = a + b + c + d + e + f
                        n += 1
                        if word.count('О') == 3:  # с тремя буквами О
                            if len(set(word)) == 4:  # остальные буквы при этом не повторяются
                                print(n)
'''

# Задача 12
'''
for n in range(4, 10000):
    s = '0' + '2' * n

    while '002' in s or '22' in s:
        if '002' in s:
            s = s.replace('002', '44', 1)
        else:
            s = s.replace('22', '0', 1)
        if '222' in s:
            s = s.replace('222', '2', 1)
    summa = sum(map(int, s))
    if summa == 42:
        print(n)
# Ответ: 56
'''


# Задача 13
'''
from ipaddress import *
net = ip_network('10.112.0.0/255.248.0.0', 0)
cnt = 0
for ip in net:
    s = f'{ip:b}'
    if s.count('1') % 3 == 0:
        cnt += 1
print(cnt)
'''


# Задача 14
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    r = ''
    while n > 0:
        r += alphabet[n % b]
        n //= b
    return r[::-1]


for x in range(2042):
    n = 25**61 + 5**178 - x
    s = convert(n, 5)
    if s.count('0') == 60:
        print(x)
'''

# Задача 25
# https://education.yandex.ru/ege/task/d02f4351-acc7-4b66-9ca1-83d0d1887db7
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            div.append(j)
            div.append(x // j)
    return sorted(set(div))


k = 0
for x in range(700_000+1, 10**10):
    d = [j for j in divisors(x) if j % 10 == 7 and j != 7]
    if len(d) > 0:
        print(x, min(d))
        k += 1
        if k == 5:
            break
'''


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 13, 14, 25]
# КЕГЭ  = []
# на следующем уроке:
