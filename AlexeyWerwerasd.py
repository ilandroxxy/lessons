# region Домашка: ************************************************************


# endregion Домашка: *********************************************************
# #
# #
# region Урок: ************************************************************


# Задача 5
'''
def convert(n, b):
    r = ''
    while n > 0:
        r += str(n % b)
        n //= b
    return r[::-1]


R = []
for n in range(1, 1000):
    s = convert(n, 3)
    if n % 3 == 0:
        s = s + s[-2:]
    else:
        summa = sum(map(int, s))
        s = s + convert(summa, 3)
    r = int(s, 3)
    if r > 220 and r % 2 == 0:
        R.append(r)
print(min(R))
'''


# Задача 8
'''
s = sorted('ЯНВАРЬ')
n = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    n += 1
                    if a != 'Я' and slovo.count('Ь') <= 1:
                        if 'ЯЯ' not in slovo:
                            print(n)
'''


'''
n = 0
for s in open('files/9.txt'):
    M = [int(x) for x in s.split()]
    n += 1
    copied = [x for x in M if M.count(x) == 3]
    not_copied = [x for x in M if M.count(x) == 1]
    if len(copied) == 6 and len(not_copied) == 1:
        if sum(copied) / 6 < sum(not_copied) / 1:
            print(n)
'''


'''
from ipaddress import *
net = ip_network('218.194.82.148/255.255.255.192', 0)
for ip in net:
    print(ip)
'''

'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:25]:
    A = int(f'11353{x}12', 25)
    B = int(f'135{x}21', 25)
    if (A + B) % 24 == 0:
        print((A + B) // 24)
'''
# 1, 2, 3, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, 22, 23, 25

'''
import sys
sys.setrecursionlimit(10000)

def F(n):
    if n < 5:
        return n
    if n >= 5:
        return 2*n * F(n-4)


print((F(13766) - 9 * F(13762)) / F(13758))
'''

'''
M = [int(x) for x in open('files/17.txt')]
D = [x for x in M if len(str(abs(x))) == 5 and str(x)[-2:] == '43']
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if x in D or y in D or z in D:
        if (x**2 + y**2 + z**2) <= max(D)**2:
            R.append(x**2 + y**2 + z**2)
print(len(R), min(R))
'''

'''
def F(a, b):
    if a < b or a == 24:
        return 0
    if a == b:
        return 1
    else:
        return F(a-1, b) + F(a-6, b) + F(a//2, b)
    
    
print(F(34, 29) * F(29, 19) * F(19, 6))
'''

# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# ФИПИ = [1, 2, 3, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, 22, 23, 25]
# КЕГЭ = []
# на следующем уроке: 18, 19-21, 26
