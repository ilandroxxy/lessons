# region Домашка: ************************************************************

# № 11291 (Уровень: Средний)
# Сколько существует шестеричных семизначных чисел,
# содержащих в своей записи ровно одну цифру 2,
# при этом никакая чётная цифра не стоит рядом с цифрой 2?
''
from itertools import *
count = 0
for a in product('012345', repeat=7):
    num = ''.join(a)
    if num[0] != '0' and num.count('2') == 1:
        num = num.replace('0', '4')
        if '42' not in num and '24' not in num:
            count += 1
print(count)
''
'''
from itertools import *
count = 0
for a in product('012345', repeat=7):
    num = ''.join(a)
    if num[0] != '0' and num.count('2') == 1:
        if all(p not in num for p in '20 02 42 24'.split()):
            count += 1
print(count)
'''

'''
from itertools import *

count = 0
for a in product('012345', repeat=7):
    num = ''.join(a)
    if num[0] != '0':
        if num.count('2') == 1:
            if num.count('22') == 0 and num.count('42') == 0 and num.count('24') == 0 and num.count(
                    '20') == 0 and num.count('02') == 0:
                count += 1
print(count)
'''

'''
from itertools import *

count = 0
for a in product('0123456', repeat=7):
    s = ''.join(a)
    if s[0] != '0':
        print([y in '0246' for y in s])
        if sum([y in '0246' for y in s]) == 2:
            count += 1
print(count)
'''

'''
from itertools import *
A = []
for b, a in enumerate(product(sorted('ПАРУС'), repeat=5), 1):
    num = ''.join(a)
    if num.count('У') <= 1 and 'АА' not in num:
        A.append(b)
print(max(A))
'''

# № 12917 (Уровень: Базовый)
# (PRO100 ЕГЭ) Петя составляет слова путём перестановки букв в слове ПРОСТО.
# Сколько он сможет составить слов, если запрещено ставить рядом две одинаковые буквы?
'''
from itertools import *
R = []
for p in permutations('ПРОСТО'):
    s = ''.join(p)
    if 'ОО' not in s:
        R.append(s)
print(len(set(R)))
'''
'''
count = 0
for a in '012345678':
    for b in '012345678':
        for c in '012345678':
            for d in '012345678':
                for e in '012345678':
                    s = a + b + c + d + e
                    if s.count('5') == 1 and a != '0':
                        if a != b and b != c and c != d and d != e:
                            count += 1
print(count)

import time
start = time.time()

count = 0
s = '012345678'
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    if slovo.count('5') == 1 and a != '0':
                        if a != b != c != d != e:
                            count += 1
print(count)

print(time.time() - start)  # 0.017
'''

'''
import time
start = time.time()

from itertools import *
count = 0
for p in product('012345678', repeat=5):
    slovo = ''.join(p)
    a, b, c, d, e = slovo
    if slovo.count('5') == 1 and a != '0':
        if a != b != c != d != e:
            count += 1
print(count)

print(time.time() - start)  # 0.017
'''


# Функция перевода в b-ую систему счисления
'''
from string import *
alphabet = digits + ascii_uppercase
def convert(n, b):
    r = ''
    while n > 0:
        r = alphabet[n % b] + r
        n //= b
    return r


r = convert(8, 2)
print(r)  # 1000
print(int(r, 2))  # 8
'''


from string import *
alphabet = digits + ascii_uppercase
print(alphabet)
def convert(n, b):
    r = ''
    while n > 0:
        r += alphabet[n % b]
        n //= b
    return r[::-1]


R = []
for n in range(1, 10000):
    s = convert(n, 7)
    if s.count('2') % 2 == 0:
        s += '555'
    else:
        s = '1' + s
    r = int(s, 7)
    if r < 3799:
        R.append(n)
print(max(R))

# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************


# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3?, 4, 5, 6, 7?, 8, 9, 10?, 11?, 12, 14?, 15?, 16?, 17, 19-21?, 23]
# КЕГЭ = []
# на следующем уроке:
