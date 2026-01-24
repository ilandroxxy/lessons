# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************



# Номер 8 Статград вариант 1
'''
cnt = 0
s = '0123456789ABCDE'
for a in s:
    for b in s:
        for c in s:
            for d in s:
                num = a + b + c + d
                if a != '0':
                    if num.count('8') == 1:
                        if all(num[i] != num[i+1] for i in range(len(num)-1)):
                            cnt += 1
print(cnt)


cnt = 0
from itertools import product
for p in product('0123456789ABCDE', repeat=4):
    num = ''.join(p)
    a , b, c, d = num
    if num[0] != '0':
        if num.count('8') == 1:
            if all(num[i] != num[i+1] for i in range(len(num)-1)):
                cnt += 1
print(cnt)
'''


# Номера 19-21 Статград вариант 1
'''
from math import ceil, floor
def F(s, n):
    if s <= 505:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s - 3, n - 1), F(floor(s/5), n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h) # else any(h)

print([s for s in range(506, 20000) if F(s, n=2)])
print([s for s in range(506, 10000) if F(s, n=3) and not F(s, n=1)])
print([s for s in range(506, 10000) if F(s, n=4) and not F(s, n=2)])


from math import ceil, floor
def F(s, n):
    if s <= 505:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s - 3, n - 1), F(floor(s / 5), n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h) # else any(h)

print([s for s in range(506, 20000) if F(s, n=2)])
print([s for s in range(506, 10000) if F(s, n=3) and not F(s, n=1)])
print([s for s in range(506, 10000) if F(s, n=4) and not F(s, n=2)])
'''


# Номер 13 Статград вариант 1
'''
from ipaddress import *
net = ip_network('167.66.136.176/255.254.0.0', 0)
for ip in net.hosts():
    print(ip)
    break
'''

# Номер 14 Статград вариант 1
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r

R = []
for x in range(1, 8410):
    n = 29**293 + 29**271 - x
    s = convert(n, 29)
    R.append(s.count('0'))
print(max(R))
'''


# Номер 23 Статград вариант 1
'''
def F(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    else:
        return F(a+1, b) + F(a*2, b) + F(a*3, b)

print(F(6, 14) * F(14, 18) * F(18, 48))  # 24
print(F(6, 14) * F(14, 48))  # 45
print(F(6, 18) * F(18, 48))  # 48

print((45 + 48) - 24)  # 69
'''


# Номер 9 Статград вариант 1
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied1 = [x for x in M if M.count(x) == 1]
    if 2 <= M.count(min(M)) <= 3 and 5 <= len(copied1) <= 6:
        if min(copied1) ** 2 + max(copied1) ** 2 <= (sum(copied1) - max(copied1) - min(copied1)) ** 2:
            cnt += 1
print(cnt)
'''

# Номер 17 Статград вариант 1

M = [int(x) for x in open('files/17.txt')]
A = [x for x in M if x < 0 and len(str(abs(x))) == 3 and abs(x) % 6 == 0]
R = []
for i in range(len(M) - 1):
    x, y = M[i], M[i+1]
    if (x < 0) + (y < 0) == 1:
        if (x + y) > max(A):
            R.append(x**2 + y**2)
print(len(R), max(R))


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25, 27]
# КЕГЭ = [19-21]
# на следующем уроке: 10, (26)