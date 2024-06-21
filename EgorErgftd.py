# region Домашка: ******************************************************************

"""
a = int(input())

d = str(a)
while len(d) != 5:
    a = int(input())
    d = str(a)

q = [int(w) for w in str(a)]
'''
q = []
for i in range(5):
    w = a % 10
    q.append(w)
    a //= 10
q.reverse()
'''

if q[0] * q[2] == q[1] + q[3] + q[4]:
    print("Да")
else:
    print("Нет")
"""

"""
a = int(input())
b = int(input())
c = int(input())

suma = 0

if (a % 7 == 0 and a % 49 != 0) or a % 40 == 0:
    suma += a
if (b % 7 == 0 and b % 49 != 0) or b % 40 == 0:
    suma += b
if (c % 7 == 0 and c % 49 != 0) or c % 40 == 0:
    suma += c

print(suma)
"""

"""
a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print('Это равносторонний треугольник')
elif a == b and a + b > c or b == c and b + c > a or c == a and a + c > b:
    print('Это равнобедренный треугольник')
elif a + b > c or b + c > a or a + c > b:
    print('Это разносторонний треугольник')
else:
    print('Это не треугольник')
"""
# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Два типа циклов for, while

# for: отвечает на запросы: "повтори n раз", "пробеги от a до b"
'''
for i in range(10):  # range(START=0, STOP=10-1, STEP=1)
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
print()

for i in range(2, 10):  # range(START=2, STOP=10-1, STEP=1)
    print(i, end=' ')  # 2 3 4 5 6 7 8 9
print()


for i in range(2, 10, 2):  # range(START=2, STOP=10-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 - все четные
print()


for i in range(1, 10, 2):  # range(START=1, STOP=10-1, STEP=2)
    print(i, end=' ')  # 1 3 5 7 9 - все нечетные
print()

for i in range(2, 10+1, 2):  # range(START=2, STOP=10-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10
print()

for i in range(10, 0, -1):
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1
print()

# через цикл for удобно работать с последовательностями

# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']

print(len(M))  # 5

for x in M:
    print(x, end=' ')  # a b c d e 
print()  


for x in M:
    if x in 'aeui':
        print(x, end=' ')  # a e 
print()  


for i in range(len(M)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e
print()

for i in range(len(M)):
    M[i] = M[i] * i
print(M)  # ['', 'b', 'cc', 'ddd', 'eeee']
'''

# while: отвечает на запросы: "пока условие выполняется..", "бесконечный цикл"

for i in range(2, 10+1, 2):  # range(START=2, STOP=10-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10
print()

i = 2
while i <= 10:
    print(i, end=' ')  # 2 4 6 8 10
    i += 2
print()

# Функция для перевода в n-ую систему счисления
'''
num = 8
base = 2
res = ''
while num > 0:
    res += str(num % base)
    num //= base
res = res[::-1]
print(res)
'''

'''
num = 8
base = 2
res = ''
while num > 0:
    res = str(num % base) + res
    num //= base
print(res)
'''
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
num = 8
base = 2
res = ''
while num > 0:
    res = alphabet[num % base] + res
    num //= base
print(res)
'''

'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
num = int(input('Введите 10-е число: '))
base = int(input('Введите n-ю систему счисления: '))
res = ''
while num > 0:
    res = alphabet[num % base] + res
    num //= base
print(res)
'''


# Бесконечный цикл
'''
k = 0
while True:
    k += 1
    print(k)
'''
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
while True:
    case = int(input('case 1: Перевод из 10-й в base систему счисления \n'
                     'case 2: Перевод из base системы счисления в 10-ю \n'
                     'case 3: Перевод из base системы счисления в n-ю систему \n'
                     'case 0: exit \n'))

    if case == 1:
        num = int(input('Введите 10-е число: '))
        base = int(input('Введите base систему счисления: '))
        res = ''
        while num > 0:
            res = alphabet[num % base] + res
            num //= base
        print(f'Результат перевода: {res} \n')

    elif case == 2:
        base = int(input('Введите base систему счисления: '))
        res = input(f'Введите число в {base}-й системе счисления: ')
        print(f'Результат перевода: {int(res, base)} \n')

    elif case == 3:
        pass

    elif case == 0:
        print('Конец программы.')
        break
'''

from random import randint, choice
import time

list_of_variants = [
    'Пароль неверный, повторите попытку: ',
    'Неправильный пароль, пожалуйста, попробуйте еще раз: ',
    'Пароль введен неверно, попробуйте еще раз: ',
    'Не верный пароль, пожалуйста, повторите ввод: ',
    'Введен неправильный пароль, попробуйте еще раз: '
]


def verify_captcha():
    b = randint(0, 10)
    c = choice(['+', '-', '//', '*'])
    a = randint(b, 10+b)

    x = int(input(f'Пройдите проверку на 🤖, решив задачу: {a} {c} {b} = '))
    if c == '+' and x == a + b:
        return 0
    elif c == '-' and x == a - b:
        return 0
    elif c == '*' and x == a * b:
        return 0
    elif c == '//' and x == a // b:
        return 0
    else:
        print('Вы не прошли проверку, попробуйте повторить попытку через 5 минут')
        time.sleep(5 * 60)
        return 0


password = 'qwerty'
pas = input('Введите ваш пароль: ')
count = 0
while True:
    count += 1
    if pas == password:
        print('Welcome!')
        break
    if count == 3:
        count = verify_captcha()
    pas = input(choice(list_of_variants))

print('Добро пожаловать в ваш личный кабинет..')

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
