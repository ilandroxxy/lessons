# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Тип 2 Номер 17856
'''
b = 0, 1
print(b)  # (0, 1)
print(type(b))  # <class 'tuple'>

print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((w <= y) <= x) or (not z)
                if F == 0:
                    print(x, y, z, w)
'''


# Тип 2 Номер 18483
'''
print('x y z w F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((y <= w) == (x <= (not z))) and (x or w)
                if F == 0:
                    print(x, y, z, w, int(F))

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((y <= w) == (x <= (not z))) and (x or w)
                if F == 1:
                    print(x, y, z, w, int(F))
'''

# Тип 5 Номер 17859

'''
# i  0  1  2  3
M = [4, 5, 6, 7][2:]
'''

'''
R = []
for n in range(1, 12+1):
    s = f'{n:b}'  # s = bin(n)[2:]
    if n % 2 == 0:
        s = '10' + s
    else:
        s = '1' + s + '01'
    r = int(s, 2)  # Из двоичной в десятичную
    R.append(r)

print(max(R))
'''

'''
s = '0123456789AB'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    num = a + b + c + d + e
                    if num[0] != '0':
                        if num.count('7') == 1:
                            if num.count('9') + num.count('A') + num.count('B') <= 3:
                                cnt += 1
print(cnt)  # 67476
'''
'''
s = '0123456789AB'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    num = a + b + c + d + e
                    if num[0] != '0':
                        if num.count('7') == 1:
                            if len([x for x in num if x > '8']) <= 3:
                                cnt += 1
print(cnt)  # 67476


from itertools import *
cnt = 0
for per in product('0123456789AB', repeat=5):
    num = ''.join(per)
    if num[0] != '0':
        if num.count('7') == 1:
            if len([x for x in num if x > '8']) <= 3:
                cnt += 1
print(cnt)
'''
'''
s = '1' * 81
while '11111' in s or '888' in s:
    if '11111' in s:
        s = s.replace('11111', '88', 1)
    else:
        s = s.replace('888', '8', 1)
print(s)
'''

'''
R = []
for n in range(4, 10000):
    s = '8' + '4' * n
    while '11' in s or '444' in s or '8888' in s:
        if '11' in s:
            s = s.replace('11', '4', 1)
        if '444' in s:
            s = s.replace('444', '88', 1)
        if '8888' in s:
            s = s.replace('8888', '1', 1)
    # summa = sum(map(int, s))
    summa = sum([int(x) for x in s])
    R.append(summa)
    print(max(R))
'''


# Тип 14 Номер 17868
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:19]:
    A = int(f'98897{x}21', 19)
    B = int(f'2{x}923', 19)
    if (A + B) % 18 == 0:
        print((A + B) // 18)
'''

# Тип 14 Номер 17869
'''
n = 3*3125**8 +2*625**7 -4*625**6 +3*125**5-2*25**4 - 2025
b = 25
M = []
while n > 0:
    M.append(n % b)
    n //= b
M.reverse()
print(M.count(0))
'''

# Тип 14 Номер 17870
'''
for x in range(0, 2030+1):
    n = 7**170 + 7**100 - x
    b = 7
    M = []
    while n > 0:
        M.append(n % b)
        n //= b
    M.reverse()
    if M.count(0) == 71:
        print(x)
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 14]
# КЕГЭ  = []
# на следующем уроке:
