# region Домашка: ******************************************************************

'''
n = int(input())
m = [int(input()) for i in range(n)]
print([i for i in m if i % 2 == 0])
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Открываем файл для 17 номера
'''
M = [int(x) for x in open('0. files/17.txt')]
print(M)
'''

# Открываем файл для 9 номера
'''
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(',')]
    print(M)
'''


# Правильное открытие файла в Python
'''
with open('0. files/17.txt') as file:
    M = [int(x) for x in file]
    print(M)
# Тут файл уже закрыт
'''



# Три основных типа 17 номеров:
'''
# i  0  1  2  3  4
M = [1, 2, 3, 4, 5]

# 1. Под парой подразумевается два идущих подряд элемента последовательности.
# 12 23 34 45

for i in range(len(M)-1):
    x, y = M[i], M[i+1]



# 2. Под тройкой подразумевается три идущих подряд элемента последовательности.
# 123 234 345

for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]


# 3. Под парой подразумевается два различных элемента последовательности.
# 12 13 14 15
# 23 24 25
# 34 35
# 45

for i in range(len(M)):
    for j in range(i+1, len(M)):
        x, y = M[i], M[j]
        print(f'{x}{y}', end=' ')
    print()
'''

'''
# ГЕНЕРАТОР[что_кладем откуда_берем]
A = [x for x in range(10)]  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# ГЕНЕРАТОР[что_кладем откуда_берем при_каком_условии]
A = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

A = [x**2 for x in range(10) if x % 2 == 0]  # [0, 4, 16, 36, 64]

print(A)
'''



M = [int(x) for x in open('0. files/17.txt')]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]



# № 23563 Пересдача 03.07.25 (Уровень: Базовый)
'''
M = [int(x) for x in open('0. files/17.txt')]
B = [x for x in M if abs(x) % 35 == 0 and x > 0]
count = 0
maxi = 0
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if x != y:
        if abs(x - y) % min(B) == 0:
            count += 1
            maxi = max(maxi, x + y)
print(count, maxi)

# Вариант номер 2
M = [int(x) for x in open('0. files/17.txt')]
B = [x for x in M if abs(x) % 35 == 0 and x > 0]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if x != y and abs(x - y) % min(B) == 0:
        R.append(x + y)
print(len(R), max(R))
'''

# M = list(map(int, f.readlines()))

M = [int(x) for x in open('0. files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 5]
B3 = [x for x in M if abs(x) % 3 == 0]
B5 = [x for x in M if abs(x) % 5 == 0]
C = [x for x in M if abs(x) % 1000 == 238]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x in A) + (y in A) + (z in A) in (1, 2):
        if ((x in B3) + (y in B3) + (z in B3)) > ((x in B5) + (y in B5) + (z in B5)):
            if (x + y + z) > max(C):
                R.append(x + y + z)
print(len(R), max(R))


'''
a = [int(s) for s in open('0. files/17.txt')]
a238 = max([x for x in a if x % 1000 == 238])
count = 0
s3 = []
for i in range (len(a) - 2):
    troika = [a[i] , a[i+1] , a[i+2]]
    a3 = [x for x in troika if x % 3 == 0]
    a5 = [x for x in troika if x % 5 == 0]
    raz5 = [x for x in troika if len(str(x)) == 5]
    if sum(troika) > a238:
        if len(a3) > len (a5):
            if 0 < len(raz5) < 3:
                s3.append(sum(troika))
print(len(s3),max(s3))
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
