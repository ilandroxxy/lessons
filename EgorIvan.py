# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

#1
'''print('1 2 3 4 5 6 7 8')
from itertools import permutations
table = '12 14 17 21 24 28 34 36 37 41 42 43 56 58 63 65 68 71 73 82 85 86'
graph = 'BH HB FB BF FC CF CH HC AC CA AH HA AE EA ED DE DG GD EG GE GF FG'
for p in permutations('ABCDEFGH'):
    nt = table
    for i in range(1, 8+1):
        nt = nt.replace(str(i), p[i-1])
    if set(nt.split()) == set(graph.split()):
        print(*p)'''
#65

#2
'''print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (not(x) and y and z and not(w)) or (not(x) and y and not(z) and not(w)) or (x and y and z and not(w))
                if F == 1:
                    print(x, y, z, w, int(F))'''
#xwzy

#5
'''R = []
for n in range(1, 10000):
    d = bin(n)[2:]
    if n % 2 == 0:
        d = '10' + d
    else:
        d = '1' + d + '10'
    r = int(d, 2)
    if n > 18:
        R.append(r)
print(min(R))'''
#84

#6
'''import turtle as t
t.tracer(0)
t.screensize(5000, 5000)
size = 30

for i in range(2):
    t.forward(1 * size)
    t.left(270)
    t.forward(16 * size)
    t.right(90)

t.up()

t.backward(4 * size)
t.right(90)
t.forward(10 * size)
t.left(90)

t.down()

for i in range(2):
    t.forward(17 * size)
    t.right(90)
    t.forward(7 * size)
    t.right(90)

t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * size, y * size)
        t.dot(3, 'red')

t.update()
t.done()'''
#129

#7
'''a = 2
b = 24000
c = 8
t = 180
T = a*b*c*t
print(T)
V = 48000
print(T/V) 
'''
#1440

#8
'''n = '0123456'
cnt = 0
for a in n:
    for b in n:
        for c in n:
            for d in n:
                for e in n:
                    num = a + b + c + d + e
                    if a != '0':
                        if num.count('0') == 1:
                            if num.count('1') <= 2:
                                cnt+=1
print(cnt)'''
#5100

#9
'''cnt = 0
for s in open('9 (1).csv'):
    M = sorted([int(x) for x in s.split(',')])
    copied1 = [x for x in M if M.count(x) == 1]
    if len(copied1) == 5:
        if (M[0] + M[4])*2 == M[1] + M[2] + M[3]:
            cnt += 1
    print(cnt)'''
#50019


#10
#Ответ 66

#13
'''from ipaddress import *
net = ip_network('172.16.160.0/255.255.240.0', 0)
cnt = 0
for ip in net:
    s = f'{ip:b}'
    if s.count('1') % 2 == 0:
        cnt += 1
print(cnt)'''
#2048


#15
'''
def F(x, A):
    return (x % 21 == 0) <= ((x % A != 0) <= (x % 77 != 0))


RES = []
for A in range(1, 5000):
    if all(F(x, A) for x in range(1, 10000)):
        RES.append(A)
print(max(RES))
'''


#16
'''from functools import *
@lru_cache(None)

def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n * F(n-1)

for i in range(1, 2025):
    F(i)

print((F(2024) - 2 * F(2023)) / F(2022))'''
#4090506

#17
'''
M = [int(s) for s in open('files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 4 or 1000 <= abs(x) <= 9999]
B = [x for x in A if abs(x) % 100 == 43]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x in A) + (y in A) >= 1:
        if (x + y) ** 2 < max(B) ** 2:
            R.append((x + y) ** 2)
print(len(R), max(R))
'''



#19-21
'''
def F(a, s, n):
    if a + s >= 207:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a+1,s,n-1), F(a,s+1,n-1), F(a*2,s,n-1), F(a,s*2,n-1)]
    return any(h) if (n-1) % 2 == 0 else all(h)
    return any(h) if (n-1) % 2 == 0 else any(h)

print([s for s in range(2, 190) if F(17, s, n=2)]) #172?
print([s for s in range(2, 190) if (not F(17, s, n = 1)) and F(17, s, n = 3)]) #86 94
print([s for s in range(2, 190) if (F(17, s, n = 2) or F(17, s, n = 4)) and not F(17, s, n = 2)])#85'''
'''


#23

def F(a, b):
    if a <= b:
        return a == b
    return F(a -1, b) + F(a // 2, b)

print(F(40, 16) * F(16,6))
#60
'''

#25
'''
from fnmatch import *
for x in range(271, 10**8, 271):
    if fnmatch(str(x), '12??15*6'):
        print(x, x // 271)
'''

#1202156 4436
#12001506 44286
#12131586 44766
#12421556 45836
#12711526 46906

'''
print(bin(800)[2:])  # 1100100000
print(int('1000100000', 2))  # 544
'''


# Номер 9 Досрочная волна 07.04.26 вариант 1 (https://disk.yandex.ru/i/vSKwP7fEAs4V0g)
'''
from itertools import permutations
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(',')]
    if max(M) < sum(M) - max(M):
        if all(p[0] + p[1] != p[2] + p[3] for p in permutations(M, r=4)):
            cnt += 1
print(cnt)
'''


# # endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 25, 27]
# КЕГЭ = [7, 11, ]
# на следующем уроке: немного 5 и переходим к 8, 4, 17, 12, 22, 27, 24, 26


# region 📖 Пробник (Вариант 2)

# Студент #Иван
# Дата: #Пятница #06Марта2026
# ✅ Верно: 1, 2, 3, 6, 7, 9, 11, 13, 14, 16, 18, 19, 20, 21, 23, 25
# ⛔️ Неверно: 4, 5, 8, 10, 12, 15, 17, 22, 24, 26, 27
# ❔ Без ответа: Нет
# Итог: 16/29 первичных балла ~ 67 вторичных


# Студент #Egor
# Дата: #Понедельник #16Марта2026
# ✅ Верно: 1, 2, 3, 15, 16, 19, 20, 21, 25
# ⛔️ Неверно: 6
# ❔ Без ответа: 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 17, 18, 22, 23, 24, 26, 27
# Итог: 9/29 первичных балла ~ 48 вторичных

# region 📖 Пробник (Вариант 2)
