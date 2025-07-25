# region Домашка: ******************************************************************

'''
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print("Равносторонний")
elif a != b != c != a:
    print('Разносторонний')
else:
    print("Равнобедренный")
'''


'''
H = int(input())
M = int(input())
if 0 <= H <= 4:
    print('Ночь')
elif H == 5:
    if 0 <= M <= 29:
        print('Ночь')
    else:
        print('Утро')
'''


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Цикл for отвечает на запросы: "повтори 10 раз", "пробеги от А до В"
'''
# Работа for с функцией range(START, STOP, STEP)
# range(STOP-1)
# range(START, STOP-1)
# range(START, STOP-1, STEP)


for i in range(10):  # range(STAR=0, STOP=10-1)
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
print()

for i in range(2, 10):  # range(STAR=2, STOP=10-1)
    print(i, end=' ')  # 2 3 4 5 6 7 8 9
print()

for i in range(2, 10, 2):  # range(STAR=2, STOP=10-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8
print()

for i in range(2, 10+1, 2):  # range(STAR=2, STOP=10-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10
print()

for i in range(10, 0, -1):  # # range(STAR=10, STOP=1, STEP=-1)
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1
print()


# Работа цикла for с списками
# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']

print(len(M))  #


# Такой способ используется для перебора и фильтрации элементов списка
for x in M:
    print(x, end=' ')  # a b c d e
print()


for x in M:
    if x > 'a' and x < 'e':
        print(x, end=' ')  # b c d 
print()


# Такой способ используется, если мы хотим изменить элементы списка
for i in range(len(M)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e
print()


for i in range(len(M)):
    M[i] = M[i] * i
print(M)  # ['', 'b', 'cc', 'ddd', 'eeee']
'''

# Цикл while отвечает на запросы: "повторяй пока условие верно", "бесконечный цикл"

for i in range(2, 10+1, 2):  # range(STAR=2, STOP=10-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10
print()

i = 2
while i <= 10:
    print(i, end=' ')
    i += 2  # 2 4 6 8 10
print()

'''
n = 8
b = 2
r = ''
while n > 0:
    r = str(n % b) + r
    n //= b
print(r)


alp = sorted('0123456789qwertyuiopasdfghjklzxcvbnm')
def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r


print(convert(8, 2))
print(convert(8, 3))
'''


# Бесконечный цикл и операторы break, continue, exit()
'''
k = 0
while True:
    k += 1
    if k % 2 == 0:
        continue  # прерывает итерацию (шаг) цикла 
    if k == 50_000:
        exit()  # прерывание вообще всей программы
    if k == 100_000:
        break  # прерывает выполнение цикла в котором лежит
    print(k)
print('Продолжение программы')
'''


# Программу для проверки паролей:

from random import randint, choice
from time import sleep

password_error_messages = [
    "Неверный пароль, попробуйте снова:",
    "Неправильный пароль, введите еще раз:",
    "Пароль не подходит, попробуйте еще:",
    "Ошибка в пароле, повторите попытку:",
    "Введен неверный пароль, попробуйте еще раз:",
    "Пароль не совпадает, введите снова:",
    "Неверный пароль, пожалуйста, попробуйте еще:",
    "Пароль ошибочный, повторите ввод:",
    "Неправильный пароль, введите заново:",
    "Пароль не принят, попробуйте снова:"
]

password = 'qwerty'
count = 0
pas = input('Введите пароль: ')
while True:
    if pas == password:
        print('Пароль верный')
        break
    count += 1
    if count == 3:
        print('Пройди проверку на робота: ')
        a = randint(1, 100)
        b = randint(1, 100)
        x = int(input(f'Решите пример: {a} + {b} = '))
        if x == a + b:
            count = 0
            print("Проверка пройдена успешно!")
        else:
            print('Проверка не пройдена, попробуйте через 5 минут')
            sleep(5 * 60)
    pas = input(choice(password_error_messages))

print('Добро пожаловать в программу ')

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
