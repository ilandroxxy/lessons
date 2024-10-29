# region Домашка: ************************************************************


# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************


# № 18164 (Уровень: Базовый)
'''
from itertools import *
table = '13 15 16 17 23 27 31 32 36 45 47 51 54 56 61 63 65 71 72 74'
graph = 'AB BA AF FA FG GF GB BG BC CB CD DC GD DG DE ED GE EG EF FE'
for per in permutations('ABCDEFG'):
    new_table = table
    for i in range(1, 7+1):
        new_table = new_table.replace(str(i), per[i-1])
    if set(new_table.split()) == set(graph.split()):
        print('1 2 3 4 5 6 7')
        print(*per)
'''

# Ответ: 25


# № 18162 (Уровень: Базовый)
# Петя заполнял таблицу истинности логической функции
# F = ((a → b) ≡ c) ∨ d
'''
print('a b c d')
for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            for d in 0, 1:
                F = ((a <= b) == c) or d
                if F == 0:
                    print(a, b, c, d)
'''
# Ответ: a d b c


'''
def convert(n, b):
    s = ''
    while n > 0:
        s += str(n % 3)
        n //= 3
    s = s[::-1]
    return s

R = []
for n in range(1, 1000):
    s = convert(n, 3)
    summa = sum(map(int, s))
    if summa % 2 == 0:
        s = '1' + s + '2'
    else:
        s = '2' + s + '0'
    r = int(s, 3)
    if r > 100:
        R.append(r)
print(min(R))
'''
# Ответ: 113


# print(51*36 + 36*18 - 11*6)
'''
import turtle as t
t.screensize(-4000, 4000)
t.tracer(0)
t.left(90)
size = 20

for i in range(9):
    t.forward(50 * size)
    t.right(90)
    t.forward(35 * size)
    t.right(90)
t.up()
t.forward(5 * size)
t.right(90)
t.forward(10 * size)
t.right(90)
t.down()
for i in range(4):
    t.forward(35 * size)
    t.right(90)
    t.forward(17 * size)
    t.right(90)

t.up()
for x in range(-50, 50):
    for y in range(-50, 80):
        t.goto(x * size, y * size)
        t.dot(3, 'red')

t.update()
t.done()
'''
# Ответ: 2418


# № 18191 (Уровень: Средний)
'''
pixels = 1920 * 1080
i = 8
I_p = ((pixels * i) * 60) * 60  # бит

a = 2
b = 24000
c = 6
t = 60
I_v = a * b * c * t  # бит

print(((I_v + I_p) * 50) / 2**13)
'''


# № 18120 (Уровень: Базовый)
'''
from itertools import *
cnt = 0
n = 0
for per in product(sorted('ПРЕСТОЛ'), repeat=5):
    s = ''.join(per)
    n += 1
    if n % 2 != 0:
        if s[-1] in 'ЕО':
            sogl = [x for x in s if x in 'ПРСТЛ']
            if len(sogl) <= 3:
                cnt += 1
print(cnt)
'''


# № 18174 (Уровень: Средний)
'''
cnt = 0
for s in open('files/9.txt'):
    M = [int(x) for x in s.split()]
    if len(set(M)) == 5:
        plus = [x for x in M if x > 0]
        minu = [abs(x) for x in M if x < 0]
        if sum(minu) > sum(plus):
            cnt += 1
print(cnt)
'''


# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 7, 8, 9-, 11, 12, 14, 15, 16, 17-, 18, 19-21, 22, 23, 25.1]
# КЕГЭ = [12]
# на следующем уроке:
