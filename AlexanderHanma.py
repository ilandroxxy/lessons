# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# print(int('23534252', 37))
# ValueError: int() base must be >= 2 and <= 36, or 0

for i, x in enumerate(['a', 'b', 'c', 'd', 'e'], 1 ):
    print(i, x)
    # 1 a
    # 2 b
    # 3 c
    # 4 d
    # 5 e

# Функция перевода из любой системы счисления в 10-ю
'''
def my_int(L: list, b: int):  # L - число в виде списка в b-й системе счисления
    return sum(x * b ** i for i, x in enumerate(L[::-1], 0))


print(int('1000', 2))  # 8
print(my_int([1, 0, 0, 0], 2))  # 8
'''


# № 18616 (Уровень: Средний)
'''
def my_int(L, b: int):
    return sum(x * b ** i for i, x in enumerate(L[::-1], 0))


for x in range(0, 37):
    A = my_int([12, 5, 9, x, 11, 10, 9, 8, 15], 37)
    B = my_int([14, 3, x, 5, 13, 10, 9, 12, 6], 37)
    if (A * B) % 36 == 0:
        print(x, my_int([2, x, 1], 37))
'''



# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке:
