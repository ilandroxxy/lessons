# region Домашка: ******************************************************************


# https://education.yandex.ru/ege/task/cf899119-5ce5-4245-b13a-33214cacb8e9
'''
from itertools import *
cnt = 0
for p in product('0123456789ABCDE', repeat=5):
    word = ''.join(p)
    if word[0] != '0':
        a, b, c, d, e = [int(x, 15) for x in word]
        N1 = [a % 2 == 0, b % 3 == 0, c % 2 == 0, d % 3 == 0, e % 2 == 0]
        N2 = [a % 3 == 0, b % 2 == 0, c % 3 == 0, d % 2 == 0, e % 3 == 0]
        if sum(N1) == 5 or sum(N2) == 5:
            cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/task/ddce5ec5-c1e4-4e47-94a2-f5e19c7519dd
'''
from itertools import *

s = '0123456789'
cnt = 0
for p in product(s1, s2, s1, s2, s, s, s, s, s):
    print(p)
    word = ''.join(p)
    if word[0] != '0':
        not_copied = [x for x in word if word.count(x) == 1]
        if len(not_copied) >= 3:
            cnt += 1
print(cnt)'''


'''
import time
start = time.time()

cnt = 0
for x in range(100000000, 1000000000):
    if len(set(str(x))) >= 3:
        cnt += 1
print(cnt)

print(time.time() - start)


from itertools import permutations

R = []
for p in permutations('ХАЧАНАБАДЖАТ'):
    word = ''.join(p)
    if word.count('ААААА') == 0:
        R.append(word)
print(len(set(R)))
'''


from itertools import *
n = 0
for p in permutations('01234567', 5):
    num = ''.join(p)
    if num[0] != '0' and num.count('1') == 0:
        num = num.replace('3', '*').replace('5', '*').replace('7', '*')
        num = num.replace('2', '+').replace('4', '+').replace('6', '+').replace('0', '+')
        if '++' not in num and '**' not in num:
            n += 1
print(n)

from itertools import product

cnt = 0
for p in product('01234567', repeat=5):
    word = ''.join(p)
    if word[0] != '0' and word.count('1') == 0:
        if len(word) == len(set(word)):
            for i in '0246':
                word = word.replace(i, '0')
            for i in '1357':
                word = word.replace(i, '1')
            if '00' not in word and '11' not in word:
                cnt += 1
print(cnt)



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
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ  = [8]
# на следующем уроке:

