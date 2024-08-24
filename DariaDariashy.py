# region Домашка: ******************************************************************

# КЕГЭ № 8602 (Уровень: Базовый)
'''
s = sorted('АЕКНС')
num = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for g in s:
                        slovo = a + b + c + d + e + g
                        num += 1
                        if slovo == 'СЕНЕКА':
                            print(num)


from itertools import product
num = 0
for p in product(sorted('АЕКНС'), repeat=6):
    slovo = ''.join(p)
    num += 1
    if slovo == 'СЕНЕКА':
        print(num)


from itertools import product
for num, p in enumerate(product(sorted('АЕКНС'), repeat=6), 1):
    slovo = ''.join(p)
    if slovo == 'СЕНЕКА':
        print(num)
'''

'''
M = [x for x in range(10)]
print(M)

M = [x ** 2 for x in range(10)]
print(M)

M = [x for x in range(10) if x % 2 == 0]
print(M)
'''

# print('РСЛВ' == 'СРЛВ')   # False


# КЕГЭ № 8417 (Уровень: Базовый)
'''
s = 'ЯРОСЛАВ'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    if len(slovo) == len(set(slovo)):  # буквы в коде не должны повторяться
                        sogl = [x for x in slovo if x in 'РСЛВ']
                        glas = [x for x in slovo if x in 'ЯОА']
                        if len(sogl) > len(glas):
                            slovo = slovo.replace('Я', 'А').replace('О', 'А')
                            if 'АА' not in slovo:
                                cnt += 1
print(cnt)

from itertools import permutations
cnt = 0
for p in permutations('ЯРОСЛАВ', 5):
    slovo = ''.join(p)
    sogl = [x for x in slovo if x in 'РСЛВ']
    glas = [x for x in slovo if x in 'ЯОА']
    if len(sogl) > len(glas):
        slovo = slovo.replace('Я', 'А').replace('О', 'А')
        if 'АА' not in slovo:
            cnt += 1
print(cnt)
'''


# КЕГЭ № 17627 Основная волна 19.06.24 (Уровень: Базовый)
#
# Определите количество 15-ричных пятизначных чисел, в записи которых ровно одна цифра 8
# и не менее двух цифр с числовым значением, превышающим 9.
'''
s = '0123456789ABCDE'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    n = a + b + c + d + e
                    if n[0] != '0':  # if a != '0':
                        if n.count('8') == 1:
                            if len([x for x in n if x > '9']) >= 2:
                                cnt += 1
print(cnt)


from itertools import *
cnt = 0
for p in product('0123456789ABCDE', repeat=5):
    n = ''.join(p)
    if n[0] != '0':
        if n.count('8') == 1:
            if len([x for x in n if x > '9']) >= 2:
                cnt += 1
print(cnt)
'''
# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Тип 6 №47210
# В начальный момент Черепаха находится в начале координат,
# её голова направлена вдоль положительного направления
# оси ординат, хвост опущен.

# Черепахе был дан для исполнения следующий алгоритм:
# Повтори 7 [Вперёд 10 Направо 120].
#
# Определите, сколько точек с целочисленными координатами
# будут находиться внутри области, ограниченной линией,
# заданной данным алгоритмом.
# Точки на линии учитывать не следует.
'''
import turtle as t
t.tracer(0)  # Отключает анимацию - мгновенная отрисовка картинки
t.left(90)
l = 40

for i in range(7):
    t.forward(10 * l)
    t.right(120)

t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x*l, y*l)
        t.dot(3, 'red')

t.update()
t.done()
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 8, 12, 13, 14]
# КЕГЭ  = []
# на следующем уроке:
