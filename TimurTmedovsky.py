# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Задание 25 https://education.yandex.ru/ege/task/4c423ac1-ef41-4eba-b73c-f8f714df7cd5
'''
from fnmatch import *
for x in range(96437, 10**10, 96437):
    if fnmatch(str(x), '7?2*4??9?'):
        print(x, x // 96437)
'''


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

'''
def divisors(x):
    div = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            div.append(j)
            div.append(x // j)
    return sorted(set(div))


print(divisors(24))  # [1, 2, 3, 4, 6, 8, 12, 24]
print(divisors(16))  # [1, 2, 4, 8, 16]
print(divisors(100_000_000))

print(time.time() - start)  # 2.9304 -> 0.00036
'''

# https://education.yandex.ru/ege/task/26295a68-9546-4dd9-87ca-c8f32bd7a755
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):  # не считая самого числа.
        if x % j == 0:
            div.append(j)
            div.append(x // j)
    return sorted(set(div))


for x in range(114578, 114616+1):
    d = [j for j in divisors(x) if j % 10 == 8]
    R = sum(d)
    if R % 10 == 6:
        print(x, R)
'''


# https://education.yandex.ru/ege/task/e63ff042-e377-4101-96a1-4cc4d5ba7be0


from fnmatch import  *
for x in range(53191, 10**10, 53191):
    if fnmatch(str(x), '?136*'):
        if str(x)[0] in '02468':
            if str(x)[-1] in '13579':
                print(x, x // 53191)

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 13, 14, 25]
# КЕГЭ  = []
# на следующем уроке:
