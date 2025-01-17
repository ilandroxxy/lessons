# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Срезы строк/списков
'''
# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
# -i -5   -4   -3   -2   -1
s = 'abcde'

print(M[2:4])  # ['c', 'd'] - Крайний справа индекс не берется
print(M[2:])  # ['c', 'd', 'e'] - Все элемента справа от 2 индекса включительно
print(M[:4])  # ['a', 'b', 'c', 'd'] - Все элементы слева до 4 индекса невключительно

# Популярные срезы
print(M[2:])  # ['c', 'd', 'e'] - Все элементы кроме первых двух
print(M[::2])  # ['a', 'c', 'e'] - Все элементы на четных индексах
print(M[1::2])  # ['b', 'd'] - Все элементы на нечетных индексах
print(M[-2:])  # ['d', 'e'] - Оканчиваются, то есть крайние два элемента справа
print(M[::-1])  # ['e', 'd', 'c', 'b', 'a'] - Все элементы в обратном порядке

for x in range(5, 100, 5):  # - все числа от 5 до 100 кратные 5
    print(x, end=' ')
'''

"""
from string import *
alphabet = digits + ascii_uppercase
#                i 0123456789
print(alphabet)  # 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ

alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')


def convert(n, b):
    r = ''
    while n > 0:
        r += alphabet[n % b]
        n //= b
    return r[::-1]

'''
def convert(n, b):
    r = ''
    while n > 0:
        r = str(n % b) + r
        n //= b
    return r
'''

print(convert(8, 2))



print(int('2342', 37))
# ValueError: int() base must be >= 2 and <= 36, or 0
"""


alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    r = ''
    while n > 0:
        r += alphabet[n % b]
        n //= b
    return r[::-1]

# № 19551 (Уровень: Базовый)
'''
M = []
for n in range(1, 1000):
    s = convert(n, 3)
    s = s.replace('2', '*').replace('0', '2').replace('*', '0')
    r = int(s, 3)
    res = abs(n - r)
    if res == 378:
        M.append(n)
print(min(M))
'''


# № 19237 ЕГКР 21.12.24 (Уровень: Базовый)
'''
M = []
for n in range(1, 1000):
    s = convert(n, 3)
    if n % 3 == 0:
        s += s[-2:]
    else:
        # summa = s.count('1') + s.count('2') * 2
        # summa = sum([int(x) for x in s])
        summa = sum(map(int, s))
        s += convert(summa, 3)
    r = int(s, 3)
    if r % 2 == 0 and r > 220:
        M.append(r)
print(min(M))
'''

#
# № 17869 Демоверсия 2025 (Уровень: Базовый)
'''
n = 3*3125**8 + 2*625**7 - 4*625**6 + 3*125**5 - 2*25**4 - 2025
b = 25
s = convert(n, b)
print(s.count('0'))
'''

'''
for x in range(2030+1):
    n = 7**170 + 7**100 - x
    s = convert(n, 7)
    if s.count('0') == 71:
        print(x)
'''
# 2029

'''
for x in range(2030+1):
    n = 7**170 + 7**100 - x
    s = []
    while n > 0:
        s.append(n % 7)
        n //= 7
    if s.count(0) == 71:
        print(x)
'''


'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:24]:
    A = int(f'12{x}734', 24)
    B = int(f'8{x}95{x}3', 24)
    C = int(f'24{x}796', 24)
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
# ФИПИ = [1, 2? сопоставление, 3, 4, 5? переводы, 7, 8-, 9-, 11-, 12-, 13-, 15-, 16-, 19-21-, 22]
# КЕГЭ  = []
# на следующем уроке:  5, 8, 14, 15,
