# region Домашка: ******************************************************************

# № 11228 (Уровень: Сложный) 🌶
'''
from itertools import *

summa = 0
for s in open('0. files/9.csv'):
    M = sorted([int(x) for x in s.split(',')])
    povt3 = [x for x in M if M.count(x) == 3]
    povt2 = [x for x in M if M.count(x) == 2]
    if len(povt3) == 3 and len(povt2) == 4:
        if any((((p[0] + p[1]) % 2 != 0) + ((p[2] + p[3]) % 2 != 0)) == 2 for p in permutations(M[:4])):
            summa += sum(M)
print(summa)
'''

# № 9778 Основная волна 20.06.23 (Уровень: Средний)
'''
n = 0
for s in open('0. files/9.csv'):
    n += 1
    M = sorted([int(x) for x in s.split(',')])

    copied2 = [x for x in M if M.count(x) == 2]
    not_copied = [x for x in M if M.count(x) == 1]
    if len(copied2) == 2 and len(not_copied) == 4:
        if sum(copied2) / 2 >= sum(not_copied) / 4:
            print(n)
            break
'''


# № 9539  (Уровень: Средний)
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = sorted([int(x) for x in s.split(',')])
    b = [x for x in M if M.count(x) == 2]
    n = [x for x in M if M.count(x) == 1]
    if len(b) == 4 and len(n) == 1:
        if n[0] == M[2]:
            cnt += 1
print(cnt)
'''

# i           0   1   2  3  4
# M = sorted([14, 14, 8, 9, 9])

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# https://education.yandex.ru/ege/task/a63bca73-d464-4237-a1f3-60131bbbee77
'''
s = open('0. files/24.txt').readline()
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

count = 1
maxi = 0
new_s = ' '
for i in range(len(s)-1):
    count += 1

    if s[i] in alphabet[:16] and s[i] not in new_s:
        if s[i] > max(new_s):
            new_s += s[i]
            maxi = max(maxi, count)
        else:
            new_s = ' '
            count = 1
print(maxi)
'''

'''
s = 'xxxxxTxxxxTxxxxxTxxxxxTxxxxTxxxxTxxxxxTxxxx'
# ['xxxxx', 'xxxx', 'xxxxx', 'xxxxx', 'xxxx', 'xxxx', 'xxxxx', 'xxxx']
# 22 xxxxxTxxxxTxxxxxTxxxxx
# 21 xxxxTxxxxxTxxxxxTxxxx
# 21 xxxxxTxxxxxTxxxxTxxxx
# 21 xxxxxTxxxxTxxxxTxxxxx
# 20 xxxxTxxxxTxxxxxTxxxx
s = s.split('T')
maxi = 0
for i in range(len(s)-3):
    r = 'T'.join(s[i:i+4])
    print(len(r), r)
    maxi = max(maxi, len(r))
print(maxi)
'''

# № 10105 Демоверсия 2024 (Уровень: Средний)
'''
s = open('0. files/24.txt').readline()
s = s.split('T')
maxi = 0
for i in range(len(s)-100):
    r = 'T'.join(s[i:i+101])
    maxi = max(maxi, len(r))
print(maxi)'''


# № 13715 (Уровень: Средний)

'''
s = open('0. files/24.txt').readline()
s = s.split('AB')
maxi = 0
for i in range(len(s)-50):
    r = 'B' + 'AB'.join(s[i:i+51]) + 'A'
    maxi = max(maxi, len(r))
print(maxi)
'''

# https://education.yandex.ru/ege/task/764352cd-1971-4c8f-ac18-f74a63b9e5f2
'''
s = open('0. files/24.txt').readline()
s = s.replace('C', 'D').replace('F', 'D')
s = s.replace('O', 'A')
s = s.split('DA')
maxi = 0
for i in range(len(s)-5):
    r = 'A' + 'DA'.join(s[i:i+6]) + 'D'
    maxi = max(maxi, len(r))
print(maxi)
'''

# № 13100 (Уровень: Средний)
'''
s = open('0. files/24.txt').readline()
s = s.replace('C', 'C ').replace('D', 'D ')
s = s.split()
maxi = 0
for i in range(len(s)-5):
    r = ''.join(s[i:i+5])[:-1]
    if r.count('C') == 2 and r.count('D') == 2:
        maxi = max(maxi, len(r))
print(maxi)
'''

# https://education.yandex.ru/ege/task/b80b725b-df8b-407d-b120-941e53aa5df9
'''
s = open('0. files/24.txt').readline()
s = s.replace('A', 'A ').replace('O', 'O ')
s = s.split()
maxi = 0
for i in range(len(s)-201):
    r = ''.join(s[i:i+201])[:-1]
    if r.count('A') == 100 and r.count('O') == 100:
        maxi = max(maxi, len(r))
print(maxi)
'''


s = open('0. files/24.txt').readline()
print(s)
s = s.replace('XA', '**').replace('XY', '++').replace('TXA', '---')
s = s.upper()
for x in '0123456789QWERTYUIOPASDFGHJKLZXCVBNM':
    s = s.replace(x, ' ')
print(max([len(x) for x in s.split()]))

# endregion Урок: ********************************************************************
# #
# #
# region Разобрать: ********************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ  = [5, 9, 14, 15, 16, 17, 22, 23]
# на следующем уроке:


# Первый пробник 21.12.24:
# Александр 19/25 -> 75 вторичных баллов +[1-5, 7, 9-10, 12, 14-16, 18-22, 24, 25] -[6, 8, 11, 13, 17, 23]
# Саша
