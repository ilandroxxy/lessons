# region Домашка: ******************************************************************

# https://stepik.org/lesson/1038706/step/12?unit=1062774
'''
def F(x,A):
    return (x & 39 == 0) or ((x & 11 == 0) <= (x & A !=0))

for A in range(0, 1000):
    if all(F(x,A)for x in range (0,10000)):
        print(A)
        break
'''


# https://education.yandex.ru/ege/inf/task/237b7023-9d4e-4268-a733-b7e1d23ff11b



# Номер 23
# Прибавить 1
# Прибавить 2
# Умножить на 3
# Сколько существует программ, для которых при исходном
# числе 4 результатом является число 22
# и при этом траектория вычислений содержит число 10,
# но не содержит число 20?
'''
def F(a, b):
    if a > b or a == 20:
        return 0
    elif a == b:
        return 1
    else:
        return F(a+1, b) + F(a+2, b) + F(a*3, b)

print(F(4, 10) * F(10, 22))

# Вариант 2
def F(a, b):
    if a >= b or a == 20:
        return a == b
    return F(a+1, b) + F(a+2, b) + F(a*3, b)

print(F(4, 10) * F(10, 22))
'''

# № 23761 Демоверсия 2026 (Уровень: Базовый)
'''
def F(a, b):
    if a <= b or a == 7:
        return a == b
    return F(a-1, b) + F(a-4, b) + F(a//3, b)

print(F(19, 13) * F(13, 2))
'''


# № 19883 (Уровень: Средний)
'''
def F(a, b):
    if a <= b or a == 24:
        return a == b
    return F(a-1, b) + F(int(a**0.5), b) + F(a//10, b)

print(F(602, 7))
'''


# № 19784 (Уровень: Базовый)
'''
def F(a, b):
    if a <= b or a == 28:
        return a == b
    h = [F(a-2, b)]
    if a % 2 == 0:
        h += [F(a//2, b)]
    else:
        h += [F(a-3, b)]
    return sum(h)

print(F(98, 1))

# Вариант 2
def F(a, b):
    if a <= b or a == 28:
        return a == b
    return F(a-2, b) + F(a // 2 if a % 2 == 0 else a - 3, b)

print(F(98, 1))
'''


# № 7011 (Уровень: Средний)
'''
def F(a, b, c):
    if a >= b or a == 28:
        return a == b and 'BACA' not in c
    return F(a+2, b, c+'A') + F(a+3, b, c+'B') + F(a*2, b, c+'C')

print(F(2, 40, ''))
'''


# 16387
'''
def F(a, b):
    if a > b or a == 16:
        return 0
    elif a == b:
        return 1
    else:
        return F(a + 1, b) + F(a + 2, b) + F(a * 3, b)
print (F(2, 9) * F(9, 18))
'''

# 17534
'''
def F(a, b):
    if a < b:
        return 0
    elif a == b:
         return 1
    else:
        return F(a - 1, b) + F(a // 2, b)
print (F(30, 8) * F(8, 1))
'''


# № 17562 Основная волна 08.06.24 (Уровень: Базовый)
'''
def F(a, b):
    if a > b:
        return 0
    elif a == b:
        return 1
    else:
        return F(a + 1, b) + F(a + 2, b) + F(a + 3, b)


print(F(5, 7) * F(7, 11))
'''

# № 16332 Открытый вариант 2024 (Уровень: Базовый)
'''
def F(a ,b):
    if a > b:
        return 0
    elif a == b:
        return 1
    else:
        return F(a +1,b) + F(a +2,b) + F(a * 2,b)

print(F(4, 11) * F(11, 13) * F(13, 15))
'''


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 13, 14, 15, 23]
# КЕГЭ = []
# на следующем уроке: 16, 19-21
