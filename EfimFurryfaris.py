# region Домашка: ************************************************************


# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************

# Номер 7: 20804
'''
pixels = 1280 * 960
colors = 2048  # colors >= 2 ** i
i = 11  # бит на один пиксель
bit = pixels * i  # бит на одну картинку

u = 96_468_992  # бит/с
t = 132  # c
bit_n = u * t  # бит на весь пакет (n картинок)

n = bit_n / bit
print(n)  # 942.08
'''


# Номер 15 20809
'''
def F(x, A):
    B = 60 <= x <= 80
    return (x % A == 0) or (B <= (x % 22 != 0))

for A in range(1, 10000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
'''

# Номер 17 17558
'''
M = [int(x) for x in open('0. files/17.txt')]
A = [x for x in M if abs(x) % 32 == 0]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    # if (x < 0) or (y < 0):
    if (x < 0) + (y < 0) >= 1:
        if (x + y) < len(A):
            R.append(x + y)
print(len(R), max(R))
'''

# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7?, 8, 9, 10?, 11?, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ = [9, 13, 22, 24, 25]
# на следующем уроке:


# Первый пробник 21.12.24:
# Ефим 12/25 -> 56 вторичных баллов +[1-4, 7, 8, 11, 14-18] -[5, 6, 9, 10, 12, 19-21, 22, 23, 24, 25]
