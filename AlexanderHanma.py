# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Задач 6
'''
from turtle import *
screensize(-10000, 10000)
tracer(0)
left(90)
l = 40
rt(90)
for i in range(3):
    rt(45)
    fd(10*l)
    rt(45)
rt(315)
fd(10*l)
for i in range(2):
    rt(90)
    fd(10*l)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*l, y*l)
        dot(2, 'red')
done()
'''

# Задача 5
'''
def convert(n, b):
    r = ''
    while n > 0:
        r += str(n % b)
        n //= b
    return r[::-1]


R = []
for n in range(1, 1000):
    s = convert(n, 3)
    if n % 3 == 0:
        s = '1' + s + '02'
    else:
        x = (n % 3) * 4
        s += convert(x, 3)
    r = int(s, 3)
    if r < 199:
        R.append(n)
print(max(R))
'''


# Задача 8
'''
from itertools import *
cnt = 0
for p in product('0123456789ABCDEF', repeat=3):
    s = ''.join(p)
    if s[0] != '0':
        if len(set(s)) == len(s):
            for x in '02468ACE':
                s = s.replace(x, '2')
            for x in '13579BDF':
                s = s.replace(x, '1')
            if '11' not in s and '22' not in s:
                cnt += 1
print(cnt)


from itertools import *
cnt = 0
for p in permutations('0123456789ABCDEF', r=3):
    s = ''.join(p)
    if s[0] != '0':
        for x in '02468ACE':
            s = s.replace(x, '2')
        for x in '13579BDF':
            s = s.replace(x, '1')
        if '11' not in s and '22' not in s:
            cnt += 1
print(cnt)


from itertools import *
cnt1 = 0
cnt2 = 0
s1 = '13579BDF'
s2 = '02468ACE'
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for p in permutations(alp[:16], r=3):
    s = ''.join(p)
    if s[0] != '0':
        if s[0] in s1 and s[1] in s2 and s[2] in s1:
            cnt1 += 1
        if s[0] in s2 and s[1] in s1 and s[2] in s2:
            cnt2 += 1
print(cnt1, cnt2)
'''

# Задача 11
'''
symb = 10
al = 52
V = 65536
i = 6
b = symb*i
# минимально возможное целое число байт.
print(b / 8)  # 7.5 -> 8
byte = 8
print((byte*V) // 2**10)  # 512.0
'''


# Задание 13
'''
from ipaddress import *
for mask in range(33):
    net = ip_network(f'213.168.83.190/{mask}', 0)
    # if str(net.network_address) == '213.168.64.0':
    if '213.168.64.0' in str(net):
        print(32 - mask)
        # 14
        # 13
'''

# Задание 14
'''
R = []
alp = sorted('1234567890QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alp[:23]:
    s = int(f'7{x}38596', 23)
    a = int(f'14{x}36', 23)
    x = int(f'61{x}7', 23)
    if (s + a + x) % 22 == 0:
        R.append(s // 22)
print(min(R))  # 53581385
'''


# Задание 15
'''
def f(x, y, A):
    return (x + 2 * y > A) or (y < x) or (x < 30)


R = []
for A in range(1, 1000):
    if all(f(x, y, A) for x in range(100) for y in range(100)):
        R.append(A)
print(max(R))
'''




# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# todo Разобрать как быть с гласными https://education.yandex.ru/ege/task/bdfb8f12-2b10-4f4b-99b0-6d2e045552e2
'''
s = open('files/24.txt').readline()
for x in 'AEIOUY':
    s = s.replace(x, ' ')
s = s.split()
print(s)
maxi = 0
for i in range(len(s)-1):
    r = s[i] + s[i+1]
    if list(r) == sorted(r):
        if len(r) + 1 > maxi:
            maxi = len(r) + 1
print(maxi)
'''

# Разбираем сложный 24 номер
'''
# максимальное количество идущих подряд символов Y встречается не более 3 раз.
s = 'xxxxYxxxYxxxxxYxxxYxxxxxYxxxYxxxxxYxxxxxYxxx'
# ['xxxx', 'xxx', 'xxxxx', 'xxx', 'xxxxx', 'xxx', 'xxxxx', 'xxxxx', 'xxx']
# 18 xxxxYxxxYxxxxxYxxx
# 19 xxxYxxxxxYxxxYxxxxx
# 19 xxxxxYxxxYxxxxxYxxx
# 19 xxxYxxxxxYxxxYxxxxx
# 21 xxxxxYxxxYxxxxxYxxxxx
# 19 xxxYxxxxxYxxxxxYxxx

s = s.split('Y')
maxi = 0
for i in range(len(s)-3):
    r = 'Y'.join(s[i:i+4])  # i, i+1, i+2, i+3
    print(len(r), r)
    maxi = max(maxi, len(r))
print(maxi)


s = open('files/24.txt').readline()
s = s.split('Y')
maxi = 0
for i in range(len(s)-150):
    r = 'Y'.join(s[i:i+151])  # i, i+1, i+2, i+3, ...., i+150
    maxi = max(maxi, len(r))
print(maxi)
'''

# № 19254 ЕГКР 21.12.24 (Уровень: Базовый)
# Текстовый файл состоит из символов F, G, Q, R, S и W.
# Определите в прилагаемом файле максимальное количество идущих
# подряд символов, среди которых подстрока FSRQ встречается ровно 80 раз.
'''
s = open('files/24.txt').readline()
s = s.split('FSRQ')
maxi = 0
for i in range(len(s)-80):
    r = 'SRQ' + 'FSRQ'.join(s[i:i+81]) + 'FSR'  # i, i+1, i+2, i+3, ...., i+80
    maxi = max(maxi, len(r))
print(maxi)

# Ответ: 2379 - 2373 = 6

# (len('FSRQ') - 1) * 2 = 6
# (len('FSRQI') - 1) * 2 = 8

# максимальное количество идущих подряд символов FSRQ встречается не более 3 раз.
s = 'xxxxFSRQxxxFSRQxxxxxFSRQxxxFSRQxxxxxFSRQxxxFSRQxxxxxFSRQxxxxxFSRQxxx'
# ['xxxx', 'xxx', 'xxxxx', 'xxx', 'xxxxx', 'xxx', 'xxxxx', 'xxxxx', 'xxx']

s = s.split('FSRQ')
maxi = 0
for i in range(len(s)-3):
    r = 'SRQ' + 'FSRQ'.join(s[i:i+4]) + 'FSR'  # i, i+1, i+2, i+3
    print(len(r), r)
    maxi = max(maxi, len(r))
print(maxi)
'''
# Ответ: 36 - 30 = 6

'''
l=[]
s = open('C:/24.txt').readline()
maxi = 0
while '' in s or '*+' in s or  '++' in s or  '+*' in s:
    for x in ' ++ +* *+'.split():
        s = s.replace(x, ' ')
for i in s.split():
    if i[0] in '*+':
        i = i[1:]
    if i[-1] in '*+':
        i = i[:-1]
    if len(i) == 168:
        l.append([(i)])
print(l)
'''

print(eval('(45 + 65) * 2'))


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Александр 19/25 -> 75 вторичных баллов +[1-5, 7, 9-10, 12, 14-16, 18-22, 24, 25] -[6, 8, 11, 13, 17, 23]
# Саша
