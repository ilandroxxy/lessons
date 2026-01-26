
# Цикл это некоторое повторяющееся действие


# Цикл for - отвечает на запросы: "Повтори n раз", "Пробеги от А до В"


# Работа с функцией range()

# range(0, STOP-1, 1)
# range(START, STOP)
# range(START, STOP, STEP)
'''
# range(0, STOP-1, 1)
for i in range(10):
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
print()

# range(START=3, STOP-1, 1)
for i in range(3, 10):
    print(i, end=' ')  # 3 4 5 6 7 8 9
print()

# range(START=2, STOP-1, STEP=2)
for i in range(2, 10, 2):
    print(i, end=' ')  # 2 4 6 8
print()

# range(START=2, STOP-1, STEP=2)
for i in range(2, 10+1, 2):
    print(i, end=' ')  # 2 4 6 8
print()

# range(START=10, STOP-1, STEP=-1)
for i in range(10, 0, -1):
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1
print()
'''


# Работа с последовательностями
'''
# i  01234
s = 'abcde'

# i   0    1    2    3    4
T = ('A', 'B', 'C', 'D', 'E')
L = ['A', 'B', 'C', 'D', 'E']

for x in L:
    print(x, end=' ')  # A B C D E
print()

for x in L:
    if x in 'AEUO':
        print(x, end=' ')  # A E
print()

print(len(L))  # 5 - Возвращает длину последовательности/кол-во элементов

# range(0, STOP = 5-1, 1)
for i in range(len(L)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(L[i], end=' ')  # A B C D E
print()

# i   0    1    2    3    4
L = ['A', 'B', 'C', 'D', 'E']

# Через индексы мы можем изменять элементы списка (последовательности)
for i in range(len(L)):
    L[i] = L[i] * i
print(L)  # ['', 'B', 'CC', 'DDD', 'EEEE']


M = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for x in M:
    if x % 2 == 0:
        print(x, end=' ')  # 2 4 6 8
print()

for i in range(len(M)):
    if M[i] % 2 == 0:
        M[i] = M[i] ** 2
print(M)  # [1, 4, 3, 16, 5, 36, 7, 64, 9]
'''




# Цикл while - отвечает на запросы: "Пока условие верное - цикл выполняется", "Бесконечные циклы"
'''
n = 123456
print(n % 10)  # 6
print(n % 100)  # 56
print(n % 1000)  # 456


# Забираем остаток через % и отбрасываем его через //
n = 123456

print(n % 10)  # 6
n //= 10
print(n)  # 12345

print(n % 10)  # 5
n //= 10
print(n)  # 1234

print(n % 10)  # 4
n //= 10
print(n)  # 123


# Программа разбиения целого числа на цифры 

n = 123456
N = []
while n > 0:
    print(n % 10, end=' ')  # 6 5 4 3 2 1 0
    N.append(n % 10)
    n //= 10

print(N)  # [6, 5, 4, 3, 2, 1]
'''


# Перевод в различные системы счисления
'''
n = int(input('Десятичное число: '))
b = int(input('Система счисления: '))
r = ''
while n > 0:
    r = str(n % b) + r
    n //= b
print(r)
'''


# Бесконечные циклы и операторы break, continue, exit(), pass
'''
k = 0
while True:
    k += 1
    if k % 2 != 0:
        continue  # Прерывает шаг итерации цикла в котором лежит
    if k == 100_000:
        break  # Прерывает выполнение цикла в котором сейчас лежит
    if k == 100:
        pass  # Пробка для условий или циклом
    if k == 50_000:
        exit()  # Функция, которая прерывает выполнение ВСЕЙ программы
    print(k)
    
print('Продолжение программы после циклы ')
'''

from random import randint
from time import time, sleep

password = 'qwerty'
pas = input('Введите пароль: ')
count = 0

while True:

    if pas == password:
        print('Пароль верный.')
        break

    else:
        count += 1
        if count == 3:
            print()
            print('Много неверных попыток.\n'
                  'Пройдите проверку на робота: ')
            a = randint(0, 100)
            b = randint(0, 100)
            x = int(input(f'Решите пример: {a} + {b} = '))
            if a + b == x:
                print('Пример решен верно.')
                print()
                count = 0
            else:
                print('Неверно пройдена проверка, повторите попытку через 5 минут! ')
                sleep(5 * 60)

        pas = input('Пароль неверный, повторите: ')


print('Добро пожаловать!')




































