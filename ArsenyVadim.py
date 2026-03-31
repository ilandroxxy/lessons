# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


'''
# 2
print('x y w z F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((not(z)) and y and x and (not(w))) or ((not(z)) and y and (not(x)) and (not(w))) or (z and y and x and (not(w)))
                if F == 1:
                    print(x, y, w, z, F)
'''
'''
# 5
# 15 = 127
for n in range(31, 32):
    b = f'{n:b}'
    if n % 3 == 0:
        b = b + b[-3:]
    else:
        b = b + bin((n%3) * 3)[2:]
    r = int(b, 2)
    if 125 <= r <= 135:
        print(r)
'''

'''
# 13
cnt = 0
from ipaddress import *
net = ip_network('172.16.96.0/255.255.224.0', 0)
for ip in net:
    ip = str(ip)
    ip = ip.split('.')
    print(ip)
    k = 0
    for i in ip:
        b = bin(int(i))[2:]
        k += b.count('1')
    if k % 2 == 0:
        cnt += 1
print(cnt)
'''

'''
# 14
def F(n,k):
    b = ''
    while n > 0:
        b += str(n % k)
        n //= k
    return b[::-1]

S = []
for x in range(1, 2031):
    a = 6 ** 2030 + 6 ** 100 - x
    a = F(a, 6)
    S.append(a.count('0'))
print(min(S))
'''
'''
# 15

def F(x, A):
    return (x % 25 == 0) <= ((not(x % A == 0)) <= (not(x % 60 == 0)))
for A in range(1, 100000):
    if all(F(x, A) for x in range(1000)):
        print(A)
'''
'''
# 16
import sys
sys.setrecursionlimit(10**8)
def F(n):
    if n == 1:
        return 1
    return n * F(n - 1)

print((F(2024) - 5 * F(2023)) / F(2022))

'''
'''
# 19-21
def F(s, a, n):
    if s + a >= 211:
        return n % 2 == 0
    if n == 0:
        return 0
    H = [F(s + 1, a, n- 1), F(s * 2, a, n- 1), F(s, a + 1, n- 1), F(s, a * 2, n- 1)]
    return any(H) if (n- 1) % 2 == 0 else all(H)
print(19, [s for s in range(1, 193) if F(s, 17, 2)])
print(20, [s for s in range(1, 193) if F(s, 17, 3) and not F(s, 17, 1)])
print(21, [s for s in range(1, 193) if F(s, 17, 4) and not F(s, 17, 2)])
'''
'''
# 23
def F(a, b):
    if a == b:
        return 1
    if a < b:
        return 0
    return F(a- 1, b) + F(a // 2, b)
print(F(40, 17) * F(17, 6))
'''
'''
# 25
from re import *
for x in range(171, 10**8 + 1, 171):
    x = str(x)
    if x[0] == '1' and x[-1] == '6' and x[-2] == '5':
        if x[-5] == '3' and x[-6] == '2':
            print(int(x), int(x) // 171)
'''



'''
# 27
from math import *

clustersA = [[], []]
clustersB = [[], [], []]

def center(cl):
    S = []
    for p in cl:
        summa = 0
        for g in cl:
            summa += dist(p, g)
        S.append([summa, p])
    return min(S)[1]

# A) y = 15

for s in open('27A.csv'):
    x, y = [float(i) for i in s.split(';')]
    if y > 15:
        clustersA[0].append([x, y])
    else:
        clustersA[1].append([x, y])

# B) 1) y > 20 2) y < 20 x < 24 3) y < 20 x > 24

for s in open('27B.csv'):
    x, y = [float(i) for i in s.split(';')]
    if y > 20:
        clustersB[0].append([x, y])
    elif y < 20 and x > 24:
        clustersB[1].append([x, y])
    elif y < 20 and x < 24:
        clustersB[2].append([x, y])
        '''
'''
# a1 = 301
# a2 = 31.927251878500773
print(center(clustersA[0])) # [8.856, 20.903738]
print(center(clustersA[1])) # [6.016644, 8.404493]
print(dist([8.856, 20.903738], [-1.0, 1.3]) + dist([6.016644, 8.404493], [-1.0, 1.3]) )
'''
'''
cnt = 0
print(center(clustersB[0])) # [17.867681, 28.209279] 902
print(center(clustersB[1])) # [27.887459, 15.531916]
print(center(clustersB[2]))  # [20.396937, 17.39094] 200
for p in clustersB[2]:
    if dist([20.396937, 17.39094], p) <= 1.6:
         cnt += 1
print(cnt) # b1= 182
'''
'''
S = []
for p in clustersB[0]:
    S.append(dist([17.867681, 28.209279], p))
print(max(S)) # b2 = 2.6825911735801244
'''
'''
# 17
M = []
for s in open('17.txt'):
    M.append(int(s))

# K = max([x for x in M if 1000 <= abs(x) <= 9999 and x % 100 == 43]) 9943
S = []

for i in range(len(M) - 1):
    if 1000 <= abs(M[i]) <= 9999 or 1000 <= abs(M[i + 1]) <= 9999:
        if (M[i] + M[i + 1]) ** 2 < 9943 ** 2:
            S.append(M[i] + M[i + 1])
print(len(S), max(S))
'''




# Номер 8 Апробация вариант 1
'''
n = 0
from itertools import *
for x in product(sorted('ЦИТРУС'), repeat=5):
    word = ''.join(x)
    n += 1
    if word.count('И') == 2 and 'ЦЦ' not in word:
        print(n)
'''

# Номер 9 Апробация вариант 1
'''
n = 0
for s in open('files/9.csv'):
    M = sorted([int(x) for x in s.split(',')])
    n += 1
    copy1 = [x for x in M if M.count(x) == 1]
    if len(copy1) == 5:
        if M[-1] - M[0] == M[1] + M[2] + M[3]:
            print(n)
            break
'''


# Номер 7 Апробация вариант 1
'''
ql = 192 * 960
ves = ((90 * 1024 * 8) / 85) * 100
print(ves / ql)  # 4.7058 -> 4  2 ** 4 = 16
'''


# Номер 11 Апробация вариант 1
'''
alp = 10 + 26 + 8164
# print(alp, 2**14)
i = 14

n = 835
ves = 156 * 1024
print(ves / n) # 191.31017964071856
byte = 192
print(192 * 8)
bit = 1536


print(bit / i)
# 109.7142 -> 109
'''


# Номер 17 Апробация вариант 1
'''
M = []
for s in open('files/17.txt'):
    M.append(int(s))

# K = max([x for x in M if 1000 <= abs(x) <= 9999 and x % 100 == 43]) 9943
S = []

for i in range(len(M) - 1):
    if 1000 <= abs(M[i]) <= 9999 or 1000 <= abs(M[i + 1]) <= 9999:
        if (M[i] + M[i + 1]) ** 2 < 9943 ** 2:
            S.append((M[i] + M[i + 1]) ** 2)
print(len(S), max(S))

M = [int(x) for x in open('files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 4]
B = [x for x in A if abs(x) % 100 == 43]
S = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x in A) + (y in A) >= 1:
        if (x + y) ** 2 < max(B) ** 2:
            S.append((x + y) ** 2)
print(len(S), max(S))
'''



# Номер 24 Апробация вариант 1
'''
s = open('files/24.txt').readline()
s = s.split('Z')
R= []
for i in range(len(s) - 268):
    x = 'Y' + 'Y'.join(s[i:i+269]) + 'Y'
    R.append(len(x))
print(min(R))
'''


# 1. 45 +
# 2. wzxy +
# 3. 1041 -
# 4. 24 -
# 5. 31 +
# 7. 8 -
# 8. 7741 -
# 9. 994 -
# 10. 51 +
# 11. 33 -
# 12. 512 -
# 13. 4096 +
# 14. 1930 +
# 15. 300 +
# 16. 4084437 +
# 17. 1218 9942 -
# 18. 2661 336 +
# 19. 49 +
# 20. 88 96 +
# 21. 87 +
# 22. 10 -
# 23. 56 +
# 24. 1063 -
# 25. 1237356 7236 +
# 10231956 59836
# 12232656 71536
# 14233356 83236
# 16234056 94936
# 18234756 106636
# 27. 301 319272 ++
# 182 26825
# 67 баллов


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.2, 25, 27]
# КЕГЭ = [11]
# на следующем уроке: 7, 24 номера через замену, 24 номера через замену + split()


# region 📖 Пробник (Вариант 2)

# Студент #Арсений
# Дата: #Пятница #27Февраля2026
# ✅ Верно: 1, 2, 4, 5, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 23
# ⛔️ Неверно: 3, 9, 17, 22, 27
# ❔ Без ответа: 6, 24, 25, 26
# Итог: 19/29 первичных балла ~ 75 вторичных

# endregion 📖 Пробник (Вариант 2)

