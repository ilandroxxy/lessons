# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# 19-21
'''
from math import ceil, floor
def F(s, n):
    if s <= 505:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s - 3, n - 1), F(floor(s / 5), n - 1)]
    return any(h) if (n-1) % 2 == 0 else all(h)

print(max([s for s in range(505, 20000) if F(s, n = 2)]))
print([s for s in range(505, 10000) if not F(s, n=1) and F(s, n=3)])
print([s for s in range(505, 10000) if F(s, n=4) and not F(s, n = 2)])
'''


# 9
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied1 = [x for x in M if M.count(x) == 1]
    # if (M.count(min(M)) == 2 or M.count(min(M)) == 3) and (len(copied1) == 6 or len(copied1) == 5):
    if 2 <= M.count(min(M)) <= 3 and 5 <= len(copied1) <= 6:
        if min(copied1) ** 2 + max(copied1) ** 2 <= (sum(copied1) - min(copied1) - max(copied1)) ** 2:
            cnt += 1
print(cnt)
'''


# 17
'''
M = [int(x) for x in open('files/17.txt')]
A = [x for x in M if x < 0 and abs(x) % 6 == 0 and len(str(abs(x))) == 3]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x < 0) + (y < 0) == 1:
        if (x + y) > max(A):
            R.append(x ** 2 + y ** 2)
print(len(R), max(R))
'''


#
'''
def divisors(x):
    d = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            d.append(j)
            d.append(x // j)
    return sorted(set(d))


print([x for x in range(2, 100) if len(divisors(x)) == 2])
'''

# 25
'''
def divisors(x):
    d = []
    for j in range(2, int(x**0.5)+1):  # не считая самого числа.
        if x % j == 0:
            d.append(j)
            d.append(x // j)
    return sorted(set(d))

cnt = 0
for x in range(1_325_000-1, -1, -1):
    d = [j for j in divisors(x) if len(divisors(j)) == 0]
    if len(d) > 0:
        S = sum(d)
        if S != 0 and S <= 30000 and S % 5 == 0:
            print(x)
            cnt += 1
            if cnt == 5:
                break
'''

# 11
'''
sym = 102

byte = 53 * 2**20 / 282_952
print(byte)  # 196.409 -> 196 (отведено не более 53 Мбайт)
bit = 196 * 8

i = bit / sym
print(i)  # 15.372 -> 15 (отведено не более 53 Мбайт)

print(2 ** 15)
print(2 ** 14 + 1)
'''


# 7
'''
# V = a * b * c * t

a = 4  # формате квадро
b = 33000  # с частотой дискретизации 33 000 Гц
c = 37  # и разрешением 37 бит
t = 41 * 60 + 33

V = a * b * c * t

U = 363_956_352  # бит/с
T = 307
V_all = U * T

print((V_all - V) / 30)
print(((V_all - V) / 30) / 2**13)
'''

# 23
'''
def F(a, b):
    if a >= b:
        return a == b
    return F(a + 1, b) + F(a * 2, b) + F(a * 3, b)

print(F(6, 14) * F(14, 18) * F(18, 48))  # и через 14 и через 18 (пересечение)
print(F(6, 14) * F(14, 48))  # разность - только через 14
print(F(6, 18) * F(18, 48))  # разность - только через 18

print(45 + 48 - 24)  # 69
'''


# # endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 25, 27]
# КЕГЭ = []
# на следующем уроке: 12, 9, 25, 22, 27
