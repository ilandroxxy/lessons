# region Домашка: ************************************************************


# endregion Домашка: *********************************************************
# #
# #
# region Урок: ************************************************************

# Цикл - это некоторое повторяющееся действие

# Цикла for отвечает на запрос: "повтори n раз", "пробеги от a до b"

for i in range(10):  # range(START=0, STOP=10-1, STEP=1)
    print(i, end=' ')
print()  # 0 1 2 3 4 5 6 7 8 9

for i in range(2, 10):  # range(START=2, STOP=10-1, STEP=1)
    print(i, end=' ')  # 2 3 4 5 6 7 8 9
print()

for i in range(2, 10, 3):  # range(START=2, STOP=10-1, STEP=3)
    print(i, end=' ')  # 2 5 8
print()


for i in range(3, 20, 5):
    print(i, end=' ')  # 3 8 13 18
print()
















# range(STOP), range(START, STOP), range(START, STOP, STEP)

for i in range(10):  # range(START=0, STOP=10-1, STEP=1)
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
print()

for i in range(2, 10):  # range(START=2, STOP=10-1, STEP=1)
    print(i, end=' ')  # 2 3 4 5 6 7 8 9
print()

for i in range(2, 10, 2):  # range(START=2, STOP=10-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 - Все четные числа или числа кратные 2
print()

for i in range(2, 10+1, 2):  # range(START=2, STOP=11-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 - Все четные числа или числа кратные 2
print()

for i in range(1, 10, 2):  # range(START=1, STOP=10-1, STEP=2)
    print(i, end=' ')  # 1 3 5 7 9 - Все нечетные числа
print()

for i in range(10, 0):  # range(START=10, STOP=0-1, STEP=1)
    print(i, end=' ')  #
print()

for i in range(10, 0, -1):  # range(START=10, STOP=0-1, STEP=-1)
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1
print()

# Работа цикла for с последовательностями
L = [1, 2, 3]
T = (1, 2, 3)
S = {1, 2, 3}

# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']

print(M[0])  # a
print(len(M))  # Функция len() - возвращает длину списка/последовательности (кол-во элементов).

for i in range(len(M)):  # range(start=0, stop=5-1, step=1)
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e

# i  0   1   2    3    4      5
B = [2, '3', 5, True, 17, [1, 2, 3]]
print(B[1])  # '3'
print(B[4])  # 17
print(B[5])  # [1, 2, 3]


# i  0     1     2     3      4       5
A = [41, '45', 'ABC', 'V', (3, 4), False]
print(A[4])  # (3, 4)
print(A[5])  # False
print(B[3])  # True
print(len(A))  # 6


# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
print(len(M))  # 5
for i in range(5):       # range(START, STOP, STEP)
    print(i)








# Цикл while отвечает на запрос: "делай действие пока условие верно", "бесконечные циклы"

# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# ФИПИ = []
# КЕГЭ = []
# на следующем уроке:
