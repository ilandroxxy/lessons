# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# https://education.yandex.ru/ege/inf/task/bfdcf7a3-606f-4e4d-ac7e-3a26594a79a2
'''
def F(x, A):
    B = 160 <= x <= 180
    return B <= ((x % 35 == 0) <= (x % A == 0))

for A in range(1, 5000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
'''


# https://education.yandex.ru/ege/inf/task/055dd302-c963-4b41-aae6-b931c4708fa9
'''
def F(x, A):
    B = 50 <= x <= 70
    return (x % A == 0) or ((B) <= (x % 21 != 0))


for A in range(1, 50000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
'''

# https://education.yandex.ru/ege/inf/task/fd0c928b-5f41-4a18-acf2-75a6503fe8df
'''
def F(x, A):
    B = 50 <= x <= 70
    return (x % A == 0) or ((x % 23 == 0) <= (not B) )

for A in range(1, 5000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
'''

# https://education.yandex.ru/ege/inf/task/2726d97c-4a83-470a-be75-341f5fa1c65c
'''
def F(x, A):
    return ((x & 42 != 0) and (x & 34 == 0)) <= (x & A != 0)

for A in range(0, 10000):
    if all(F(x, A) for x in range(0, 10000)):
        print(A)
        break
'''

# https://education.yandex.ru/ege/inf/task/6a427e57-e7bf-417e-a0b0-caac3d5585ec
'''
def F(x, A):
    return (x & 52 == 4) <= ((x & 26 == 2) <= (x & A == 6))

for A in range(0, 5000):
    if all(F(x, A) for x in range(0, 10000)):
        print(A)
'''

# https://education.yandex.ru/ege/inf/task/5ed718bc-b630-46ba-b08b-581549fab275
'''
def F(x, A):
    return ((x & 103 == 0) and (x & 94 != 0)) <= (x & A != 0)


for A in range(1, 10000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
        break
'''


# https://education.yandex.ru/ege/inf/task/8f13d075-e784-4654-ae10-7d109cee90e9
'''
def F(x, y, A):
    return (3*x + y > A) and (y < x) and (x < 30)

for A in range(0, 10000):
    if all(F(x, y, A) == False for x in range(0, 100) for y in range(0, 100)):
        print(A)
        break
'''

# https://education.yandex.ru/ege/inf/task/fd0de4d6-16b4-46bd-a500-5283d78def62
'''
def F(x, y, A):
    return(x * y > A) or (x > y) or (8 > x)

for A in range(0, 1000):
    if all(F(x, y, A) for x in range(0, 100) for y in range(0, 100)):
        print(A)
'''

# https://education.yandex.ru/ege/inf/task/f71d47a8-80ff-416b-97f5-2b76ec1022cc
'''
def f(x, y, a):
    return (x >= 15) or (a > (x * y)) or (y > 3)


for a in range(0, 5000):
    if all(f(x, y, a) for x in range(0, 100) for y in range(0, 100)):
        print(a)
        break
'''

# https://education.yandex.ru/ege/inf/task/219c0d8e-bf34-4ec2-8f11-cf4d06a6fae7

def F(x, a1, a2):
    P = 15 <= x <= 40
    Q = 21 <= x <= 63
    A = a1 <= x <= a2
    return (not P) <= (((Q) and (not A)) <= (P))

R = []
M = [x / 10 for x in range(5 * 10, 80 * 10)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(min(R))  # 22.75 -> 22.799 ->



# https://education.yandex.ru/ege/inf/task/ad49b4d3-62dc-420f-aa97-519d891a80f5
'''
def F(x, a1, a2):
    P = 20 <= x <= 67
    Q = 33 <= x <= 98
    A = a1 <= x <= a2
    return (P) <= (((Q) and (not A)) <= (not P))

R = []
M = [x / 4 for x in range(5 * 4, 80 * 4)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(min(R))
'''

# https://education.yandex.ru/ege/inf/task/64eaf0ef-e15b-40b9-b5d4-d21fb7bc925c
'''
def F(x, a1, a2):
    P = 7 <= x <= 16
    Q = 25 <= x <= 32
    A = a1 <= x <= a2
    return ((P) <= (A)) or ((not Q) <= (A))

R = []
M = [x / 4 for x in range(5 * 4, 40 * 4)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2-a1)
print(min(R))
'''

# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 25, 27.1]
# КЕГЭ = [3, 5, 7, 8, 9, 12, 14, 15, 16, 17, 18, 19-21, 23, 25]
# на следующем уроке: 17, 22 номер


# region 📖 Пробник (Вариант 2)

# Студент #Влад
# Дата: #Четверг #12Марта2026
# ✅ Верно: 1, 2, 3, 4, 10, 14, 16, 18, 19, 20, 21, 23
# ⛔️ Неверно: 6, 7, 8
# ❔ Без ответа: 5, 9, 11, 12, 13, 15, 17, 22, 24, 25, 26, 27
# Итог: 12/29 первичных балла ~ 56 вторичных

# endregion 📖 Пробник (Вариант 2)
