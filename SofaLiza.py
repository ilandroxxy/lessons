# region Домашка: ******************************************************************

# https://stepik.org/lesson/1038700/step/4?unit=1062785
'''
from ipaddress import *
net = ip_network('136.36.240.16/255.255.255.248', 0)
cnt = 0
for ip in net:
    s = f'{ip:b}'
    if "101" not in s:
        cnt += 1
print(cnt)
'''


# https://stepik.org/lesson/1038700/step/5?unit=1062785
'''
from ipaddress import *
RES = []
for mask in range(32+1):
    net1 = ip_network(f'165.112.200.70/{mask}', 0)
    net2 = ip_network(f'165.112.175.80/{mask}', 0)
    if net1 == net2:
        RES.append(mask)
print(max(RES))
'''


# https://stepik.org/lesson/1038700/step/10?unit=1062785
'''
from ipaddress import *
RES = []
for mask in range(32+1):
    net1 = ip_network(f'10.96.180.231/{mask}', 0)
    net2 = ip_network(f'10.96.140.118/{mask}', 0)
    if net1 != net2:
        RES.append(32 - mask)
print(max(RES))
'''


# https://stepik.org/lesson/1038700/step/15?unit=1062785
'''
from ipaddress import *
net = ip_network('185.8.0.0/255.255.128.0', 0)
RES = []
for ip in net:
    s = f'{ip:b}'
    RES.append(s.count('1'))
print(max(RES))
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 23561 Пересдача 03.07.25 (Уровень: Базовый)
# Для какого наибольшего натурального числа А выражение
# ДЕЛ(х,128) → (¬ДЕЛ(х,А) → ¬ДЕЛ(х,80))
# истинно (т.е. принимает значение 1) при любом натуральном значении переменной х?
'''
# Вариант 1
def F(x, A):
    return (x % 128 == 0) <= ((x % A != 0) <= (x % 80 != 0))

RES = []
for A in range(1, 5000):
    flag = True
    for x in range(1, 10000):
        if F(x, A) == False:
            flag = False
            break
    if flag == True:
        RES.append(A)
print(max(RES))


# Вариант 2
def F(x, A):
    return (x % 128 == 0) <= ((x % A != 0) <= (x % 80 != 0))

RES = []
for A in range(1, 5000):
    cnt = 0
    for x in range(1, 10000):
        if F(x, A) == True:
            cnt += 1
    if cnt == 9999:
        RES.append(A)
print(max(RES))


# Вариант 3
def F(x, A):
    return (x % 128 == 0) <= ((x % A != 0) <= (x % 80 != 0))

RES = []
for A in range(1, 5000):
    if all(F(x, A) for x in range(1, 10000)):
        RES.append(A)
print(max(RES))

# Вариант 4
print(max([A for A in range(1, 5000) if all( ((x % 128 == 0) <= ((x % A != 0) <= (x % 80 != 0))) for x in range(1, 10000))]))
'''


# № 23374 Резервный день 19.06.25 (Уровень: Базовый)
# Для какого наименьшего целого положительного числа А выражение
# (x<A) ∧ (y<3A) ∨ (2x+y>128)
# истинно (т.е. принимает значение 1) при любых целых положительных х и у?
'''
def F(x, y, A):
    return (x < A) and (y < 3*A) or (2*x + y > 128)

RES = []
for A in range(1, 5000):
    if all(F(x, y, A) for x in range(1, 100) for y in range(1, 100)):
        RES.append(A)
print(min(RES))
'''


# № 20823 (Уровень: Базовый)
# Найдите минимальное натуральное значение А, при котором значение выражения
# (x&A=0)→((x&77=0)∧(x&44=0))
'''
def F(x, A):
    return (x & A == 0) <= ((x & 77 == 0) and (x & 44 == 0))

RES = []
for A in range(1, 5000):
    if all(F(x, A) for x in range(1, 10000)):
        RES.append(A)
print(min(RES))
'''

# № 20584 (Уровень: Базовый)
# Для какого наименьшего натурального числа А формула
# (ДЕЛ(405,x)→ДЕЛ(81,x)) ∨ (A–x>162)
# тождественно истинна (то есть принимает значение 1 при любом натуральном значении переменной х)?
'''
def F(x, A):
    return ((405 % x== 0) <= (81 % x== 0)) or (A - x >162)

RES = []
for A in range(1, 5000):
    if all(F(x, A) for x in range(1, 10000)):
        RES.append(A)
print(min(RES))
'''


# Софья
# № 20580 (Уровень: Базовый)
# (М. Попков) Для какого наибольшего натурального значения A выражение
# (9x + y > A) ∨ (x ≥ 36) ∨ (y ≥ 18)
# тождественно истинно для любых положительных и целых x и y? В ответ запишите целое число – значение A.
'''
def F(x, y, A):
    return ((9 * x + y) > A) or (x >= 36 ) or (y >= 18)

RES = []
for A in range(1, 5000):
    if all(F(x, y, A) for x in range(1, 100) for y in range(1, 100)):
        RES.append(A)
print(max(RES))
'''

# № 20809 Апробация 05.03.25 (Уровень: Базовый)
# Пусть на числовой прямой дан отрезок B = [60,80].
# Для какого наибольшего натурального числа А логическое выражение
# ДЕЛ(x,А) ∨ ((x∈B) → ¬ДЕЛ(x,22))
# истинно (т.е. принимает значение 1) при любом целом положительном значении переменной х?
'''
def F(x, A):
    B = 60 <= x <= 80  # (x∈B)
    return (x % A == 0) or ((B) <= (x % 22 != 0))

RES = []
for A in range(1, 5000):
    if all(F(x, A) for x in range(1, 10000)):
        RES.append(A)
print(max(RES))
'''


# № 20905 Апробация 05.03.25 (Уровень: Базовый)
# На числовой прямой даны два отрезка: P = [17; 58] и Q = [29; 80].
# Укажите наименьшую возможную длину такого отрезка A, что логическое выражение
# (x∈P)→(((x∈Q)∧¬(x∈A))→¬(x∈P))
#  истинно (т.е. принимает значение 1) при любом значении переменной х.
'''
def F(x, a1, a2):
    P = 17 <= x <= 58
    Q = 29 <= x <= 80
    A = a1 <= x <= a2
    return (P) <= (((Q) and (not A)) <= (not P))


RES = []
M = [x / 5 for x in range(10 * 5, 100 * 5)]
print(M)
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            RES.append(a2 - a1)
print(min(RES))  # 29.0 -> 29
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 13, 14, 15]
# КЕГЭ = []
# на следующем уроке:
