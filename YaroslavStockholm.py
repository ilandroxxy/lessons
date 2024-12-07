# region Домашка: ******************************************************************

'''
from itertools import *

for p in product('abc', repeat=5):
    print(p)  # ('c', 'c', 'c', 'c', 'c')
    print(''.join(p))  # 'ccccc'


for p in permutations('abc', r=3):
    print(p)  # ('c', 'b', 'a')
    print(''.join(p))  # 'cba'
'''


# № 776 Джобс (Уровень: Сложный)
'''
from itertools import *
R = []
for p in permutations(['1' * 20, '3' * 40, '2' * 15], r=3):
    s = '>' + ''.join(p) + '<'

    while '><' not in s:
        s = s.replace('>1', '3>', 1)
        s = s.replace('>2', '2>', 1)
        s = s.replace('>3', '1>', 1)
        s = s.replace('3<', '<1', 1)
        s = s.replace('2<', '<3', 1)
        s = s.replace('1<', '<2', 1)
    summa = sum([int(x) for x in s if x.isdigit()])
    R.append(summa)
print(max(R))
'''

'''
def is_prime(x):  # x = 12 -> [1 - 12]
    if x <= 1:
        return False
    for j in range(2, x):  # [2,  11]
        if x % j == 0:
            return False
    return True


print(is_prime(7))  # True
print(is_prime(1))  # False
print(is_prime(8))  # False
print([x for x in range(100) if is_prime(x)])
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
'''


'''
from itertools import  *
def is_primary(x):
    if x <= 1:
        return False
    for z in range(2, x):
        if x % z == 0:
            return False
    return True


R = []

for n in range(0, 10 ** 10):
    for p in permutations(['2' * 39, '0' * 39, '1' * n ]):
        s = '>' + ''.join(p)
        while '>1' in s or '>2' in s or '>0' in s:
            if '>1' in s:
                s = s.replace('>1', '22>', 1)
            if '>2' in s:
                s = s.replace('>2', '2>', 1)
            if '>0' in s:
                s = s.replace('>0', '1>', 1)
        summa = sum([int(x) for x in s if x.isdigit()])
        if is_primary(summa) == True:
            print(n)
            exit()
'''


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
    if is_prime(summa) == True:
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


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 12, 14]
# КЕГЭ  = []
# на следующем уроке:
