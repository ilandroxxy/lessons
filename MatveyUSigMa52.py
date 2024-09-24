# region Домашка: ******************************************************************

# Проверка соотношения для пятизначного числа
'''
a = int(input())
p1 = a // 10000
p2 = (a // 1000) % 10
p3 = (a // 100) % 10
p4 = (a // 10) % 10
p5 = a % 10
proiz = p1 * p3
summa = p2 + p4 + p5
if proiz == summa:
    print("Да")
else:
    print("Нет")
'''

'''
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print("Равносторонний")
elif a == b or a == c or b == c:
    print("Равнобедренный")
elif a != b and a != c:
    print("Разносторонний")


a = int(input())
b = int(input())
if max(a, b) % min(a, b) == 0:
    print('Делится')
else:
    print('Не делится')
'''
# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Цикл for отвечает на запросы: "повтори n раз", "пробеги от А до В"

# Работа с циклом for через функцию range()

# range(STOP)
# range(START, STOP-1)
# range(START, STOP-1, STEP)
'''
for i in range(10):  # range(START=0, STOP=10-1, STEP=1)
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
print()


for i in range(2, 10):  # range(START=2, STOP=10-1, STEP=1)
    print(i, end=' ')  # 2 3 4 5 6 7 8 9
print()


for i in range(2, 10, 2):  # range(START=2, STOP=10-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8
print()


for i in range(2, 10+1, 2):  # range(START=2, STOP=11-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10
print()


for i in range(10, 0):  # range(START=10, STOP=0-1, STEP=1)
    print(i, end=' ')  #
print()


for i in range(10, 0, -1):  # range(START=10, STOP=0-1, STEP=-1)
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1
print()


# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']

print(len(M))  # Функция len() - возвращает длину списка (кол-во элементов в нем)

for i in range(len(M)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e
print()


for i in range(len(M)):
    M[i] = M[i] * i

print(M)  # ['', 'b', 'cc', 'ddd', 'eeee']
'''

# Работа с циклом for напрямую с последовательностями
'''
# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']

for x in M:
    print(x, end=' ')  # a b c d e
print()

for x in M:
    if x in 'ae':  # a e 
        print(x, end=' ')
print()
'''

# Цикл while отвечает на запросы: "пока условие верно, повторяй действие", "бесконечные циклы"
'''
for i in range(2, 10+1, 2):  # range(START=2, STOP=11-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10
print()

i = 2
while i <= 10:
    print(i, end=' ')  # 2 4 6 8 10 
    i += 2  # i = i + 2
print()
'''

# Алгоритм перевода через список
'''
n = 8
b = 2
R = []  # Создание пустого списка
while n > 0:
    R.append(n % b)
    n //= b  # n = n // b
R.reverse()
print(R)
'''

# Алгоритм перевода через строку
'''
n = 8
b = 2
r = ''
while n > 0:
    r = str(n % b) + r
    n //= b  # n = n // b
print(r)

print(int(r, 2))  # 8
'''

# Универсальный алгоритм перевода
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
n = 8
b = 2
r = ''
while n > 0:
    r = alphabet[n % b] + r
    n //= b  # n = n // b
print(r)

print(int(r, 2))  # 8
'''


# Универсальный алгоритм перевода упакованный в функцию
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    r = ''
    while n > 0:
        r = alphabet[n % b] + r
        n //= b
    return r


print(convert(8, 2))  # 1000
print(convert(123456789, 16))  # 75BCD15
print(int('75BCD15', 16))  # 123456789
'''


# Бесконечные циклы и операторы break, continue, exit()
'''
k = 0
while True:
    k += 1
    if k % 2 == 0:
        continue  # Прерывает итерацию цикла 
    if k == 1_000_000:
        break  # Прерывает цикл в котором мы сейчас находимся
    if k == 2_000_000:
        exit()  # Полностью останавливает программу
    print(k)

print('Продолжение программы')
'''

'''
from random import randint
from time import sleep

password = 'qwerty'
pas = input('Введите пароль для проверки: ')
count = 0
while True:
    if pas == password:
        print('Добро пожаловать!')
        break
    count += 1
    if count == 3:
        print('\nПройдите проверку на робота, решив пример: ')
        a = randint(0, 100)
        b = randint(0, 100)
        x = int(input(f'{a} + {b} = '))
        if x == a + b:
            print('Проверка пройдена успешно.')
            count = 0
        else:
            print('Неверная попытка, попробуйте через 5 минут')
            sleep(5 * 60)
    pas = input('Пароль неверный, повторите попытку: ')
'''

# endregion Урок: ********************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = []
# КЕГЭ  = []
# на следующем уроке:
