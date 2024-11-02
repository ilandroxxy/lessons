# region Домашка: ************************************************************


# endregion Домашка: *********************************************************
#
# #
# region Урок: ************************************************************

'''
def my_sqrt(n):
    return n ** (1/2)  # return - Возвращает значение функции


import math
print(math.sqrt(16))  # print() - Выводит результат в консоль

print(my_sqrt(16))

x = my_sqrt(16)  # Мы вернули значение функции и положили его в переменную
print(x)
'''


# Тип 16 №5650
'''
def F(n):
    if n <= 2:
        return n + 1
    if n > 2:
        return F(n - 1) + 2 * F(n - 2)


print(F(4))  # 13
'''


# Тип 16 №6234
'''
def F(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2:
        return F(n - 2) * (n + 1)

print(F(8))
'''


# Тип 16 №59809
'''
import sys
sys.setrecursionlimit(2024)

def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n - 2 + F(n - 1)


print(F(2023) - F(2021))  # 4041
# [Previous line repeated 996 more times]
# RecursionError: maximum recursion depth exceeded

# F(2023) = 2021 + F(2022)
# F(2022) = 2020 + F(2021) - F(2021)
print(2021 + 2020)  # 4041
'''


# Тип 16 №6779
'''
def F(n):
    if n == 1:
        return 1
    if n >= 2:
        return F(n - 1) - G(n - 1)

def G(n):
    if n == 1:
        return 1
    if n >= 2:
        return F(n - 1) + G(n - 1)

print(F(5) / G(5))
'''

'''
def F(n):
    if n == 0:
        return 0
    if n % 2 == 0 and n > 0:
        return F(n / 2)
    if n % 2 != 0:
        return F(n - 1) + 1

cnt = 0
for x in range(1, 500+1):
    if F(x) == 3:
        cnt += 1
print(cnt)
'''

def F(n):
    if n >= 2025:
        return n
    if n < 2025:
        return n + 3 + F(n + 3)

print(F(23) - F(21))


# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# ФИПИ = [2, 5, 6, 8, 12, 13, 14, 16, 23, 25]
# КЕГЭ = []
# на следующем уроке:
