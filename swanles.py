

# Типы данных переменных
'''
a = 5  # int (integer) - целочисленные значения
print(a, type(a))  # 5 <class 'int'>

b = 5.0  # float (число с плавающей точкой) - дроби
print(4 / 2, type(4 / 2))  # 2.0 <class 'float'>

c = '5'  # str (string) - строковый тип данных для хранения текста и символов
print(c * 4)  # 5555
print('Hello ' * 4)  # Hello Hello Hello Hello

c1 = 'Hello, '
c2 = 'world!'
c = c1 + c2  # - операция конкатенации строк (склеивание)
print(c)  # Hello, world!

s = '7' + '5' * 10
print(s)  # 75555555555

d1 = True  # bool (Boolean) - Булевой алгебры / математическая логика
d0 = False

print(4 < 10)  # True
print(4 == 10)  # False
'''


# Типы данных коллекций (последовательностей)
'''
L = ['a', 'b', 'c', 'd', 'e']  # list (список)
# 1. Могут хранить неограниченное кол-во элементов
# 2. Элементы могут быть в различных типах данных
# 3. Каждый элемент имеет свой порядковый номер - индекс
# 4. Индексы можно считать слева-направо начиная с 0 или справа-налево начиная с -1
# 5. Через индексы мы можем изменять значение элементов списка

# i   0    1    2    3    4
L = ['a', 'b', 'c', 'd', 'e']
# -i -5   -4   -3   -2   -1

print('Первый элемент списка: ', L[0])
print('Последний элемент списка: ', L[-1])


L[0], L[-1] = L[-1], L[0]
print(L)  # ['e', 'b', 'c', 'd', 'a']

L[0] = L[0].upper()
L[-1] = L[-1].upper()
print(L)  # ['E', 'b', 'c', 'd', 'A']


M = [2, '2', 2.0, True, [1, 2, 3]]
for x in M:
    print(type(x), x)
    # <class 'int'> 2
    # <class 'str'> 2
    # <class 'float'> 2.0
    # <class 'bool'> True
    # <class 'list'> [1, 2, 3]

T = ('a', 'b', 'c', 'd', 'e')  # tuple (кортеж)
# 1. Полностью идентичен спискам, но нельзя изменять значение элементов

S = {1, 3, 3, 2, 3, 2, 1}  # set (множества)
# 1. Не могут хранить коппии элементов - копии удаляются
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

A = [1, 2, 2, 3, 3, 3]
print(type(A), A)   # <class 'list'> [1, 2, 2, 3, 3, 3]

A = tuple(A)
print(type(A), A)  # <class 'tuple'> (1, 2, 2, 3, 3, 3)

A = set(A)
print(type(A), A)  # <class 'set'> {1, 2, 3}

A = list(A)
print(type(A), A)  # <class 'list'> [1, 2, 3]
'''



# Ввод данных с клавиатуры input()
'''
age = int(input('Введите возраст: '))
print('Возраст пользователя: ', age, type(age))
# ValueError: invalid literal for int() with base 10: '26edlwifjh   /.?>'

name = input('Введите имя пользователя: ')
print('Имя пользователя: ', name)
'''


# f-строки
'''
name = input('Введите имя пользователя: ')
age = int(input('Введите возраст: '))

# Имя пользователя name, а возраст age. Доступ разрешен!
# Имя пользователя name, а возраст age. Доступ запрещен!

if age >= 18:
    print('Имя пользователя ', name, ', а возраст ', age, '. Доступ разрешен!')
    print('Имя пользователя ' + name + ', а возраст ' + str(age) + '. Доступ разрешен!')
    print('Имя пользователя {}, а возраст {}. Доступ разрешен!'.format(name, age))
    print(f'Имя пользователя {name}, а возраст {age}. Доступ разрешен!')
else:
    print(f'Имя пользователя {name}, а возраст {age}. Доступ запрещен!')
'''



# Базовая арифметика
'''
a, b = 7, 2
print(a / b)  # 3.5
print(a // b)  # 3
print(a % b)  # 1


n = 734
print(n // 10)  # 73
print(n % 10)  # 4 - взятие последней цифры числа

print(n // 100)  # 7
print(n % 100)  # 34 - взятие последних двух цифр

n = 52439078
print(n % 10000)  # 9078



n = 43089
a = n // 10000
b = (n // 1000) % 10
c = 0
d = 0
e = n % 10
print(a, b, c, d, e)


print(2 ** 3)  # 8 
print(16 ** (1/2))
print(27 ** (1/3))
'''


# Услоные операторы: if, elif, else
'''
n = int(input())
if n > 0:  # если 
    print('Число положительное')
elif n < 0:  # иначе если 
    print('Число отрицательное')
else:  # иначе 
    print('Число равно 0')
'''

'''
x, y = -5, 5
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
print('Условие закончилось')
'''


# Логические связки: and, or, not, not in, in, ==, !=


a, b, c = 4, -5, -4

print(a == c)  # True
print(a == b)  # False

print(a != c)  # False
print(a != b)  # True

if a > 0 and b > 0 and c > 0:
    print('AND - все три условия верные')
if a > 0 or b > 0 or c > 0:
    print('OR - хотя бы одно условие верное')

print(True + True + True + False)  # 3

if (a > 0) + (b > 0) + (c > 0) == 3:
    print('Все три условия выполнялись')
if (a > 0) + (b > 0) + (c > 0) == 1:
    print('Выполняется только одно условие')
if (a > 0) + (b > 0) + (c > 0) >= 1:
    print('Хотя бы одно условие выполняется')
if (a > 0) + (b > 0) + (c > 0) <= 2:
    print('Не более двух условий')


flag = True
print(not flag)  # False
print(not( not flag))  # True


s = '2kjl3423kj43234'
for x in s:
    print(x, end=' ')  # 2 k j l 3 4 2 3 k j 4 3 2 3 4
print()


s = '2kjl3423kj43234'

for x in s:
    if x in '0123456789':
        print(x, end=' ')  # 2 3 4 2 3 4 3 2 3 4
print()

for x in s:
    if x not in '0123456789':
        print(x, end=' ')  # k j l k j
print()


s = '123213142145'
print(sum([int(x) for x in s]))  # 29

s = '1232df131.4 2145'
print(sum([int(x) for x in s if x in '0123456789']))  # 29
# ValueError: invalid literal for int() with base 10: 'd'




