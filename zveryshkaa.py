
# - однострочный комментарий

'''
- блочный комментарий
'''


n = 'Илья'
a = 28

# Типы данных переменных
'''
a = 5  # int (integer) - целочисленные значения
print(type(a))  # <class 'int'>

b = 5.0  # float (число с плавающей точкой) - вещественные значения (дроби)
print(4 / 2, type(4 / 2))  # 2.0 <class 'float'>

c = "5"  # str (string) - строковый тип данных для хранения текста и символов
print(c * 4)  # 5555
print('hello ' * 4)  # hello hello hello hello - при умножении строки на целое число строка дублируется

c1 = 'Hello, '
c2 = 'world!'
c = c1 + c2  # - операция конкатенации строк (склеивание строк)
print(c)  # Hello, world!

s = '7' + '5' * 8  # 755555555

d1 = True  # bool (Boolean) - Булева алгебра / математическая логика
d0 = False
print(4 < 10)  # True
print(4 == 10)  # False

a = 5
print(a == 5)  # True
print(a != 5)  # False
'''


# Конвертация типов данных
'''
a = 5
print(type(a), a)  # <class 'int'> 5

a = str(a)
print(type(a), a)  # <class 'str'> 5

a = float(a)
print(type(a), a)  # <class 'float'> 5.0

a = int(a)
print(type(a), a)  # <class 'int'> 5
'''

# Ввод данных с клавиатуры input()
'''
age = int(input('Введите возраст пользователя: '))
print(type(age))
print(f'Возраст пользователя: {age}')

name = input('Введите имя пользователя: ')
print(f'Имя пользователя: {name}')
print('Имя пользователя:', name)


print(f'Имя пользователя: {name}, а возраст: {age} лет!')
print('Имя пользователя:', name, ', а возраст:', age, 'лет!')
'''


# Базовая арифметика
'''
a, b = 7, 2

print(f'{a} + {b} = {a + b} \n'  # \n - переход на новую строку 
      f'{a} - {b} = {a - b} \n'
      f'{a} * {b} = {a * b} ')

print()  # В каждой функции print() есть переход на новую строку \n

print(f'{a} / {b} = {a / b}')  # 3.5 - обычное вещественное деление
print(f'{a} // {b} = {a // b}')  # 3 - взятие только целой части от деления
print(f'{a} % {b} = {a % b}')  # 1 - взятие остатка от деления

n = 327
print(n // 10)  # 32
print(n % 10)  # 7 - возвращает последнюю цифру числа

print(n // 100)  # 3
print(n % 100)  # 27 - возвращает последние две цифры числа

print(n % 2 == 0)  # False
print(n % 2 != 0)  # True

print(n % 3 == 0)  # True


print(2 ** 3)  # 8

print(16 ** (1 / 2))  # 4.0
print(27 ** (1 / 3))  # 3.0
'''


# Условные операторы if, elif, else
'''
n = int(input('n: '))
if n > 0:
    print('Положительное')
elif n < 0:
    print('Отрицательное')
else:
    print('Равно нулю')


n = int(input('n: '))
if n > 0:
    print('Положительное')
if n < 0:
    print('Отрицательное')
if n == 0:
    print('Равно нулю')
'''


# Логические связки: and, or, not, in, not in

a, b, c = 4, -5, -4

if a > 0 and b > 0 and c > 0:
    print('AND - все условия верные')
if a > 0 or b > 0 and c > 0:
    print('OR - хотя бы одно условие выполняется')

if (a > 0 and b < 0 and c < 0) or (a < 0 and b > 0 and c < 0) or (a < 0 and b < 0 and c > 0):
    print('Вполняется только одно условие')

#       1      1      1       0
print(True + True + True + False)  # 3

if (a > 0) + (b > 0) + (c > 0) == 1:
    print('ТОлько одно условие выполняется')
if (a > 0) + (b > 0) + (c > 0) == 2:
    print('ТОлько два условия выполняются')
if (a > 0) + (b > 0) + (c > 0) == 3:
    print('Выполняются все условия')
if (a > 0) + (b > 0) + (c > 0) >= 1:
    print('хотя бы одно условие выполняется')


flag = True
print(not flag)  # False
print(not(not flag))  # True

s = 'hiu4235hiu345'

for x in s:
    print(x, end=' ')  # h i u 4 2 3 5 h i u 3 4 5
print()

for x in s:
    if x in '0123456789':
        print(x, end=' ')  # 4 2 3 5 3 4 5
print()

for x in s:
    if x not in '0123456789':
        print(x, end=' ')  # h i u h i u
print()

