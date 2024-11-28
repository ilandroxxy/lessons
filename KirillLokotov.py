# region Домашка: ************************************************************


# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************

# Задание 25 https://education.yandex.ru/ege/task/4c423ac1-ef41-4eba-b73c-f8f714df7cd5
# Найдите среди натуральных чисел, не превышающих 10**10,
# все числа, которые соответствуют маске 7?2*4??9?
# и делятся на 96437 без остатка.
'''
from fnmatch import *

for x in range(96437, 10**10+1, 96437):
    if fnmatch(str(x), '7?2*4??9'):
        print(x, x // 96437)
'''


# Задание 25 https://education.yandex.ru/ege/task/6afeb600-dd0b-4fc3-8585-846136911c1e
'''
from fnmatch import *

for x in range(31, 10**9+1, 31):
    if fnmatch(str(x), '12345?7?8'):
        print(x, x // 31)
'''


# Задание 25 https://education.yandex.ru/ege/task/e63ff042-e377-4101-96a1-4cc4d5ba7be0
'''
from fnmatch import *


for x in range(53191, 10**10+1, 53191):
    if fnmatch(str(x), '?136*'):
        if str(x)[0] in '02468':
            if str(x)[-1] in '13579':
                print(x, x // 53191)
'''


# Задание 25 https://education.yandex.ru/ege/task/a7d40d31-e448-4fe4-bcbd-6fb94af87a43
'''
from fnmatch import *

cnt = 0
for x in range(700_000+1, 10**10):
    if x % 13 == 0:
        if not fnmatch(str(x), '*0?3*'):
            if not fnmatch(str(x), '*4?2'):
                if not fnmatch(str(x), '*1*'):
                    summa = sum([int(i) for i in str(x)])
                    print(x, summa)
                    cnt += 1
                    if cnt == 5:
                        break
'''


# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 13, 14, 25]
# КЕГЭ = []
# на следующем уроке:
