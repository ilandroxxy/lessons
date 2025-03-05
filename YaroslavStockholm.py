# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 17562 Основная волна 08.06.24 (Уровень: Базовый)
# У исполнителя есть три команды, которым присвоены номера:
# A. Прибавить 1
# B. Прибавить 2
# C. Прибавить 3
# Сколько существует программ, которые преобразуют число 5 в число 11,
# и при этом траектория вычислений содержит число 7?

# 5 -> 7 -> 11  (+1 +2 +3)
'''
# a - старт, b - конец
def F(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    else:
        return F(a+1, b) + F(a+2, b) + F(a+3, b)

print(F(5, 7) * F(7, 11))

# Вариант 2
def F(a, b):
    if a >= b:
        return a == b
    return F(a+1, b) + F(a+2, b) + F(a+3, b)

print(F(5, 7) * F(7, 11))
'''


# № 17534 Основная волна 07.06.24 (Уровень: Базовый)
# У исполнителя есть две команды:
# A. Вычти 1
# B. Найти целую часть от деления на 2
# Сколько существует программ, для которых при исходном числе 30
# результатом является число 1
# и при этом тракетория вычислений содержит число 8?
'''
def F(a, b):
    if a <= b:
        return a == b
    return F(a-1, b) + F(a // 2, b)

print(F(30, 8) * F(8, 1))
'''


# № 18047 (Уровень: Базовый)
# А. Вычесть 2
# В. Вычесть 3
# С. Найти целую часть от деления на 4
# Сколько существует программ, для которых при исходном
# числе 36 результатом является число 13,
# при этом траектория вычислений не содержит числа 24?
'''
def F(a, b):
    if a <= b or a == 24:  # не содержит числа 24
        return a == b
    return F(a-2, b) + F(a-3, b) + F(a//4, b)

print(F(36, 13))
'''


# № 18267 (Уровень: Средний)
# А. Прибавить 2
# В. Прибавить 5
# С. Возвести в квадрат
# Сколько существует программ, для которых при исходном числе 4 результатом
# является число 36, при этом последняя в них команда — не C?

def F(a, b, c: str):
    if a >= b:
        print(c, a == b)  # CBBBAC 4**2 + 5 + 5 + 5 + 2 **2
        return a == b and c[-1] != 'C'
        # return a == b and c[-1] in 'AB'
    return F(a+2, b, c+'A') + F(a+5, b, c+'B') + F(a**2, b, c+'C')


print(F(4, 36, ''))

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 10, 12, 13, 14, 15, 16, 23, 25]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Женя 5/7 -> 34 вторичных баллов +[2, 5, 8, 12, 14] -[6, 10]
# Ярослав 2/7 -> 14 вторичных баллов +[2, 12] -[5, 6, 8, 10, 14]

# Второй пробник 28.02.25:
# Женя 9/29 -> 48 вторичных баллов +[2, 5, 6, 10, 13, 14, 16, 23, 25] -[8, 12]
# Ярослав 10/29 -> 51 вторичных баллов +[2, 5, 6, 10, 12, 13, 14, 15, 16, 23] -[25]
