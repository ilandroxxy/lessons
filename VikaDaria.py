# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************



# (PRO100 ЕГЭ) Назовём маской числа последовательность цифр, в которой
# также могут встречаться следующие символы:
#
# — символ «?» означает ровно одну произвольную цифру;
# — символ «*» означает любую последовательность цифр произвольной длины;
# в том числе «*» может задавать и пустую последовательность.
#
# Среди натуральных чисел, не превышающих 107, найдите все простые числа,
# соответствующие маске 3?1111*
'''
from fnmatch import *

def prost(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

for x in range(1, 10**7):
    if fnmatch(str(x), '3?1111*'):
        if prost(x):
            print(x)
'''
from typing import is_protocol

# https://stepik.org/lesson/1228669/step/4?unit=1242202
# Найдите все натуральные числа N, принадлежащие отрезку
# [400_000_000; 600_000_000], которые можно представить в виде,
# N = 2 ** m * 3 ** n где m — чётное число, n — нечётное число.
#  В ответе запишите все найденные числа в порядке возрастания.
'''
R = []
for m in range(0, 30+1, 2):
    for n in range(1, 19+1, 2):
        N = 2 ** m * 3 ** n
        if 400_000_000 <= N <= 600_000_000:
            R.append(N)

for x in sorted(R):
    print(x)
'''


# Статград 16.12.25 Вариант 2 Номер 11
'''
sym = 128

byte = 29 * 2**20 / 335_793
print(byte) # 90.557 -> 90  (отведено не более 29 Мбайт)
bit = 90 * 8

i = bit / sym
print(i)  # 5.625 -> 5  (отведено не более 29 Мбайт)

print(2 ** 5)  # 32
print(2 ** 4 + 1)
'''


# Статград 16.12.25 Вариант 1 Номер 11
'''
sym = 30
alp = 26 * 2 + 10 + 15  # 25 + 52
i = 7

bit = sym * i
print(bit / 8)  # 26.25 -> 27
byte = 27

dop = 28

user = byte + dop

print(2 * 2 ** 20 / user)  # 38130.036
'''


# Статград 16.12.25 Вариант 1 Номер 6
'''
import turtle as t

t.tracer(0)
t.screensize(5000, 5000)
t.left(90)
size = 15

t.right(180)
for i in range(9):
    t.forward(59 * size)
    t.left(90)
    t.forward(84 * size)
    t.left(90)
t.up()
t.forward(18 * size)
t.left(90)
t.forward(38 * size)
t.right(90)
t.down()
for i in range(9):
    t.forward(120 * size)
    t.right(90)
    t.forward(99 * size)
    t.right(90)

t.up()
for x in range(-50, 150):
    for y in range(-50, 50):
        t.goto(x * size, y * size)
        t.dot(2, 'red')

t.update()
t.done()
'''

# Статград 16.12.25 Вариант 1 Номер 8
# Определите количество 16-ричных шестизначных чисел, в записи которых
# содержится не менее одной цифры 5 и ровно две цифры с числовым
# значением, превышающим 12, причём стоящие рядом.
'''
cnt = 0
from itertools import *
for i in product('0123456789ABCDEF', repeat = 6):
    word = ''.join(i)
    if word[0] != '0':
        if word.count('5') >= 1:
            for x in 'DEF':
                word = word.replace(x, 'D')
            if word.count('DD') == 1 and word.count('D') == 2:
                cnt += 1
print(cnt)
'''

# Вариант 2
'''
K = []
for x in 'DEF':
    for y in 'DEF':
        K.append(x + y)

from itertools import *
cnt = 0
for i in product('0123456789ABCDEF', repeat = 6):
    word = ''.join(i)
    if word[0] != '0':
        if word.count('5') >= 1:
            k = 0
            for x in K:
                if x in word:
                    k += 1
            if k == 1:
                M = [p for p in word if p in 'DEF']
                if len(M) == 2:
                    cnt += 1
print(cnt)
'''


# Статград 16.12.25 Вариант 1 Номер 9
'''
n = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    chet = [x for x in M if x % 2 == 0]
    nechet = [x for x in M if x % 2 != 0]
    n += 1
    if M == sorted(set(M)):
        if len(chet) == len(nechet):
            print(n, sum(M))
'''


'''
from re import *
for x in range(2026, 10 ** 10, 2026):
    if fullmatch('7[02468]23[02468]64[0-9]*8', str(x)):
        print(x)
'''


# todo глянуть интересный 24 номер статград
'''
from re import *
s = open('files/24.txt').readline()
# s = 'AC12BDE3F2ED6'
# pat = '[0-9]([A-Z]+[0-9])+'
pat = '[0-9][A-Z]+[0-9]+'
M = [x.group(0) for x in finditer(pat, s)]
print(M)
# print(min([len(x) for x in M if len(x) > 10000]))

#    2BDE3F2       2 BDE3 F2
# AC12BDE3F2ED6
#        3F2ED6    3 F2 ED6
'''

'''
s = open('files/24.txt').readline()
for i in '0123456789':
    s = s.replace(i, '*')
c = 0
k = []
for i in s:
    if i == '*':
        c += 1
    else:
        if c != 0:
            k.append(c)
        c = 0
print(k)

s = s.split('*')
mini = 10 ** 10
m = [len(i) for i in s if len(i) != 0]
print(m)
for i in range(len(m) - 9999):
    summ = sum(m[i:i + 10000])
    if summ < mini:
        mini = summ
        l = sum(k[i:i + 10000])
print(mini + l)
'''



f = open('files/27B_new.txt', mode='w')

for s in open('files/27B.txt'):
    s = s.replace('.', ',')
    f.write(s)







# 17 25 27,
# ?: 24, 27 (не получилось построить диаграмму)



# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 6, 7, 8, 9, 11, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25, 27]
# КЕГЭ = [6, 7, 9, 11, 25]
# на следующем уроке:
# Разбирать задачи 24 номера по типу арифметика и символ X 80 раз (как 51993 решу егэ)
