# region Домашка: ******************************************************************


# https://stepik.org/lesson/1038816/step/3?unit=1062780
'''
from fnmatch import *

k = 0
for x in range(700000, 1000000000):
    if x % 13 == 0:
        if not fnmatch(str(x), '*0??3*') and not fnmatch(str(x), '*4??2') and not fnmatch(str(x), '*1*'):
            summa = sum([int(i) for i in str(x)])
            print(x, summa)
            k = k + 1
            if k == 5:
                break
'''


# https://stepik.org/lesson/1038816/step/8?unit=1062780
'''
k = 0
for x in range(320_401, 10**10):
    # if x % 10 == 0 and x % 12 == 0 and x % 14 == 0 and x % 16 == 0 and x % 18 == 0:
    if all(x % j == 0 for j in [10, 12, 14, 16, 18]):
        print(x, x // 18)
        k = k + 1
        if k == 5:
            break
'''


'''
from fnmatch import *

R = []
for x in range(11071, 10 ** 10, 11071):
    if fnmatch(str(x), '?136*1'):
        if str(x)[0] in '13579' and str(x)[-2] in '02468':
            R.append([x, x // 11071])

print(*R[-5])
print(*R[-4])
print(*R[-3])
print(*R[-2])
print(*R[-1])
'''

# https://stepik.org/lesson/1038816/step/13?unit=1062780
'''
from fnmatch import *

for x in range(21, 10 ** 8, 21):
    if fnmatch(str(x), '1*5*9'):
        if len(set(str(x))) == len(str(x)):
            if sorted(str(x)) == list(str(x)):
                print(x, x // 21)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


'''
import time
start = time.time()

"""
def divisors(x):  
    div = []
    for j in range(1, x+1):
        if x % j == 0:
            div.append(j)
    return div
"""


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

print(time.time() - start)  # 2.901639 -> 0.0003
'''

# https://education.yandex.ru/ege/task/f057cfef-606b-4010-8258-037b3517a524
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):  # не считая единицы и самого числа.
        if x % j == 0:
            div.append(j)
            div.append(x // j)
    return sorted(set(div))


k = 0
for x in range(424_242+1, 10**10):
    d = divisors(x)
    if len(d) >= 2:
        M = max(d) + min(d)
        if M % 2024 == 42:
            print(x, M)
            k = k + 1
            if k == 8:
                break
'''


# https://education.yandex.ru/ege/task/41a06b51-e4e0-4204-b3ac-432f00e2ac2c
'''
def divisors(x):
    div = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            div.append(j)
            div.append(x // j)
    return sorted(set(div))


for x in range(977_004, 977_022+1):
    d = [j for j in divisors(x) if j % 2 == 0]
    if len(d) >= 6:
        print(x, d[-2])
'''

# endregion Урок: ********************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 14, 25]
# КЕГЭ  = []
# на следующем уроке:
