# region Домашка: ******************************************************************

# № 3691 (Уровень: Базовый)
# https://stepik.org/lesson/1038816/step/8?unit=1062780
'''
k = 0
for x in range(320_400+1, 10**8):
    if all(x % p == 0 for p in (10, 12, 14, 16, 18)):
        print(x, x // 18)
        k += 1
        if k == 5:
            break
'''

# ? - 0123456789
# 1? -> 10, 12, 14, 16, 18


# № 17642 Основная волна 19.06.24 (Уровень: Базовый)
# https://stepik.org/lesson/1038816/step/10?unit=1062780
'''
def divisors(x):  # 24
    div = []
    for j in range(2, int(x**0.5)+1):  #  не равный ни самому числу
        if x % j == 0:
            div.append(j)  # 4
            div.append(x // j)  # 24 // 4 = 6
    return sorted(set(div))


k = 0
for x in range(800000+1, 10**8):
    d = [j for j in divisors(x) if j % 10 == 9 and j != 9]
    if len(d) > 0:
        print(x, min(d))
        k += 1
        if k == 5:
            break
'''


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
M = []
for x in open('0. files/17.txt'):
    M.append(int(x))
print(M)


with open(file='0. files/17.txt', mode='r') as f:
    M = []
    for x in f:
        M.append(int(x))
    print(M)
# Считается, что файл закрыт
'''

# Способ чтения файла для 17.txt:
'''
M = [int(x) for x in open('0. files/17.txt')]
R = []  # сюда мы будем складывать наши результаты
'''

# Рассмотрим три прототипа задач:
'''
# i  0  1  2  3  4
M = [1, 2, 3, 4, 5]

# 1. Под парой подразумевается два идущих подряд элемента последовательности
# 12 23 34 45
for i in range(len(M)-1):
    x, y = M[i], M[i+1]

# 2. Под тройкой подразумевается три идущих подряд элемента последовательности
# 123 234 345
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]

# 3. Под парой подразумевается два различных элемента последовательности
# 12 13 14 15
# 23 24 25
# 34 35
# 45
for i in range(len(M)):
    for j in range(i+1, len(M)):
        x, y = M[i], M[j]
'''


#
# № 19249 ЕГКР 21.12.24 (Уровень: Базовый)
'''
M = [int(x) for x in open('0. files/17.txt')]
D = [x for x in M if abs(x) % 100 == 43 and len(str(abs(x))) == 5]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x in D) or (y in D) or (z in D):
        if (x**2 + y**2 + z**2) <= max(D)**2:
            R.append(x**2 + y**2 + z**2)
print(len(R), min(R))
'''


# № 17558 Основная волна 08.06.24 (Уровень: Базовый)
'''
M = [int(x) for x in open('0. files/17.txt')]
D = [x for x in M if x % 32 == 0]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x < 0) or (y < 0):
        if (x + y) < len(D):
            R.append(x + y)
print(len(R), max(R))
'''


# 7718 (Уровень: Средний)
'''
M = [int(x) for x in open('0. files/17.txt')]
R = []
for i in range(len(M)):
    for j in range(i+1, len(M)):
        x, y = M[i], M[j]
        if ((x + y) % 18 == 0) + ((x * y) % 18 == 0) == 1:
            R.append(x + y)
print(len(R), max(R))
'''
# (True) + (True) == 2
# (True) + (False) == 1
# (False) + (True) == 1
# (False) + (False) == 0


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 6, 5, 8, 12, 13, 14, 15, 16, 17, 23, 25]
# КЕГЭ  = []
# на следующем уроке:

# Первый пробник 21.12.24:
# Захар 4/6 -> 27 вторичных баллов +[2, 8, 12, 14] -[5, 6]
# Kirill 3/6 -> 20 вторичных баллов +[8, 12, 14] -[2, 5, 6]
