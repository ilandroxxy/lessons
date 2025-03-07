# region Домашка: ******************************************************************

'''
def convert(n, b):
    alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
    s = ''
    while n > 0:
        s += alphabet[n % b]
        n //= b
    return s[::-1]

R = []
for n in range(1, 1000):
    c = convert(n, 3)
    if n % 3 == 0:
        c = c + c[-3:]
    else:
        c = c + convert(((n % 3) * 3), 3)
    r = int(c, 3)
    if r > 150:
        R.append(n)
print(min(R))
'''


'''
# 2, 3, 4, 5, 6, 7, 8, 9
def convert(n,b):
    s = ''
    while n>0:
        s += str(n%b)
        n //= b
    return s[::-1]

# 2-36
def convert(n, b):
    alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
    s = ''
    while n > 0:
        s += alphabet[n % b]
        n //= b
    return s[::-1]


# 2-36
def convert(n, b):
    alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
    s = ''
    while n > 0:
        s = alphabet[n % b] + s
        n //= b
    return s
'''

# Номер 8
'''
from itertools import *
n=0
for s in product(sorted('СБОРНИК'), repeat=6):
    word=''.join(s)
    n+=1
    if word[0] != 'Р' and word.count('Б')==2 and word.count('К')<=1:
        print(n, word)
'''
# Ответ: 117601


# Номер 12
'''
for n in range(4, 10000):
    word = '5' + '2' * n
    while '52' in word or '1122' in word or '2222' in word:
        if '52' in word:
            word = word.replace('52', '11', 1)
        elif '2222' in word:
            word = word.replace('2222', '5', 1)
        elif '1122' in word:
            word = word.replace('1122', '25', 1)
    if sum([int(x) for x in word])==64:
        print(n)
        break
'''


# Номер 15
'''
def F(x, y, A):
    return (x<A) or (3*y+2*x>120) or (A>y)

for A in range(1, 10000):
    if all(F(x, y, A) for x in range(1, 100) for y in range(1, 100)):
        print(A)
        break
'''


# Номер 25
'''
from fnmatch import *
for x in range(2023, 10**8, 2023):
    if fnmatch(str(x), '2*1?71'):
        print(x, x // 2023)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
M = [int(x) for x in open('0. files/17.txt')]
print(M)

# Три прототипа задач:
# i  0  1  2  3  4
M = [1, 2, 3, 4, 5]

# 1. под парой подразумевается два идущих подряд элемента последовательности
# 12 23 34 45
for i in range(len(M)-1):
    x, y = M[i], M[i+1]

# 2. под тройкой подразумевается три идущих подряд элемента последовательности
# 123 234 345
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]

# 3. под парой подразумевается два различных элемента последовательности
# 12 13 14 15
# 23 24 25
# 34 35
# 45
for i in range(len(M)):
    for j in range(i+1, len(M)):
        x, y = M[i], M[j]
'''


# № 17636 Основная волна 19.06.24 (Уровень: Средний)
'''
M = [int(x) for x in open('0. files/17.txt')]
A = [x for x in M if abs(x) % 10 == 3 and len(str(abs(x))) == 3]
R = []  # сюда будем складывать результаты
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x in A) + (y in A) + (z in A) >= 1:
        if (x + y + z) < max(A):
            R.append(x + y + z)
print(len(R), max(R))
'''


# № 17680 Пересдача 04.07.24 (Уровень: Базовый)
'''
M = [int(x) for x in open('0. files/17.txt')]
A = [x for x in M if x > 0 and x % 41 == 0]
R = []
for i in range(len(M)-1):
    x, y= M[i], M[i+1]
    if x != y:
        if abs(x - y) % min(A) == 0:
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
# ФИПИ = [2, 5, 6, 8, 10, 12, 13, 14, 15, 16, 17, 23, 25]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Женя 5/7 -> 34 вторичных баллов +[2, 5, 8, 12, 14] -[6, 10]
# Ярослав 2/7 -> 14 вторичных баллов +[2, 12] -[5, 6, 8, 10, 14]

# Второй пробник 28.02.25:
# Женя 10/29 -> 51 вторичных баллов +[2, 5, 6, 10, 13, 14, 15, 16, 23, 25] -[8, 12]
# Ярослав 10/29 -> 51 вторичных баллов +[2, 5, 6, 10, 12, 13, 14, 15, 16, 23] -[8, 25]
