# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 19249 ЕГКР 21.12.24 (Уровень: Базовый)
'''
M = [int(s) for s in open('files/17.txt')]
D = [x for x in M if abs(x) % 100 == 43 and len(str(abs(x))) == 5]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    # if x in D or y in D or z in D:
    if (x in D) + (y in D) + (z in D) >= 1:
        if (x**2 + y**2 + z**2) <= max(D)**2:
            R.append(x**2 + y**2 + z**2)
print(len(R), min(R))
'''


# № 18617 (Уровень: Средний)
'''
M = [int(s) for s in open('files/17.txt')]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x % 3 == max(M) % 3) or (y % 3 == max(M) % 3):
        if (x % 7 == min(M) % 7) or (y % 7 == min(M) % 7):
            R.append(x + y)
print(len(R), max(R))
'''


# № 14952 (Уровень: Средний)
'''
M = [int(s) for s in open('files/17.txt')]
D = [x for x in M if len(str(abs(x))) == 4 and x % 2 == 0]
B = [x for x in M if abs(x) % 1000 == 121]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x in D) + (y in D) + (z in D) <= 1:
        if (x + y + z) <= max(B):
            R.append(x + y + z)
print(len(R), max(R))
'''


# № 14653 Открытый курс "Слово пацана" (Уровень: Сложный)

# 1. Только два элемента являются трехзначными числами
# 2. Ровно один элемент делится на 18
# 3. Сумма элементов делится на сумму двух минимальных
# положительных элементов последовательности, кратных 17
# 4. Произведение элементов не превосходит квадрат
# максимального элемента последовательности, оканчивающегося на 69
'''
M = [int(s) for s in open('files/17.txt')]
D = [x for x in M if len(str(abs(x))) == 3]
B = sorted([x for x in M if x > 0 and x % 17 == 0])
C = [x for x in M if abs(x) % 100 == 69]
R = []
for i in range(len(M)-3):
    x, y, z, w = M[i], M[i+1], M[i+2], M[i+3]
    if (x in D) + (y in D) + (z in D) + (w in D) == 2:  # 1
        if (x % 18 == 0) + (y % 18 == 0) + (z % 18 == 0) + (w % 18 == 0) == 1:  # 2
            if (x + y + z + w) % (B[0] + B[1]) == 0:  # 3
                if (x * y * z * w) <= max(C) ** 2:  # 4
                    R.append((x + y + z + w) ** 2)
print(len(R), min(R))
'''


# № 12926 PRO100 ЕГЭ 26.01.24 (Уровень: Сложный)
'''
M = [int(s) for s in open('files/17.txt')]
D = [x for x in M if 10 <= abs(x) <= 99]
A = -10**9
R = []
for i in range(len(M)-3):
    x, y, z, w = M[i], M[i+1], M[i+2], M[i+3]
    if (abs(x) % 10) == (abs(y) % 10) == (abs(z) % 10) == (abs(w) % 10):
        print(x, y, z, w)
        A = max(A, x + y + z + w)

for i in range(len(M)-4):
    x, y, z, w, t = M[i], M[i+1], M[i+2], M[i+3], M[i+4]
    if (x < A) + (y < A) + (z < A) + (w < A) + (t < A) == 1:
        # print(x, y, z, w, t, A)
        if (x + y + z + w + t) % max(D) == 0:
            R.append(x + y + z + w + t)
print(len(R), min(R))
'''

'''
import time
start = time.time()

# def IsPrime(n):
#     d = 2
#     while n % d != 0:
#         d += 1
#     return d == n

def IsPrime(n):
    if n <= 1:
        return False
    for j in range(2, int(n**0.5)+1):
        if n % j == 0:
            return False
    return True


M = [x for x in range(2, 10000) if IsPrime(x)]
print(M)


print(time.time() - start)  # 0.20528 -> 0.0046
'''


# № 9993 (Уровень: Сложный)
'''
def IsPrime(n):
    if n <= 1:
        return False
    for j in range(2, int(n**0.5)+1):
        if n % j == 0:
            return False
    return True


M = [int(s) for s in open('files/17.txt')]
D = [x for x in M if abs(x) % 100 == 17]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if IsPrime(abs(x)) + IsPrime(abs(y)) == 1:
        if (x + y) % max(D) == 0:
            R.append(x * y)
print(len(R), max(R))
'''

# endregion Урок: ********************************************************************
# #
# #
# region Разобрать: ********************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ  = [5, 14, 15, 16, 22, 23]
# на следующем уроке: 17, 9, 24


# Первый пробник 21.12.24:
# Александр 19/25 -> 75 вторичных баллов +[1-5, 7, 9-10, 12, 14-16, 18-22, 24, 25] -[6, 8, 11, 13, 17, 23]
# Саша
