



# - однострочный комментарий

'''
- многострочный комментарий
'''


# Типа данных переменных
'''
a = 5  # int (integer) - целочисленные значения
print(a, type(a))  # 5 <class 'int'>

b = 5.0  # float (число с плавающей точкой) - дроби
print(4 / 2, type(4 / 2))  # 2.0 <class 'float'>

c=(5,0)  # !!!!
print(type(c))  # <class 'tuple'>

c = '5'  # str (string) - строковый тип данных для хранения текста и символов
print(c * 5)  # 55555
print('Hello ' * 4)  # Hello Hello Hello Hello
# Строка при умножении на целое число дублируется

c1 = 'Hello, '
c2 = 'world!'
c = c1 + c2  # - опреация конкатенации строк (склеивание строк)
print(c)  # Hello, world!

s = '7' + '4' * 10
print(s)  # 74444444444

d1 = True  # bool  - основы математической логики
d0 = False
print(4 < 10)  # True
print(4 == 10)  # False
'''

# Типы данных коллекций (последовательностей)
'''
# i  0  1  2  3  4  5
L = [1, 2, 2, 3, 3, 3]  # list (список)
# -i-6 -5 -4 -3 -2 -1

# 1. Хранить неограниченное кол-во элементов
# 2. Элементы могут быть различных типов данных (в отличие от массивов)
# 3. Каждый элемент списка имеет свой порядковый номер - индекс
# 4. Индексы могут считаться слева-направо начиная с 0 или справа-налево начиная с -1
# 5. Через индексы мы можем изменять значение элементов (в отличие от кортежей и строк)

print('Первый элемент списка L: ', L[0])
print('Последний элемент списка L: ', L[-1])

L[0], L[-1] = L[-1], L[0]
print(L)  # [3, 2, 2, 3, 3, 1]


M = [2, '2', 2.0, True, 7/2, [1, 2, 3]]
for x in M:
    print(type(x), x)
    # <class 'int'> 2
    # <class 'str'> 2
    # <class 'float'> 2.0
    # <class 'bool'> True
    # <class 'float'> 3.5
    # <class 'list'> [1, 2, 3]


T = (1, 2, 2, 3, 3, 3)  # tuple (кортеж)
# Полностью идентичны спискам, но нельзя изменять элементы кортежа

S = {1, 2, 2, 3, 3, 3}  # set (множество)
# Не могут хранить копии элементов - то есть копии удаляются
print(S)  # {1, 2, 3}
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


A = [1, 2, 3, 2, 3, 3]
print(type(A), A)  # <class 'list'> [1, 2, 3, 2, 3, 3]

A = tuple(A)
print(type(A), A)  # <class 'tuple'> (1, 2, 3, 2, 3, 3)

A = set(A)
print(type(A), A)  # <class 'set'> {1, 2, 3}

A = list(A)
print(type(A), A)  # <class 'list'> [1, 2, 3]
'''


# Ввод данных с клавиатуры
'''
age = int(input('Возраст пользователя: '))
# ValueError: invalid literal for int() with base 10: '20ewklj'
if age > 18:
    print('Доступ разрешено')
else:
    print('Запрещен')

name = input('Введите имя пользователя: ')
print(name)
'''


# f-строка
'''
age = int(input('Возраст пользователя: '))
name = input('Введите имя пользователя: ')

# Привет, name! Твой возраст age?
print('Привет, ', name, '! Твой возраст ', age, '?')
print('Привет, ' + name + '! Твой возраст ' + str(age) + '?')
print('Привет, {}! Твой возраст {}?'.format(name, age))
print(f'Привет, {name}! Твой возраст {age}?')
'''



# Базовая арифметика
'''
a, b = 7, 2
print(a / b)  # 3.5
print(a // b)  # 3
print(a % b)  # 1

n = 123
print(n // 10)   # 12
print(n % 10)  # 3 - берет последнюю цифру числа

print(n // 100)  # 1
print(n % 100)  # 23 - берет две последние цифры

n = 29038403923
print(n % 10000)  # 3923

n = int(input())
if n % 2 == 0:
    print('Число делится на 2 | число кратно 2 | число четное ')


print(2 ** 3)  # 8
print(2 ** 4)  # 16


print(16 ** (1 / 2))  # 4.0
print(27 ** (1 / 3))  # 3.0
'''



# Условные операторы: if, elif, else  (ветвление)
'''
n = int(input('n: '))
if n > 0:  # если 
    print('Положительное')
elif n < 0:  # иначе если 
    print('Отрицательное')
else:  # иначе 
    print('Равно нулю')
'''

'''
# x = int(input('x: '))
# y = int(input('y: '))
x, y = 5, 6
if x > 0 and y > 0:
    print('Первая четверть')
elif x < 0 and y > 0:
    print('Вторая четверть')
elif x < 0 and y < 0:
    print('Третья четверть')
elif x > 0 and y < 0:
    print('Четвертая четверть')
else:
    print('Лежит на осях')
'''


# Логические связки: and, or, not, in, not in, ==, !=

a, b, c = 4, 5, 4

print(a == c)  # True
print(a != c)  # False

if a > 0 and b > 0 and c > 0:
    print('and - выполняются все условия')
if a > 0 or b > 0 or c > 0:
    print('or - хотя бы одно условие выполянется ')

print(True + True + True + False)  # 3

if (a > 0) + (b > 0) + (c > 0) == 3:
    print('Выполняются все три условия')
if (a > 0) + (b > 0) + (c > 0) == 1:
    print('Выполняется только одно условие')
if (a > 0) + (b > 0) + (c > 0) >= 1:
    print('Выполняется хотя бы одно условие')
if (a > 0) + (b > 0) + (c > 0) <= 2:
    print('Выполняется не более двух условий')


flag = True
print(not flag)  # False
print(not(not flag))  # True


s = '2jk34hjk23h4'
for x in s:
    print(x, end=' ')  # 2 j k 3 4 h j k 2 3 h 4
print()

for x in s:
    if x in '0123456789':
        print(x, end=' ')  # 2 3 4 2 3 4
print()

for x in s:
    if x not in '0123456789':
        print(x, end=' ')  # j k h j k h
print()


s = '234234235'
print([int(x) for x in s])  # [2, 3, 4, 2, 3, 4, 2, 3, 5]
print(sum([int(x) for x in s]))  # 28

s = '2f34234g .235'
# print(sum([int(x) for x in s]))  - ValueError: invalid literal for int() with base 10: 'f'

s = '2f34234g .235'
print(sum([int(x) for x in s if x in '0123456789']))  # 28



s = '234234'
print(len(s))

M = [1, 2, 23 ,21,4]
print(len(s))


def hello_start(first_name):
    return f'Привет, {first_name}!'

text = hello_start('Алексей')
print(text)



print(hello_start('Илья'))





















