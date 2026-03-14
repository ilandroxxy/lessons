# region Домашка: ******************************************************************



# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


#2
'''
print('x y z w')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                F = (x or (not y)) and (not(y == z)) and (not w)
                if F == 1:
                    print(x, y, z, w)
'''
#6
'''
import turtle as t
k = 30
t.screensize(-2000,2000)
t.tracer(0)
t.left(90)
t.down()
for i in range(4):
    t.forward(10*k)
    t.right(270)
t.up()
t.forward(3*k)
t.right(270)
t.forward(5*k)
t.right(90)
t.down()
for j in range(2):
    t.forward(10*k)
    t.right(270)
    t.forward(12*k)
    t.right(270)
t.up()
for x in range(-30,30):
    for y in range(-30,30):
        t.setpos(x*k,y*k)
        t.dot(3,'red')
t.update()
t.done()
'''
#7
'''
pixels = 1024*512
i = 4 * 8
u = 32_768
v = pixels * i
t = v/u
print(t)
'''

#8
'''
from itertools import product
n = 0
for p in product(sorted('СБОРНИК'), repeat = 6):
    word = ''.join(p)
    n += 1
    if word[0] != 'Р':
        if word.count('Б') == 2:
            if word.count('К') <= 1:
                print(n)
'''

#14
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:19]:
    A = int(f'83{x}916', 19)
    B = int(f'123{x}45', 19)
    C = int(f'67{x}89', 19)
    if (A + B + C) % 17 == 0:
        print((A + B + C) // 17)
'''

#15
'''
def F(x, y, A):
    return (x < A) or (3*y + 2*x > 120) or (A > y)

R = []
for A in range(0, 1000):
    if all(F(x, y, A) == 1 for x in range(0, 100) for y in range(0, 100)):
        R.append(A)
print(min(R))
'''

#16
'''
import sys
sys.setrecursionlimit(10**8)

def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n - 1 + F(n - 1)
print(F(2024) - F(2022))
'''
#17
'''
M = [int(i) for i in open ('files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 5]
B = [x for x in M if abs(x) % 100 == 29]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x in A) + (y in A) + (z in A) == 2:
        if (x + y + z) <= max(B): 
            R.append(x + y + z)
print(len(R), max(R))
'''

#19,20,21
'''
def F(s,n):
    if s >= 473:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s+1, n - 1), F(s + 5, n -1), F(s * 4, n -1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

print([s for s in range(1, 473) if not F(s,1) and F(s,2)])
print([s for s in range(1, 473) if not F(s,1) and F(s, 3)])
print([s for s in range(1, 473) if not F(s,2) and F(s, 4)])
'''
#23
'''
def F(a, b):
    if (a > b) or (a == 13):
        return 0
    if a == b:
        return 1
    if a < b:
        return F(a + 1, b) + F(a + 2, b) + F(a * 3, b)

print(F(3, 8) * F(8, 18))
'''
# ОТВЕТЫ:
# 1) 25
# 2) xyzw
# 3) 2000
# 4) 7
# 6) 216
# 7) 512
# 8) 114816
# 10) 42
# 14) 1405686
# 15) 0
# 16) 4045
# 18) 2292 524
# 19) 118
# 20) 113 117
# 21) 112
# 23) 200


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 6, 7, 8, 9, 11, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 25]
# КЕГЭ = []
# на следующем уроке: 17, 25, 7, 11


# 📖 Пробник (Вариант 2)
# Студент #Илья сдал ответы на пробник, вот результаты:
# Дата: #Вторник #03Марта2026
# ✅ Верно: 1, 2, 4, 6, 7, 10, 14, 16, 17, 18, 19, 20, 21, 23
# ⛔️ Неверно: 3, 8, 15
# ❔ Без ответа: 5, 9, 11, 12, 13, 22, 24, 25, 26, 27
# Итог: 14/29 первичных балла ~ 62 вторичных

