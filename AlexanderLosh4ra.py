# region Домашка: ******************************************************************

'''
import itertools
M = ['1' * 20, '2' * 15, '3' * 40]
for var in itertools.permutations(M):
    s = '>' + ''.join(var) + '<'
    old_s = s

    while '><' not in s:
        s = s.replace('>1', '3>', 1)
        s = s.replace('>2', '2>', 1)
        s = s.replace('>3', '1>', 1)
        s = s.replace('3<', '<1', 1)
        s = s.replace('2<', '<3', 1)
        s = s.replace('1<', '<2', 1)
    summ = sum([int(x) for x in s if x.isdigit()])
    print(summ, old_s)
'''

'''
M = ['1' * 20 + '2' * 15 + '3' * 40,
     '1' * 20 + '3' * 40 + '2' * 15,
     '3' * 40 + '1' * 20 + '2' * 15]
for elem in M:
    s = '>' + elem + '<'
    while '><' not in s:
        s = s.replace('>1', '3>', 1)
        s = s.replace('>2', '2>', 1)
        s = s.replace('>3', '1>', 1)
        s = s.replace('3<', '<1', 1)
        s = s.replace('2<', '<3', 1)
        s = s.replace('1<', '<2', 1)
    summa = sum([int(x) for x in s if x.isdigit()])
    print(summa)
'''


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Тип 8 №3233
'''
s = sorted('АКРУ')
num = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    num += 1
                    if num == 250:
                        print(slovo)

from itertools import *
num = 0
for per in product(sorted('АКРУ'), repeat=5):
    slovo = ''.join(per)
    num += 1
    if num == 250:
        print(slovo)

from itertools import *
for num, per in enumerate(product(sorted('АКРУ'), repeat=5), 1):
    slovo = ''.join(per)
    if num == 250:
        print(slovo)
'''

'''
# i       0    1    2    3
array = ['a', 'b', 'c', 'd']

for i, elem in enumerate(array):
    print(i, elem)
    # 0 a
    # 1 b
    # 2 c
    # 3 d

for i, elem in enumerate(array, 1):
    print(i, elem)
    # 1 a
    # 2 b
    # 3 c
    # 4 d
'''


# Тип 8 №18079
# Вася составляет 6-буквенные слова из букв К, О, Т.
# Причем буква К используется в каждом слове ровно 1 раз.
# Остальные буквы могут быть использованы любое количество раз,
# в том числе совсем отсутствовать. Сколько слов может составить Вася?\
'''
s = 'КОТ'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        slovo = a + b + c + d + e + f
                        if slovo.count('К') == 1:
                            cnt += 1
print(cnt)


from itertools import *
cnt = 0
for per in product('КОТ', repeat=6):

    slovo = ''.join(per)  # ('Т', 'Т', 'Т', 'Т', 'К', 'О') -> 'ТТТТКО'
    if slovo.count('К') == 1:
        cnt += 1
print(cnt)
'''


# Тип 8 №7667
# Сколько слов длины 5, начинающихся с гласной буквы, можно
# составить из букв Е, Г, Э? Каждая буква может входить в слово несколько раз.
# Слова не обязательно должны быть осмысленными словами русского языка.
'''
from itertools import *
cnt = 0
for per in product('ЕГЭ', repeat=5):
    slovo = ''.join(per)
    if slovo[0] in 'ЕЭ':
        cnt += 1
print(cnt)


from itertools import product
print([slovo[0] in 'ЕЭ' for slovo in product('ЕГЭ', repeat=5)].count(True))
'''


# Тип 8 №27539
# Борис составляет 6-буквенные коды из букв Б, О, Р, И, С.
# Буквы Б и Р нужно обязательно использовать ровно по одному разу,
# букву С можно использовать один раз или не использовать совсем,
# буквы О и И можно использовать произвольное количество раз или не использовать совсем.
# Сколько различных кодов может составить Борис?
'''
from itertools import *
cnt = 0
for per in product('БОРИС', repeat=6):
    slovo = ''.join(per)
    if slovo.count('Б') == 1 and slovo.count('Р') == 1 and slovo.count('С') <= 1:
        cnt += 1
print(cnt)
'''


# Тип 8 №59746
# Сколько существует десятичных чисел, которые делятся на 5,
# при условии что все цифры числа различные?

'''
from itertools import permutations
word = '0123456789'
c = 0
for j in range(1, 11):
    for i in permutations(word, j):
        x = ''.join(i)
        if x[0] != '0' and (x[-1] == '5' or x[-1] == '0'):
            c += 1
print(c + 1)  # +1 случай когда число равно 0

from itertools import *
cnt = 0
for m in range(1, 11):
    for per in permutations('0123456789', m):
        if per[0] != '0' and per[-1] in '05':
            cnt += 1
print(cnt + 1)  # +1 случай когда число равно 0
'''

# Тип 8 №58237
# Сколько существует различных четырёхзначных чисел,
# записанных в семеричной системе счисления,
# в записи которых цифры следуют слева направо в строго убывающем порядке?
'''
from itertools import *
cnt = 0
for per in product('0123456', repeat=4):
    num = ''.join(per)
    if num[0] != '0':
        if num[0] > num[1] > num[2] > num[3]:
            cnt += 1
print(cnt)
'''

# Тип 8 №59742
# Определите количество четырехзначных чисел, записанных в десятичной системе счисления,
# в записи которых все цифры различны и никакие две чётные и две нечётные цифры не стоят рядом.
'''
from itertools import *
cnt = 0
for per in permutations('0123456789', 4):
    num = ''.join(per)
    if num[0] != '0':
        #  никакие две чётные и две нечётные цифры не стоят рядом.
        num = num.replace('0', '2').replace('4', '2').replace('6', '2').replace('8', '2')
        num = num.replace('3', '1').replace('5', '1').replace('7', '1').replace('9', '1')
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
