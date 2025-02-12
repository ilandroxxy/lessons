# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Номер 5
'''
R = []
for n in range(1, 10000):
    n2 = bin(n)[2:]
    if n2.count('0') % 2 == 0:
        n2 = '1' + n2 + '1'
    else:
        n2 = '10' + n2
    r = int(n2, 2)
    if r < 100:
        R.append(r)
print(max(R))
'''


# Номер 8
'''
from itertools import permutations
my_set = set()
for p in permutations('ПАРИЖАНКА'):
    word = ''.join(p)
    D = [1 for i in range(len(word)-1) if word[i:i+2] in ('ИА', 'АИ', 'АА')]
    if sum(D) == 1:
        my_set.add(word)

print(len(my_set))


from itertools import permutations
my_set = set()
for p in permutations('ПАРИЖАНКА'):
    word = ''.join(p)
    new_word = word.replace('И',  'А')
    if new_word.count('АА') == 1 and 'ААА' not in new_word:
        my_set.add(word)
print(len(my_set))
'''


'''
def f(x, y, c):
    if x > y:
        return 0
    elif x == y:
        c = c.split()
        return 1 and (not('20' in c and '30' in c))
    return f(x + 2, y, c + ' ' + str(x)) + f(x + 3, y, c + ' ' + str(x)) + f(x * 2, y, c + ' ' + str(x))


print(f(8, 35, ''))


def f(x, y, c):
    if x >= y:
        c = c.split()
        return x == y and (not('20' in c and '30' in c))
    return f(x + 2, y, c + ' ' + str(x)) + f(x + 3, y, c + ' ' + str(x)) + f(x * 2, y, c + ' ' + str(x))


print(f(8, 35, ''))


# Не должно в траектории быть команды BACA
def f(x, y, c):
    if x >= y or x == 28:
        return x == y and 'BACA' not in c
    return f(x + 2, y, c + 'A') + f(x + 3, y, c + 'B') + f(x * 2, y, c + 'C')


print(f(2, 40, ''))
'''

'''
f = open('24.txt').readline().strip()

f = f.replace('WSFWW','i')

z = f.split('i')

print(z)

otv = []

for s in z:
    #q = s.replace('WWF','x')

    if s.count('WWF')<=120:
        print(len(s),s)
        otv.append(len(s))

print(max(otv))
'''
'''
s = open('0. files/24.txt').readline()
s = s.split('WSFWW')
maxi = 0
for i in range(len(s)-120):
    r = 'SFWW' + 'WSFWW'.join(s[i:i+1]) + 'WSFW'
    maxi = max(maxi, len(r))
print(maxi)
'''

# 'WSFWWxxxxxxWSFWWxxxxxxxxWSFWW'
# 'SFWWxxxxxxWSFWWxxxxxxxxWSFW'
# 'xxxxxxWSFWWxxxxxxxx'

'''
s = 'TxxxxxTxxxxTxxxxxTxxxxxTxxxxTxxxxxxTxxxxxT'
# ['', 'xxxxx', 'xxxx', 'xxxxx', 'xxxxx', 'xxxx', 'xxxxxx', 'xxxxx', '']
# 17 TxxxxxTxxxxTxxxxx
# 22 xxxxxTxxxxTxxxxxTxxxxx
# 21 xxxxTxxxxxTxxxxxTxxxx
# 23 xxxxxTxxxxxTxxxxTxxxxxx
# 23 xxxxxTxxxxTxxxxxxTxxxxx
# 18 xxxxTxxxxxxTxxxxxT
s = s.split('T')
for i in range(len(s)-3):
    r = 'T'.join(s[i:i+4])
    print(len(r), r)
'''


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# todo Широковещательный адрес изучить

# номер 13
'''
from ipaddress import *

ip1 = '158.214.121.40'
mask = '255.255.255.224'
net = ip_network(ip1+'/'+mask, 0)
print(net.num_addresses)
cnt = 0
for ip in net:

    print(ip)
    cnt += 1
print(cnt)
print(net.broadcast_address)
'''
# 158.214.121.63
# 11111111.11111111.11111111.11100000

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = []
# КЕГЭ  = []
# на следующем уроке: 8, 9, 11, 13, 17, 18, 11, 25

# Первый пробник 5.02.24:
# Ангелина 11/27 -> 54 вторичных баллов +[1-5, 7, 14-16, 20-21] -[6, 8, 9, 10, 11, 12, 13, 17, 18, 19, 22, 23, 25]
# Сергей 16/27 -> 67 вторичных баллов +[1-6, 10, 12, 14, 15, 16, 19-21, 23, 24] -[7, 8, 9, 11, 13, 17, 18, 22, 25]
