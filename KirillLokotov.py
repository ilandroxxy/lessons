

# № 23375 Резервный день 19.06.25 (Уровень: Базовый)
'''
import sys
sys.setrecursionlimit(50000)

def F(n):
    return G(n - 1) + G(n - 3)

def G(n):
    if n <= 9:
        return 3 * n
    if n > 9:
        return G(n - 4) + 2

print(F(42999))
'''


# № 21711 ЕГКР 19.04.25 (Уровень: Базовый)
'''
import sys
sys.setrecursionlimit(10000)

def F(n):
    if n < 20:
        return n
    if n >= 20:
        return (n - 6) * F(n - 7)

print((F(47872) - 290 * F(47865)) / F(47858))
'''

# № 20906 Апробация 05.03.25 (Уровень: Базовый)
'''
import sys
sys.setrecursionlimit(10000)

def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n * F(n - 1)

print((F(2024) // 4  +F(2023)) // F(2022))
'''
# OverflowError: integer division result too large for a float



# № 18931 Новогодний вариант 2025 (Уровень: Базовый)
'''
from functools import *
import sys
sys.setrecursionlimit(100000)

@lru_cache(None)
def F(n):
    if n <= 3:
        return n - 1
    if n > 3 and n % 2 == 0:
        return F(n - 2) + n/2 - F(n - 4)
    if n > 3 and n % 2 != 0:
        return F(n - 1) * n + F(n - 2)

for n in range(5000):
    F(n)

print(F(4952)+2 * F(4958)+F(4964))
'''


# № 23380 Резервный день 19.06.25 (Уровень: Базовый)
# Сколько существует программ, для которых при исходном числе 3 результатом
# является число 20, при этом траектория вычислений содержит число 7 и не содержит 10?
'''
def F(a, b):
    if a > b or a == 10:
        return 0
    if a == b:
        return 1
    else:
        return F(a+1, b) + F(a+2, b) + F(a*2, b)


print(F(3, 7) * F(7, 20))
'''

'''
f = open("17_23201.txt")
a = [int(i) for i in f]
mini = min(x for x in a if 100 <= x < 1000 and x % 10 == 7)
l = []
for x, y in zip(a, a[1:]):
    if (100 <= x < 1000) + (100 <= y < 1000) == 1 and (x + y) % mini == 0:
        l.append(x + y)
print(len(l), min(l))
'''

'''
a = [int(i) for i in open('0. files/17.txt')]
mini = min([x for x in a if 100 <= x < 1000 and x % 10 == 7])
l = []
for x, y in zip(a, a[1:]):
    if (100 <= x < 1000) + (100 <= y < 1000) == 1 and (x + y) % mini == 0:
        l.append(x + y)
print(len(l), min(l))


a = [int(i) for i in open('0. files/17.txt')]
b = [x for x in a if len(str(abs(x))) == 3]
c = [x for x in b if abs(x) % 10 == 7]
l = []
for i in range(len(a)-1):
    x, y = a[i], a[i+1]
    if (x in b) + (y in b) == 1:
        if (x + y) % min(c) == 0:
            l.append(x + y)
print(len(l), min(l))
'''

# № 20907 Апробация 05.03.25 (Уровень: Базовый)
# 2 кучи: a+1, s+1, a*2, s*2 | a + s >= 81 | 1 ≤ s ≤ 73 | a = 7
'''
def F(a, s, n):
    if a + s >= 81:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a+1, s, n-1), F(a, s+1, n-1), F(a*2, s, n-1), F(a, s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

print([s for s in range(1, 74) if F(7, s, n=2)])
print([s for s in range(1, 74) if F(7, s, n=3) and not F(7, s, n=1)])
print([s for s in range(1, 74) if F(7, s, n=4) and not F(7, s, n=2)])
'''

# n - шаг игры
# n = 1: Петя первый ход
# n = 2: Ваня первый ход
# n = 3: Петя второй ход
# n = 4: Ваня второй ход


# № 23374 Резервный день 19.06.25 (Уровень: Базовый)
'''
def F(x, y, A):
    return (x < A) and (y < 3*A) or (2*x + y > 128)

for A in range(1, 10000):
    if all(F(x, y, A) for x in range(1, 100) for y in range(1, 100)):
        print(A)
        break
'''


# № 20584 (Уровень: Базовый)
'''
def F(x, A):
    return ((405 % x == 0) <= (81 % x == 0)) or (A - x > 162)

for A in range(1, 10000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
        break
'''


# № 20577 (Уровень: Базовый)
'''
def F(x, A):
    return (x & A != 0) <= ((x & 698 == 0) <= (x & 321 != 0))

for A in range(1, 10000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
'''

#
# № 17871 Демоверсия 2025 (Уровень: Базовый)
def F(x, a1, a2):
    P = 15 <= x <= 40
    Q = 21 <= x <= 63
    A = a1 <= x <= a2
    return (P) <= (((Q) and (not A)) <= (not P))


R = []
M = [x / 4 for x in range(10 * 4, 80 * 4)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(min(R))