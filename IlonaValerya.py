# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# 12 задача: 21707
'''
for n in range(4, 10000):
    s = '4' + '2'*n
    summ = 0
    while '42' in s or '8222' in s or '2222' in s:
        if '42' in s:
            s = s.replace('42','2',1)
        if '8222' in s:
            s = s.replace('8222', '24', 1)
        if '2222' in s:
            s = s.replace('2222', '8', 1)
    summ = sum(map(int, s))
    if summ == 110:
        print(n)
        break
'''


# 15 задача: 21710
'''
def F(x,a1,a2):
    B = 36 <= x <= 75
    C = 60 <= x <= 110
    A = a1 <= x <= a2
    return (not A) <= (B == C)

R = []
M = [x/4 for x in range(20*4,120*4)]
for a1 in M:
    for a2 in M:
        if all(F(x,a1,a2)for x in M):
            R.append(a2 - a1)
print(min(R))
'''


# 17 задача: 21712
'''
M = [int(x) for x in open('0. files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 4 and abs(x) % 10 == 6]
B = [x for x in A if x > 0]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x in A) + (y in A) + (z in A) == 1:
        if (x + y + z) <= min(B):
            R.append(x + y + z)
print(len(R), max(R))
'''


# 25 задача: 21718
'''
from fnmatch import *
for x in range(7993, 10**10, 7993):
    if fnmatch(str(x), '4*4736*1'):
        print(x, x // 7993)


from re import *
for x in range(7993, 10**10, 7993):
    if fullmatch('4[0-9]*4736[0-9]*1', str(x)):
        print(x, x // 7993)
'''


# № 18591 (Уровень: Средний)
'''
from re import *
for x in range(1984, 10**10, 1984):
    if fullmatch('[02468]9[0-9]23[0-9][0-9]*23[13579][02468]', str(x)):
        print(x, x // 1984)
'''

from re import *
for x in range(153,10**8,153):
    if fullmatch('1[13579]2[24680]3[13579]45',str(x)):
        print(x,x//153)

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 25]
# КЕГЭ = []
# на следующем уроке: 1 и 4 номера
