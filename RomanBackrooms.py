# region Домашка: ******************************************************************
'''
def is_prime(x):  # x == 12
    if x <= 1:
        return False
    for j in range(2, x):
        if x % j == 0:
            return False
    return True


# print([x for x in range(100) if is_prime(x)])
for n in range(1, 1000):
    s = '>' + '0' * 39 + '1' * n + '2' * 39

    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1', '22>', 1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>0' in s:
            s = s.replace('>0', '1>', 1)

    s = s.replace('>', '')
    summa = sum(map(int, s))

    # summa = sum(map(int, s[:-1]))

    # summa = sum([int(x) for x in s if x.isdigit()])

    if is_prime(summa):
        print(n)
        break
'''



# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************



# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# https://education.yandex.ru/ege/task/96e3d78c-ad84-4cec-9408-3f6837ac765c
# Прототип номер 1 с алфавитным порядком

# Вариант 1
'''
s = sorted('ШАТЕР')
n = 0
R = []
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    word = a + b + c + d + e
                    n += 1
                    if word.count('А') <= 1 and 'ЕЕ' not in word:
                        R.append(n)
print(min(R))


# Вариант 2

from itertools import *
n = 0
for p in product(sorted('ШАТЕР'), repeat=5):
    word = ''.join(p)
    n += 1
    if word.count('А') <= 1 and 'ЕЕ' not in word:
        print(n)
        break

# Вариант 3

from itertools import *

for n, p in enumerate(product(sorted('ШАТЕР'), repeat=5), 1):
    word = ''.join(p)
    if word.count('А') <= 1 and 'ЕЕ' not in word:
        print(n)
        break
'''

'''
from itertools import product, permutations

for p in product('abc', repeat=5):
    word = ''.join(p)
    print(p, word)
    # ('c', 'c', 'c', 'a', 'c') cccac
    # ('c', 'c', 'c', 'b', 'a') cccba
    # ('c', 'c', 'c', 'b', 'b') cccbb


for p in permutations('abc', r=3):
    word = ''.join(p)
    print(p, word)
    # ('a', 'b', 'c') abc
    # ('a', 'c', 'b') acb
    # ('b', 'a', 'c') bac
    # ('b', 'c', 'a') bca
    # ('c', 'a', 'b') cab
    # ('c', 'b', 'a') cba
'''


'''
from itertools import *
n = 0
R = []
for p in product(sorted('БМЮРН'), repeat=6):
    word = ''.join(p)
    n += 1
    if n % 2 != 0:
        if word[0] != 'М':
            if word.count('Р') >= 2:
                if 'Ю' not in word:
                    R.append(n)
print(max(R))
'''


# https://education.yandex.ru/ege/task/c6167029-d804-421e-865f-aa96e4c98ecd
'''
from itertools import *
n = 0
for p in product(sorted('АВОРТ'), repeat=6):
    word = ''.join(p)
    n += 1
    if word == 'ВОРОТА':
        print(n)
'''

# https://education.yandex.ru/ege/task/c6167029-d804-421e-865f-aa96e4c98ecd
'''
from itertools import *
cnt = 0
for p in permutations('01234567', r=5):
    num = ''.join(p)
    if num[0] != '0':
        if '1' not in num:
            for x in '046':
                num = num.replace(x, '2')
            for x in '357':
                num = num.replace(x, '1')
            if '11' not in num and '22' not in num:
                cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/task/787e3e6e-9284-4a9d-953a-8c3d24123b2a
'''
from itertools import *
cnt = 0
for p in permutations('АРТЕМ'):
    word = ''.join(p)
    if not(word[0] in 'АЕ' and word[-1] in 'АЕ'):
        cnt += 1
print(cnt)
'''

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 6, 8, 12]
# КЕГЭ  = []
# на следующем уроке:
