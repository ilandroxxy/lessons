# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

"""
import time
start = time.time()

'''
def divisors(x):
    div = []
    for j in range(1, x+1):
        if x % j == 0:
            div.append(j)
    return div
'''

def divisors(x):
    div = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x//j]
    return sorted(set(div))

print(divisors(100_000_000))

print(time.time() - start)
"""

'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x//j]
    return sorted(set(div))


k = 0
for x in range(600_001, 10**10):
    d = [i for i in divisors(x) if i % 10 == 7 and i != 7]
    if len(d) > 0:
        print(x, min(d))
        k += 1
        if k == 5:
            break
'''
# 600001 437
# 600002 47
# 600003 1227
# 600005 217
# 600012 16667

'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x//j]
    return sorted(set(div))


k = 0
for x in range(700_001, 10**10):
    d = divisors(x)
    if len(d) > 0:
        M = min(d) + max(d)
        if M % 10 == 8:
            print(x, M)
            k += 1
            if k == 5:
                break
'''
# 700005 233338
# 700007 100008
# 700012 350008
# 700015 140008
# 700031 24168


from functools import *
lru_cache(None)
def divisors(x):
    div = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x//j]
    return sorted(set(div))


for x in range(35_000_000, 40_000_000+1):
    n = [i for i in divisors(x) if i % 2 != 0]
    if len(n) == 5:
        print(x)

# endregion Урок: ******************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ= [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ  = [5, 8, 9, 14, 17]
# на следующем уроке: 22 и 24 с новых вариантов и 25 номер на отрезки.
