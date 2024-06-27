# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
R = []
for n in range(1, 1000):
    s = f'{n:b}'  # s = bin(n)[2:]
    if s.count('1') % 2 == 0:
        s = '10' + s[2:] + '0'
    else:
        s = '11' + s[2:] + '1'
    r = int(s, 2)
    if r > 50:
        R.append(n)
print(min(R))
'''

'''
import turtle as t
t.left(90)
t.tracer(0)
l = 20

for i in range(9):
    t.fd(22*l)
    t.rt(90)
    t.fd(6*l)
    t.rt(90)
t.up()
t.fd(1*l)
t.rt(90)
t.fd(5*l)
t.lt(90)
t.down()
for i in range(9):
    t.fd(53*l)
    t.rt(90)
    t.fd(75*l)
    t.rt(90)

t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * l, y * l)
        t.dot(2, 'red')
t.done()
'''

'''
pixels = 1024 * 960  # кол-во пикселей
colors = 8192  # 2**i >= colors
print(2**13)
i = 13  # бит на один пиксель
bit = pixels * i  # бит - вес одной картинки.


bits = 1_474_500 * 280  # бит на пакет фотографий
print(bits / bit)
'''
# 32.306 -> 32

'''
s = '01234567'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    num = a + b + c + d + e
                    if num[0] != '0':
                        if num[0] not in '1357' and num[-1] not in '26':
                            if num.count('7') <= 2:
                                cnt += 1
print(cnt)
'''

'''
cnt = 0
for s in open('9.csv'):
    M = sorted([int(x) for x in s.split(';')])
    if M[3] < M[0] + M[1] + M[2]:
        if len(set(M)) == 3:
            cnt += 1
print(cnt)
'''


# № 11234 (Уровень: Базовый)
'''
def F(x, A):
    B = 120 <= x <= 130
    return ((B) <= (x % 7 != 0)) or (A > 2*x)

for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
        break
'''


# № 11837 (Уровень: Базовый)
'''
def F(x, y, A):
    return (x ** 2 + y**2 > 1024 - x) or (y < -2*x + A)

for A in range(1, 1000):
    if all(F(x, y, A) for x in range(1, 100) for y in range(100)):
        print(A)
        break
'''


# № 13895 (Уровень: Базовый)
'''
def F(x, a1, a2):
    B = 34 <= x <= 72
    C = 32 <= x <= 61
    A = a1 <= x <= a2
    return ((B) <= (A)) and ((not C) or (A))

R = []
M = [x for x in range(20, 100)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(min(R))
'''
# Ответ: 40

'''
for x in range(2030+1):
    n = 7**91 + 7**160 - x
    M = []
    while n > 0:
        M.append(n % 7)
        n = n // 7
    if M.count(0) == 70:
        print(x)
'''
# 2029

'''
alphabet = 10 + 52*2 + 458  # 2**i >= alphabet (572)
i = 10
# bit = symbols * i

byte = (276 * 1024) / 862  # байт на один серийный номер
print(byte)  # 327.870
byte = 327  # отведено не более 276 Кбайт памяти.
bit = byte * 8
symbols = bit / i
print(symbols)  # 261.6
'''
# 261


# № 17562 Основная волна 08.06.24 (Уровень: Базовый)
# Сколько существует программ, которые преобразуют число 5 в число 11,
# и при этом траектория вычислений содержит число 7?
'''
def F(a, b):
    if a > b:  # Прибавить a > b, Вычти a < b
        return 0
    elif a == b:
        return 1
    else:
        return F(a+1, b) + F(a+2, b) + F(a+3, b)

print(F(5, 7) * F(7, 11))
'''



# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке:
