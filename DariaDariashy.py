# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Тип 8 №3227
# Все 5-буквенные слова, составленные из букв И, О, У, записаны в алфавитном порядке и пронумерованы.
# Вот начало списка:
# 1. ИИИИИ
# 2. ИИИИО
# 3. ИИИИУ
# 4. ИИИОИ
# Запишите слово, которое стоит под номером 240.
'''
# Вариант 1

s = sorted('ИОУ')
num = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    num += 1
                    if num == 240:
                        print(slovo)

# Вариант 2

from itertools import *
num = 0
for p in product(sorted('ИОУ'), repeat=5):
    slovo = ''.join(p)
    num += 1
    if num == 240:
        print(slovo)
'''


# Тип 8 №35466
# Вероника составляет 3-буквенные коды из букв В, Е, Р, О, Н, И, К, А,
# причём буква В должна входить в код ровно один раз.
# Все полученные коды Вероника записала в алфавитном порядке и пронумеровала.
# Начало списка выглядит так:
#
# 1. ААВ
# 2. АВА
# 3. АВЕ
#
# На каком месте будет записан первый код, не содержащий ни одной буквы А?
'''
R = []
s = sorted('ВЕРОНИКА')
num = 0
for a in s:
    for b in s:
        for c in s:
            slovo = a + b + c
            if slovo.count('В') == 1:
                num += 1
                if 'А' not in slovo:
                    R.append(num)
print(min(R))


from itertools import *
R = []
num = 0
for p in product(sorted('ВЕРОНИКА'), repeat=3):
    slovo = ''.join(p)
    if slovo.count('В') == 1:
        num += 1
        if 'А' not in slovo:
            R.append(num)
print(min(R))
'''


# Тип 8 №17374
# Полина составляет 6-буквенные коды из букв П, О, Л, И, Н, А.
# Каждую букву нужно использовать ровно 1 раз, при этом нельзя ставить подряд две гласные или две согласные.
# Сколько различных кодов может составить Полина?
'''
from itertools import *
cnt = 0
for p in permutations('ПОЛИНА'):
    slovo = ''.join(p)
    slovo = slovo.replace('Л', 'П').replace('Н', 'П')
    slovo = slovo.replace('О', 'А').replace('И', 'А')
    if 'ПП' not in slovo and 'АА' not in slovo:
        cnt += 1
print(cnt)


s = 'ПОЛИНА'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        slovo = a + b + c + d + e + f
                        if len(set(slovo)) == len(slovo):
                            slovo = slovo.replace('Л', 'П').replace('Н', 'П')
                            slovo = slovo.replace('О', 'А').replace('И', 'А')
                            if 'ПП' not in slovo and 'АА' not in slovo:
                                cnt += 1
print(cnt)
'''

'''
slovo1 = 'АБВГД'
print(set(slovo1))  # {'Д', 'А', 'Б', 'Г', 'В'}
print(len(slovo1) == len(set(slovo1)))  # True

slovo2 = 'АБВГДД'
print(set(slovo2))  # {'Д', 'Б', 'А', 'В', 'Г'}
print(len(slovo2) == len(set(slovo2)))  # False
'''


# Тип 8 №59832
# Игорь составляет пятизначные числа, используя цифры девятеричной системы счисления.
# Сколько различных чисел может составить Игорь, в которых ровно две цифры 3 и нечётные цифры не стоят рядом с цифрой 2?
'''
s = '012345678'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    num = a + b + c + d + e
                    if num[0] != '0':
                        if num.count('3') == 2:
                            if all(pair not in num for pair in '12 21 23 32 25 52 27 72'.split()):
                                cnt += 1

print(cnt)
print('12 21 23 32 25 52 27 72'.split())


from itertools import *
cnt = 0
for p in product('012345678', repeat=5):
    num = ''.join(p)
    if num[0] != '0':
        if num.count('3') == 2:
            if all(pair not in num for pair in '12 21 23 32 25 52 27 72'.split()):
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
# ФИПИ = [5, 8, 12, 14]
# КЕГЭ  = []
# на следующем уроке:
