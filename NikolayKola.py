# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************
'''
from ipaddress import *
M = []
for mask in range(33):
    net1 = ip_network(f'10.96.180.231/{mask}', 0)
    net2 = ip_network(f'10.96.140.118/{mask}', 0)
    if net1 != net2:
        M.append(32 - mask)
print(max(M))
'''


'''
from ipaddress import *
my_set = set()
for mask in range(33):
    net = ip_network(f'133.57.64.130/{mask}', 0)
    if str(net) == f'133.57.64.0/{mask}':
        print(net, net.netmask)
        my_set.add(net.netmask)
print(len(my_set))
'''

'''
from ipaddress import *

net = ip_network('185.8.0.0/255.255.128.0', 0)
cnt = 0
d = []
for ip in net:
    b = f'{ip:b}'
    d.append(b.count('1'))
print(max(d))
'''

'''
s = sorted('ФОКУС')
num = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    word = a + b + c + d + e
                    num += 1
                    if 'Ф' not in word:
                        if word.count('У') == 2:
                            print(num, word)

from itertools import *
num = 0
for per in product(sorted('ФОКУС'), repeat=5):
    word = ''.join(per)
    num += 1
    if 'Ф' not in word:
        if word.count('У') == 2:
            print(num)
'''
'''
s = '01234567'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    num = a + b + c + d + e
                    if a != '0':
                        if a not in '1357':
                            if e not in '26':
                                if num.count('7') <= 2:
                                    cnt += 1
print(cnt)
'''

'''
s = '0123456'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        for g in s:
                            num = a + b + c + d + e + f + g
                            if a != '0':
                                chet = [x for x in num if x in '0246']
                                if len(chet) == 2:
                                    cnt += 1
print(cnt)
'''
'''
s = '0123456789ABCDE'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    num = a + b + c + d + e
                    if a != '0':
                        if num.count('8') == 1:
                            M = [x for x in num if x in 'ABCDE']
                            if len(M) >= 2:
                                cnt += 1
print(cnt)
'''

'''
cnt = 0
for s in open('9.csv'):
    M = [int(x) for x in s.split(';')]
    if max(M) + min(M) <= sum(M) - max(M) - min(M):
        cnt += 1
print(cnt)


cnt = 0
for s in open('9.txt'):
    M = sorted([int(x) for x in s.split()])
    if M[0] + M[3] <= M[1] + M[2]:
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
# ФИПИ = [1+, 2*+, 3, 4+, 6+, 7, 9*+, 10+, 11, 18+, 19-21, 22+]
# КЕГЭ  = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23]
# на следующем уроке:
