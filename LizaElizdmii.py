# region Домашка: ******************************************************************

# https://stepik.org/lesson/1038703/step/14?unit=1062210
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

for x in alphabet[:8]:
    for y in alphabet[:8]:
        A = int(f'{y}04{x}5', 11)
        B = int(f'253{x}{y}', 8)
        if (A + B) % 117 == 0:
            print((A + B) // 117)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Задание 8 https://education.yandex.ru/ege/task/4c1caa2c-ea34-496e-a870-8cc9f92b2583
'''
# Вариант 1

s = sorted('ГОНДУБШ')
n = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        word = a + b + c + d + e + f
                        n += 1
                        if n % 2 != 0:
                            if word[0] != 'Б':
                                if word.count('Н') >= 2:
                                    if 'У' not in word:
                                        print(n, word)


# Вариант 2

from itertools import *
n = 0
for p in product(sorted('ГОНДУБШ'), repeat=6):
    word = ''.join(p)
    n += 1
    if n % 2 != 0:
        if word[0] != 'Б':
            if word.count('Н') >= 2:
                if 'У' not in word:
                    print(n, word)

# Вариант 3

from itertools import *

for n, p in enumerate(product(sorted('ГОНДУБШ'), repeat=6), 1):
    word = ''.join(p)
    if n % 2 != 0:
        if word[0] != 'Б':
            if word.count('Н') >= 2:
                if 'У' not in word:
                    print(n, word)
'''


# Задание 8 https://education.yandex.ru/ege/task/60c1a00c-2fd4-472e-b4aa-50791d6bddb8
'''
from itertools import *
cnt = 0
for p in permutations('КАБИНЕТ'):
    word = ''.join(p)
    if word[-1] not in 'АИЕ':
        cnt += 1
print(cnt)
'''

# https://education.yandex.ru/ege/task/787e3e6e-9284-4a9d-953a-8c3d24123b2a
'''
from itertools import *
cnt = 0
for p in permutations('АРТЕМ'):
    word = ''.join(p)
    if not(word[-1] in 'АЕ' and word[0] in 'АЕ'):
        cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/task/d73b5f1e-ee81-4928-94f5-ea2abff0a9a0
'''
from itertools import *
cnt = 0
for p in permutations('01234567', 4):
    num = ''.join(p)
    if num[0] != '0' and num[0] == '3' and num[-1] == '0':
        num = num.replace('0', '2').replace('4', '2').replace('6', '2')
        if '22' not in num:
            cnt += 1
print(cnt)
'''

# https://education.yandex.ru/ege/task/78b6e053-eaf4-40bc-a7d1-53fad9f7eee4
'''
from itertools import *

for n, p in enumerate(product(sorted('БАТЫР'), repeat=5), 1):
    word = ''.join(p)
    if 'Ы' not in word:
        if 'АА' not in word:
            print(n)
            exit()
'''
'''
from itertools import *

cnt = 0
for p in product('012345', repeat=6):
    num = ''.join(p)
    if num[0] != '0' and num.count('2') == 1:
        num = num.replace('1', '*').replace('3', '*').replace('5', '*')
        if '2*' not in num and '*2' not in num:
            cnt += 1
print(cnt)
'''

from itertools import permutations

table = '15 16 23 27 28 32 36 46 48 51 57 61 63 64 72 75 78 82 84 87'
graph = 'AC CA AB BA CB BC BE EB ED DE DF FD FC CF DH HD HG GH GA AG'

print('1 2 3 4 5 6 7 9')
for per in permutations('ABCDEFGH'):
    new_table = table
    for i in range(1, 8+1):
        new_table = new_table.replace(str(i), per[i-1])
    if set(new_table.split()) == set(graph.split()):

        print(*per)

# 1 2 3 4 5 6 7 9
# H B E F G D A C
# H C F E G D A B

# Ответ: 18 + 43 = 61


# https://education.yandex.ru/ege/task/65351d01-6be4-467f-8c36-6d951bf990bb
'''
from itertools import *

cnt = 0
for p in product('ДРАКОН',repeat=8):
    num = ''.join(p)
    if num.count('А') == 1 and num.count('О') == 1:
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
