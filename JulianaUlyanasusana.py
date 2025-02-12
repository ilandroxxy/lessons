# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
s = open('0. files/24.txt').readline()
s = s.replace('B', 'A').replace('C', 'A')
# AB BA AA BB BC CB CC CA AC  -> AA
while 'AA' in s:
    s = s.replace('AA', 'A A')

print(max([len(x) for x in s.split()]))

maxi = 0
for x in s.split():
    # print(len(x), x)
    if maxi < len(x):
        maxi = len(x)
print(maxi)
'''

# M = []
# for x in open('0. files/17.txt'):
#     M.append(int(x))


# Способ открытия файла для 17 номера
'''
M = [int(x) for x in open('0. files/17.txt')]
R = []
'''


# Рассмотрим три прототипа 17 номера:
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

# № 18957 (Уровень: Средний)
'''
M = [int(x) for x in open('0. files/17.txt')]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x % 43 == min(M)) and (y % 43 == min(M)):
        R.append(abs(x - y))
print(len(R), max(R))
'''


# № 18582 (Уровень: Базовый)
'''
M = [int(x) for x in open('0. files/17.txt')]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x < 0) + (y < 0) + (z < 0) >= 2:
        if abs(x + y + z) % 10 == abs(min(M)) % 10:
            R.append(abs(x + y + z))
print(len(R), max(R))
'''

print(123 % 10)  # 3
print(-123 % 10)  # 7 -> 10 - 3 = 7
print(abs(-123) % 10)  # 3



# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 13, 14, 15, 16, 23, 25]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Ульяна 5/8 -> 14 вторичных баллов +[1, 2, 4, 6, 12] -[5, 13, 14]
