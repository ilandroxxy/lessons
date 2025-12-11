# region Домашка: ******************************************************************


# Номер 14
'''
alp = sorted('1234567890QWERTYUIOPASDFGHJKLZXCVBNM')
R = []
for x in alp[:23]:
    A = int(f'7{x}38596', 23)
    B = int(f'14{x}36', 23)
    C = int(f'61{x}7', 23)
    if (A + B + C) % 22 == 0:
        R.append((A + B + C) // 22)
print(min(R))
'''


# Номер 5
'''
def convert(n, b):
    r = ''
    while n > 0:
        r = r + str(n % b)
        n //= b
    return r[::-1]


RES = []
for n in range(1, 1000):
    n3 = convert(n, 3)
    if n % 3 == 0:  
        n3 = '1' + n3 + '02'
    else:
        n3 += convert((n % 3) * 4, 3)
    r = int(n3, 3)
    if r < 199:
        RES.append(n)
print(max(RES))
'''

# Номер 8
'''
cnt = 0
from itertools import *
for p in permutations('0123456789ABCDEF', r=3):
    num = ''.join(p)
    if num[0] != '0':
        chet = '02468ACE'
        nechet = '13579BDF'
        a, b, c = num
        if (a in chet and b in nechet and c in chet) or (a in nechet and b in chet and c in nechet):
            cnt += 1
print(cnt)


cnt = 0
s = '0123456789ABCDEF'
for a in s:
    for b in s:
        for c in s:
            num = a + b + c
            if num[0] != '0':
                # if a != b != c != c:
                if len(num) == len(set(num)):
                    for x in '02468ACE':
                        num = num.replace(x, '2')
                    for x in '13579BDF':
                        num = num.replace(x, '1')
                    if '11' not in num and '22' not in num:
                        cnt += 1
print(cnt)
'''


# Номер 13
'''
from ipaddress import*
for mask in range(32 + 1):
    net = ip_network(f'213.168.83.190/{mask}', 0)
    if '213.168.64.0' in str(net):
        print(net, mask, 32 - mask, net.netmask)
        # адрес сети, кол-во 1, кол-во 0, маска десятичная 
'''

'''
def f(x, y, A):
    return (x + 2 * y > A) or (y < x) or (x < 30)

RES = []
for A in range(1, 10000):
    if all(f(x, y, A) for x in range(1, 100) for y in range(1, 100)):
        RES.append(A)
print(max(RES))
'''


# n = 0
# n = 1: Петя первый ход
# n = 2: Ваня первый ход
# n = 3: Петя второй ход
# n = 4: Ваня второй ход
'''
def F(s, n):
    if s >= 111:
        return n % 2 == 0
    if n == 0:
        return 0
    h = (F(s+1, n-1), F(s+3, n-1), F(s*4, n-1))
    return any(h) if (n-1) % 2 == 0 else all(h)

print([s for s in range(1, 110+1) if F(s, n=2)])
print([s for s in range(1, 110+1) if F(s, n=3) and not F(s, n=1)])
print([s for s in range(1, 110+1) if F(s, n=4) and not F(s, n=2)])
'''

# Номер 27
'''
from math import dist

clustersA = [[],[]]
clustersB = [[], [], []]
for s in open('0. files/27A.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
    if y < -6:
        clustersA[0].append([x, y])
    else:
        clustersA[1].append([x, y])

for s in open('0. files/27B.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
    if 0 < y < 6:
        clustersB[0].append([x, y])
    if y > 6 and x < -4:
        clustersB[1].append([x, y])
    if y > 6 and x > -4:
        clustersB[2].append([x, y])

def center(cl):
    R = []
    for p in cl:
        summa = 0
        for g in cl:
            summa += dist(p, g)
        R.append([summa, p])
    return min(R)[1]

print(center(clustersA[0]))  # [5.178596535006889, -8.303106988723517]
print(center(clustersA[1]))  # [-2.772853872531587, -0.10134157243340036]

PxA = (5.178596535006889 + -2.772853872531587) / 2 * 10000
PyA = (-8.303106988723517 + -0.10134157243340036) / 2 * 10000
print(int(abs(PxA)), int(abs(PyA)))
'''


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************



# № 24886 (Уровень: Базовый)
# На вход алгоритма подаётся натуральное число N.
# Алгоритм строит по нему новое число R следующим образом.
# 1 Строится двоичная запись числа N.
# 2 Далее эта запись обрабатывается по следующему правилу:
# а) если число N делится на 5, то к этой записи дописывается
# справа две единицы;
# б) если число N на 5 не делится, то результат целочисленного
# деления N на 5 переводится в двоичную систему счисления и дописывается в конец числа.
# Полученная таким образом запись является двоичной записью искомого числа R.

# Укажите минимальное чётное число N, для которого с помощью
# описанного алгоритма получается число, превышающее 896 В ответе запишите это число в десятичной системе счисления.
'''
def convert(n, b):
    r = ''
    while n > 0:
        r = str(n % b) + r
        n //= b
    return r

for n in range(1, 10000):
    # n2 = bin(n)[2:]
    # n2 = f'{n:b}'
    n2 = convert(n, 2)
    if n % 5 == 0:
        n2 = n2 + '11'
    else:
        n2 = n2 + f'{(n // 5):b}'
    r = int(n2, 2)
    if n % 2 == 0:
        if r > 896:
            print(n)
            break
'''

# № 23364 Резервный день 19.06.25 (Уровень: Базовый)
'''
def convert(n, b):
    r = ''
    while n > 0:
        r = str(n % b) + r
        n //= b
    return r

RES = []
for n in range(1, 10000):
    n3 = convert(n, 3)
    if n % 3 == 0:
        n3 = '1' + n3 + '02'
    else:
        x = (n % 3) * 4
        n3 = n3 + convert(x, 3)
    r = int(n3, 3)
    if r < 100:
        RES.append(n)
print(max(RES))
'''


# № 22457 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r

RES = []
for n in range(1, 10000):
    n7 = convert(n, 7)
    summa = sum(map(int, n7))
    if summa % 2 == 0:
        n7 += '555'
    else:
        n7 = '33' + n7 + '6'
    r = int(n7, 7)
    if r < 12717:
        RES.append(n)
print(max(RES))
'''


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 25, 27]
# КЕГЭ = []
# на следующем уроке: 10, (26, 24)
