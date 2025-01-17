


# f = open("text.txt")
# a = [list(map(int, i.split())) for i in f]
'''
cnt = 0
for s in open('9.txt'):
    M = [int(x) for x in s.split()]
    flag = True
    for i in range(len(M)):
        for j in range(i+1, len(M)):
            x, y = M[i] + M[j]
            if (x + y) % 2 != 0:
                flag = False
                break
    if flag == True:
        cnt += 1
'''


# A. вычти 1
# B. вычти 6
# C. найди целую часть от деления на 2
# Сколько существует таких программ, которые
# исходное число 34 преобразуют в число 6,
# и при этом траектория вычислений содержит
# числа 19 и 29 и не содержит числа 24?
'''
def F(a, b):
    if a <= b or a == 24:
        return a == b
    return F(a-1, b) + F(a-6, b) + F(a//2, b)


print(F(34, 29) * F(29, 19) * F(19, 6))


def F(a, b, c):
    if a <= b or a == 24:
        print(c, a == b)
        return a == b and 'AB' not in c
    return F(a-1, b, c+'A') + F(a-6, b, c+'B') + F(a//2, b, c+'C')


print(F(34, 5, ''))


def F(a, b, c):
    if a <= b or a == 24:
        print(c, a == b)
        return a == b
    return F(a-1, b, c+' '+str(a)) + F(a-6, b, c+' '+str(a)) + F(a//2, b, c+' '+str(a))


print(F(34, 5, ''))
'''


# № 18931 Новогодний вариант 2025 (Уровень: Базовый)
'''
from functools import *
import sys
sys.setrecursionlimit(10000)

@lru_cache(None)
def F(n):
    if n <= 3:
        return n - 1
    if n > 3 and n % 2 == 0:
        return F(n-2) + n/2 - F(n-4)
    if n > 3 and n % 2 != 0:
        return F(n - 1) * n + F(n - 2)


for n in range(5000):
    F(n)

print(F(4952) + 2 * F(4958) + F(4964))
'''
# RecursionError: maximum recursion d

'''
for A in range(1, 1000):
    flag = True
    for x in range(1, 100):
        for y in range(1, 100):
            F = ((x - 3*y < A) or (y > 400) or (x > 56))
            if not F:
                flag = False
                break
    if flag == True:
        print(A)
        break
'''

# № 19247 ЕГКР 21.12.24 (Уровень: Базовый)
'''
def F(x, y, A):
    return (x - 3*y < A) or (y > 400) or (x > 56)

for A in range(1, 1000):
    if all(F(x, y, A) for x in range(1, 100) for y in range(1, 100)):
        print(A)
        break
'''

# № 18266 (Уровень: Базовый)
'''
def F(x, A):
    return (x & 57 == 0) or ((x & 23 == 0) <= (x & A != 0))

for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
        break
'''

# № 18175 (Уровень: Базовый)
'''
def F(x, A):
    return ((x % 7 != 0) and (x % 13 == 0)) <= (x > A - 40)

R = []
for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        R.append(A)
print(max(R))


print(max([A for A in range(1, 1000) if all((((x % 7 != 0) and (x % 13 == 0)) <= (x > A - 40)) for x in range(1, 10000))]))
'''


# № 18595 (Уровень: Базовый)
'''
def F(x, a1, a2):
    C = 48 <= x <= 94
    J = 83 <= x <= 100
    A = a1 <= x <= a2
    return (not(C or J)) <= (not A)


R = []
M = [x / 4 for x in range(40 * 4, 110 * 4)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(max(R))
'''
# 52.75 -> 52.80 -> 52.89 -> 53



'''
def is_prime(x):
    if x <= 1:
        return False
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            return False
    return True


R = []
for x in range(1, 100):
    for y in range(1, 100):
        s = '0' + '1' * x + '2' * y
        if len(s) > 40:
            while '01' in s or '02' in s:
                s = s.replace('02', '1110', 1)
                s = s.replace('01', '220', 1)
            summa = sum(map(int, s))
            if is_prime(summa):
                R.append(x+y*2)
print(min(R))
'''


'''
from itertools import *
cnt = 0
for n, p in enumerate(product(sorted('ПРЕСТОЛ'), repeat=5), 1):
    slovo = ''.join(p)
    sogl = [x for x in slovo if x in 'ПРСТЛ']
    if n % 2 != 0:
        if slovo[-1] in 'ЕО':
            if len(sogl) <= 3:
                cnt += 1
print(cnt)
'''



# 5*, 8, 9, 13, 18, 19-21, 22, 24