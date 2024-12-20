# region Домашка: ******************************************************************

# № 17547 Основная волна 08.06.24 (Уровень: Средний)
'''
import turtle as t
t.left(90)
t.tracer(0)
t.screensize(-2000, 2000)
size = 20

# тут будет псевдокод
for i in range(3):
    t.forward(7 * size)
    t.right(90)
    t.forward(12 * size)
    t.right(90)
t.up()
t.forward(4 * size)
t.right(90)
t.forward(6 * size)
t.left(90)
t.down()
for i in range(4):
    t.forward(83 * size)
    t.right(90)
    t.forward(77 * size)
    t.right(90)

t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * size, y * size)
        t.dot(3, 'red')

t.update()
t.done()
'''
# print(8*13 + 84*78 - 4*7)


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
from itertools import *
n = 0
for p in product(sorted('КОДИМ'), repeat=5):
    word = ''.join(p)
    n += 1
    if word.count('М') == 2 and 'ММ' not in word:
        print(n, word)
'''


# № 18042 (Уровень: Базовый)
'''
from itertools import *
cnt = 0
for p in product('ЛЮСТРА', repeat=5):
    word = ''.join(p)
    if word.count('Ю') <= 2:
        if word[-1] not in 'ЛСТР':
            cnt += 1
print(cnt)
'''


# № 17862 Демоверсия 2025 (Уровень: Базовый)
'''
from itertools import *
cnt = 0
for p in product('0123456789AB', repeat=5):
    num = ''.join(p)
    if num[0] != '0':
        if num.count('7') == 1:
            D = [x for x in num if x > '8']
            if len(D) <= 3:
                cnt += 1
print(cnt)
'''


# № 17799 (Уровень: Средний)
'''
from itertools import *
n = 0
for p in product(sorted('АРГУМЕНТ'), repeat=4):
    word = ''.join(p)
    n += 1
    if len(word) == len(set(word)):
        if list(word) == sorted(word):
            print(n)


from itertools import *
s = sorted('АРГУМЕНТ')
for n, p in enumerate(product(s, repeat=4), 1):
    word = ''.join(p)
    if len(word) == len(set(word)):
        if list(word) == sorted(word):
            print(n)
'''

'''
R = []
for x in range(2, 2025+1):
    n = 5**2025 + 5**200 - x
    r = ''
    while n > 0:
        r += str(n % 5)
        n //= 5
    r = r[::-1]
    print(r.count('4'), x)
    R.append([r.count('4'), x])

print(max(R))  # [199, 1876]
'''
# 199 1251
# 199 1876

'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:24]:
    A = int(f'12{x}734', 24)
    B = int(f'8{x}95{x}3', 24)
    C = int(f'24{x}796 ', 24)
    if (A + B + C) % 23 == 0:
        print((A + B + C) // 23)
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 23, 25]
# КЕГЭ  = []
# на следующем уроке:
