# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


#1
'''print('1 2 3 4 5 6')
from itertools import permutations
table = '13 16 24 25 26 31 34 35 42 43 46 52 53 61 62 64'
graph = 'AD DA DB BD AC CA BC CB BE EB CE EC EF FE AF FA'
for p in permutations('ABCDEFG'):
    nt = table
    for i in range(1, 6+1):
        nt = nt.replace(str(i), p[i-1])
    if set(nt.split()) == set(graph.split()):
        print(*p)'''
#Ответ: 45

#2
'''print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (not(z) and y and x and not(w)) or (not(z) and y and not(x) and not(w)) or (z and y and x and not(w))
                if F == 1:
                    print(x, y, z, w, int(F))'''
#Ответ: wzxy

#5
'''R = []
for n in range(1, 1000,2):
    s = bin(n)[2:]
    if n % 3 == 0:
        R = s + bin(n)[-3:]
    else:
        R = n
    r = int(R, 2)
    if r >= 130:
        print(n)
        break'''

#6
'''import turtle as t
t.tracer(0)
t.screensize(70000, 70000)
size = 30

for i in range(2):
    t.forward(3 * size)
    t.left(90)
    t.back(10 * size)
    t.left(90)

t.up()

t.backward(10 * size)
t.right(90)
t.forward(8 * size)
t.left(90)

t.down()

for i in range(2):
    t.forward(16 * size)
    t.right(90)
    t.forward(8 * size)
    t.right(90)

t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * size, y * size)
        t.dot(3, 'red')
t.update()
t.done()'''
#Ответ: 422

#8
'''s = sorted('ЦИТРУС')
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    word = a + b + c + d + e
                    if word.count('И') == 2 and 'ЦЦ' not in word:
                        cnt += 1
print(cnt)'''
#Ответ: 1193

#9
'''cnt = 0
for s in open('9.csv'):
    M = [int(x) for x in s.split(',')]
    if len(M) == len(set(M)):
        M = sorted(M)
        if M[4] - M[0] == M[1] + M[2] + M[3]:
            cnt += 1
print(cnt)'''
#Ответ: 22

#10
#Ответ: 51

#13
'''from ipaddress import *
net = ip_network('172.16.96.0/255.255.224.0', 0)
cnt = 0
for ip in net:
    s = f'{ip:b}'
    if bin(s.count('1') % 2 == 0):
        cnt += 1
print(cnt)'''
#Ответ:8192


#14
'''
def convert(n, b):
    r = ''
    while n > 0:
        r = str(n % b) + r
        n //= b
    return r

RES = []
for x in range(1, 2031):
    n = 6**2030 + 6**100 - x
    s = convert(n, 6)
    RES.append(s.count('0'))
print(min(RES))
'''


#15
'''def F(x, A):
    return (x & 25 == 0) <= ((not(x & A == 0)) <= (not(x & 60 == 0)))
RES = []
for A in range(1, 5000):
    if all(F(x, A) for x in range(1,10000)):
        RES.append(A)
print(max(RES))'''
#Ответ: 61

#16
'''from functools import *
@lru_cache(None)
def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n * F(n - 1)

for i in range(2, 3000):
    F(i)

print((F(2024) - 5 * F(2023)) / F(2022))'''
#Ответ: 4084437

#19-21
'''def F(a, s, n):
    if a+s >= 211:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a+1, s, n - 1), F(a, s+1, n - 1), F(a*2, s, n - 1), F(a, s*2, n - 1)]
    return all(h) if (n - 1) % 2 == 0 else any(h)  # else any(h)
print([s for s in range(1, 194) if (not(F(17, s, n = 1))) and F(17, s, n = 2)]) #176
print([s for s in range(1, 194) if not(F(17, s, n = 1)) and F(17, s, n = 3)]) #88 96
print([s for s in range(1, 194) if (F(17, s, n = 2) or F(17, s, n = 4)) and not(F(17, s, 2))]) #87'''

#23
'''def F(a, b):
    if a <= b:
        return a == b
    return F(a - 1, b) + F(a // 2, b)
print(F(40, 17) * F(17, 6))'''
#Ответ: 56

#25
'''from fnmatch import *
for x in range(171, 10**8, 171):
    if fnmatch(str(x), '1*23??56'):
        print(x, x // 171)'''
#Ответ:
#1237356 7236
#10231956 59836
#12232656 71536
#14233356 83236
#16234056 94936
#18234756 106636


# Номер 7
'''
pixels = 192 * 960
I = 90 * 2**13  # бит - на сжатый файл (85%)
I = (I / 85) * 100  # бит - исходный файл (100%)

# I = pixels * i
i = I / pixels
print(i)  # 4.705 -> 4

colors = 2 ** 4
print(colors)  # 16

# 100% -> -15% = 85%
'''


# Номер 11
'''
alp = 10 + 26 + 8164
# print(alp, 2**14)
i = 14   # 2 ** 14 >= alp

byte = 156 * 2**10 / 835
print(byte)  # 191.3101 -> 192
bit = 192 * 8

# bit = sym * i
sym = bit / i
print(sym)  # 109.7142 -> 109 
'''


# Номер 12
'''
print(bin(800)[2:])  # 1100100000
print(int('1000100000', 2))  # 544
'''


# Номер 17
'''
M = [int(x) for x in open('files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 4]
B = [x for x in A if abs(x) % 100 == 43]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x in A) + (y in A) >= 1:
        if (x + y) ** 2 < max(B) ** 2:
            R.append((x + y) ** 2)
print(len(R), max(R))
'''


# № 27762 Апробация 04.03.26 (Уровень: Базовый)
'''
# I = a * b * c * t

a = 2
t = 180
b = 24000
c = 8

I = a * b * c * t  # бит
U = 48000  # бит/с

print(I / U)  # 1440
'''


# № 25346 ЕГКР 13.12.25 (Уровень: Базовый)
# Прибор автоматической фиксации нарушений правил дорожного
# движения делает цветные фотографии размером 1024×960 пикселей,
# используя палитру из 16 384 цветов. Для передачи снимки группируются
# в пакеты по 400 штук.
# Определите размер одного пакета фотографий в Мбайт.
'''
pixels = 1024 * 960
colors = 16384
i = 14  # 2 ** 14 >= colors

I = pixels * i  # бит вес картинки

I_400 = I * 400
print(I_400 / 2**23)
# 656.25 -> 656
'''

# # endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 25, 27]
# КЕГЭ = []
# на следующем уроке: 4, 7, 17, 12, 22, 27, 24, 26


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
