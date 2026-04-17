# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
print('x y z w F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = w <= ((z <= y) and x)
                if F == 0:
                    print(x, y, z, w, int(F))

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = w <= ((z <= y) and x)
                if F == 1:
                    print(x, y, z, w, int(F))
'''


# Номер 5
'''
RES = []
for n in range(1, 10000):
    n2 = f'{n:b}'
    if sum(map(int, n2)) % 2 == 0:
        n2 = '1' + n2[2:] + '0'
    else:
        n2 = '11' + n2[2:] + '1'
    r = int(n2, 2)
    if r < 744:
        RES.append([r, n])
print(max(RES))
'''

# Номер 8
'''
cnt = 0
from itertools import product
for p in product('0123456789ABCDEF', repeat=4):
    num = ''.join(p)
    if num[0] != '0':
        if num.count('D') == 1:
            for x in '13579BF':
                num = num.replace(x, '*')
            if '*D' not in num and 'D*' not in num:
                cnt += 1
                print(num)
print(cnt)
'''


# Номер 9
'''
n = 0
summa = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    n += 1
    copied4 = [x for x in M if M.count(x) == 4]
    copied1 = [x for x in M if M.count(x) == 1]
    if len(copied4) == 4 and len(copied1) == 3:
        if M == sorted(M):
            summa += n
print(summa)
'''


# Номер 13
'''
from ipaddress import *
net = ip_network('134.80.0.0/255.240.0.0', 0)
R = []
for ip in net:
    ip2 = f'{ip:b}'
    if ip2.count('1') == ip2.count('0'):
        summa = sum([int(x) for x in str(ip).split('.')])
        R.append(summa)
print(max(R))
'''

M = [int(s)for s in open('files/17.txt')]
A = [x for x in M if len(str(abs(x))) ==4]
B = [x for x in A if abs(x)% 100 == 43]
print(B)
R = []
for i in range(len(M)-1):
    x, y = M[i],M[i+1]
    if (x in A)+(y in A) >=1:
        if (x+y)**2 < (max(B))**2:
            R.append((x+y)**2)
print(len(R),max(R))

M = [int(x) for x in open('files/17.txt')]
R = []
A = [x for x in M if len(str(abs(x))) == 4]
B = [x for x in A if abs(x) % 100 == 43]
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x in A) + (y in A) >= 1:
        if (x + y) ** 2 < max(B) ** 2:
            R.append((x + y) ** 2)
print(len(R), max(R))



# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 25, 27.1]
# КЕГЭ = [3, 5, 7, 8, 9, 12, 14, 15, 16, 17, 18, 19-21, 23, 25]
# на следующем уроке: 8


# region 📖 Пробник (Вариант 2)

# Студент #Влад
# Дата: #Четверг #12Марта2026
# ✅ Верно: 1, 2, 3, 4, 10, 14, 16, 18, 19, 20, 21, 23
# ⛔️ Неверно: 6, 7, 8
# ❔ Без ответа: 5, 9, 11, 12, 13, 15, 17, 22, 24, 25, 26, 27
# Итог: 12/29 первичных балла ~ 56 вторичных

# endregion 📖 Пробник (Вариант 2)
