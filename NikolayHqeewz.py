# region Домашка: ******************************************************************

# Примитивный поиск делителей
'''
n = int(input())  # 8
for j in range(1, n+1):
    if n % j == 0:
        print(j, end=' ')
        # print(j, end=', ')  # 1, 2, 3, 4, 6, 8, 12, 24,
'''

# Вариант 1
'''
n = int(input())
r = 1
for j in range(1, n+1):
    if n % j == 0:
        r *= j
print(r)
'''


# Вариант 2
'''
from math import prod  # prod - возвращает произведение элементов списка

n = int(input())
r = []
for j in range(1, n+1):
    if n % j == 0:
        r.append(j)  # .append() - добавляет новые элементы в конец списка
print(prod(r))
'''

'''
n = int(input())

import time
start = time.time()

# r = []
# for j in range(1, n+1):
#     if n % j == 0:
#         r.append(j)  # .append() - добавляет новые элементы в конец списка
# print(r)  # [1, 2, 3, 4, 6, 8, 12, 24]


r = []
for j in range(1, int(n**0.5)+1):
    if n % j == 0:
        r.append(j)
        r.append(n // j)
print(sorted(set(r)))  # [1, 2, 3, 4, 6, 8, 12, 24]

print(time.time() - start)  # 10.867799043655396 (100_000_000)
# 0.0016 (100_000_000)
'''

'''
n = int(input())
R = []
while n > 0:
    end = n % 10
    R.append(end)
    n //= 10
print(max(R))
print(min(R))
'''

'''
n = int(input())
summa = 0
count = 0
prodd = 1
while n > 0:
    end = n % 10
    summa += end
    count += 1
    prodd *= end
    n //= 10
print(summa)
print(count)
print(prodd)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Тип 2 №28538
# Логическая функция F задаётся выражением ((x ∧ y) → (¬z ∨ w))∧((¬w→x) ∨ ¬y).

print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((x and y) <= ((not z) or w)) and (((not w) <= x) or (not y))
                if F == 0:
                    print(x, y, z, w)
# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2]
# КЕГЭ  = []
# на следующем уроке:
