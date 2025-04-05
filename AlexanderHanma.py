# region Домашка: ******************************************************************

# № 20811 Апробация 05.03.25 (Уровень: Базовый)
# 1 куча: +1, +4, *2 | >= 51 | 1 ≤ S ≤ 50

# n = 1: Петя первый ход
# n = 2: Ваня первый ход
# n = 3: Петя второй ход
# n = 4: Ваня второй ход
'''
def F(s, n):
    if s >= 51:
        return n % 2 == 0  # True - если Ваня / False - если Петя
    if n == 0:
        return 0  # False
    h = [F(s+1, n-1), F(s+4, n-1), F(s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)


print([s for s in range(1, 51) if F(s, 2)])  # При любом ходе Пети Ваня может выиграть своим первым ходом
print([s for s in range(1, 51) if F(s, 3) and not F(s, 1)])
print([s for s in range(1, 51) if F(s, 4) and not F(s, 2)])
'''


# 18144 (Уровень: Базовый)
# 1 куча: -4, -6, /2 вверх | <= 19 | S ≥ 20
'''
from math import ceil, floor

def F(s, n):
    if s <= 19:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s-4, n-1), F(s-6, n-1), F(ceil(s/2), n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)


print([s for s in range(20, 1000) if F(s, 2)])  # При любом ходе Пети Ваня может выиграть своим первым ходом
print([s for s in range(20, 1000) if F(s, 3) and not F(s, 1)])
print([s for s in range(20, 1000) if F(s, 4) and not F(s, 2)])
'''

# № 20907 Апробация 05.03.25 (Уровень: Базовый)
# 2 кучи: a+1, s+1, a*2, s*2 | >= 81 | 1 ≤ S ≤ 73 | В первой куче 7
'''
def F(a, s, n):
    if a+s >= 81:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a+1, s, n-1), F(a, s+1, n-1), F(a*2, s, n-1), F(a, s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

# [19,
print([s for s in range(1, 74) if F(7, s, 2)])  # При любом ходе Пети Ваня может выиграть своим первым ходом
print([s for s in range(1, 74) if F(7, s, 3) and not F(7, s, 1)])
print([s for s in range(1, 74) if F(7, s, 4) and not F(7, s, 2)])
'''

# № 19635 (Уровень: Базовый)
'''
from math import ceil,floor
def F(a, s, n):
    if a+s<= 100:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a-3, s-3, n-1), F(floor(a/2), s, n-1), F(a,floor(s/2), n-1)]
    return any(h) if (n - 1) % 2 == 0 else any(h)

print([s for s in range(53, 1000) if F(48, s, 2)])  # [52
print([s for s in range(53, 1000) if F(48, s, 3) and not F(48, s, 1)])
print([s for s in range(53, 1000) if F(48, s, 4) and not F(48, s, 2)])
'''


# № 19120 (Уровень: Базовый)
'''
from math import ceil,floor
def F(s, n):
    if s <= 12:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s-1, n-1),F(s-2, n-1),F(s-3, n-1),F(s-4, n-1),F(s-5, n-1),F(floor(s/5), n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

print([s for s in range(20,1000) if F(s, 2)])  # [59
print([s for s in range(20,1000) if F(s, 3) and not F(s, 1)])
print([s for s in range(20,1000) if F(s, 4) and not F(s, 2)])
'''


# № 15336 Досрочная волна 2024 (Уровень: Базовый)
'''
def F(a,s, n):
    if a+s>=123:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a+1,s, n-1),F(a,s+1, n-1),F(a*2,s, n-1),F(a,s*2, n-1),]
    return any(h) if (n - 1) % 2 == 0 else all(h)

print([s for s in range(1,110) if F(13,s, 2)])  # [59
print([s for s in range(1,110) if F(13,s, 3) and not F(13,s, 1)])
print([s for s in range(1,110) if F(13,s, 4) and not F(13,s, 2)])
'''
# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 18176 (Уровень: Средний)
'''
R = []
M = [int(x) for x in open('0. files/17.txt')]
W = [x for x in M if abs(x) % 10 == 4 and x > 0]
for i in range(len(M) - 2):
    a, b, c = M[i], M[i + 1], M[i + 2]
    summa = sum([int(x) for x in str(a) + str(b) + str(c) if x.isdigit()])
    if summa == min(W):
        R.append(a + b + c)
print(len(R), max(R))
'''


# № 21161 (Уровень: Сложный)
'''
from re import *
s = open('0. files/24.txt').readline()
word = r'([ABCabc][abc]*)'
pred = rf'[ABC][abc]*( {word})*.'
m = [x.group() for x in finditer(pred,s)]
# for x in m:
#     print(x)
print(max([len(x) for x in m]))
'''

# № 20813 Апробация 05.03.25 (Уровень: Сложный)
'''
from re import *
s = open('0. files/24.txt').readline()
num = r'([789][0789]*|0)'
reg = rf'{num}([-*]{num})+'
m = [x.group() for x in finditer(reg,s)]
for x in m:
    print(x)
"""
98789-89099089999-99-8-8888
8877-9078
98-9798087
9*0-7*9009
8
0-7-9998-8-778
"""

# m = [x.group() for x in finditer(reg,s)]
# print(max([len(x) for x in m]))
print(max([len(x.group()) for x in finditer(reg,s)]))
'''


# № 19968 (Уровень: Сложный)
'''
from re import *
s = open('0. files/24.txt').readline()
# num = r'([12345][012345]*|0)'
num = r'(?:[1-5][0-5]*|0)'  # ?:
reg = rf'{num}([+*]{num})+'
print(max([len(x.group()) for x in finditer(reg,s)]))
'''


# № 19967 (Уровень: Сложный)
'''
from re import *
s = open('0. files/24.txt').readline()

num = r'([1-9][0-9]*|0)'
reg = rf'AFD{num}([+*]{num})+'
print(max([len(x.group()) for x in finditer(reg,s)]))
'''

# № 19719 (Уровень: Базовый)
'''
from re import *
s = open('0. files/24.txt').readline()
num = r'([12349][012349]*|0)'
reg = rf'{num}([-*]{num})+'
print(max([len(x.group()) for x in finditer(reg,s)]))
'''


# № 18619 (Уровень: Сложный)
'''
from re import *
s = open('0. files/24.txt').readline()
num = r'([1-6][1-6]*)'
reg = rf'B{num}([-*]{num})*'
print(max([len(x.group()) for x in finditer(reg,s)]))
'''


# № 18285 (Уровень: Сложный)
'''
from re import *
s = open('0. files/24.txt').readline()
num = r'([1-9][0-9]*)'
reg = rf'{num}([+*]{num})*'
m = [x.group() for x in finditer(reg,s)]
for x in m:
    print(x)
print(max([len(x.group()) for x in finditer(reg,s)]))
'''


# № 18147 (Уровень: Средний)
'''
from re import *
R = []
s = open('0. files/24.txt').readline()
num = r'([789][789]*)'
reg = rf'{num}([*+]{num})*'
m = [x.group() for x in finditer(reg,s)]
for x in m:
    print(x)
    R.append(eval(x))
print(max(R))
'''
# 89797978998877


# № 17878 Демоверсия 2025 (Уровень: Сложный)
'''
from re import *
s = open('0. files/24.txt').readline()
num = r'([6789][06789]*)'
reg = rf'{num}([-*]{num})*'
m = [x.group() for x in finditer(reg,s)]
for x in m:
    print(x)
print(max([len(x.group()) for x in finditer(reg,s)]))
'''

# № 20814 Апробация 05.03.25 (Уровень: Базовый)
'''
def divisors(x):
    div=[]
    for i in range(2,int(x**0.5)+1):  # не считая единицы и самого числа.
    # for i in range(1,int(x**0.5)+1):  #  считая единицы и само число.
        if x%i==0:
            div+=[i,x//i]
    return sorted(set(div))

cnt = 0
for x in range(500_000+1, 10**10):
    d = divisors(x)
    d = [j for j in divisors(x) if j % 2 == 0]  # все четные делители
    d = [j for j in divisors(x) if j % 2 != 0]  # все нечетные делители
    d = [j for j in divisors(x) if j % 10 == 9 and j != 9]  # делители, которые оканчиваются на 9 и не равны 9
    d = [j for j in divisors(x) if len(divisors(j)) == 0]  # делители, которые являются простыми числами
    R = sum(d)
    if R % 10 == 9:
        print(x, R)
        cnt += 1
        if cnt == 5:
            break
'''


# № 17564 Основная волна 08.06.24 (Уровень: Средний)
'''
def divisors(x):
    div = []
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            div += [i, x // i]
    return sorted(set(div))


cnt = 0
for x in range(700_000 + 1, 10 ** 10):
    d = divisors(x)
    if len(d) > 0:
        M = max(d) + min(d)
        if M % 10 == 4:
            print(x, M)
            cnt += 1
            if cnt == 5:
                break
'''

'''
def divisors(x):
    div=[]
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            div+=[i,x//i]
    return sorted(set(div))

cnt=0
for x in range(800_000+1, 10**10):
    d=[a for a in divisors(x) if a%10==9 and a!=9]
    if len(d) > 0:
        print(x, min(d))
        cnt+=1
        if cnt==5:
            break
'''

# endregion Урок: ********************************************************************
# #
# #
# region Разобрать: ********************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25, 26.1]
# КЕГЭ  = [5, 9, 14, 15, 16, 17, 22, 23]
# на следующем уроке:


# Первый пробник 21.12.24:
# Александр 19/25 -> 75 вторичных баллов +[1-5, 7, 9-10, 12, 14-16, 18-22, 24, 25] -[6, 8, 11, 13, 17, 23]

# Второй пробник 28.02.25:
# Александр 24/25 -> 88 вторичных баллов +[1-10, 12-25] -[11]
# Саша 10/25 -> 51 вторичных баллов +[1, 2, 4, 12, 14-16, 19, 23, 25] -[3, 5, 6-10, 11, 13, 17, 18, 20-22, 24]
