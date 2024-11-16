# region Домашка: ************************************************************

# https://stepik.org/lesson/1038816/step/3?unit=1062780
'''
from fnmatch import *

count = 0
for x in range(700000, 1000000):
    if fnmatch(str(x), '*0??3*') or fnmatch(str(x), '*4??2') or fnmatch(str(x), '*1*'):
        continue
    if x % 13 == 0:
        count += 1
        # summa = sum([int(i) for i in str(x)])
        print(map(int, str(x)))  # <map object at 0x104250dc0>
        print(list(map(int, str(x))))  # [7, 0, 0, 2, 0, 6]
        summa = sum(map(int, str(x)))
        print(x, summa)
        if count == 5:
            break
'''


'''
from fnmatch import *

count = 0
for x in range(700011, 1000000, 13):
    if not fnmatch(str(x), '*0??3*'):
        if not fnmatch(str(x), '*4??2'):
            if not fnmatch(str(x), '*1*'):
                summa = sum([int(i) for i in str(x)])
                count += 1
                print(x, summa)
                if count == 5:
                    break
'''


# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************


# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************

# todo Решить и поправить Степик № 11953 (Уровень: Средний) +++
'''
from functools import lru_cache


@lru_cache(None)
def F(a, b):

    if a >= b or a == 100:
        return a == b

    count = 0

    x = a % 10  # Команда A: Прибавить последнюю цифру
    if x != 0:
        count += F(a + x, b)

    x = a % 68   # Команда B: Добавить остаток от деления на 68
    if x != 0:
        count += F(a + x, b)

    x = a ** 2   # Команда C: Возвести в квадрат
    if x != a:
        count += F(x, b)

    return count


print(F(2, 68) * F(68, 680))
'''
# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3?, 4, 5, 6, 7?, 8, 9, 10?, 11?, 12, 14, 15, 16, 17, 19-21?, 23, 25]
# КЕГЭ = []
# на следующем уроке:
