# region Домашка: ******************************************************************

'''
a, b, c = int(input()), int(input()), int(input())
if (a == b) or (b == c) or (a == c):
    print('Это равнобедренный треугольник')
elif a == b == c:
    print('Это равносторонний треугольник')
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Цикл - это некоторое повторяющееся действие.

# Цикл for отвечает на запросы: "Повтори n раз", "

# Работа цикла for с функцией range()
'''
for i in range(10):  # range(START=0, STOP=10-1, STEP=1)
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
print()


for i in range(2, 10):  # range(START=2, STOP=10-1, STEP=1)
    print(i, end=' ')  # 2 3 4 5 6 7 8 9
print()

for i in range(2, 10, 2):  # range(START=2, STOP=10-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 - числа кратные 2
print()


for i in range(2, 10+1, 2):  # range(START=2, STOP=10-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10 - числа кратные 2
print()


for i in range(1, 10, 2):  # range(START=1, STOP=10-1, STEP=2)
    print(i, end=' ')  # 1 3 5 7 9 - числа некратные 2
print()


for i in range(10, 0):  # range(START=10, STOP=0-1, STEP=1)
    print(i, end=' ')  # 2 4 6 8 - числа кратные 2
print()

for i in range(10, 0, -1):  # range(START=10, STOP=0-1, STEP=-1)
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1 - диапазон в обратном порядке
print()
'''

'''
for i in range(6518, 10**10, 6518):  
    print(i, end=' ')  # 2 4 6 8 - числа кратные 6518
print()
'''

# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
# -i -5   -4   -3   -2   -1
'''
print(len(M))  # 5 - len() возвращает длину списка M (кол-во элементов в списке).

for i in range(len(M)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e
print()

for i in range(len(M)):
    M[i] = M[i]  # ['a', 'b', 'c', 'd', 'e']
print(M)

for i in range(len(M)):
    M[i] = M[i] * i  # ['', 'b', 'cc', 'ddd', 'eeee']
print(M)


# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
# -i -5   -4   -3   -2   -1

s = ''
for i in range(len(M)):
    s += M[i]
    M[i] = M[i] + s
print(M)  # ['aa', 'bab', 'cabc', 'dabcd', 'eabcde']
'''

# Работа цикла for напрямую с последовательностями
'''
# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
# -i -5   -4   -3   -2   -1

for x in M:
    print(x, end=' ')  # a b c d e
print()

import random
M = [random.randint(0, 100) for _ in range(10)]
for x in M:
    if x % 2 == 0:  # Таким образом отсеиваем только четные элементы
        print(x, end=' ')  # 70 4 58 40 84
print()
'''

# Цикл while отвечает на запросы: "Повторяй действие пока условие истинно", "Бесконечные циклы"
'''
for i in range(2, 10+1, 2):  # range(START=2, STOP=11-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10
print()

i = 2
while i <= 10:
    print(i, end=' ')  # 2 4 6 8 10
    i += 2
'''


# Переводы в base системы счисления
'''
n = 8  # n - number
b = 2  # b - base
r = ''  # r - result
while n > 0:
    r += str(n % b)
    n //= b
r = r[::-1]
print(r)  # 1000


n = 8  # n - number
b = 2  # b - base
r = ''  # r - result
while n > 0:
    r = str(n % b) + r
    n //= b
r = r
print(r)  # 1000

alphabet = sorted('1234567890QWERTYUIOPASDFGHJKLZXCVBNM')
print(alphabet)
n = int(input('Введите число в 10-й системе: '))  # n - number
b = int(input('Введите base систему счисления: '))  # b - base
r = ''  # r - result
while n > 0:
    r = alphabet[n % b] + r
    n //= b
r = r
print(r)  # 1000
'''
# 1112


# Бесконечные циклы и операторы break, continue, exit()
'''
k = 0
while True:
    k += 1
    if k % 2 != 0:
        continue  # - прерывает итерацию (шаг) цикла в котором лежит
    if k == 50000:
        exit()  # выходит полностью из выполнения программы
    if k == 100000:
        break  # - прерывает цикл в котором сейчас находится
    print(k)
print('КОНЕЦ')
'''

alphabet = sorted('1234567890QWERTYUIOPASDFGHJKLZXCVBNM')
while True:

    case = int(input(f'\n'
                     f'case 1: Перевод из 10-й в base систему счисления.\n'
                     f'case 2: Перевод из base в 10-ю систему счисления.\n'
                     f'case 3: Перевод из base в n-ю систему счисления.\n'
                     f'case 0: \n\n'))

    if case == 1:
        n = int(input('Введите число в 10-й системе: '))  # n - number
        b = int(input('Введите base систему счисления: '))  # b - base
        r = ''  # r - result
        while n > 0:
            r = alphabet[n % b] + r
            n //= b
        r = r
        print(f'Результат перевода в {b}-ю систему счисления: {r}')

    elif case == 2:
        b = int(input('Введите base систему счисления: '))
        r = input(f'Введите число в {b}-й системе: ')
        print(f'Результат перевода в 10-ю систему счисления: {int(r, b)}')
        # ValueError: int() base must be >= 2 and <= 36, or 0

    elif case == 3:
        pass  # todo #ДЗ попробовать прописать case 3

    elif case == 0:
        break

    else:
        print('Что-то я не очень понял вас. ')


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = []
# КЕГЭ  = []
# на следующем уроке:
