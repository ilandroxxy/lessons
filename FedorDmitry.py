# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Открытие файла для 17 номера
'''
with open('0. files/17.txt', mode='r') as file:
    M = [int(s) for s in file]

M = [int(s) for s in open('0. files/17.txt')]
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



# № 21903 Открытый вариант 2025 (Уровень: Базовый)
'''
M = [int(s) for s in open('0. files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 3 and abs(x) % 100 == 15]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if ((x > 0) and (y > 0) and (z > 0)) or ((x < 0) and (y < 0) and (z < 0)):
        if max(x, y, z) * min(x, y, z) > min(A) ** 2:
            R.append(max(x, y, z) * min(x, y, z))
print(len(R), min(R))
'''

'''
print(123 % 10)  # 3
print(-123 % 10)  # 7

print(123 % 100)  # 23
print(-123 % 100)  # 77
'''

# № 21712 ЕГКР 19.04.25 (Уровень: Базовый)
'''
M = [int(s) for s in open('0. files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 4 and abs(x) % 10 == 6]
B = [x for x in A if x > 0]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x in A) + (y in A) + (z in A) == 1:
        if (x + y + z) <= min(B):
            R.append(x + y + z)
print(len(R), max(R))
'''


# № 18142 (Уровень: Базовый)
'''
M = [int(s) for s in open('0. files/17.txt')]
A = [x for x in M if abs(x) % 10 == 8]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x % 16 == min(A)) + (y % 16 == min(A)) == 1:
        R.append(x + y)
print(len(R), max(R))
'''


# № 16264 Джобс 03.05.24 (Уровень: Базовый)
'''
M = [int(s) for s in open('0. files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 2 and x % sum(map(int, str(x))) == 0]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x % min(A) == 0) + (y % min(A) == 0) >= 1:
        R.append(x + y)
print(len(R), max(R))
'''


# № 23905 (Уровень: Средний)
'''
M = [int(s) for s in open('0. files/17.txt')]
A = [x for x in M if abs(x) % 100 == 32]
B = [x for x in M if len(set(str(x)[-2:])) == 1]
cnt = 0
for i in range(len(M)-3):
    x, y, z, w = M[i], M[i+1], M[i+2], M[i+3]
    if (x > max(A)) + (y > max(A)) + (z > max(A)) + (w > max(A)) == 2:
        if (x in B) + (y in B) + (z in B) + (w in B) == 1:
            cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/inf/task/7a1920ba-8e25-4c9b-ad1f-4f12d81514ab
'''
z = [int(i) for i in open('0. files/17.txt')]
A = [x for x in z if len(str(abs(x))) == 3 and str(x)[-1] == '7']
R = []
for i in range(len(z) - 1):
    a, b = z[i], z[i + 1]
    la = len(str(abs(a)))
    lb = len(str(abs(b)))
    if (la == 3) + (lb == 3) == 1:
        if abs(a + b) % min(A) == 0:
            R.append(a + b)
print(len(R), min(R))
'''


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 8, 14, 15, 16, 17, 23, 19-21, 25]
# КЕГЭ = []
# на следующем уроке: Из пробника глянуть 8, 17 номера
