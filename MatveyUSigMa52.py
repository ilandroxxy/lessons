# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Номер 5
'''
def covert(n, b):
    s = ''
    while n > 0:
        s = s + str(n % b)
        n = n // b
    return s[::-1]


m = []
for n in range(1, 1000):
    s = covert(n, 3)
    if n % 3 == 0:
        s = s + s[-3:]
    else:
        s = s + covert((n%3)*3, 3)
    r = int(s, 3)
    if r > 150:
        m.append(n)
print(min(m))
'''


# Номер 12
'''
summa=0
for n in range(3,10000):
    s='5'+'2'*n
    while '52' in s or '1122' in s or '2222' in s:
        if '52' in s:
            s=s.replace('52','11',1)
        if '2222' in s:
            s=s.replace('2222','5',1)
        if '1122' in s:
            s=s.replace('1122','25',1)

    summa = s.count('1') + s.count('2') * 2 + s.count('5') * 5

    summa = 0
    for x in s:
        summa += int(x)

    summa = sum([int(x) for x in s])

    summa = sum(map(int, s))

    if summa == 64:
        print(n)
        break
'''


# Номер 8
'''
from itertools import *

n = 0
m = []
for p in product(sorted('СБОРНИК'), repeat=6):
    word = ''.join(p)
    n = n + 1
    if word.count('Б') == 2 and word.count('К') <= 1 and word[0] != 'Р':
        m.append(n)
print(max(m))
'''


# Номер 13
'''
from ipaddress import *
for mask in range(33):
    net=ip_network(f'111.118.179.50/{mask}',0)
    if '111.118.178.0' in str(net):
        print(net.netmask)
'''

# Номер 9
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied2 = [x for x in M if M.count(x) == 2]
    uncopied = [x for x in M if M.count(x) == 1]
    if len(copied2) == 4 and len(uncopied) == 3:
        if sum(copied2) / 4 < sum(uncopied) / 3:
            cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/task/9a4ed264-8f61-4713-91c3-37fceb735e15
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    flag = 0
    if len(M) == len(set(M)):
        flag += 1
    if max(M) > sum(M) - max(M):
        flag += 1
    if flag == 1:
        cnt += 1
print(cnt)
'''

# endregion Урок: ********************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1.1, 2, 5, 6, 8, 12, 13, 14, 15, 16, 23, 25]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Матвей 10/14 -> 51 вторичных баллов +[1, 3, 4, 6, 7, 10, 11, 14, 18, 25] -[2, 5, 8, 12]

# Второй пробник 28.02.25:
# Матвей 14/29 -> 62 вторичных баллов +[1-4, 6, 7, 10, 11, 14, 15, 16, 18, 23, 25] -[5, 8, 12, 13]
