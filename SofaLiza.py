# region Домашка: ******************************************************************



# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# ЕГКР 13.12.25 Вариант 1 - Номер 7
'''
pixels = 1024 * 960
colors = 16384

i = 14 # 2 ** 14 >= 16384

V_photo = pixels * i

V_all = V_photo * 400

print(V_all / 2 ** 23)  # бит
'''
from zoneinfo import reset_tzpath

# 656.25 -> 656


# ЕГКР 13.12.25 Вариант 1 - Номер 11
'''
sym = 105
byte = 7 * 2 ** 20 /  65536
print(byte) # 112.0
bit = 112 * 8
i = bit / sym
print(i) #8.53333333333333
i = 9
print(f'Максимальную мощность алфавита: {2 ** 9}')
print(f'Минимальная мощность алфавита: {2 ** 8 + 1}')
'''


# ЕГКР 13.12.25 Вариант 1 - Номер 13
'''
from ipaddress import *
net = ip_network('190.202.83.62/255.255.252.0', 0)
for ip in net:
    print(ip, sum([int(x) for x in str(ip).split('.')]))

print(190 + 202 + 83 + 254)
'''


# ЕГКР 13.12.25 Вариант 1 - Номер 15
'''
def F(x, y, A):
    return (78125 != y + 4 * x) or (A > x) and (A > y)

# y = 78125 - 4 * x
for A in range(0, 100000):
    if all(F(x, 78125 - 4 * x, A) for x in range(1, 20000)):
        print(A)
        break
'''
# Натуральыне числа range(1, ....)
# Целые положительные числа range(1, ....)
# Целые неотрицательные числа range(0, ....)


# ЕГКР 13.12.25 Вариант 1 - Номер 16
'''
from functools import *

@lru_cache(None)
def F(n):
    if n >= 19:
        return F(n - 4) + 3580
    if n < 19:
        return 6 * (G(n - 7) - 36)

@lru_cache(None)
def G(n):
    if n >= 248_045:
        return n / 20 + 28
    if n < 248_045:
        return G(n + 9) - 4

for n in range(250_000-1, -1, -1):
    G(n)

for n in range(1, 1000):
    F(n)

print(F(673))
'''

# Вариант 3
'''
G = [0] * 250000
F = [0] * 1000

for n in range(250_000-1, -1, -1):
    if n >= 248_045:
        G[n] = n / 20 + 28
    if n < 248_045:
        G[n] = G[n + 9] - 4

for n in range(0, 1000):
    if n >= 19:
        F[n] = F[n - 4] + 3580
    if n < 19:
        F[n] = 6 * (G[n - 7] - 36)

print(F[673])
'''


# Номер 7 задачи с музыкой

# V_music = a * b * c * t (бит)
# a - кол-во каналов (шт) моно/стерео/квадра - 1/2/4
# b - частота дискретизации (Гц)
# c - разрешение/глубина кодирования (бит)
# t - время звукозаписи (сек)


# https://education.yandex.ru/ege/inf/task/7407e7ee-2ca4-4372-b173-b39bffa2d1d9
'''
a = 2
b = 44000
c = 16
t = 60
V_music = a * b * c * t

V_all = V_music * 32

U = 1_802_240  # бит/с
# T - ?

# V = U * T
# T = V / U
T = V_all / U
print(T)  # сек
'''



# Голосовое сообщение длительностью 180 секунд было закодировано
# в формате квадро с разрешением 16 бит и частотой дискретизации 48000
# измерений в секунду и передано по каналу связи. Производилось
# сжатие данных. После сжатия размер аудиофайла уменьшился на 50%.
# Пропускная способность канала связи равна 4800 бит/с.
# Определите, сколько минут потребуется для передачи голосового
# сообщения. В ответе запишите только целое число.
'''
a = 4
b = 48000
c = 16
t = 180
V_music = (a * b * c * t) * 0.5

U = 4800  # бит/с
T = V_music / U
print(T / 60)
'''

# ----------------------------------------

# ЕГКР 13.12.25 вариант 1 (https://disk.yandex.ru/i/lYw4X69j5TfdKg) Номер 25
'''
M = [int(s) for s in open('0. files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 4]
B = [x for x in M if abs(x) % 100 == 30]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x in A) + (y in A) + (z in A) == 0:
        if (x + y + z) > max(B):
            R.append(x + y + z)
print(len(R), max(R))
'''


# ЕГКР 13.12.25 вариант 1 (https://disk.yandex.ru/i/lYw4X69j5TfdKg) Номер 25
'''
def divisors(n):
    d = []
    for j in range(1, int(n ** 0.5)+1):
        if n % j == 0:
            d.append(j)
            d.append(n // j)  # n = 24 j = 4  24 // 4 = 6
    return sorted(set(d))

cnt = 0
for n in range(1_350_050+1, 10**10):
    d = [j for j in divisors(n) if j != n and j != 11 and j % 100 == 11]
    if len(d) > 0:
        print(n, min(d))
        cnt += 1
        if cnt == 5:
            break
'''


# https://stepik.org/lesson/1038609/step/5?unit=1062783
'''
pixels = 1280 * 1024

U = 1_966_080   
T = 280
V_all = U * T

V_photo = V_all / 39
print(V_photo)

i = V_photo / pixels
print(i)  # 10.769 -> 10

print(2 ** 10)
'''


# https://stepik.org/lesson/1038609/step/4?unit=1062783
'''
# V_music = a * b * c * t

a = 2
# b = ?
c = 6
t = 3 * 60 + 15

V_music = 12 * 2**23  # Мбайт -> бит

b = V_music / (a * c * t)
print(b)  # 43018.50
'''


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 14, 15, 16, 17, 19-21, 23, 25, 27]
# КЕГЭ = []
# на следующем уроке: Вариант ЕГКР добиваем 27 номер, Обсуждаем пробник
