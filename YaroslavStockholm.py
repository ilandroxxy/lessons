# region Домашка: ******************************************************************

'''
a = int(input())
b = int(input())
c = int(input())
summa = 0
if a % 7 == 0 and a % 49 != 0 or a % 40 == 0:
    summa += a
if b % 7 == 0 and b % 49 != 0 or b % 40 == 0:
    summa += b
if c % 7 == 0 and c % 49 != 0 or c % 40 == 0:
    summa += c  # summa = summa + c
print(summa)
'''

'''
x = 15
x -= 5
print(x)  # 10
x **= 2
print(x)  # 100
x //= 2
print(x)  # 50
'''

'''
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print('Равносторонний')
elif a != b != c != a:
    print('Разносторонний')
else:
    print('Равнобедренный')
'''

'''
print(max([1, 2, 3, 4, 5]))
print(max(1, 2, 3, 4, 5))
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Цикл for отвечает на запросы: "повтори N раз", "пробеги от А до В"
'''
# Работа цикла for с функцией range()
# range(STOP-1)
# range(START, STOP-1)
# range(START, STOP-1, STEP)


for i in range(10):  # range(START=0, STOP=10-1, STEP=1)
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
print()

for i in range(2, 10):  # range(START=2, STOP=10-1, STEP=1)
    print(i, end=' ')  # 2 3 4 5 6 7 8 9
print()

for i in range(2, 10, 2):  # range(START=2, STOP=10-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8
print()

n = 10
for i in range(2, n+1, 2):  # range(START=2, STOP=11-1, STEP=2)
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
print(len(M))  # 5 - возвращает длину последовательности (кол-во элементов в ней)

for i in range(len(M)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e
print()


for i in range(len(M)):
    M[i] = M[i] * i
print(M)  # ['', 'b', 'cc', 'ddd', 'eeee']
'''

# Работа с последовательностями напрямую через цикл for
'''
# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']

for x in M:
    print(x, end=' ')  # a b c d e
print()

for x in M:
    if x in 'ae':
        print(x, end=' ')  # a e
print()

A = ['a', 'h', 'a', 'b', 'b', 'h', 'b', 'b', 'e', ]
for x in A:
    if x in 'aeo':
        print(x, end=' ')  # a a e
print()
'''

# Цикл while отвечает на запросы: "пока условие верно, выполняем действие", "бесконечные циклы"

'''
for i in range(2, 10+1, 2):  # range(START=2, STOP=11-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10
print()

i = 2
while i <= 10:
    print(i, end=' ')  # 2 4 6 8 10
    i += 2
print()
'''

# Перевод из 10-й в n-ую систему счисления
'''
n = int(input('n: '))
b = int(input('b: '))
R = []
while n > 0:
    R.append(n % b)
    n //= b
R.reverse()
print(R)


print(int('1000'))    # 1000
print(int('1000', 2))    # 8 - перевод из 2-й в 10-ю
print(int('1000', 16))    # 4096 - перевод из 16-й в 10-ю
'''


# Перевод из 10-й в n-ую систему счисления (через строку)
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

n = int(input('n: '))
b = int(input('b: '))
r = ''
while n > 0:
    r += alphabet[n % b]
    n //= b
r = r[::-1]  # Развернули строку в обратном порядке
print(r)  # 7511213115 -> 75BCD15
# n: 123456789
# b: 16
# 75BCD15
'''

'''
from string import *
alphabet = digits + ascii_uppercase
# print(alphabet)  # 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ

def convert(n, b):
    r = ''
    while n > 0:
        r += alphabet[n % b]
        n //= b
    r = r[::-1]
    return r


n = 123456789
b = 16
r = convert(n, b)
print(r)  # 75BCD15
print(int(r, 16))  # 123456789
'''


# Бесконечные циклы и операторы break, continue, exit
'''
k = 0
while True:
    k += 1
    if k % 2 == 0:
        continue  # Прерывает итерацию (шаг) цикла
    if k == 2_000_001:
        break  # Прерывает исполнение цикла в котором он лежит
    if k == 1_000_000:
        exit()  # Просто прерывает выполнение программы
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
# КЕГЭ  = []
# на следующем уроке: Напишем программу проверки паролей,
# и консольную программу калькулятор перевода в системы счисления
