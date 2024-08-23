# region Домашка: ************************************************************


# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************

# Тип номер 16 из варианта: https://kompege.ru/variant?kim=25057665
'''
import sys
sys.setrecursionlimit(10000)

def F(n):
    if n == 1:
        return 1
    if n > 1:
        return (n - 1) * F(n - 1)


print((F(2024) // 7 - F(2023)) / F(2022))
'''


# Тип номер 14 из варианта: https://kompege.ru/variant?kim=25057665
'''
for x in range(2030+1):
    n = 6 ** 260 + 6 ** 160 + 6 ** 60 - x
    M = []
    while n > 0:
        M.append(n % 6)
        n //= 6
    M.reverse()
    if M.count(0) == 202:
        print(x)
'''
'''
for x in range(2030+1):
    n = 7 ** 91 + 7 ** 160 - x
    M = []
    while n > 0:
        M.append(n % 7)
        n //= 7
    M.reverse()
    if M.count(0) == 70:
        print(x)
'''

'''
from ipaddress import *
net = ip_network('115.192.0.0/255.192.0.0', 0)
cnt = 0
for ip in net:
    s = f'{ip:b}'
    if s.count('1') % 3 != 0:
        cnt += 1
print(cnt)
'''


'''
s = sorted("ЛАЙМ")
k = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    k += 1
                    if "М" not in slovo and "Л" not in slovo and "ЙЙ" not in slovo:
                        print(k)
'''


M = [int(x) for x in open('17.txt')]
D = [x for x in M if x > 0 and x % 41 == 0]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if x != y and abs(x - y) % min(D) == 0:
        R.append(x + y)
print(len(R), max(R))

# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 7, 8, 9-, 11, 12, 14, 15, 16, 17-, 18, 19-21, 22, 23, 25.1]
# КЕГЭ = [12]
# на следующем уроке:
