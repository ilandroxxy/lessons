# region Домашка: ******************************************************************


'''
from turtle import *
lt(90)
tracer(0)
l=20
screensize(-10000,10000)
for i in range(3):
    fd(27*l)
    rt(90)
    fd(12*l)
    rt(90)
up()
fd(4*l)
rt(90)
fd(6*l)
lt(90)
down()
for i in range(4):
    fd(83*l)
    rt(90)
    fd(77*l)
    rt(90)
up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*l,y*l)
        dot(3, 'red')
update()
done()
'''


# 17549
'''
from itertools import *

n = 0
for s in product(sorted('ФОКУС'), repeat=5):
    d = ''.join(s)
    n += 1
    if 'Ф' not in d and d.count('У') == 2:
        print(n)
'''


# 17863
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    Z = [x for x in M if M.count(x) == 3]
    E = [x for x in M if M.count(x) == 1]
    if len(Z) == 3 and len(E) == 3:
        if sum(Z) ** 2 > sum(E) ** 2:
            cnt += 1
print(cnt)
'''


# 20807
'''
from ipaddress import *

net = ip_network(f'172.16.192.0/255.255.192.0', 0)
cnt = 0
for ip in net:
    s = f'{ip:b}'
    if s.count('1') % 5 != 0:
        cnt += 1
print(cnt)
'''

'''
from string import *
alphabet = digits + ascii_uppercase
# alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    r = ''
    while n > 0:
        r += alphabet[n % b]
        n //= b
    return r[::-1]

maxi = 0
for x in range (1, 2030+1):
    n = 7**170 + 7**100 - x
    s = convert(n, 7)
    if maxi <= s.count('0'):
        maxi = s.count('0')
        print(x, maxi)
'''

'''
maxi = 0
for x in range (1, 2030+1):
    n = 7**170 + 7**100 - x
    cnt = 0
    while n > 0:
        if n % 7 == 0:
            cnt += 1
        n //= 7
    if maxi <= cnt:
        maxi = cnt
        print(x, maxi)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

#
# № 19712 (Уровень: Средний)
# А. Вычесть 2
# В. Если число четное, Разделить на 2, Иначе Вычесть 7
#
# Сколько существует программ, для которых при исходном числе 40 результатом является число 1
# и при этом никакая команда не повторяется более двух раз подряд?
'''
def F(a, b, c):
    if a <= b:
        return a == b and 'AAA' not in c and 'BBB' not in c
    summa = 0
    summa += F(a - 2, b, c+'A')
    if a % 2 == 0:
        summa += F(a // 2, b, c+'B')
    else:
        summa += F(a - 7, b, c+'B')
    return summa


print(F(40, 1, ''))
'''


# № 19778 (Уровень: Средний)
# Обозначим через F целую часть среднего арифметического всех простых делителей целого числа,
# не считая самого числа.
#
# Напишите программу, которая перебирает целые числа, большие 9 500 000,
# в порядке возрастания и ищет среди них такие, для которых значение F не равно нулю и кратно 813.
# Выведите первые 5 найденных числа в порядке возрастания и справа от каждого числа –
# соответствующее значение F.

def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):  # # не считая самого числа.
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


cnt = 0
for x in range(9_500_000+1, 10**10):
    d = [j for j in divisors(x) if len(divisors(j)) == 0]
    if len(d) > 0:
        F = sum(d) // len(d)
        if F != 0 and F % 813 == 0:
            print(x, F)
            cnt += 1
            if cnt == 5:
                break



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

# Второй пробник 28.02.25:
# Александр 24/25 -> 88 вторичных баллов +[1-10, 12-25] -[11]
# Саша 10/25 -> 51 вторичных баллов +[1, 2, 4, 12, 14-16, 19, 23, 25] -[3, 5, 6-10, 11, 13, 17, 18, 20-22, 24]
