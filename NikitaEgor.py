# region Домашка: ******************************************************************
from turtledemo.round_dance import stop

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: *************************************************************


# № 48393 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alp[:8]:
    for y in alp[:8]:
        A = int(f'{y}04{x}5', 11)
        B = int(f'253{x}{y}', 8)
'''





# https://stepik.org/lesson/1038709/step/10?unit=1062775
'''
import sys
sys.setrecursionlimit(10**8)

def F(n):
    if n == 1:
        return 1
    if n > 1:
        return 2 * n * F(n - 1)

print((F(2024) // 16 - F(2023)) // F(2022))
'''



'''
def F(n):
    if n == 1:
        return 1
    if n > 1:
        return 2 * n * F(n - 1)
    
for n in range(0, 3000, 1):
    F(n)



def F(n):
    if n == 1:
        return 1
    if n > 1:
        return 2 * n * F(n + 1)

for n in range(3000-1, -1, -1):
    F(n)
'''

# https://stepik.org/lesson/1038709/step/10?unit=1062775
'''
from functools import *

@lru_cache(None)
def F(n):
    if n == 1:
        return 1
    if n > 1:
        return 2 * n * F(n - 1)

for n in range(0, 3000, 1):
    F(n)

print((F(2024) // 16 - F(2023)) // F(2022))
'''

# № 21902 Открытый вариант 2025(Уровень: Базовый)
'''
from functools import *

@lru_cache(None)
def F(n):
    if n >= 2025:
        return n
    if n < 2025:
        return n * 2 + F(n + 2)

for n in range(100-1, -1, -1):
    F(n)

print(F(82) - F(81))
'''


#
# № 21711 ЕГКР 19.04.25(Уровень: Базовый)
# Алгоритм вычисления значения функции
# F(n), где n – целое число, задан следующими соотношениями:
# F(n)=n при n<20;
# F(n)=(n−6)×F(n–7), если n≥20.
# Чему равно значение выражения (F(47872)−290×F(47865))/F(47858)?
'''
from functools import *
@lru_cache(None)
def F(n):
    if n < 20:
        return n
    if n >= 20:
        return (n - 6) * F(n - 7)

for n in range(0, 50000, 1):
    F(n)

print((F(47872) - 290 * F(47865)) // F(47858))
'''


# № 18123 (Уровень: Базовый)
# (Д. Бахтиев) Алгоритм вычисления значения функции
# F(n), где n – натуральное число, задан следующими соотношениями:
# F(n)=n, при  n≥2010;
# F(n)=F(n+3)+F(n+2)+F(n+1), если n<2010
# Чему равно значения выражения (F(2000)−2⋅(F(2002)+F(2003))) / F(2004)?
'''
from functools import *

@lru_cache(None)
def F(n):
    if n >= 2010:
        return n
    if n < 2010:
        return F(n + 3) + F(n + 2) + F(n + 1)

for n in range(3000 - 1, -1, -1):
    F(n)

print((F(2000) - 2 * (F(2002) + F(2003))) // F(2004))
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
    else:
        return 6 * (G(n - 7) - 36)

@lru_cache(None)
def G(n):
    if n >= 248045:
        return n / 20 + 28
    else:
        return G(n + 9) - 4

for n in range(250_000-1, -1, -1):
    G(n)

for n in range(1000):
    F(n)

print(F(673))
'''


# № 25397 (Уровень: Средний)

from functools import *

@lru_cache(None)
def F(n):
    if n > 40:
        return F(n - 4) + 3020
    else:
        return 3 * (G(n - 2) - 15)

@lru_cache(None)
def G(n):
    if n >= 301_208:
        return 10 * n + 50
    else:
        return G(n + 7) - 21

for n in range(302_000-1, -1, -1):
    G(n)

for n in range(2050):
    F(n)

print(F(2026))



# endregion Урок: *************************************************************
# #
# #
# 2027
# ФИПИ = [1, 5, 14, 16]
# КЕГЭ = []
#
# 2026
# ФИПИ = [1, 2, 3, 5, 8, 11, 10, 13, 14, 15, 16, 17, 18, 19-21, 22]
# КЕГЭ = [1, 2, 3, 12, 10]
# на следующем уроке: Добиваем 3 прототип 14 номера
