# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
from fnmatch import *
for x in range(9601, 10**10, 9601):
    if fnmatch(str(x), '19*105*9'):
        print(x, x // 9601)
'''


# № 20541(Уровень: Базовый)
'''
from math import prod
from fnmatch import *
for x in range(4321, 10**9, 4321):
    if fnmatch(str(x), '34*56?7'):
        print(x, prod([int(i) for i in str(x)]))
'''

'''
def divisors(x):
    d = []
    for j in range(1, x+1):
        if x % j == 0:
            d.append(j)
    return d


def divisors(x):
    d = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            d.append(j)
            d.append(x // j)
    return sorted(set(d))

print(divisors(24))  # [1, 2, 3, 4,     6, 8, 12, 24]

print(divisors(1_000_000_000))
'''


# № 18620 (Уровень: Средний)
# Пусть M (N) – сумма 2 наибольших различных натуральных
# делителей натурального числа N, не считая самого числа и единицы.
# Если у числа N меньше 2 таких делителей, то M (N) считается равным 0.
# Найдите все такие числа N, что 112 500 000 ≤ N ≤ 112 550 000,
# а десятичная запись числа M (N) заканчивается на 1214.
'''
def divisors(x):
    d = []
    for j in range(2, int(x**0.5)+1):  # не считая самого числа и единицы.
        if x % j == 0:
            d += [j, x // j]
    return sorted(set(d))

for n in range(112_500_000, 112_550_000+1):
    d = divisors(n)
    if len(d) >= 2:
        M = d[-1] + d[-2]
        if M % 10000 == 1214:
            print(n)
'''


#
# № 18148 (Уровень: Базовый)
# (В. Колчев) Пусть M – сумма минимального и максимального
# натуральных делителей целого числа, не считая единицы и самого числа.
# Если таких делителей у числа нет, то считаем значение M равным нулю.
# Напишите программу, которая перебирает целые числа, бо́льшие 900 000,
# в порядке возрастания и ищет среди них такие, для которых
# M оканчивается на 46. В ответе запишите в первом столбце таблицы
# первые пять найденных чисел в порядке возрастания, а
# во втором столбце – соответствующие им значения M.
# Количество строк в таблице для ответа избыточно
'''
def divisors(x):
    d = []
    for j in range(2, int(x**0.5)+1):  # не считая самого числа и единицы.
        if x % j == 0:
            d += [j, x // j]
    return sorted(set(d))

cnt = 0
for n in range(900_000+1, 10**10):
    d = divisors(n)
    if len(d) >= 2:
        M = min(d) + max(d)
        if M % 100 == 46:
            print(n, M)
            cnt += 1
            if cnt == 5:
                break
'''


# № 20969 (Уровень: Базовый)
'''
from fnmatch import *
for x in range(154682, 10**11, 154682):
    if fnmatch(str(x), '*192?3*68'):
        print(x, x // 154682)
'''


# № 20814 Апробация 05.03.25 (Уровень: Базовый)
'''
def divisors(x):
    d = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            d += [j, x // j]
    return sorted(set(d))

k = 0
for n in range(500_001, 1000_000_000):
    P = sum(divisors(n))
    if P % 10 == 9:
        print(n, P)
        k += 1
        if k == 5:
            break
'''


# № 17879 Демоверсия 2025 (Уровень: Базовый)
# Пусть M – сумма минимального и максимального натуральных делителей целого числа,
# не считая единицы и самого числа. Если таких делителей у числа нет, то считаем значение M равным нулю.
# Напишите программу, которая перебирает целые числа, бо́льшие 800 000,
# в порядке возрастания и ищет среди них такие, для которых
# M оканчивается на 4. В ответе запишите в первом столбце таблицы первые пять
# найденных чисел в порядке возрастания, а во втором столбце – соответствующие им значения M.
'''
def divisers(x):
    d = []
    for j in range(2, int(x ** 0.5) + 1):
        if x % j == 0:
            d += [j, x // j]
    return sorted(set(d))

cnt = 0
for n in range(800_000+1, 10 ** 10):
    d = divisers(n)
    if len(d) >= 2:
        M = min(d) + max(d)
        if M % 10 == 4:
            print(n, M)
            cnt += 1
            if cnt == 5:
                break
'''


# № 20144
'''
def divisors(x):
    d = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            d += [j, x // j]
    return sorted(set(d))

cnt = 0
for n in range(3_333_337+1, 10**10):
    d = [j for j in divisors(n) if len(divisors(j)) == 0]
    if len(d) > 0:
        R = max(d) - min(d)
        if R > 1000 and R % 3 == 0:
            print(n, R)
            cnt += 1
            if cnt == 5:
                break

# Вариант 2

def is_prime(x):
    if x <= 1:
        return False
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            return False
    return True

def divisors(x):
    d = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            d += [j, x // j]
    return sorted(set(d))

cnt = 0
for n in range(3_333_337+1, 10**10):
    d = [j for j in divisors(n) if is_prime(j) == True]
    if len(d) > 0:
        R = max(d) - min(d)
        if R > 1000 and R % 3 == 0:
            print(n, R)
            cnt += 1
            if cnt == 5:
                break
'''


# № 23569 Пересдача 03.07.25 (Уровень: Средний)
'''
def is_prime(x):
    if x <= 1:
        return False
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            return False
    return True

def divisors(x):
    d = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            if is_prime(j) and is_prime(x // j):
                if str(j).count('6') == 1 and str(x // j).count('6') == 1:
                    d += [j, x // j]
    return sorted(set(d))

cnt = 0
for n in range(6_086_055+1, 10**10):
    d = divisors(n)
    if len(d) > 0:
        print(n, max(d))
        cnt += 1
        if cnt == 5:
            break

'''



# № 23282 Основная волна 11.06.25 (Уровень: Средний)
# Пусть М - сумма минимального и максимального простых натуральных делителей
# целого числа, не считая самого числа. Если таких делителей у числа нет,
# то значение М считается равным нулю.
# Напишите программу, которая перебирает целые числа, большие 5 400 000,
# в порядке возрастания и ищет среди них такие, для которых М больше 60 000
# и является палиндромом, т.е. одинаково читается слева направо и справа налево.
# В ответе запишите в первом столбце
# таблицы первые  пять найденных чисел в порядке возрастания,
# а во втором столбце - соответствующие им значения М.
'''
def divisors(x):
    d = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            d += [j, x // j]
    return sorted(set(d))

cnt = 0
for n in range(5_400_000+1, 10**10):
    d = [j for j in divisors(n) if len (divisors(j))==0]
    if len(d) >= 2:
        R = max(d) + min(d)
        if R > 60000 and str(R) == str(R)[::-1]:
            print(n, R)
            cnt += 1
            if cnt == 5:
                break
'''

'''
s = sorted("ОДСАЦЛФЩ")
r = []
n = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                word = a + b + c + d
                n += 1
                if n % 2 != 0:
                    if a != "А" and d != 'А' and word.count("Л") >= 3:
                        r.append(n)
print(min(r))
'''


'''
from functools import *

@lru_cache(None)
def F(n):
    if n >= 20:
        return F(n - 4) + 4620
    if n < 20:
        return 8 * (G(n - 12) - 21)

@lru_cache(None)
def G(n):
    if n >= 384_242:
        return n / 4 + 18
    if n < 384_242:
        return 12 + G(n + 41)

for n in range(400_000, 0, -1):
    G(n)

for n in range(1, 1000):
    F(n)
    
print(F(913))
'''



from turtle import*
screensize(10000, 10000)
tracer(0)
k = 20
# Повтори 2 [Повтори 2 [Вперёд 180 Направо 120] Направо 120]
# Направо 150 Вперёд 15 Направо 90 Вперёд 360 Направо 90 Вперёд 15
# Направо 30 Вперёд 74
for i in range(2):
    for t in range(2):
        forward(180*k)
        right(120)
    right(120)
right(150)
forward(15*k)
right(90)
forward(360*k)
right(90)
forward(15*k)
right(30)
forward(74*k)

up()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x*k, y*k)
        dot(3, "green")
exitonclick()
print(16*4)



# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 8, 13, 14, 15, 16, 18, 19-21, 23, 25, 27.1]
# КЕГЭ = [3, 5, 8, 14, 15, 16, 23, 19-21, 25]
# на следующем уроке:
