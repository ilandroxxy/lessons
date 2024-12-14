# region Домашка: ******************************************************************

# Функция поиска простого числа
'''
def is_prime(x):  # 12
    if x <= 1:
        return False  # число составное
    for j in range(2, x):  # [2, ..., 11]
        if x % j == 0:
            return False  # число составное
    return True  # # число простое


print(is_prime(7))
print(is_prime(8))
print([x for x in range(100) if is_prime(x)])
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
'''


# № 6786 (Уровень: Средний)
'''
def is_prime(x):
    if x <= 1:
        return False
    for j in range(2, x):
        if x % j == 0:
            return False
    return True


for n in range(1, 1000):
    s = '>' + '0' * 39 + '1' * n + '2' * 39

    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1', '22>', 1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>0' in s:
            s = s.replace('>0', '1>', 1)
    summa = sum([int(x) for x in s if x.isdigit()])
    if is_prime(summa):
        print(n)
        break
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
from itertools import *

for p in product('01', repeat=2):
    num = ''.join(p)
    print(p, num)
    # ('0', '0') 00
    # ('0', '1') 01
    # ('1', '0') 10
    # ('1', '1') 11

for p in permutations('01', 2):
    num = ''.join(p)
    print(p, num)
    # ('0', '1') 01
    # ('1', '0') 10
'''


# Задание 8 https://education.yandex.ru/ege/task/4b7aa1a3-0a20-4901-b4dc-cafda6f242e6
'''
# Вариант 1

s = sorted('БМЮРН')
n = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        word = a + b + c + d + e + f
                        n += 1
                        if n % 2 != 0 and a != 'М':
                            if word.count('Р') >= 2 and 'Ю' not in word:
                                print(n)


# Вариант 2

from itertools import *
n = 0
for p in product(sorted('БМЮРН'), repeat=6):
    word = ''.join(p)
    n += 1
    if n % 2 != 0 and word[0] != 'М':
        if word.count('Р') >= 2 and 'Ю' not in word:
            print(n)

# Вариант 3

from itertools import *

for n, p in enumerate(product(sorted('БМЮРН'), repeat=6), 1):
    word = ''.join(p)
    if n % 2 != 0 and word[0] != 'М':
        if word.count('Р') >= 2 and 'Ю' not in word:
            print(n)
'''


# https://education.yandex.ru/ege/task/783a4cad-5d6e-49b9-a85d-82e9895d80ad
'''
from itertools import *
n = 0
for p in product(sorted('КОФЕ'), repeat=5):
    word = ''.join(p)
    n += 1
    if word.count('О') == 1:
        if all(pair not in word for pair in 'КО ОК ФО ОФ'.split()):
            print(n)
'''


# https://education.yandex.ru/ege/task/65351d01-6be4-467f-8c36-6d951bf990bb
'''
from itertools import *
cnt = 0
for p in product('ДРАКОН', repeat=8):
    word = ''.join(p)
    if word.count('А') == 1 and word.count('О') == 1:
        cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/task/2d4c8b35-1807-4960-8f25-dfae6342c9a7
'''
from itertools import *
cnt = 0
for p in permutations('КОБУРА'):
    word = ''.join(p)
    word = word.replace('К', 'Б').replace('Р', 'Б')
    word = word.replace('О', 'А').replace('У', 'А')
    if 'ББ' not in word and 'АА' not in word:
        cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/task/154b58da-493e-4901-accb-5d8cbff32f0b
'''
from itertools import *
cnt = 0
for p in product('0123456789ABCDEF', repeat=5):
    num = ''.join(p)
    if num[0] != '0':
        M = [x for x in num if x in '0123456789']
        if len(M) == 1:
            cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/task/e327b270-8faa-450f-a350-e313a28bbee9
'''
from itertools import *
cnt = 0
for p in product('0123', repeat=4):
    num = ''.join(p)
    if num[0] != '0':
        if any(num.count(x) >= 2 for x in num):
            cnt += 1
print(cnt)
'''
# Ответ: 174


# https://education.yandex.ru/ege/task/08a16fb2-3773-4f00-8961-cfa21b2e65a9
'''
from itertools import *
cnt = 0
for p in product('ГИПЕРБОЛА', repeat=6):
    word = ''.join(p)
    if word[0] not in 'ИЕОА' and word[-1] not in 'ИЕОА':
        for x in 'ИЕОА':
            word = word.replace(x, 'А')
        for x in 'ГПРБЛ':
            word = word.replace(x, 'Б')
        if 'БАБ' not in word:
            cnt += 1
print(cnt)
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 14]
# КЕГЭ  = []
# на следующем уроке:
