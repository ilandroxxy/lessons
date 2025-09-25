# region Домашка: ******************************************************************



# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# 23746 Демоверсия 2026 (Уровень: Базовый)
'''
n = 0
s = sorted('СТРОКА')
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    word = a + b + c + d + e
                    n += 1
                    if n % 2 == 0:
                        if a not in 'АСТ':
                            if word.count('О') == 2:
                                print(n)
'''

'''
n = 0
from itertools import product
for p in product(sorted('СТРОКА'), repeat=5):
    word = ''.join(p)
    n += 1
    if n % 2 == 0:
        if word[0] not in 'АСТ':
            if word.count('О') == 2:
                print(n)
'''


'''
ip = '34.54.234.122'
print(ip.split('.'))  # ['34', '54', '234', '122']

IP = ['34', '54', '234', '122']
print('*'.join(IP))  # '34*54*234*122'
'''


# № 23554 Пересдача 03.07.25 (Уровень: Базовый)
'''
R = []
n = 0
from itertools import product
for p in product(sorted('АЛГОРИТМ'), repeat=5):
    word = ''.join(p)
    n += 1
    if n % 2 == 0:
        if word[0] not in 'АГ':
            if word.count('Р') >= 2:
                R.append(n)
print(min(R))
'''


# № 21407 Досрочная волна 2025 (Уровень: Базовый)
'''
cnt = 0
s = 'ДГИАШЭ'
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    word = a + b + c + d + e
                    if a not in 'ИАЭ':
                        if e not in 'ДГШ':
                            cnt += 1
print(cnt)

cnt = 0
from itertools import product
for p in product('ДГИАШЭ', repeat=5):
    word = ''.join(p)
    a, b, c, d, e = word
    if a not in 'ИАЭ':
        if e not in 'ДГШ':
            cnt += 1
print(cnt)
'''


#
# № 20898 Апробация 05.03.25 (Уровень: Базовый)
'''
cnt = 0
s = '012345678'
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    num = a + b + c + d + e
                    if a != '0':
                        if num.count('0') == 1:
                            for x in '1357':
                                num = num.replace(x, '1')
                            if '10' not in num and '01' not in num:
                                cnt += 1
print(cnt)
'''


# Под каким номером в списке идёт последнее слово, которое не начинается с буквы Я,
# содержит не более одной буквы Ь и не содержит букв Я, стоящих рядом?
'''
L = []
n = 0
from itertools import product

for p in product(sorted('ЯНВАРЬ'), repeat=5):
    word = ''.join(p)
    n += 1
    if word[0] not in 'Я':
        if word.count('Ь') == 1:
            if 'ЯЯ' not in word:
                L.append(n)
print(max(L))
'''


# № 18133 (Уровень: Базовый)  Татьяна
# (В. Колчев) Все 5-буквенные слова, в составе которых могут быть только буквы К,О,Д,И,М,
# записаны в алфавитном порядке и пронумерованы.
# Вот начало списка:
# 1. ДДДДД
# 2. ДДДДИ
# 3. ДДДДК
# 4. ДДДДМ
# 5. ДДДДО

# Под каким номером в списке идёт последнее слово, которое содержит
# ровно две буквы М и не содержит букв М, стоящих рядом?
'''
L = []
n = 0
s = sorted('КОДИМ')
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    word = a + b + c + d + e
                    n += 1
                    if word.count('M') == 2:
                        if 'MM' not in word:
                            L.append(n)
print(max(L))
'''


# № 11292 (Уровень: Средний)
# Сколько существует шестнадцатеричных пятизначных чисел, содержащих в своей
# записи ровно две цифры 6, при этом никакая чётная цифра не стоит рядом с цифрой 6?
cnt = 0
s = '0123456789ABCDEF'
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    num = a + b + c + d + e
                    if a != '0':
                        if num.count('6') == 2:
                            for x in '0248ACE':
                                num = num.replace(x, '*')
                            if '*6' not in num and '6*' not in num and '66' not in num:
                                cnt += 1
print(cnt)




# № 11291 (Уровень: Средний)
# Сколько существует шестеричных семизначных чисел, содержащих в своей
# записи ровно одну цифру 2, при этом никакая чётная цифра не стоит рядом с цифрой 2?
'''
cnt = 0
s = '012345'
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        for g in s:
                         num = a + b + c + d + e + f + g
                         if a != '0':
                             if num.count('2') == 1:
                                 for x in '04':
                                     num = num.replace(x, '+')
                                 if '+2' not in num and '2+' not in num and '22' not in num: 
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
# ФИПИ = [2, 5, 6, 14]
# КЕГЭ = []
# на следующем уроке:
