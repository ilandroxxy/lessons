# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 17859 Демоверсия 2025 (Уровень: Базовый)
'''
R = []
for n in range(1, 13):
    b = f'{n:b}'  # b = bin(n)[2:]
    if n % 2 == 0:
        b = '10' + b
    else:
        b = '1' + b + '01'
    r = int(b, 2)
    # ValueError: int() base must be >= 2 and <= 36, or 0
    R.append(r)
print(max(R))


maxi = 0
for n in range(1, 13):
    b = f'{n:b}'  # b = bin(n)[2:]
    if n % 2 == 0:
        b = '10' + b
    else:
        b = '1' + b + '01'
    r = int(b, 2)
    # ValueError: int() base must be >= 2 and <= 36, or 0
    maxi = max(maxi, r)

print(maxi)
'''


# № 17860 Демоверсия 2025 (Уровень: Базовый)
# В начальный момент Черепаха находится в начале координат, её голова
# направлена вдоль положительного направления оси ординат, хвост опущен.

# Черепахе был дан для исполнения следующий алгоритм:
# Повтори 9 [Вперёд 22 Направо 90 Вперед 6 Направо 90]
# Поднять хвост
# Вперед 1 Направо 90 Вперёд 5 Налево 90
# Опустить хвост
# Повтори 9 [Вперёд 53 Направо 90 Вперёд 75 Направо 90]
#
# Определите периметр области пересечения фигур, ограниченных заданными алгоритмом линиями.
'''
import turtle as t
t.screensize(-5000, 5000)
t.tracer(0)  # Отключает анимацию отрисовки
t.left(90)
l = 20

# Переписываем псевдокод:
for i in range(9):
    t.forward(22 * l)  # fd(22 * l)
    t.right(90)  # rt(90)
    t.forward(6 * l)
    t.right(90)
t.up()
t.forward(1 * l)
t.right(90)
t.forward(5 * l)
t.left(90)
t.down()
for i in range(9):
    t.forward(53 * l)
    t.right(90)
    t.forward(75 * l)
    t.right(90)


t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * l, y * l)
        t.dot(3, 'red')

t.update()  # Чтобы корректно работал t.tracer(0)
t.done()
'''


# № 17862 Демоверсия 2025 (Уровень: Базовый)
'''
s = '0123456789AB'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    num = a + b + c + d + e
                    if a != '0' and num.count('7') == 1:
                        if len([x for x in num if x > '8']) <= 3:
                            cnt += 1
print(cnt)


# Вариант 2
from itertools import product
cnt = 0
for p in product('0123456789AB', repeat=5):
    num = ''.join(p)
    if num[0] != '0' and num.count('7') == 1:
        if len([x for x in num if x > '8']) <= 3:
            cnt += 1
print(cnt)
'''


'''
for s in open('9.txt'):
    M = [int(x) for x in s.split()]
    print(M)

for s in open('9.csv'):
    M = [int(x) for x in s.split(';')]
    print(M)
'''


# № 17863 Демоверсия 2025 (Уровень: Средний)
'''
cnt = 0
for s in open('9.txt'):
    M = [int(x) for x in s.split()]
    copied = [x for x in M if M.count(x) == 3]
    not_copied = [x for x in M if M.count(x) == 1]
    if len(copied) == 3 and len(not_copied) == 3:
        if sum(copied) ** 2 > sum(not_copied) ** 2:
            cnt += 1
print(cnt)
'''


# № 17867 Демоверсия 2025 (Уровень: Базовый)
'''
from ipaddress import *
net = ip_network('172.16.168.0/255.255.248.0', 0)
cnt = 0
for ip in net:
    b = f'{ip:b}'
    print(ip, b)
    if b.count('1') % 5 != 0:
        cnt += 1
print(cnt)
'''


# № 17869 Демоверсия 2025 (Уровень: Базовый)
'''
n = 3*3125**8 + 2*625**7 - 4*625**6 + 3*125**5 - 2 * 25**4 - 2025
b = 25
M = []
while n > 0:
    M.append(n % b)
    n //= b
M.reverse()
print(M)
print(M.count(0))
'''


# № 17870 Демоверсия 2025 (Уровень: Базовый)
'''
for x in range(2030+1):
    n = 7**170 + 7**100 - x
    b = 7
    M = []
    while n > 0:
        M.append(n % b)
        n //= b
    M.reverse()
    if M.count(0) == 71:
        print(x)
'''


# № 17870 Демоверсия 2025 (Уровень: Базовый)
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:19]:
    A = int(f'98897{x}21', 19)
    B = int(f'2{x}923', 19)
    if (A + B) % 18 == 0:
        print((A + B) // 18)
'''


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = []
# КЕГЭ  = []
# на следующем уроке:
