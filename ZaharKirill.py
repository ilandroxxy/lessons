# region Домашка: ******************************************************************

# Разработка программы для определения вида треугольника
'''
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print("Равносторонний")
elif a != b != c != a:
    print('Разносторонний')
else:
    print('Равнобедренный')
'''


# Определение года високосного
'''
a = int(input())
if a % 400 == 0:
    print("Високосный")
elif a % 4 == 0 and a % 100 != 0:
    print("Високосный")
else:
    print("Обычный")
'''


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Цикла for отвечает на запросы: "повтори N раз", "пробеги от A до B"
'''
# range() - перебирает диапазон
# range(STOP-1)
# range(START, STOP-1)
# range(START, STOP, STEP-1)

for i in range(10):  # range(start=0, STOP=10-1, step=1)
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
print()


for i in range(2, 10):  # range(START=2, STOP=10-1, step=1)
    print(i, end=' ')  # 2 3 4 5 6 7 8 9
print()

for i in range(2, 10, 2):  # range(START=2, STOP=10-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8
print()

n = 10
for i in range(2, n+1, 2):  # range(START=2, STOP=11-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10
print()

for i in range(10, 0):  # range(START=10, STOP=01-, STEP=1)
    print(i, end=' ')  #
print()

for i in range(10, 0, -1):  # range(START=10, STOP=01-, STEP=1)
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1
print()


# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']

print(len(M))  # 5 - Возвращает длину списка, то есть кол-во элементов в нем

for i in range(len(M)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e
print()

for i in range(len(M)):
    M[i] = M[i] * i
print(M)  # ['', 'b', 'cc', 'ddd', 'eeee']

# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']

for x in M:
    print(x, end=' ')  # a b c d e
print()

for x in M:
    if x in 'ae':
        print(x, end=' ')
print()  # a e 
'''

# Цикла while отвечает на запросы: "пока условие верно, выполнять действие", "бесконечные циклы"

'''
for i in range(2, 10+1, 2):  # range(START=2, STOP=11-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10
print()

i = 2
while i <= 10:
    print(i, end=' ')  # 2 4 6 8 10
    i += 2
'''


# Перевод из 10-й в b-ю систему счисления
'''
n = int(input('Введите число для перевода: '))
b = int(input('Введите b-ю систему счисления: '))
r = ''
while n > 0:
    r += str(n % b)
    n //= b
print(r[::-1])  # 1000 - результат перевода перевернули в обратном порядке 
'''

'''
n = 8
r = bin(n)[2:]
print(r)  # 1000

print(int(r, 2))
'''


# Бесконечные циклы и операторы break, continue, exit()
'''
k = 0
while True:
    k += 1
    if k % 2 != 0:
        continue  # Прерывает итерацию цикла (шаг)
    if k == 2_000_000:
        exit()  # Выход и программы
    if k == 1_000_000:
        break  # - Прерывает выполнение цикла в котором сейчас лежит
    print(k)

print('Продолжение программы')
'''


# Калькулятор систем счисления

from string import *
alphabet = digits + ascii_uppercase
# 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ

while True:
    case = input('\n'
                 'case 1: Перевод из 10-й в b-ю систему \n'
                 'case 2: Перевод из b-й в 10-ю систему \n'
                 'case 3: Перевод из b-й в k-ю систему \n'
                 'case 0: Выход из программы \n')

    if case == '1':
        n = int(input('Введите число для перевода: '))
        b = int(input('Введите b-ю систему счисления: '))
        r = ''
        while n > 0:
            r += alphabet[n % b]
            n //= b
        print(f'Результат перевода: {r[::-1]}')

    elif case == '2':
        b = int(input('Введите b-ю систему счисления: '))
        r = input(f'Введите число в {b}-й  системе для перевода: ')
        print(f'Результат перевода: {int(r, b)}')

    elif case == '3':
        pass

    elif case == '0':
        print('Спасибо, что вы пользовались нашей программой!')
        break

    else:
        print('Я не пониманию никаких команд кроме case 1, 2, 3, 0.')



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
