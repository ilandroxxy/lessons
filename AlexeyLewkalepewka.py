# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 18119 (Уровень: Базовый)
'''
def convert(n, base):
    r = ''
    while n > 0:
        r = str(n % base) + r
        n //= base
    return r


R = []
for N in range(1, 1000):
    s = convert(N, 3)
    if sum([int(x) for x in s]) % 2 == 0:
        s = '1' + s + '2'
    else:
        s = '2' + s + '0'
    r = int(s, 3)
    if r > 100:
        R.append(r)
print(min(R))
'''


# https://education.yandex.ru/ege/task/08a16fb2-3773-4f00-8961-cfa21b2e65a9
'''
from itertools import *
cnt = 0
for p in product('ГИПЕРБОЛА', repeat=6):
    word = ''.join(p)
    if word[0] not in 'ИЕОА' and word[-1] not in 'ИЕОА':
        for sogl in 'ГПРБЛ':
            word = word.replace(sogl, '*')
        for glas in 'ИЕОА':
            word = word.replace(glas, '+')
        if '*+*' not in word:
            cnt += 1
print(cnt)


from itertools import product

cnt = 0
for p in product('ГИПЕРБОЛА', repeat=6):
    word = ''.join(p)
    for i in 'ИЕО':
        word = word.replace(i, 'А')
    for i in 'ГПРЛ':
        word = word.replace(i, 'Б')
    if word[0] != 'А' and word[-1] != 'А':
        if 'БАБ' not in word:
            cnt += 1
print(cnt)
'''

'''
from itertools import permutations

cnt = 0
for p in permutations('АРТЁМ'):
    word = ''.join(p)
    print(word)
    if ((word[0] in 'АЁ') + (word[-1] in 'АЁ')) < 2:
        cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/task/310d22e7-bde6-4f5c-99ff-3d2861ebf37a
'''
from itertools import product
cnt = 0
s1 = '13579B'
s2 = '02468AC'
for p in product(s1, s2, s1, s2, s1, s2, s1):
    num = ''.join(p)
    if num.count('5') >= 2:
        cnt += 1
for p in product(s2, s1, s2, s1, s2, s1, s2):
    num = ''.join(p)
    if num[0] != '0':
        if num.count('5') >= 2:
            cnt += 1
print(cnt)
'''

# Задание 8 https://education.yandex.ru/ege/task/be9de2da-7a85-4442-8890-8e6e45842260
'''
from itertools import product

cnt = 0
for p in product(sorted('ОМГД'), repeat=4):
    word = ''.join(p)
    cnt += 1
    print(cnt, word)
    if cnt == 10:
        break
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ  = [8]
# на следующем уроке:

