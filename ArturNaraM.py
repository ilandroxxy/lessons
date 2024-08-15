

# int, float, str
'''
print(4 // 2, type(4 // 2))   # 2 <class 'int'>
print(4 / 2, type(4 / 2))   # 2.0 <class 'float'>

print('Hello' * 4)  # HelloHelloHelloHello
# print('4' + 4)  # TypeError: can only concatenate str (not "int") to str
'''


'''
m = 5
# s = input()  # str
n = int(input())  # int
if n % 2 == 0:
    print('четное число')
else:
    print('нечетное число')
'''


'''
k = 0
while True:  # Бесконечный цикл
    print(k)
    k += 1
'''


# Цикл - это повторяющееся действие


# Цикл for отвечает на вопросы: "повтори N раз", "пробеги от A до B"

# 1. Цикл for с функцией range(START, STOP, STEP)
'''
for i in range(10):  # range(START=0, STOP=10-1, STEP=1)
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
print()

for i in range(3, 10):  # range(START=3, STOP=10-1, STEP=1)
    print(i, end=' ')  # 3 4 5 6 7 8 9
print()

for i in range(2, 10, 2):  # range(START=2, STOP=10-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8
print()

for i in range(1, 10+1, 3):  # range(START=1, STOP=10-1, STEP=3)
    print(i, end=' ')  # 1 4 7 10
print()

for i in range(10, 1):  # range(START=10, STOP=1-1, STEP=1)
    print(i, end=' ')  #
print()

for i in range(10, 1, -1):  # range(START=10, STOP=1-1, STEP=-1)
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2
print()
'''

# 2. Цикл for с последовательностями напрямую
'''
# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']

print(M[0])  # a
print(M[1:4])  # ['b', 'c', 'd']

for x in M:
    print(x, end=' ')  # a b c d e
print()

for x in M:
    if x in 'ae':
        print(x, end=' ')  # a e
print()

print(len(M))  # 5, Функция len() - возвращает длину последовательности (кол-во элементов в немё)

for i in range(len(M)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e 
print()
'''


# Цикл while:
'''
for i in range(2, 10+1, 2):  # range(START=2, STOP=10+1-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10
print()

i = 2
while i <= 10:
    print(i, end=' ')  # 2 4 6 8 10
    i += 2
print()
'''

'''
x = 234
print(x / 10)  # 23.4
print(x // 10)  # 23
print(x % 10)  # 4

x2 = 4567
print(x2 // 100)  # 45
print(x2 % 100)  # 67

n = int(input())  # 4357846
while n > 0:
    print(n % 10)
    n //= 10
'''

'''
from random import choice, randint
from time import sleep

password_messages = [
    "Неправильный пароль, попробуйте снова: ",
    "Пароль не подходит, пожалуйста, введите заново: ",
    "Ошибка в пароле, повторите ввод: ",
    "Неправильный пароль, попробуйте ещё раз: ",
    "Пароль неверный, повторите: ",
    "Неверный пароль, введите ещё раз: ",
    "Пароль не совпадает, попробуйте заново: ",
    "Пароль введён неверно, повторите попытку: ",
    "Ошибка: неправильный пароль. Пожалуйста, повторите: ",
    "Пароль введён неправильно, введите снова: "
]

password = 'qwerty'
cnt = 0
pas = input('Введите пароль от вашей учетной записи: ')
while True:
    if pas == password:
        print('Добро пожаловать!')
        break
    cnt += 1
    if cnt == 3:
        print('Пройдите проверку на робота: ')
        a = randint(0, 100)
        b = randint(0, 100)
        x = int(input(f'Решите пример: {a} + {b} = '))
        if x == a + b:
            print('Проверка пройдена успешно')
            cnt = 0
        else:
            print('Проверка не пройдена, повторите попытку через 5 минут')
            sleep(5 * 60)

    pas = input(choice(password_messages))
print('welcome')
'''