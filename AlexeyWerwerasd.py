# region Домашка: ************************************************************


# endregion Домашка: *********************************************************
#
# #
# region Урок: ************************************************************

'''
from itertools import *
for p in product('abc', repeat=2):
    slovo = ''.join(p)
    print(p, slovo)
    # ('a', 'a') aa
    # ('a', 'b') ab
    # ('a', 'c') ac
    # ('b', 'a') ba
    # ('b', 'b') bb
    # ('b', 'c') bc
    # ('c', 'a') ca
    # ('c', 'b') cb
    # ('c', 'c') cc

from itertools import *
for p in permutations('abc', r=2):
    slovo = ''.join(p)
    print(p, slovo)
    # ('a', 'b') ab
    # ('a', 'c') ac
    # ('b', 'a') ba
    # ('b', 'c') bc
    # ('c', 'a') ca
    # ('c', 'b') cb
'''


# Тип 8 №38942
# Все четырёхбуквенные слова, в составе которых могут быть только буквы А, В, Т, О, Р,
# записаны в алфавитном порядке и пронумерованы, начиная с 1. Ниже приведено начало списка:
# 1.АААА
# 2.АААВ
# 3.АААО
# 4.АААР
# 5.АААТ
# 6.ААВА
#
# Под каким номером в списке идёт слово ВАТА?
'''
# Вариант 1
s = sorted('АТВОР')
num = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                slovo = a + b + c + d
                num += 1
                if slovo == 'ВАТА':
                    print(num, slovo)

# Вариант 2
from itertools import *
num = 0
for p in product(sorted('АТВОР'), repeat=4):
    slovo = ''.join(p)
    num += 1
    if slovo == 'ВАТА':
        print(num, slovo)


# Вариант 3
from itertools import *
for num, p in enumerate(product(sorted('АТВОР'), repeat=4), 1):
    slovo = ''.join(p)
    if slovo == 'ВАТА':
        print(num, slovo)
'''


# Тип 8 №59743
'''
# Вариант 1
s = 'МАНГУСТ'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        slovo = a + b + c + d + e + f
                        if a != 'А' and slovo.count('У') >= 1:
                            if slovo.count('М') == 2:
                                cnt += 1
print(cnt)

# Вариант 2
from itertools import *
cnt = 0
for p in product('МАНГУСТ', repeat=6):
    slovo = ''.join(p)
    if slovo[0] != 'А' and slovo.count('У') >= 1:
        if slovo.count('М') == 2:
            cnt += 1
print(cnt)
'''

# Тип 8 №70535
# Определите количество 12-ричных пятизначных чисел, в записи которых
# ровно одна цифра 7 и не более трёх цифр с числовым значением, превышающим 8.
'''
# Вариант 1
s = '0123456789AB'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    num = a + b + c + d + e
                    if num[0] != '0':
                        if num.count('7') == 1:
                            D = [x for x in num if x > '8']
                            if len(D) <= 3:
                                cnt += 1
print(cnt)


# Вариант 2
from itertools import *
cnt = 0
for p in product('0123456789AB', repeat=5):
    num = ''.join(p)
    if num[0] != '0':
        if num.count('7') == 1:
            D = [x for x in num if x > '8']
            if len(D) <= 3:
                cnt += 1
print(cnt)
'''

'''
s = sorted('ЕКМОПРТЬ')
R = []
num = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    num += 1
                    if 'К' not in slovo and slovo.count('Р') == 2:
                        R.append(num)
print(max(R))
'''

s = sorted('АБВГД')
n = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    if a not in 'АЕЁИЮЯЙЭ' and all(pair not in slovo for pair in ['АА', 'ББ', 'ВВ', 'ГГ', 'ДД']):
                        n += 1
                        print(n)


# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# ФИПИ = [2, 5, 6, 8, 12, 14]
# КЕГЭ = []
# на следующем уроке:
