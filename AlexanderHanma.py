# region Домашка: ******************************************************************

'''
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print('Это равносторонний треугольник')
elif a != b and b != c and a != c:
    print('Это разносторонний треугольник')
else:
    print('Это равнобедренный треугольник')
'''

'''
a = int(input())
b = int(input())
c = int(input())
summa = 0
if (a % 7 == 0 and a % 49 != 0) or a % 40 == 0:
    summa += a
if (b % 7 == 0 and b % 49 != 0) or b % 40 == 0:
    summa += b
if (c % 7 == 0 and c % 49 != 0) or c % 40 == 0:
    summa += c
print(summa)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Циклы - это какие-то повторяющиеся действия

# for: отвечает на запросы: "повтори n раз", "пробеги от a до b"

# Работа цикла for с функцией range()
'''
for i in range(10):   # range(START=0, STOP=10-1, STEP=1)
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
print()


for i in range(2, 10):   # range(START=2, STOP=10-1, STEP=1)
    print(i, end=' ')  # 2 3 4 5 6 7 8 9
print()

for i in range(2, 10, 2):   # range(START=2, STOP=10-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 - все четные
print()

for i in range(1, 10, 2):   # range(START=2, STOP=10-1, STEP=2)
    print(i, end=' ')  # 1 3 5 7 9 - все нечетные
print()

for i in range(2, 10+1, 2):   # range(START=2, STOP=10-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10 - все четные
print()

for i in range(10, 0, -1):  # range(START=10, STOP=0-1, STEP=-1)
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1 
print()

# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
print(len(M))  # 5 - функция len() - возвращает длину списка М


for i in range(len(M)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e
print()

for i in range(len(M)):
    M[i] = M[i]
print(M)  # ['a', 'b', 'c', 'd', 'e']

for i in range(len(M)):
    M[i] = M[i] * i
print(M)  # ['', 'b', 'cc', 'ddd', 'eeee']
'''

# Работа цикла for с последовательностями
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

M = [2**i for i in range(20)]
print(M)  # [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]
'''


# while: отвечает на запросы: "выполняй действие пока истинно", "бесконечный цикл"

for i in range(2, 10+1, 2):   # range(START=2, STOP=10-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10 - все четные
print()

i = 2
while i <= 10:
    print(i, end=' ')  # 2 4 6 8 10
    i += 2
print()


# Перевод из 10-й в base-ю систему счисления:

num = 8
base = 2
M = []
while num > 0:
    M.append(num % base)  # .append() - метод добавления нового элемента в конец списка
    num //= base
M.reverse()
print(M)  # [1, 0, 0, 0]

num = 8
base = 2
res = ''
while num > 0:
    res = str(num % base) + res  # .append() - метод добавления нового элемента в конец списка
    num //= base
print(res)  # 1000

'''
num = int(input('Введите 10-е число: '))
base = int(input('Введите base систему счисления: '))
res = ''
while num > 0:
    res = str(num % base) + res  # .append() - метод добавления нового элемента в конец списка
    num //= base
print(res)  
'''

'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
num = int(input('Введите 10-е число: '))
base = int(input('Введите base систему счисления: '))
res = ''
while num > 0:
    res = alphabet[num % base] + res  # .append() - метод добавления нового элемента в конец списка
    num //= base
print(res)
'''

'''
a, b = 7, 2
# a = a + b
a += b
print(a)

a, b = 7, 2
# a = a // b
a //= b
print(a)
'''

# Бесконечный цикл while:
'''
k = 0
while True:
    k += 1
    if k % 2 != 0:
        continue  # прерывает итерацию цикла 
    if k == 100000:
        break  # - прерывает цикл в котором лежит
        exit()  # - Выход из программы (остановит программу)
    print(k)
'''

'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
while True:
    case = int(input('\n\ncase 1: Перевод из 10-й в base систему счисления \n'
                     'case 2: Перевод из base в 10-ю систему счисления \n'
                     'case 3: Перевод из base в n-ю систему счисления\n'
                     'case 0: exit \n\n\n'))

    if case == 1:
        num = int(input('Введите 10-е число: '))
        base = int(input('Введите base систему счисления: '))
        res = ''
        while num > 0:
            res = alphabet[num % base] + res  # .append() - метод добавления нового элемента в конец списка
            num //= base
        print(res)

    if case == 2:
        base = int(input('Введите base систему счисления: '))
        res = input(f'Введите число в {base}-й системе счисления: ')
        print(int(res, base))

    if case == 3:
        pass

    if case == 0:
        exit()
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
# на следующем уроке:
