# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Цикл for отвечает на запросы: "повтори N раз", "пробеги от А до В"

# Работы через функцию range()
'''
# range(0, STOP-1, 1)    range(10)
# range(START, STOP-1, 1)    range(2, 10)
# range(START, STOP-1, STEP)    range(2, 10, 2)

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

for i in range(10, 1, -1):
    print(i, end=' ')
print()
'''


# Работы напрямую через последовательность
'''
# i   0    1    2    3    4
L = ['a', 'b', 'c', 'd', 'e']

for x in L:
    print(x, end=' ')  # a b c d e
print()

for x in L:
    if x in 'ae':
        print(x, end=' ')  # a e
print()


print(len(L))  # 5 - Кол-во элементов в списке L

for i in range(len(L)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(L[i], end=' ')  # a b c d e
print()

for i in range(len(L)):
    L[i] = L[i] * i
print(L)  # ['', 'b', 'cc', 'ddd', 'eeee']
'''


# Цикл while отвечает на запросы: "пока условие верное - делаем действие", "бесконечный цикл"
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


# Перевод из 10-й в b-ю систему
'''
n = 8
b = 2
r = ''
while n > 0:
    r = str(n % b) + r
    n //= b
print(r)
'''

'''
from string import *
alp = digits + ascii_uppercase
print(alp) # 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(alp[:2]) # 01
print(alp[:8]) # 01234567
print(alp[:16]) # 0123456789ABCDEF

# alp = '0123456789ABCDE....'

alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r

print(convert(10000, 2))  # 10011100010000
print(convert(10000, 8))  # 23420
print(convert(10000, 16))  # 2710
print(convert(10000, 24))  # H8G
'''


# Бесконечные циклы и операторы: break, continue, exit()
'''
k = 0
while True:
    k += 1
    if k % 2 != 0:
        continue  # Прерывает итерацию (шаг) цикла
    if k == 50_000:
        break  # Прерывает цикл в котором мы лежим
    if k == 100_000:
        exit()  # Прерывает выполнение сразу всей программы
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
# на следующем уроке:
