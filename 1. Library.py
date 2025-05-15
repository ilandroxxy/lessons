
# region 1 номер

# endregion 1 номер
#
#
# region 2 номер

# todo Хорошая задачка для 2 номера
# https://education.yandex.ru/ege/task/4820b374-36df-4864-912e-ac63edcbab34
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (not((((((w and x) == x) or 1) <= z) or (not x)) and y))
                if F == 0:
                    print(x, y, z, w)
'''


# endregion 2 номер
#
#
# region 3 номер

# № 20177 (Уровень: Базовый) (М. Попков)

# endregion 3 номер
#
#
# 3 номер № 20177 (Уровень: Базовый) (М. Попков)
#
#
# region 4 номер

# № 17912 Сергей Горбачев

# endregion 4 номер
#
#
# region 5 номер

# № 18287 (Уровень: Базовый)
# todo Номер 5: Интересная задача с ловушкой под списки и минимальный r
'''
sp = []
for n in range(3, 10000):
    bn = bin(n)[2:]
    if len(bn) % 2 == 0:
        bn = bn + '1'
    else:
        bn = '1' + bn + '0'
    r = int(bn, 2)
    if r > 666:
        print(r)
        sp.append(r)
print(min(sp))
'''

# endregion 5 номер
#
#
# region 6 номер

# endregion 6 номер
#
#
# region 7 номер

# endregion 7 номер
#
#
# region 8 номер

# endregion 8 номер
#
#
# region 9 номер

# https://education.yandex.ru/ege/task/0cee3383-2699-4e0d-a2f1-5f50a85ad086
'''
cnt = 0
from itertools import permutations
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    M = sorted(M)
    if M[-1] < (M[0] + M[1] + M[2]):
        if any(p[0] + p[1] == p[2] + p[3] for p in permutations(M)):
            cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/task/342217d2-3e89-4933-a422-940d9668bfa3
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

# endregion 9 номер
#
#
# region 10 номер

# endregion 10 номер
#
#
# region 11 номер

# endregion 11 номер
#
#
# region 12 номер

# endregion 12 номер
#
#
# region 13 номер

# endregion 13 номер
#
#
# region 14 номер

# endregion 14 номер
#
#
# region 15 номер

# № 12469 (Уровень: Базовый)
# todo Номер 15: Интересная задача с отрезками
'''
def F(x, a1, a2):
    D = 7 <= x <= 68  # x ∈ D
    C = 29 <= x <= 100
    A = a1 <= x <= a2
    return (D) <= (((not C) and (not A)) <= (not D))


R = []
M = [x / 10 for x in range(5 * 10, 110 * 10)]
print(M)
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)

print(min(R))  # 21.8 -> 21.75 -> 21.9 -> 22
'''


# endregion 15 номер
#
#
# region 16 номер

# endregion 16 номер
#
#
# region 17 номер

# endregion 17 номер
#
#
# region 18 номер

# endregion 18 номер
#
#
# region 19-21 номер

# endregion 19-21 номер
#
#
# region 22 номер

# endregion 22 номер
#
#
# region 23 номер

# endregion 23 номер
#
#
# region 24 номер

# todo просто интересная задача 24 № 7012 (Уровень: Средний)
'''
f = open('0. files/24.txt').readlines()
cnt = 0
for s in f:
    for x in 'UIOPASDFGHJKLZXCVBNM0123456789':
        s = s.replace(x, '')
    flag = ''
    bflag = 'QWERTY'
    for i in range(len(s)):
        if flag == 'QWERTY':
            cnt += 1
            break
        if s[i] == bflag[0]:
            flag += s[i]
            bflag = bflag[1:]

print(cnt)
'''


# todo интересная задача 24 номера № 14512 (Уровень: Средний)
'''
s = open('0. files/24.txt').readline()
s = s.replace('1', '1 1').replace('8', '8 8')
maxi = 0
for x in s.split():
    if x.count('1') == 1:
        if x.count('B') == x.count('C'):
            maxi = max(maxi, len(x))
print(maxi)
# print(max([len(x) for x in s.split() if x.count('1') == 1 and x.count('B') == x.count('C')]))
'''


# region todo Тут будем хранить интересные 24 номера на import re

# № 20813 Апробация 05.03.25 (Уровень: Сложный)
'''
from re import *
s = open('0. files/24.txt').readline()
num = r'([789][0789]*|[0])'
reg = rf'{num}([-*]{num})*'

M = [x.group() for x in finditer(reg, s)]
maxi = 0
for x in M:
    maxi = max(maxi, len(x))
print(maxi)

print(max([len(x.group()) for x in finditer(reg, s)]))
'''


# № 19967 (Уровень: Сложный)
'''
from re import *
s = open('24.txt').readline()
num1 = r'([AFD][1-9][0-9]*|0)'
num2 = r'([1-9][0-9]*|0)'
reg = rf'AF{num1}([+*]{num2})*'

m = [x.group() for x in finditer(reg, s)]
maxi = 0
for x in m:
    maxi = max(len(x), maxi)
print(maxi)
'''


# № 18619 (Уровень: Сложный)
'''
from re import *
s = open('24.txt').readline()
for i in 'ACD':
    s = s.replace(i, ' ')
num1 = r'[B]([1-6][1-6]*)'
num2 = r'([1-6][1-6]*)'
reg = rf'{num1}([-*]{num2})*'

m = [x.group() for x in finditer(reg, s)]
maxi = 0
for x in m:
    maxi = max(len(x), maxi)
print(maxi)
'''


# № 18285 (Уровень: Сложный)
'''
from re import *
s = open('24.txt').readline()
num = r'([1-9][0-9]*)'
reg = rf'{num}([+*]{num})*'

m = [x.group() for x in finditer(reg, s)]
maxi = 0
for x in m:
    x = x.replace('+', ' ').replace('*', ' ')
    maxi = max(maxi, len(x.split()))
print(maxi)
'''


# № 18147 (Уровень: Средний)
'''
from re import *
s = open('24.txt').readline()
num = r'([789]+)'
reg = rf'{num}([+]{num})+'

m = [x.group() for x in finditer(reg, s)]
maxi = 0
for x in m:
    if eval(x) >= maxi:
        maxi = max(eval(x), maxi)
        print(x, eval(x))
'''


# № 19968 (Уровень: Сложный)
'''
from re import *

s = open('files/24_19968.txt').readline()
num = r'([12345][012345]*)'
reg = rf'{num}([+*]{num})*'
M = [x.group() for x in finditer(reg, s)]

maxi = 0
for x in M:
    maxi = max(len(x), maxi)
print(maxi)
'''


# № 19970 (Уровень: Сложный)
'''
from re import *

s = open('files/24_19970.txt').readline()
num = rf'([1-9][0-9]*[05]|0|5)'
reg = rf'{num}([+*]{num})*'
M = [x.group() for x in finditer(reg, s)]

maxi = 0
for x in M:
    maxi = max(len(x), maxi)
    print(x)
print(maxi)
'''

# endregion

# endregion 24 номер
#
#
# region 25 номер

# endregion 25 номер
#
#
# region 26 номер

# endregion 26 номер
#
#
# region 27 номер

# endregion 27 номер








# region Все, что нужно "заучить" для экзамена

# n - число, которое переводим
# b - система счисления в которую переводим
'''
from string import digits, ascii_uppercase
alphabet = digits + ascii_uppercase

alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def G(n, b):
    r = ''
    while n > 0:
        r += alphabet[n % b]
        n //= b
    return r[::-1]

n = 8
b = 2
r = G(n, b) 
print(r) # 1000
print(int(r, b))  # 8
'''

# endregion