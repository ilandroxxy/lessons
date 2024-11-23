# region Домашка: ************************************************************

# https://stepik.org/lesson/1228669/step/5?unit=1242202
'''
from fnmatch import fnmatch


def is_prime(x):
    if x <= 1:
        return False
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            return False
    return True


for x in range(1, 10 ** 7 + 1):
    if fnmatch(str(x), '3?1111*'):
        if is_prime(x):
            print(x)
'''


# https://stepik.org/lesson/1228669/step/3?unit=1242202
'''
def divisors(x):
    div = []
    for y in range(1, int(x ** 0.5) + 1):
        if x % y == 0:
            div += [y, x // y]
    return sorted(set(div))


count = 0
for x in range(500_000+1, 10**10):
    d = [i for i in divisors(x) if i % 10 == 8 and i != 8 and i != x]
    if len(d) >= 1:
        count += 1
        print(x, min(d))
        if count == 5:
            break
'''

#  № 11953 (Уровень: Средний) +++
'''
from functools import lru_cache


@lru_cache(None)
def F(a, b):

    if a >= b or a == 100:
        return a == b

    count = 0

    x = a % 10  # Команда A: Прибавить последнюю цифру
    if x != 0:
        count += F(a + x, b)

    x = a % 68   # Команда B: Добавить остаток от деления на 68
    if x != 0:
        count += F(a + x, b)

    x = a ** 2   # Команда C: Возвести в квадрат
    if x != a:
        count += F(x, b)

    return count


print(F(2, 68) * F(68, 680))
'''

# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************

# Тип 24 №27691
# Определите максимальное количество идущих подряд символов A.
'''
# Вариант 1

s = open('files/24.txt').readline()
count = 1
maxi = 0
for i in range(len(s)-1):
    # if s[i] == 'A' and s[i+1] == 'A':
    if s[i:i+2] == 'AA':
        count += 1
        maxi = max(count, maxi)
    else:
        count = 1
print(maxi)

# Вариант 2

s = open('files/24.txt').readline()
s = s.replace('B', ' ').replace('C', ' ')
print(max([len(x) for x in s.split()]))

# Вариант 3: ctrl + F

s = open('files/24.txt').readline()
print(s)
'''

# Тип 24 №38602
# Определите максимальное количество идущих подряд символов
# в прилагаемом файле, среди которых нет идущих
# подряд символов P.
'''
s = open('files/24.txt').readline()
while 'PP' in s:
    s = s.replace('PP', 'P P')
print(max([len(x) for x in s.split()]))
'''


# Тип 24 №59848
# Необходимо найти самую длинную подстроку, которая
# может являться числом в 24-ричной системе счисления.
'''
s = open('files/24.txt').readline()
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[24:]:
    s = s.replace(x, ' ')
print(max([len(x) for x in s.split() if x[0] != '0']))
'''


# Тип 24 №58328
# Определите максимальное количество идущих подряд цифр,
# среди которых каждые две соседние различны.
'''
s = open('files/24.txt').readline()
count = 1
maxi = 0
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        count += 1
        maxi = max(maxi, count)
    else:
        count = 1
print(maxi)
'''

# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3?, 4, 5, 6, 7?, 8, 9, 10?, 11?, 12, 14, 15, 16, 17, 19-21?, 23, 24, 25]
# КЕГЭ = []
# на следующем уроке:
