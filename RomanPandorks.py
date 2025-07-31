# region Домашка: ******************************************************************

# https://stepik.org/lesson/1309432/step/6?unit=1324548
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


# https://stepik.org/lesson/1309432/step/8?unit=1324548
'''
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print("Равносторонний")
elif a == b or a == c or b == c:
    print("Равнобедренный")
else:
    print("Разносторонний")
'''


# https://stepik.org/lesson/1309432/step/10?unit=1324548
'''
a = int(input())
if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
    print("Високосный")
else:
    print("Обычный")
'''

# https://stepik.org/lesson/1309432/step/11?unit=1324548
'''
H = int(input())
M = int(input())
if 0 <= H <= 4:
    print('Ночь')
elif H == 5:
    if 0 <= M <= 29:
        print('Ночь')
    elif 30 <= M <= 59:
        print('Утро')
elif 6 <= H <= 11:
    print('Утро')
'''


# https://stepik.org/lesson/1309431/step/13?unit=1324547
'''
k = int(input())
k = str(k)
print(f'Сумма чисел: {int(k) + int(k*2) + int(k*3)}')
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# В Пайтон есть два типа циклом: for и while

# Цикл for отвечает на запросы: "повтори n раз", "пробеги от А до В"

# Работа цикла for с функцией range(START, STOP-1, STEP)
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

for i in range(1, 10, 2):  # range(START=1, STOP=10-1, STEP=2)
    print(i, end=' ')  # 1 3 5 7 9
print()

for i in range(2, 10+1, 2):  # range(START=2, STOP=10-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10
print()

for i in range(10, 0, -1):  # range(START=10, STOP=1, STEP=-1)
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1
print()


# Работа цикла for с списками и другими итерируемыми объектами:

# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']

print(len(M))  # 5 - Длину (кол-во элементов) списка

# Что такой способ позволяет просто пробегать элементы и фильтровать их
for x in M:
    print(x, end=' ')  # a b c d e
print()

for x in M:
    if x in 'ae':
        print(x, end=' ')  # a e
print()

# Такой способ позволяет изменять элементы списка

for i in range(len(M)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e
print()


for i in range(len(M)):
    M[i] = M[i] * i
print(M)  # ['', 'b', 'cc', 'ddd', 'eeee']
'''

# Цикл while отвечает на запросы: "выполняем действие, пока условие верно", "бесконечный цикл"
'''
for i in range(2, 10+1, 2):  # range(START=2, STOP=10-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10
print()


i = 2
while i <= 10:
    print(i, end=' ')  # 2 4 6 8 10 
    i += 2 
print()
'''

'''
n = int(input('n: '))  # 8
b = int(input('b: '))  # 2
r = ''
while n > 0:
    r += str(n % b)
    n //= b
r = r[::-1]
print(r)


n = int(input('n: '))  # 8
b = int(input('b: '))  # 2
r = ''
while n > 0:
    r = str(n % b) + r
    n //= b
print(r)


alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
n = int(input('n: '))  # 8
b = int(input('b: '))  # 2
r = ''
while n > 0:
    r = alp[n % b]+ r
    n //= b
print(r)
'''

'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r

print(convert(8, 2))  # 1000
print(convert(8, 4))  # 20
'''


# Бесконечные циклы и операторы: break, continue, exit()
'''
k = 0
while True:
    k += 1
    if k % 2 != 0:
        continue  # Прерывает итерацию (шаг) цикла
    if k == 100_000:
        exit()  # Прерывает выполнение вообще всей программы
    if k == 50_000:
        break  # Выход из цикла в котором сейчас находимся
    print(k)

print('Продолжение программы')
'''


# Напишем простую программу перевода в различные системы счисления

from string import digits, ascii_uppercase
alp = digits + ascii_uppercase
# print(alp)  # 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ

def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r


while True:
    case = input('\n'
                 'case 1: Перевод из 10-й в n-ую систему счисления: \n'
                 'case 2: Перевод из n-й в 10-ую систему счисления: \n'
                 'case 3: Перевод из n-й в k-ую систему счисления: \n'
                 'case 0: Выход из программы \n'
                 'case: ')


    if case == '1':
        n = int(input('Введите десятичное число, которые хотите перевести: '))
        b = int(input('Введите систему счисления в которую будем переводить: '))
        c = convert(n, b)
        print(f'Результат перевода числа {n} в {b}-ю систему: {c}')


    elif case == '2':
        b = int(input('Введите систему счисления из которой будем переводить: '))
        c = input(f'Введите число в {b}-й системе счисления: ')
        n = int(c, b)
        print(f'Результат перевода числа {c} из {b}-й системы: {n}')


    elif case == '3':
        pass


    elif case == '0':
        print('Спасибо, что пользовались нашим калькулятором!')
        break


    else:
        print('Я не понимаю никаких команд, кроме: 1/2/3/0')

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = []
# КЕГЭ = []
# на следующем уроке: Библиотеки перечислить, Условные операторы, Циклы


