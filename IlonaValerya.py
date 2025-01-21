# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
for n in range(4, 1000):
    s = '1' + '8' * n
    while '18' in s or '388' in s or '888' in s:
        if '18' in s:
            s = s.replace('18', '8', 1)
        if '388' in s:
            s = s.replace('388', '81', 1)
        if '888' in s:
            s = s.replace('888', '3', 1)
    if s.count('1') == 3:
        print(n)
'''

'''
from ipaddress import*
for mask in range(33):
    net = ip_network(f'213.168.83.190/{mask}', 0)
    if '213.168.64.0' in str(net):
        print(net.netmask, mask, 32-mask)
        # 255.255.192.0 18
        # 255.255.224.0 32-19 =
'''

'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

for x in alphabet[:23]:
    A = int(f'7{x}38596',23)
    B = int(f'14{x}36',23)
    C = int(f'61{x}7',23)
    if (A + B + C)% 22 == 0:
        print((A+B+C)//22)
'''


# № 10707 (Уровень: Средний)
'''
def convert(n, b):
    s = ''
    while n > 0:
        s = s + str(n % b)
        n = n // b
    return s[::-1]


R = []
for n in range(6, 1000):
    r = convert(n, 6)
    if n % 3 == 0:
        r += r[0] + r[1]  # r[:2]
    else:
        x = (n % 3) * 10
        r = r + convert(x, 6)
    res = int(r, 6)
    if res > 680:
        R.append(res)
print(min(R))
'''

# Прототип 25 номера с масками
'''
from fnmatch import *
for x in range(2025, 10**8, 2025):
    if fnmatch(str(x), '12*34?5'):
        print(x, x//2025)
'''


# № 18133 (Уровень: Базовый)
'''
s = sorted('КОДИМ')
n = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    word = a + b + c + d + e
                    n += 1
                    if word.count('М') == 2:
                        if 'ММ' not in word:
                            print(n)
'''


#
# № 18042 (Уровень: Базовый)
'''
s = 'ЛЮСТРА'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    word = a + b + c + d + e
                    if word.count('Ю') <= 2:
                        if word[-1] not in 'ЛСТР':
                            cnt += 1
print(cnt)
'''


# № 16255 Джобс 03.05.24 (Уровень: Средний)
'''
s = '012345678'
cnt = 0
for a in '02468':  # не начинаются с нечетных цифр
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        for g in s:
                            word = a + b + c + d + e + f + g
                            if int(word[-1]) % 3 != 0:
                                if word[0] != '0':
                                    if '6' in word:
                                        cnt += 1
print(cnt)
'''


'''
s = '0123456789ABCD'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    word = a + b + c + d + e
                    if word[0] != '0':
                        if len(set(word)) == 2:
                            if word[-1] in '03':
                                cnt += 1
print(cnt)


from itertools import *
cnt = 0
for p in product('0123456789ABCD', repeat=5):
    word = ''.join(p)
    if word[0] != '0':
        if len(set(word)) == 2:
            if word[-1] in '03':
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
# ФИПИ = [2, 5, 6, 8, 12, 13, 14, 25]
# КЕГЭ  = []
# на следующем уроке:
