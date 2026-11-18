# region Домашка: ******************************************************************

# № 8585 (Уровень: Базовый)
# 1. Вычти сумму всех цифр числа
# 2. Найди целую часть от деления на 2
# 3. Вычти 1
#
# Сколько существует программ, для которых при исходном числе
# 40 результатом является число 10, и при этом траектория вычислений содержит число 25?
'''
def F(a, b):
    if a <= b:
        return a == b
    return F(a - sum(map(int, str(a))), b) + F(a // 2, b) + F(a - 1, b)

print(F(40, 25) * F(25, 10))
'''


# Взятие суммы цифр из числа
'''
n = 12345
s = str(n)  # '12345'

# Вариант 1

summa = 0
for x in s:
    summa += int(x)
print(summa)

summa = 0
for i in range(0, 9+1):
    summa += s.count(str(i)) * i
print(summa)


summa = sum([int(x) for x in s])
print(summa)

summa = sum(map(int, s))
print(summa)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************



#
# № 4596 Основная волна 2022(Уровень: Базовый)
# Алгоритм вычисления значения функции
# F(n), где n – натуральное число, задан следующими соотношениями:
# F(n)=1 при n<3;
# F(n)=F(n−1)+n−1 если n>2 и при этом n чётно;
# F(n)=F(n−2)+2×n−2 если n>2 и при этом n нечётно.
# Чему равно значение функции F(34)?
'''
def F(n):
    if n < 3:
        return 1
    if n > 2 and n % 2 == 0:
        return F(n - 1) + n - 1
    if n > 2 and n % 2 != 0:
        return F(n - 2) + 2 * n - 2

print(F(34))
'''


# № 9747 Основная волна 19.06.23(Уровень: Базовый)
# Алгоритм вычисления значения функции
# F(n), где n – натуральное число, задан следующими соотношениями:
# F(n)=n при n<11;
# F(n)=n+F(n–1), если n≥11.
# Чему равно значение выражения
# F(2024)−F(2021)?
'''
import sys
sys.setrecursionlimit(10**8)

def F(n):
    if n < 11:
        return n
    if n >= 11:
        return n + F(n - 1)

print(F(2024) - F(2021))
'''
#   [Previous line repeated 996 more times]
# RecursionError: maximum recursion depth exceeded



# № 17557 Основная волна 08.06.24(Уровень: Базовый)
# Алгоритм вычисления значения функции
# F(n), где n – натуральное число, задан следующими соотношениями:
# F(n)=1 при n=1;
# F(n)=2×n×F(n–1), если n>1.
# Чему равно значение выражения: (F(2024)/16−F(2023))/F(2022)?
'''
import sys
sys.setrecursionlimit(10**8)

def F(n):
    if n == 1:
        return 1
    if n > 1:
        return 2 * n * F(n - 1)

print( (F(2024) // 16 - F(2023)) // F(2022) )
'''
#     print( (F(2024) / 16 - F(2023)) / F(2022) )
#             ~~~~~~~~^~~~
# OverflowError: integer division result too large for a float


# № 23275 Основная волна 11.06.25(Уровень: Базовый)
# Алгоритм вычисления значения функции
# F(n) и G(n), где n – целое число, задан следующими соотношениями:
# F(n)=2×(G(n−3)+8);
# G(n)=2×n, если n<10.
# G(n)=G(n−2)+1, если n≥10.
# Чему равно значение выражения F(15548)?
'''
import sys
sys.setrecursionlimit(10**8)

def F(n):
    return 2 * (G(n - 3) + 8)

def G(n):
    if n < 10:
        return 2 * n
    if n >= 10:
        return G(n - 2) + 1

print(F(15548))
'''

# Вариант 2
'''
from functools import *

def F(n):
    return 2 * (G(n - 3) + 8)

@lru_cache(None)
def G(n):
    if n < 10:
        return 2 * n
    if n >= 10:
        return G(n - 2) + 1
    
for n in range(16000):
    G(n)

print(F(15548))
'''


# № 25355 ЕГКР 13.12.25(Уровень: Базовый)
# Алгоритм вычисления функций
# F(n) и G(n), где n - целое число, задан следующими соотношениями:
# F(n)=F(n−4)+3580, если n≥19;
# F(n)=6×(G(n−7)−36), если n<19;

# G(n)=n/20+28, если n≥248045;
# G(n)=G(n+9)−4, если n<248045.
# Чему равно значение функции F(673)?
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
    if n >= 248045:
        return n / 20 + 28
    if n < 248045:
        return G(n + 9) - 4

for n in range(250_000-1, -1, -1):
    G(n)

for n in range(700):
    F(n)

print(F(673))
'''


#
# № 27076 (Уровень: Средний)
# (В. Лашин) Алгоритм вычисления функций F(n), G(n) и Q(n), где n – целое число, задан следующими соотношениями:
# F(n)=G(n+4), если n<43;
# F(n)=2∗F(n−2)−F(n−4)+2, если n≥43;

# G(n)=G(n+3)+2 при n<11240;
# G(n)=Q(n), если n≥11240.

# Q(n)=n+4, если n<21;
# Q(n)=Q(n−4)+2, если n≥21;
# Чему равно значение функции F(2026)?
'''
from functools import *

@lru_cache(None)
def F(n):
    if n < 43:
        return G(n + 4)
    if n >= 43:
        return 2 * F(n - 2) - F(n - 4) + 2

@lru_cache(None)
def G(n):
    if n < 11240:
        return G(n + 3) + 2
    if n >= 11240:
        return Q(n)

@lru_cache(None)
def Q(n):
    if n < 21:
        return n + 4
    if n >= 21:
        return Q(n - 4) + 2

for n in range(12000):
    Q(n)

for n in range(12000-1, -1, -1):
    G(n)

for n in range(2100):
    F(n)

print(F(2026))
'''


# № 25397 (Уровень: Средний)
# (Р. Косов) Алгоритм вычисления функций
# F(n) и G(n), где n - целое число, задан следующими соотношениями:
# F(n)=F(n−4)+3020, если n>40;
# F(n)=3×(G(n−2)−15), если n≤40;
# G(n)=10×n+50, если n≥301208;
# G(n)=G(n+7)−21, если n<301208.
# Чему равно значение функции F(2026)?
'''
from functools import *

@lru_cache(None)
def F(n):
    if n > 40:
        return F(n - 4) + 3020
    if n <= 40:
        return 3 * (G(n - 2) - 15)

@lru_cache(None)
def G(n):
    if n >= 301208:
        return 10 * n + 50
    if n < 301208:
        return G(n + 7) - 21

for n in range(301208 - 1, -1, -1):
    G(n)
    
for n in range(2100):
    F(n)
    
print(F(2026))
'''

# № 25398 (Уровень: Средний)
# (Р. Косов) Алгоритм вычисления функций
# F(n) и G(n), где n - целое число, задан следующими соотношениями:
# F(n)=F(n−6)+2048, если n>30;
# F(n)=3×(G(n−5)+13),, если n≤30;
# G(n)=2×n+50, если n≥221337;
# G(n)=G(n+11)−48, если n<221337.
# Чему равно значение функции F(5078)?

'''
from functools import *

@lru_cache(None)
def F(n):
    if n > 30:
        return F(n - 6) + 2048
    if n <= 30:
        return 3 * (G(n - 5) + 13)

@lru_cache(None)
def G(n):
    if n >= 221337:
        return 2 * n + 50
    if n < 221337:
        return G(n + 11) - 48


for n in range(221337 - 1, -1, -1):
    G(n)

for n in range(6000):
    F(n)

print(F(5078))
'''

# (Р. Косов) Алгоритм вычисления функций
# F(n) и G(n), где n - целое число, задан следующими соотношениями:
# F(n)=F(n−6)+2048, если n>30;
# F(n)=3×(G(n−5)+13),, если n≤30;
# G(n)=2×n+50, если n≥221337;
# G(n)=G(n+11)−48, если n<221337.
# Чему равно значение функции F(5078)?
from functools import *

@lru_cache(None)
def F(n):
    if n>30:
        return F(n-6)+2048
    if n<=30:
        return 3*(G(n-5)+13)
@lru_cache(None)
def G(n):
    if n>=221337:
        return 2*n+50
    if n<221337:
        return G(n+11)-48
for n in range (221337-1, -1, -1):
    G(n)
for n in range (5200):
    F(n)
print (F(5078))

# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [13, 15, 16, 23]
# КЕГЭ = []
# todo на следующем уроке: 19-21
