# region Домашка: ******************************************************************

# https://stepik.org/lesson/1038682/step/7?unit=1062773
'''
s = '>' + '1' * 11 + '2' * 12 + '3' * 30
while '>1' in s or '>2' in s or '>3' in s:
    if '>1' in s:
        s = s.replace('>1', '22>', 1)
    if '>2' in s:
        s = s.replace('>2', '222>', 1)
    if '>3' in s:
        s = s.replace('>3', '1>', 1)
s = s.replace('>', '')
print(sum(map(int, s)))

print(sum([int(x) for x in s if x.isdigit()]))
'''


# https://stepik.org/lesson/1038682/step/8?unit=1062773
'''
maxi = 0
for n in range(4, 10000):
    s = '1' + '2' * n
    while '12' in s or '322' in s or '222' in s:
        if '12' in s:
            s = s.replace('12', '2', 1)
        if '322' in s:
            s = s.replace('322', '21', 1)
        if '222' in s:
            s = s.replace('222', '3', 1)

    summa = sum(map(int, s))
    if maxi < summa:
        maxi = summa
print(maxi)
'''

# https://stepik.org/lesson/1038682/step/9?unit=1062773
'''
R = []
for n in range(210, 300):
    s = '3' + '7' * n
    while '27' in s or '377' in s or '777' in s:
        if '27' in s:
            s = s.replace('27', '32', 1)
        if '377' in s:
            s = s.replace('377', '27', 1)
        if '777' in s:
            s = s.replace('777', '3', 1)
    summa = sum(map(int, s))
    if summa % 15 == 0:
        R.append(n)
print(max(R))
'''


# https://stepik.org/lesson/1038682/step/10?unit=1062773
'''
from itertools import *
R = []
for p in permutations(['1' * 20, '2' * 15, '3' * 40]):
    s = '>' + ''.join(p) + '<'
    while '><' not in s:
       s = s.replace('>1', '3>', 1)
       s = s.replace('>2', '2>', 1)
       s = s.replace('>3', '1>', 1)
       s = s.replace('3<', '<1', 1)
       s = s.replace('2<', '<3', 1)
       s = s.replace('1<', '<2', 1)
    s = s.replace('><', '')
    summa = sum(map(int, s))
    R.append(summa)
print(max(R))
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
from itertools import *

for p in product('01', repeat=2):
    word = ''.join(p)
    print(p, word)
    # ('0', '0') 00
    # ('0', '1') 01
    # ('1', '0') 10
    # ('1', '1') 11

for p in permutations('01', r=2):
    word = ''.join(p)
    print(p, word)
    # ('0', '1') 01
    # ('1', '0') 10
'''


# 8 https://education.yandex.ru/ege/task/96e3d78c-ad84-4cec-9408-3f6837ac765c
'''
# Вариант 1
s = sorted('ШАТЕР')
n = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    word = a + b + c + d + e
                    n += 1
                    if word.count('А') <= 1 and 'ЕЕ' not in word:
                        print(n, word)
                        exit()
'''

# Вариант 2
'''
from itertools import *
n = 0
for p in product(sorted('ШАТЕР'), repeat=5):
    word = ''.join(p)
    n += 1
    if word.count('А') <= 1 and 'ЕЕ' not in word:
        print(n, word)
        break
'''


# https://education.yandex.ru/ege/task/93ac0c3b-ddee-4791-a179-b256cda73ea2
'''
from itertools import *
cnt = 0
for p in product(sorted('КЦИЧП'), repeat=6):
    word = ''.join(p)
    if word.count('И') == 3:
        cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/task/dba8a4f0-4e87-4fa6-a1a3-8706e04146bb
'''
from itertools import *
cnt = 0
for p in product('ВЗГЛЯД', repeat=4):
    word = ''.join(p)
    if 1 <= word.count('З') <= 2:
        cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/task/7bd50bb2-d36b-496b-b363-393b9ac6cb4b
'''
from itertools import *
R = []
for p in permutations('НОСОЧЕЧКИ'):
    word = ''.join(p)
    new_word = word
    new_word = new_word.replace('Е', 'О').replace('И', 'О')
    for x in 'НСЧ':
        new_word = new_word.replace(x, 'К')
    if 'КК' not in new_word and 'ОО' not in new_word:
        R.append(word)
print(len(set(R)))
'''


# https://education.yandex.ru/ege/task/0aa9c32d-bc88-4b1d-b1bd-3aded1af6388
'''
from itertools import *
cnt = 0
for p in product('ВОЛК', repeat=5):
    word = ''.join(p)
    if word.count('В') == 1:
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


# https://education.yandex.ru/ege/task/f7b3e564-4a77-4925-a995-3fd1df3171c0
'''
from itertools import *
cnt = 0
for p in product('0123456789ABCD', repeat=5):
    num = ''.join(p)
    if num[0] != '0':
        for x in 'ABCD':
            num = num.replace(x, 'A')
        for x in '13579':
            num = num.replace(x, '1')
        if '1A' not in num and 'A1' not in num:
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
# ФИПИ = [2, 6, 8, 12]
# КЕГЭ  = []
# на следующем уроке:
