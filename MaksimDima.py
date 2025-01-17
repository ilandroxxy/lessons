# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
def F(x):
    P = 10 <= x <= 35
    Q = 17 <= x <= 48
    A = a1 <= x <= a2
    return (A <= (not P)) <= (A <= Q)


M = [i / 4 for i in range(1 * 4, 60 * 4)]
R = []
for a1 in M:
    for a2 in M:
        if all(F(x) for x in M):
            R.append(a2 - a1)
print(max(R))

'''

'''
def F(x, a, b):
    P = 13 <= x <= 19
    Q = 17 <= x <= 23
    A = a <= x <= b
    return (not ((not P) <= Q)) <= (A <= ((not Q) <= P))


A = []
B = [x / 4 for x in range(10 * 4, 30 * 4)]
for a in B:
    for b in B:
        if all(F(x, a, b) for x in B):
            A.append(b - a)
print(round(max(A)))
'''

'''
def convert(n, b):
    r = ''
    while n > 0:
        r += str(n % b)
        n //= b
    return r[::-1]


R = []
for x in range(1000, 10000):
    if x % 3 != 0 and x % 17 != 0 and x % 19 != 0:
        if len(convert(x, 4)) == 6:
            R.append(x)

print(min(R), max(R))
'''


# Чтение файла
'''
file = open('files/17.txt', mode='r')
print(file)  # <_io.TextIOWrapper name='files/17.txt' mode='r' encoding='UTF-8'>

for s in file:
    print(s)


print(file.read())

file.close()


with open('files/17.txt', mode='r') as file:
    M = [int(x) for x in file]
print(M)

# Вот тут считается, что файл закрыт

M = [int(x) for x in open('files/17.txt')]
'''

'''
# Рассмотрим три прототипа задач:
M = [1, 2, 3, 4, 5]

# 1. Под парой подразумевается два идущих подряд элемента последовательности.
# 12 23 34 45
for i in range(len(M)-1):
    x, y = M[i], M[i+1]

# 2. В данной задаче под тройкой подразумевается три идущих подряд элемента последовательности.
# 123 234 345
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]

# 3. В данной задаче под парой подразумевается два различных элемента последовательности.
# 12 13 14 15
# 23 24 25
# 34 35
# 45
for i in range(len(M)):
    for j in range(i+1,  len(M)):
        x, y = M[i], M[j]
'''


# № 19249 ЕГКР 21.12.24 (Уровень: Базовый)
'''
M = [int(x) for x in open('files/17.txt')]
D = [x for x in M if str(x)[-2:] == '43' and len(str(abs(x))) == 5]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if x in D or y in D or z in D:
        if (x**2 + y**2 + z**2) <= max(D) ** 2:
            R.append(x**2 + y**2 + z**2)

print(len(R), min(R))
'''


# № 18932 Новогодний вариант 2025 (Уровень: Базовый)
'''
M = [int(x) for x in open('files/17.txt')]
D = [x for x in M if x % 2 == 0]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if x > 0 or y > 0:
        if (x + y) < len(D):
            R.append(x ** 2 + y ** 2)

print(len(R), max(R))
'''


# № 15333 Досрочная волна 2024 (Уровень: Базовый)
'''
M = [int(x) for x in open('files/17.txt')]
D = [x for x in M if x % 19 == 0]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if x > max(D) or y > max(D):
        R.append(x + y)
print(len(R), max(R))
'''


#
# № 13088 (Уровень: Средний)
'''
M = [int(x) for x in open('files/17.txt')]
D = [x for x in M if len(str(abs(x))) == 4]
B = [x for x in M if str(x)[-2:] == '17']
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x % 5 == 0) or (y % 5 == 0) or (z % 5 == 0):
        if (x in D) + (y in D) + (z in D) == 2:
            if (x + y + z) > max(B):
                print(x, y, z)
                R.append(x + y + z)
print(len(R), max(R))
'''


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [5, 8, 12, 13, 14, 15, 16, 17, 23, 25]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Дима 4/9 -> 27 вторичных баллов +[1, 12, 14, 16] -[5, 8, 13, 23, 25]
# Максим 11/14 -> 54 вторичных баллов +[1, 2, 3, 4, 5, 8, 13, 14, 16, 23, 25] -[7, 11, 12]
