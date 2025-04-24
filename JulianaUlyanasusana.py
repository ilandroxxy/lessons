# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((not x) and y and z and (not w)) or ((not x) and y and (not z) and w) or (x and y and z and (not w))
                if F == 1:
                    print(x, y, z, w)
'''


# 5
'''
def convert(n, b):
    r = ''
    while n > 0:
        r += str(n % b)
        n //= b
    return r[::-1]

R = []
for n in range(1, 10000):
    s = convert(n, 7)
    if s.count('3') % 2 == 0:
        s = '3' + s + s[0]
    else:
        s = '6' + s + s[-1]
    r = int(s, 7)
    if r < 16777:
        R.append(r)
print(max(R))
'''

# 8
'''
s = '0123456789ABC'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    num = a + b + c + d + e
                    if a != '0':
                        if len(num) == len(set(num)):
                            for x in s[::2]:
                                num = num.replace(x, '2')
                            for x in s[1::2]:
                                num = num.replace(x, '1')
                            if '22' not in num and '11' not in num:
                                cnt += 1
print(cnt)  # 10440
'''


# 9
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    flag = 0
    copied = [x for x in M if M.count(x) == 3]
    uncopied = [x for x in M if M.count(x) == 1]
    if len(copied) == 3 and len(uncopied) == 3:
        flag += 1
    if M.count(min(M)) > 1:
        flag += 1
    if flag >= 1:
        cnt += 1
print(cnt)
'''

# 12
'''
mini = 10**9
for n in range(1000):
    s = '7' * n + '8' * n + '9' * n

    while '78' in s or '98' in s or '999' in s:
        if '78' in s:
            s = s.replace('78', '8', 1)
        if '98' in s:
            s = s.replace('98', '7', 1)
        if '999' in s:
            s = s.replace('999', '9', 1)
    if sum(map(int, s)) == 801:
        mini = min(mini, n*3)
        print(mini)
'''


# 13
'''
from ipaddress import *
for A in range(255+1):
    net = ip_network(f'135.{A}.170.5/255.255.0.0', 0)
    if all(f'{ip:b}'[:16].count('1') > 10 for ip in net):
        print(A)
        break
'''


# 14
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
print(alphabet[20])  # K
def convert(n, b):
    r = ''
    while n > 0:
        r += alphabet[n % b]
        n //= b
    return r[::-1]

n = 9*57**2024 + 14 * 13**3059 - 87 * 67**1111 + 2027
s = convert(n, 36)
print(len([x for x in s if x > 'K']))
'''


# 15
'''
def F(x, a1, a2):
    P = 3 <= x <= 83
    Q = 62 <= x <= 131
    A = a1 <= x <= a2
    return (not Q) <= (((not A) and P) <= Q)

R = []
M = [x / 2 for x in range(0, 140 * 2)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(min(R))  # 58.75 -> 59
'''


# 16
'''
import sys
sys.setrecursionlimit(10000)

def F(n):
    if n < 52:
        return n
    if n >= 51:
        return 3 * F(n - 2) - n

print(F(15127) // F(15099))
'''
# 4782968


# 17
'''
M = [int(x) for x in open('0. files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 3]
B = [x for x in M if abs(x) % 7 == 0 and abs(x) % 10 == 7]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x in A) + (y in A) >= 1:
        if (x + y) > min(B):
            R.append(x**2 + y**2)
print(len(R), max(R))
'''
# 3174 9955651250


# 25
'''
from fnmatch import *
for x in range(25, 10**7, 25):
    if fnmatch(str(x), '89?45*75'):
        print(x, x // 25)
'''


# 23
'''
def F(a, b):
    if a > b or a == 0:
        return 0
    if a == b:
        return 1
    summa = F(a+3, b) + F(a+4, b)
    if a < 0:
        summa += F(abs(a), b)
    return summa


print(F(-21, -8) * F(-8, 35))
'''

'''
def F(a, s, n, c):
    if a + s >= 132:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a+2, s, n, c+'1'), F(a, s+2, n, c+'1'), F(a*2, s, n, c+'2'), F(a, s*2, n, c+'2'), F(a*3, s, n, c+'3'), F(a, s*3, n, c+'3')]
    return any(h) and c.count('3') == 1 if (n- 1) % 2 == 0 else all(h) and c.count('3') == 1

print([s for s in range(1, 101) if F(31, s, 2, '')])
# print([s for s in range(1, 101)])
# print([s for s in range(1, 101)])
'''
# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19-21, 23, 25]
# КЕГЭ = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Ульяна 5/8 -> 34 вторичных баллов +[1, 2, 4, 6, 12] -[5, 13, 14]

# Второй пробник 28.02.25:
# Ульяна 10/29 -> 51 вторичных баллов +[1-4, 6, 10, 13, 15, 16, 23] -[5, 8, 9, 12, 14, 17, 25]
