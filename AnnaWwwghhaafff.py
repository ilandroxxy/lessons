# region Домашка: ******************************************************************

# https://stepik.org/lesson/1309431/step/10?unit=1324547
'''
a = int(input())
b = int(input())
print(f'Периметр прямоугольника: {2 * (a + b)}')
print(f'Площадь прямоугольника: {(a * b)}')
'''


# https://stepik.org/lesson/1309431/step/13?unit=1324547
'''
k = int(input())
summa = k + k * 11 + k * 111
print(f'Сумма чисел: {summa}')

k = input()  # '4'
summa = int(k) + int(k * 2) + int(k * 3)
print(f'Сумма чисел: {summa}')
'''


# https://stepik.org/lesson/1309432/step/4?unit=1324548
'''
n = int(input())
if n % 2 == 0:
    print('Чётное')
else:
    print('Нечётное')
'''


# https://stepik.org/lesson/1309432/step/5?unit=1324548
'''
n = int(input()) # 41392
a = n // 10000
b = (n // 1000) % 10
c = (n // 100) % 10
d = (n % 100) //10
e = n % 10
f = a * c
g = b + d + e
if f == g :
    print('Да')
else:
    print('Нет')
'''


# https://stepik.org/lesson/1309432/step/6?unit=1324548
'''
a = int(input())
b = int(input())
c = int(input())
summa = 0
if (a % 7 == 0 and a % 49 != 0) or a % 40 == 0:
    summa += a

print(summa)
'''



'''
a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print('Равносторонний')
elif a == b or a == c or b == c:
    print('Равнобедренный')
else:
    print('Разносторонний')
'''

'''
a = int(input())
b = int(input())
if a > b:
    if a % b == 0:
        print('Делится')
    else:
        print('Не делится')
else:
    if b % a == 0:
        print('Делится')
    else:
        print('Не делится')
'''

'''
y = int(input())
if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
    print('Високосный')
else:
    print('Обычный')
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Цикл for отвечает на запросы: "повторить 5 раз", "пробежать числа от 5 до 10"
'''
# Цикл for работает с функцией range()

# range(0, STOP-1, 1)
# range(START, STOP-1, 1)
# range(START, STOP-1, STEP)

for i in range(10):
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
print()


for i in range(2, 10):
    print(i, end=' ')  # 2 3 4 5 6 7 8 9
print()


for i in range(2, 10, 2):
    print(i, end=' ')  # 2 4 6 8
print()


for i in range(2, 10+1, 2):
    print(i, end=' ')  # 2 4 6 8 10
print()

for i in range(10, 0, -1):
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1
print()



# Цикл for работает с итерируемыми объектами (list, tuple, str)

# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']

print(len(M))  # 5 - кол-во элементов в итерируемом объекте

# Прямой перебор полезен, если нам нужно просто перебрать элементы или фильтровать их

for x in M:
    print(x, end=' ')  # a b c d e
print()

for x in M:
    if x in 'ae':
        print(x, end=' ')  # a e
print()


# Перебор через индексы помогает нам изменять элементы списка

for i in range(len(M)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e
print()

# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']

for i in range(len(M)):
    M[i] = M[i] * i
print(M)  # ['', 'b', 'cc', 'ddd', 'eeee']
'''


# Цикл while отвечает на запросы: "пока условие верно - выполняем", "бесконечный цикл"
'''
for i in range(2, 10+1, 2):
    print(i, end=' ')  # 2 4 6 8 10
print()


i = 2
while i <= 10:
    print(i, end=' ')  # 2 4 6 8 10
    i += 2
print()
'''


# Перевод в различные системы счисления
'''
n = 8
b = 2  # система счисления
r = ''
while n > 0:
    r = str(n % b) + r
    n //= b
print(r)

def convert(n, b):
    r = ''
    while n > 0:
        r = str(n % b) + r
        n //= b
    return r

n = int(input('Введите число в 10-й системе для перевода: '))
b = int(input('Введите систему счисления b: '))
print(convert(n, b))  # 1000
'''


# Бесконечные циклы и операторы break, continue, exit()
'''
k = 0
while True:
    k += 1
    if k % 2 != 0:
        continue  # прерывает выполнение итерации (шаг) цикла
    if k == 50_000:
        exit()  # прерывает вообще все выполнение программы
    if k == 100_000:
        break  # прерывает цикл в котором он лежит
    print(k)

print('Продолжение программы')
'''


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = []
# КЕГЭ = []
# на следующем уроке: Пример программы с бесконечными циклами 
