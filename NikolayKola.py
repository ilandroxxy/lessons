# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
R = []
for n in range(1, 10):
    s = f'{n:b}'  # s = bin(n)[2:]
    if s.count('1') % 2 == 0:
        s = '10' + s[2:] + '0'
    else:
        s = '11' + s[2:] + '1'
    r = int(s, 2)
    if r < 20:
        R.append(n)
print(max(R))
'''

# print(int('1000'))  # 1000
# print(int('1000', 2))  # 8

'''    
/ - вещественное деление, float() 
print(4 / 2)  # 2.0

// - целая часть от деления
print(3.99999 // 3)  # 1.0

% - остаток от деления 
print(7 % 2)  # 1
'''

'''
def convert(num, base):
    res = ''
    while num > 0:
        res = str(num % base) + res
        num //= base
    return res


R = []
for n in range(1, 1000):
    s = convert(n, 3)
    if n % 3 == 0:
        s = s + s[-2:]
    else:
        x = (n % 3) * 5
        s = s + convert(x, 3)
    r = int(s, 3)
    if r > 133:
        R.append(r)
print(min(R))
'''
# 141


'''
x = 5
x **= 5  # x = x + 5
print(x)
'''

'''
s = '7' * 108
while '33333' in s or '777' in s:
    if '33333' in s:
        s = s.replace('33333', '7', 1)
    else:
        s = s.replace('777', '3', 1)
print(s)'''
# 3337

'''
from ipaddress import *
net = ip_network('106.184.0.0/255.248.0.0', 0)
cnt = 0
for ip in net:
    s = f'{ip:b}'
    if s.count('1') % 2 != 0:
        cnt += 1
print(cnt)
'''

'''
def convert(num, base):
    res = ''
    while num > 0:
        res = str(num % base) + res
        num //= base
    return res


for x in range(0, 2030+1):
    n = 3**100 - x
    s = convert(n, 3)
    if s.count('0') == 2:
        print(x)
        break
'''

'''
print(min([A for A in range(1, 1000) if all(((x % 2 == 0) <= (x % 5 != 0)) or (x + A >= 70) for x in range(1, 10000))]))
'''
'''
import sys
sys.setrecursionlimit(10000)

def F(n):
    if n == 1:
        return 1
    if n > 1:
        return 2 * n * F(n-1)

print((F(2024) - 4*F(2023)) / F(2022))
'''

'''
def F(a, b):
    if a < b:
        return 0
    elif a == b:
        return 1
    else:
        return F(a-1, b) + F(a-2, b) + F(a//3, b)

print(F(16, 11) * F(11, 6))
'''
'''
def F(a, b):
    if a <= b:
        return a == b
    return F(a - 1, b) + F(a - 2, b) + F(a // 3, b)


print(F(16, 11) * F(11, 6))
'''


M = [int(x) for x in open('17.txt')]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i-1]
    if (x % 18) + (y % 18) == min(M):
        R.append(x + y)
print(len(R), max(R))

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2*, 3, 4, 6, 7, 9*, 10, 11, 18, 19-21]
# КЕГЭ  = []
# на следующем уроке:
