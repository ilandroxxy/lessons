# region Домашка: ******************************************************************


# Поменяй местами
# https://stepik.org/lesson/1309452/step/7?unit=1324568
'''
L = [3, 7, 1, 4, 9, 2]
# L[0], L[-1] = 2, 3
# L[0], L[-1] = L[-1], L[0]
L = [2] + L[1:-1] + [3]
print(L)

s = '371492'
s = '2' + s[1:-1] + '3'
print(s)
'''


'''
M = [5]
print(M[0], M[-1])
# print(M[1])  # IndexError: list index out of range
'''


# Вычисли всё!
# https://stepik.org/lesson/1309452/step/12?unit=1324568
'''
from math import prod
n = int(input())
N = [int(x) for x in str(n)]
print(N.count(2))
print(N.count(N[-1]))
nechet = [x for x in N if x % 2 == 1]
print(len(nechet))
N7 = [x for x in N if x > 7]
# print(x)  # NameError: name 'x' is not defined
print(sum(N7))
if len(N7) == 0:
    print(11)
elif len(N7) == 1:
    print(N[0])
else:
    # total = 1
    # for x in N7:
    #     total *= x
    # print(total)
    print(prod(N7))
print(N.count(0) + N.count(4))
'''


# Уникальные элементы списка
# https://stepik.org/lesson/1309452/step/13?unit=1324568
'''
cnt = 0
M = [int(input()) for _ in range(int(input()))]

for x in M:
    if M.count(x) == 1:
        print(x)
        cnt += 1
if cnt == 0:
    print("Уникальных элементов нет")
'''

'''
n = int(input())
M = []
for i in range(n):
    x = int(input())
    M.append(x)
print(M)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# ЗАМЕНИТЬ == REPLACE
'''
s = '12321312321'
s = s.replace('2', '*')  # Заменили сразу все '2' на '*'
print(s)  # 1*3*131*3*1

s = s.replace('*', '2', 2)  # Заменил только первые два '*' на '2'
print(s)  # 1232131*3*1
'''

# Задание 12 https://education.yandex.ru/ege/task/3e23287d-ebe2-440d-9074-8cb7e8ea7fff

# ПОКА нашлось (2222) ИЛИ нашлось (7777)
#   ЕСЛИ нашлось (2222)
#     ТО заменить (2222, 77)
#   ИНАЧЕ заменить (7777, 22)
'''
s = '7' * 47
while '2222' in s or '7777' in s:
    if '2222' in s:
        s = s.replace('2222', '77', 1)
    else:
        s = s.replace('7777', '22', 1)
print(s)
'''


# Сумма цифр в строке
'''
s = '12345'
summa = 0
for x in s:
    summa += int(x)
print(summa)

summa = sum([int(x) for x in s])
'''

# Задание 12 https://education.yandex.ru/ege/task/ca477eb1-a007-4507-af8f-2b8563ac91c6
'''
for m in range(1, 1000):
    s = '4' + '6' * m

    while '46' in s or '666' in s:
        if '46' in s:
            s = s.replace('46', '5', 1)
        if '666' in s:
            s = s.replace('666', '4', 1)
    summa = sum([int(x) for x in s])
    if summa > 1000:
        print(m)
        break
'''


# Задание 12 https://education.yandex.ru/ege/task/b4a679ec-66a8-4068-bcb5-9b8c2c599e5c
'''
for n in range(1, 1000):
    s = '5' * n

    while '34' in s or '55' in s:
        if '34' in s:
            s = s.replace('34', '54321', 1)
        else:
            if '55' in s:
                s = s.replace('55', '234', 1)

    if 1000 <= len(s) <= 9999:
        print(n)
        break
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 6, 12]
# КЕГЭ  = []
# на следующем уроке:
