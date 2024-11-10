# region Домашка: ************************************************************


# № 2588 (Уровень: Базовый)
# https://stepik.org/lesson/1038816/step/4?unit=1062780
'''
def Divisors(x):
    div = []
    for j in range(1, int(x ** 0.5) + 1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


for x in range(190201, 190260+1):
    d = [j for j in Divisors(x) if j % 2 == 0]
    if len(d) == 4:
        print(d[-1], d[-2])
'''

# endregion Домашка: *********************************************************
# #
# #
# region Урок: ************************************************************

# Задание 23 https://education.yandex.ru/ege/task/7f35c6c9-51a5-4f54-bd42-92f9c15ff6af
# У исполнителя есть три команды, которым присвоены номера:
# Прибавить 1.
# Умножить на 2.
# Умножить на 3.

# Сколько существует программ, для которых при исходном числе 5
# результатом является число 43 и при этом траектория вычислений
# содержит число 9, но не содержит число 27?
'''
def F(a, b):
    if a > b or a == 27:
        return 0
    elif a == b:
        return 1
    else:
        return F(a+1, b) + F(a*2, b) + F(a*3, b)


print(F(5, 9) * F(9, 43))


# Вариант 2

def F(a, b):
    if a >= b or a == 27:
        return a == b
    return F(a+1, b) + F(a*2, b) + F(a*3, b)


print(F(5, 9) * F(9, 43))
'''

# Задание 23 https://education.yandex.ru/ege/task/b8155274-0c96-4bba-8ddf-1bee1dfc3089
'''
def F(a, b):
    if a > b or a == 33:
        return 0
    elif a == b:
        return 1
    else:
        return F(a+1, b) + F(a*2, b) + F(a**2, b)


print(F(8, 32) * F(32, 115))
'''

# Задание 23 https://education.yandex.ru/ege/task/d9374490-081c-4364-a252-892cfab6da66
'''
def F(a, b):
    if a < b:
        return 0
    elif a == b:
        return 1
    else:
        return F(a-2, b) + F(a-5, b)

print(F(24, 3))
'''

# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# ФИПИ = [2, 5, 6, 8, 12, 13, 14, 16, 23, 25]
# КЕГЭ = []
# на следующем уроке:
