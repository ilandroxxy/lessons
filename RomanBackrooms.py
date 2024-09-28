# region Домашка: ******************************************************************

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
a = int(input())
if a > 5:
    print('Слишком большое число')
else:
    print('Оценка:', a)
'''

# Проверка длины слова
'''
M = [1, 2, 3, 4, 5]
print(len(M))  # 5 - Возвращает длину списка (кол-во элементов в нем)

word = input()
if len(word) >= 10 or len(word) % 2 == 0:
    print('ДА')
else:
    print('НЕТ')
'''

'''
a = int(input())
b = int(input())
c = int(input())

if max(a, b, c) < (a + b + c) - max(a, b, c):
    print('ДА')
else:
    print('НЕТ')
'''
# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Цикл for отвечает на запросы: "повтори N раз", "пробеги от А до В"

# Цикл for с функцией range()
'''
# range(STOP-1)
# range(START, STOP-1)
# range(START, STOP-1, STEP)

for i in range(10):  # range(start=0, STOP=10-1, step=1)
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
print()


for i in range(2, 10):  # range(START=2, STOP=10-1, step=1)
    print(i, end=' ')  # 2 3 4 5 6 7 8 9
print()


for i in range(2, 10, 2):  # range(START=2, STOP=10-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8
print()


for i in range(2, 10+1, 2):  # range(START=2, STOP=10-1, STEP=2)
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

print(len(M))  # 5

for i in range(len(M)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e
print()


for i in range(len(M)):
    M[i] = M[i] * i
print(M)  # ['', 'b', 'cc', 'ddd', 'eeee']

# Работа напрямую с последовательностями

# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']

for x in M:
    print(x, end=' ')  # a b c d e
print()

for x in M:
    if x in 'ae':
        print(x, end=' ')  # a e 
print()  
'''

# Цикл while отвечает на запросы: "пока условие верно - выполняй", "бесконечный цикл"
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
n = 8
b = 2
R = []
while n > 0:
    R.append(n % b)  # .append() - добавление нового элемента в конец списка
    n //= b
R.reverse()  # .reverse() - разворачивает список
print(R)    # [1, 0, 0, 0]


print(int('1000', 2))  # 8


n = 8
b = 2
r = ''
while n > 0:
    r += str(n % b)  # .append() - добавление нового элемента в конец списка
    n //= b
r = r[::-1]  # срез в обратном порядке
print(r)    # 1000

print(int(r, 2))  # 8


alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
# print(alphabet)  # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C'

def convert(n, b):
    r = ''
    while n > 0:
        r += alphabet[n % b]
        n //= b
    r = r[::-1]
    return r


print(convert(123456789, 16))
r = convert(123456789, 16)

print(int(r, 16))  # 123456789
'''


# Бесконечные циклы и операторы break, continue, exit()
'''
k = 0
while True:
    k += 1
    if k % 2 != 0:
        continue  # прерывает итерацию (шаг) цикла
    if k == 1_000_000:
        break  # прерывает выполнение цикла в котором сейчас находится
    if k == 2_000_000:
        exit()  # выход из программы, то есть останавливает программу
    print(k)

print('Продолжение программы')
'''


'''
from random import randint, choice
from time import sleep


error_messages = [
    'Пароль неверный, повторите попытку: ',
    'Попробуйте ввести пароль еще раз: '
]

password = 'qwerty'
pas = input('Введите пароль пользователя: ')
count = 0
while True:
    if pas == password:
        print('Добро пожаловать!')
        break
    count += 1
    if count == 3:
        print('Пройдите проверку на робота решив задачу: ')
        a = randint(0, 100)
        b = randint(0, 100)
        x = int(input(f'{a} + {b} = '))
        if x == a + b:
            print('Верно, проверка пройдена.')
            count = 0
        else:
            print('Проверка не пройдена, повторите попытку через 5 минут')
            sleep(5 * 60)

    pas = input(choice(error_messages))
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
