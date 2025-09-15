# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 23746 Демоверсия 2026 (Уровень: Базовый)
'''
from itertools import product
R = []
n = 0
for p in product(sorted('СТРОКА'), repeat=5):
    # ('Т', 'Р', 'Т', 'С', 'Р') -> 'ТРТСР' через ''.join(p)
    word = ''.join(p)
    n += 1
    if n % 2 == 0:
        if word[0] not in 'АСТ':
            if word.count('О') == 2:
                R.append(n)
print(max(R))
'''
from os import confstr_names

# № 21407 Досрочная волна 2025 (Уровень: Базовый)
'''
from itertools import product
cnt = 0
for p in product('ДГИАШЭ', repeat=5):
    word = ''.join(p)
    a, b, c, d, e = word
    if a not in 'ИАЭ':
        if e not in 'ДГШ':
            cnt += 1
print(cnt)
'''


# № 20898 Апробация 05.03.25 (Уровень: Базовый)
'''
from itertools import product
cnt = 0
for p in product('012345678', repeat=5):
    num = ''.join(p)
    if num[0] != '0':
        if num.count('0') == 1:
            if all(p not in num for p in '10 01 30 03 50 05 70 07'.split()):
                cnt += 1
print(cnt)
'''


#
# № 18260 (Уровень: Базовый)
'''
from itertools import product
cnt = 0
s = '0123456789AB'
for p in product('0123456789AB', repeat=6):
    num = ''.join(p)
    if num[0] != '0':
        if num.count('B') == 1:
            chet = [x for x in num if x in '02468A']
            nechet = [x for x in num if x in s[1::2]]
            if len(chet) == len(nechet):
                cnt += 1
print(cnt)
'''

# Генераторы списков
'''
R = [int(input('x: ')) for i in range(int(input('Кол-во элементов: ')))]
print(R)

n = int(input('Кол-во элементов: '))
R = []
for i in range(n):
    x = int(input('x: '))
    R.append(x)
print(R)

# ГЕНЕРАТОР[что_берем откуда_берем]
# ГЕНЕРАТОР[что_берем откуда_берем при_каком_условии]

num = '982347983274'
chet = [x for x in num if x in '02468']
print(chet)  # ['8', '2', '4', '8', '2', '4']


num = '982347983274'
chet = [x*3 for x in num if x in '02468']
print(chet)  # ['888', '222', '444', '888', '222', '444']
'''


#
# № 6479 (Уровень: Базовый)
'''
from itertools import permutations
cnt = 0
for p in permutations('КАРПЫ', r=5):
    word = ''.join(p)
    if 'АЫ' not in word and 'ЫА' not in word:
        # if 'Р' != word[0] and 'Р' != word[-1]:
        if 'Р' not in word[0] + word[-1]:
            cnt += 1
print(cnt)
'''

# № 20833 (Уровень: Средний)
'''
from itertools import product
n = 0
for p in product('0123456789', repeat=5):
    num = ''.join(p)
    if num[0] != '0':
        n += 1
        if n % 15 == 0:
            for x in '02468':
                num = num.replace(x, '2')
            for x in '13579':
                num = num.replace(x, '1')
            if '22' not in num and '11' not in num:
                print(n)
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8]
# КЕГЭ = []
# на следующем уроке:
