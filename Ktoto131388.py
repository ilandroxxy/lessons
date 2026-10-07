

# Сравнение двух чисел и проверки деления
# https://stepik.org/lesson/1309432/step/9?unit=1324548
# Напишите программу, которая запрашивает у пользователя
# два числа и определяет, какое из чисел больше, а затем
# проверяет, делится ли большее число на второе.
# Если делится, то вывести "Делится". Иначе вывести "Не делится"
'''
a = int(input())
b = int(input())
if a > b:
    if a % b == 0:
        print("Делится")
    else:
        print("Не делится")
else:
    if b % a == 0:
        print("Делится")
    else:
        print("Не делится")
'''
from os import pread

# https://stepik.org/lesson/1309432/step/10?unit=1324548
# Определение года високосного
'''
year = int(input())
if year % 4 == 0 and year % 100 != 0:
    print("Високосный")
elif year % 400 == 0:
    print("Високосный")
else:
    print("Обычный")
'''



# Теория циклов for и while


# Цикл for отвечает на запросы: "Повтори действие N раз", "Пробеги от А до В"
'''
# range(0, STOP-1, 1)
# range(START, STOP-1)
# range(START, STOP-1, STEP)

for i in range(10):
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
print()

for i in range(2, 10+1):
    print(i, end=' ')  # 2 3 4 5 6 7 8 9 10
print()

for i in range(2, 10+1, 2):
    print(i, end=' ')  # 2 4 6 8 10
print()

for i in range(1, 10+1, 2):
    print(i, end=' ')  # 1 3 5 7 9
print()


for i in range(5, 50+1, 5):  # - Перебрали все числа, которые делятся на 5
    print(i, end=' ')  # 5 10 15 20 25 30 35 40 45 50
print()

for i in range(3, 30+1, 3):  # - Перебрали все числа, которые делятся на 3
    print(i, end=' ')  # 3 6 9 12 15 18 21 24 27 30
print()


for i in range(10, 0-1, -1):
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1 0
print()


# Работа цикла for с последовательностями

# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']

print(len(M))  # 5 - возвращает кол-во элементов в списке М (длина списка)

for x in M:
    print(x, end=' ')  # a b c d e
print()

for x in M:
    if x in 'ae':
        print(x, end=' ')  # a e
print()


for i in range(len(M)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e
print()

for i in range(len(M)):
    M[i] = M[i] * 2
print(M)  # ['aa', 'bb', 'cc', 'dd', 'ee']


# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']

for i in range(len(M)):
    M[i] = M[i] * i
print(M)  # ['', 'b', 'cc', 'ddd', 'eeee']
'''



# Цикл while  отвечает на запросы: "Пока условие верное - делаем действие", "Бесконечные циклы"
'''
for i in range(2, 10+1, 2):
    print(i, end=' ')  # 2 4 6 8 10
print()


i = 2
while i <= 10:
    print(i, end=' ')
    i += 2
print()
'''


# Бесконечный цикл и операторы break, continue и exit()
'''
k = 0
while True:
    k += 1
    if k % 2 != 0:
        continue
    if k == 50_000:
        break  # - прерывает выполнения цикла в котором лежит
    if k == 100_000:
        exit()  # - прерывает выполнение всей программы
    print(k)
print('Выход из цикла')
'''


# Пример использования бесконечного цикла
'''
password = 'qwerty'
pas = input('Введите пароль: ')
while True:
    if pas == password:
        print('Пароль верный.')
        break
    else:
        pas = input('Повторите попытку: ')

print('Добро пожаловать! ')
'''



# Цикл while используется для решения 5 и 14 номеров (перевод в различные системы счисления)
'''
def convert(n, b):
    r = ''
    while n > 0:
        r = str(n % b) + r
        n //= 2
    return r

print(convert(8, 2))  # 1000
print(int('1000', 2))  # 8


n = 8

print(bin(n)[2:])  # 1000
print(int('1000', 2))  # 8

print(oct(n)[2:])  # 10
print(int('10', 8))  # 8

print(hex(n)[2:])  # 8
print(int('8', 16))  # 8
'''



# № Напишите программу, которая принимает два натуральных числа a и b (a ≤ b) и
# выводит все целые числа от a до b включительно, удовлетворяющие хотя бы одному из условий:
#
# число кратно 20
# число кратно 7 и 14 одновременно
# число оканчивается на 9.

a = int(input())
b = int(input())

for x in range(a, b+1):
    if x % 20 == 0 or (x % 7 == 0 and x % 14 == 0) or x % 10 == 9:
        print(x)







