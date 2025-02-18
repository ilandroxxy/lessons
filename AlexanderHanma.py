# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 18591 (Уровень: Средний)
'''
from fnmatch import *
for i in range(1984, 10**10, 1984):
    s = str(i)
    if fnmatch(s, f'?9?23?*23??'):
        if s[0] in '02468' and s[-1] in '02468' and s[-2] in '13579':
            print(i, i // 1984)
'''


'''
from fnmatch import *
for i in range(1984, 10**10, 1984):
    s = str(i)
    if fnmatch(s, f'?9?23?*23??'):
        if any((s[0] == y and s[-1] == z and s[-2] == x) for x in '13579' for y in '02468' for z in '02468'):
                print(i, i//1984)

for x in '13579':
    for y in '02468':
        for z in '02468':
            print(x, y, z)
'''


# № 19482 (Уровень: Средний)
'''
symbols1 = 17
alphabet1 = 26
i1 = 5
bit1 = symbols1 * i1


symbols2 = 1
alphabet2 = 365
i2 = 9
bit2 = symbols2 * i2

bit = bit1 + bit2
print(bit / 8)  # 11.75
byte = 12

# V = byte + dop
V = (2500 / 50) - byte
print(V)  # 38
'''

'''
from turtle import *
# screensize(-1000,1000)

left(90)
l=15
for i in range(4):
    fd(27*l)
    rt(90)
    fd(21*l)
    rt(90)
up()
fd(3*l)
rt(90)
fd(7*l)
lt(90)
down()
for i in range(4):
    fd(73*l)
    rt(90)
    fd(91*l)
    rt(90)
up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*l,y*l)
        dot(3, 'red')

done()
'''


# № 19483 (Уровень: Средний)
'''
for n in range(4, 10000):
    s = '2' + n * '5'
    while '25' in s or '355' in s or '555' in s:
        if '25' in s:
            s = s.replace('25', '5', 1)
        if '355' in s:
            s = s.replace('355', '522', 1)
        if '555' in s:
            s = s.replace('555', '3', 1)
    if s.count('2') == 10:
        print(n)
        break
'''

# № 19487 (Уровень: Средний)
'''
def F(a, b):
    if a >= b:
        return a == b
    return F(a + 2, b) + F(a + 3, b) + F(a * 2, b)


print(F(8, 35) - (F(8, 20) * F(20, 30) * F(30, 35)))
'''

'''
def F(a, b, c):
    if a >= b:
        c = c.split()
        return a == b and (not('20' in c and '30' in c))
    return F(a + 2, b, c+' '+str(a)) + F(a + 3, b, c+' '+str(a)) + F(a * 2, b, c+' '+str(a))

print(F(8, 35, ''))
'''

# № 19489 (Уровень: Средний)
'''
maxi = 0
s = open('0. files/24.txt').readline()
s = s.split('WWF')
for i in range(len(s) - 106):
    r = 'WWF'.join(s[i:i + 107])
    if 'WSFWW' not in r:
        maxi = max(maxi, len(r))
print(maxi + 6)


maxi = 0
s = open('0. files/24.txt').readline()
s = s.split('WWF')
for i in range(len(s) - 120):
    r = 'WF' + 'WWF'.join(s[i:i + 121]) + 'WW'
    maxi = max(maxi, max([len(x) for x in r.replace('WSFWW', 'WSFW SFWW').split()]))
print(maxi)
'''

# endregion Урок: ********************************************************************
# #
# #
# region Разобрать: ********************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ  = [5, 9, 14, 15, 16, 17, 22, 23]
# на следующем уроке:


# Первый пробник 21.12.24:
# Александр 19/25 -> 75 вторичных баллов +[1-5, 7, 9-10, 12, 14-16, 18-22, 24, 25] -[6, 8, 11, 13, 17, 23]
# Саша
