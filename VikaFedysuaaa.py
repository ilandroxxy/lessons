# region Домашка: ******************************************************************

# https://stepik.org/lesson/1309435/step/12?unit=1324551
'''
a = int(input())
b = int(input())
for i in range(a, b + 1):
    flag = True
    if i == 1:
        continue
    for k in range(2, i):
        if i % k == 0:
            flag = False
            break
    if flag:
        print(i)
'''


# https://stepik.org/lesson/1309452/step/7?unit=1324568
'''
L = [3, 7, 1, 4, 9, 2]
x = L[0]
L[0] = L[-1]
L[-1] = x
print(L)


L = [3, 7, 1, 4, 9, 2]
L[0], L[-1] = L[-1], L[0]
print(L)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Генераторы списков
'''
# ГЕНЕРАТОР[что_кладем откуда_берем]
M = [x for x in range(10)]  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# ГЕНЕРАТОР[что_кладем откуда_берем при_каком_условии]
M = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

M = [x**2 for x in range(10) if x % 2 == 0]  # [0, 4, 16, 36, 64]

from random import randint
n = randint(5, 15)
R = [randint(0, 100) for _ in range(n)]
print(R)  # [2, 75, 93, 99, 47, 52, 7, 75, 27, 68, 5, 0, 70, 82, 42]

chet = [x for x in R if x % 2 == 0]
nechet = [x for x in R if x % 2 != 0]
print(chet)  # [2, 52, 68, 0, 70, 82, 42]

A = [x for x in R if len(str(x)) == 1]
print(A)  # [2, 7, 5, 0]

B = [x for x in R if x % 10 == 8]
print(B)  # [68]
'''



# https://stepik.org/lesson/1309452/step/9?unit=1324568
'''
n=int(input())
L=[]
for i in range(n):
    x=int(input())
    if x%2==0:
        L.append(x)
print(L)
'''

# Вариант 2 через генераторы
'''
L = [int(input()) for _ in range(int(input()))]
R = [x for x in L if x % 2 == 0]
'''


# https://stepik.org/lesson/1309452/step/8?unit=1324568
'''
a=int(input())
L=[]
for i in range(a):
    l=int(input())
    L.append(l)
L.remove(max(L))
print(max(L))
'''
# Вариант 2 через генератор
'''
L = [int(input()) for _ in range(int(input()))]
print(sorted(L)[-2])


print(sorted([int(input()) for _ in range(int(input()))])[-2])
'''

# https://stepik.org/lesson/1309452/step/12?unit=1324568
'''
# from math import prod

A = [int(x) for x in str(int(input()))]
print(A.count(2))
print(A.count(A[-1]))
nechet = [x for x in A if x % 2 != 0]
print(len(nechet))
B = [x for x in A if x > 7]
print(sum(B))
if len(B) == 0:
    print(11)
elif len(B) == 1:
    print(B[0])
else:
    total = 1
    for x in B:
        total *= x
    print(total)
    # print(prod(B))
print(A.count(0) + A.count(4))
'''


# Примерное решение 17 номера
'''
M = [int(x) for x in open('0. files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 2]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x in A) + (y in A) == 1:
        if (x + y) % min(A) == 0:
            R.append(x + y)
print(len(R), max(R))
'''








# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = []
# КЕГЭ = []
# на следующем уроке:
