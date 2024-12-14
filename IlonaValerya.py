# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
from itertools import *

# Элементы перестановки могут дублироваться:
for p in product('01', repeat=2):
    num = ''.join(p)  # это метод строк объединяющий список/кортеж строк в одну строку
    print(p, num)
    # ('0', '0') 00
    # ('0', '1') 01
    # ('1', '0') 10
    # ('1', '1') 11

# Элементы перестановки встречаются ровно 1 раз:
for p in permutations('01'):
    num = ''.join(p)
    print(p, num)
    # ('0', '1') 01
    # ('1', '0') 10
'''


# Задание 8 https://education.yandex.ru/ege/task/4c623ce7-3e25-4a25-9660-2d139d520811
'''
# Вариант 1
s = sorted('ЛАЙМ')
n = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    word = a + b + c + d + e
                    n += 1
                    if word.count('М') <= 1 and 'ЛЛ' not in word:
                        print(n)

# Вариант 2
from itertools import *
n = 0
for p in product(sorted('ЛАЙМ'), repeat=5):
    word = ''.join(p)
    n += 1
    if word.count('М') <= 1 and 'ЛЛ' not in word:
        print(n)
'''


# https://education.yandex.ru/ege/task/d1c2a7c4-3fc6-46c8-859a-1ef68e6c778d
'''
from itertools import *
cnt = 0
for p in product('ВИШНЯ', repeat=6):
    word = ''.join(p)
    if word.count('В') <= 1:  # буква В используется не более одного раза
        if word[0] != 'Ш':  # слово не должно начинаться с буквы Ш
            if word[-1] not in 'ИЯ':  # слово не должно оканчиваться гласными буквами
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

# https://education.yandex.ru/ege/task/310d22e7-bde6-4f5c-99ff-3d2861ebf37a
'''
from itertools import *
cnt = 0
for p in product('0123456789ABC', repeat=7):
    num = ''.join(p)
    if num[0] != '0':
        if num.count('5') >= 2:
            for x in '0468AC':
                num = num.replace(x, '2')
            for x in '3579B':
                num = num.replace(x, '1')
            if '11' not in num and '22' not in num:
                cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/task/b19825e6-aafc-48ed-9bd7-99033090c53c
'''
from itertools import *
cnt = 0
for p in product('012345', repeat=6):
    num = ''.join(p)
    if num[0] != '0':
        if num.count('2') == 1:
            num = num.replace('3', '1').replace('5', '1')
            if '12' not in num and '21' not in num:
                cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/task/ae97ab85-969c-401a-b0aa-38efd2a6ac5f
'''
from itertools import *
cnt = 0
for p in permutations('012346789', 5):
    num = ''.join(p)
    if num[0] != '0':
        for x in '0468':
            num = num.replace(x, '2')
        for x in '3579':
            num = num.replace(x, '1')
        if '11' not in num and '22' not in num:
            cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/task/08a16fb2-3773-4f00-8961-cfa21b2e65a9
'''
from itertools import *
cnt = 0
for p in product('ГИПЕРБОЛА', repeat=6):
    word = ''.join(p)
    if word[0] not in 'ИЕОА' and word[-1] not in 'ЕИОА':
        for x in 'ИЕО':
            word = word.replace(x, 'А')
        for x in 'ГПРЛ':
            word = word.replace(x, 'Б')
        if 'БАБ' not in word:
            cnt += 1
            print(word)
print(cnt)
'''

# https://education.yandex.ru/ege/task/6f7a985f-c404-4ebe-a856-f7ed7e6d5b46
'''
from itertools import *
cnt = 0
for p in permutations('01234567', 6):
    num = ''.join(p)
    if num[0] != '0':
        if int(num, 8) % 5 == 0:  # десятичная запись которых делится на 5
            for x in '046':
                num = num.replace(x, '2')
            for x in '357':
                num = num.replace(x, '1')
            if '11' not in num and '22' not in num:
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
