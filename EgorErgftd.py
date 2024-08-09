# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Тип 8 №15822
'''
# Вариант 1
s = sorted('РЕКА')
R = []
num = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                slovo = a + b + c + d
                num += 1
                if 'А' not in slovo:
                    print(num, slovo)
                    R.append(num)
print(min(R))

# Вариант 2
from itertools import *
num = 0
R = []
for p in product(sorted('РЕКА'), repeat=4):
    slovo = ''.join(p)
    num += 1
    if 'А' not in slovo:
        R.append(num)
print(min(R))

# Вариант 3
from itertools import *
R = []
for num, p in enumerate(product(sorted('РЕКА'), repeat=4), 1):
    slovo = ''.join(p)
    if 'А' not in slovo:
        R.append(num)
print(min(R))
'''


# Тип 8 №59713
'''
# Вариант 1
s = 'ПЯТНИЦА'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    if a != 'Н' and slovo.count('Я') == 1:
                        cnt += 1
print(cnt)

# Вариант 2
from itertools import product

count = 0
for p in product("ПЯТНИЦА", repeat=5):
    if p.count("Я") == 1 and p[0] != "Н":
        count += 1
print(count)
'''


# Тип 8 №51977
'''
from itertools import *
cnt = 0
for p in product('ВЕРОНИКА', repeat=6):
    slovo = ''.join(p)
    glas = [x for x in slovo if x in 'ЕОИА']
    sogl = [x for x in slovo if x in 'ВРНК']
    if len(glas) > len(sogl):
        cnt += 1
print(cnt)
'''


# Тип 8 №59741
# Сколько существует чисел, восьмеричная запись которых содержит 5 цифр, причем в записи нет цифры 1.
# Также все цифры записи различны и никакие две чётные и две нечётные цифры не стоят рядом.
'''
s = '01234567'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    num = a + b + c + d + e
                    if num[0] != '0' and '1' not in num:
                        if len(num) == len(set(num)):
                            num = num.replace('0', '2').replace('4', '2').replace('6', '2')
                            num = num.replace('3', '1').replace('5', '1').replace('7', '1')
                            if '11' not in num and '22' not in num:
                                cnt += 1
print(cnt)

from itertools import *
cnt = 0
for p in permutations('01234567', 5):
    num = ''.join(p)
    if num[0] != '0' and '1' not in num:
        num = num.replace('0', '2').replace('4', '2').replace('6', '2')
        num = num.replace('3', '1').replace('5', '1').replace('7', '1')
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
