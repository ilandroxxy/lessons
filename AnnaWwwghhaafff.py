# region Домашка: ******************************************************************

# https://stepik.org/lesson/1309433/step/8?unit=1324549
'''
a = input()
if a == 'Информатика' or a == 'Программирование':
    print("Петя берёт с собой компьютер")
else:
    print("Петя берёт с собой тетрадь")
'''


# Пару слов про функцию len()
'''
n = 56  # неитерируемый объект
# print(len(n))
# TypeError: object of type 'int' has no len()

# i  01
s = '56'  # итерируемый объект
L = ['5', '6']
print(len(s))  # 2 - Функция len() возвращает длину (кол-во элементов) списка/строки..
'''


# https://stepik.org/lesson/1309433/step/9?auth=login&unit=1324549
'''
a = input()
if len(a) >= 10 or len(a) % 2 == 0:
    print("ДА")
else:
    print("НЕТ")
'''


# https://stepik.org/lesson/1309433/step/10?auth=login&unit=1324549
'''
a = int(input())
b = int(input())
c = int(input())

if max(a, b, c) <= (a + b + c) - max(a, b, c):
    print('ДА')
else:
    print('НЕТ')
'''

'''
a = int(input())
b = int(input())
c = int(input())

if a > b and a > c:
    if a <= c + b:
        print('ДА')
    else:
        print('НЕТ')
elif b > a and b > c:
    if c <= a + b:
        print('ДА')
    else:
        print('НЕТ')
elif c > a and c > b:
    if c <= a + b:
        print('ДА')
    else:
        print('НЕТ')
elif a == b == c:
    print('ДА')
else:
    print('НЕТ')
'''


# https://stepik.org/lesson/1309434/step/5?unit=1324550
'''
a = int(input())
b = int(input())
if a < b:
    for i in range(a, b+1):
        print(i)
else:
    for i in range(a, b-1, -1):
        print(i)
'''


# https://stepik.org/lesson/1309434/step/6?unit=1324550
'''
a = int(input())
b = int(input())
for i in range(a, b+1):
    if (i % 20 == 0) or (i % 7 == 0 and i % 14 == 0) or (i % 10 == 9):
        print(i)
'''


# https://stepik.org/lesson/1309434/step/7?unit=1324550
'''
m = int(input())  # 14
total = 1
for j in range(1, m+1):
    if m % j == 0:
        total *= j
print(total)
'''


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
from random import randint
from time import sleep


password = 'qwerty'
pas = input('Введите пароль: ')
count = 1
while True:
    if pas == password:
        print('Пароль верный!')
        break
    else:
        count += 1
        pas = input('Пароль неверный, повторите попытку: ')
        if count == 3:
            print('Пройдите проверку на робота. ')
            a = randint(0, 100)
            b = randint(0, 100)
            x = int(input(f'Решите пример: {a} + {b} = '))
            if x == a + b:
                print('Пример решен верно.')
                count = 0
            else:
                print('Повторите попытку через 5 минут.')
                sleep(5 * 60)

print('Добро пожаловать в личный кабинет.')
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
