# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Типы данных переменных
'''
a = 5  # int (integer) - целочисленные значения

b = 5.0  # float (число с плавающей точкой) - вещественное значение/дробь
print(4 + 5.0)  # 9.0
print(4 / 2, type(4/ 2))  # 2.0 <class 'float'>

c = '5'  # str (string) - строковый тип данных для хранения текста
print(a, c)  # 5 5
print(a * 4, c * 4)  # 20 5555
print('Hello ' * 4)  # Hello Hello Hello Hello - при умножении строки на целое число происходит дублирование строки

c1 = 'Hello, '
c2 = 'world!'
print(c1 + c2)  # Hello, world! - конкатенация (склеивание) строк

d1 = True  # bool (Boolean) - Основы Булевой алгебры (ака Математическая логика)
d0 = False
print(4 == 4)  # True
print(4 == 10)  # False
'''

# Типы данных коллекций (последовательности)
'''
A = [1, 2, 3, '4', 5.0, True, [1, 2, 3]]  # list (список)
# 1. Может хранить в себе неограниченное кол-во элементов
# 2. При это эти элементы могут быть различных типов данных
# 3. Каждый элемент списка имеет свой порядковый номер: индекс
# 4. Индексы можно считать слева-направо начиная с 0 или справа-налево начиная с -1
# 5. В отличие от кортежей и строк мы можем изменять элементы списка через индексы

print(f'Первый элемент списка А: {A[0]}')  # 1
print(f'Последний элемент списка А: {A[-1]}')  # [1, 2, 3]

A[0] = '111'
print(A)  # ['111', 2, 3, '4', 5.0, True, [1, 2, 3]]
print(f'Первый элемент списка А: {A[0]}')  # '111'


B = (1, 2, 3)  # tuple (кортеж)
# 1. Все тоже самое, что и со списками, только нельзя изменять элементы кортежа

C = {1, 2, 2, 3, 3, 3}  # set (множество)
print(C)  # {1, 2, 3}
# 1. Множества не могут хранить в себе копии элементов


D = {'один': 'one', 'два': 'two'}  # dict (словарь)
# 1. Элементы словаря разбиваются на две части: ключ и значение
# 2. Доступ к значению элемента осуществляется через ключ
# 3. Ключи индивидуальны, то есть нельзя создать два одинаковых иначе новый заменит старый

print(D['один'])  # one
D['один'] = 1
print(D)  # {'один': 1, 'два': 'two'}
'''


# Конвертация типов данных
'''
a = 5
print(a, type(a))  # 5 <class 'int'>

a = str(a)
print(a, type(a))  # 5 <class 'str'>

a = float(a)
print(a, type(a))  # 5.0 <class 'float'>

a = int(a)
print(a, type(a))  # 5 <class 'int'>


A = [1, 2, 2, 3, 3, 3]
print(A, type(A))  # [1, 2, 2, 3, 3, 3] <class 'list'>

A = tuple(A)
print(A, type(A))  # (1, 2, 2, 3, 3, 3) <class 'tuple'>

A = set(A)
print(A, type(A))  # {1, 2, 3} <class 'set'>

A = list(A)
print(A, type(A))  # [1, 2, 3] <class 'list'>
'''


# Ввод данных с клавиатуры
'''
text = input('Введите текст: ')
print(text, type(text))

number = int(input('Введите число: '))
print(number, type(number))
'''


# Пример использования f-строки
'''
weather = 'облачно'
temperature = 24
print('Привет, сегодня', weather, ', а температура', temperature, 'градусов!')
print(f'Привет, сегодня {weather}, а температура {temperature} градусов!')
'''


# Деление в пайтон:

a, b = 7, 2

print(f'{a} / {b} = {a / b} \n'  # 3.5 - вещественное деление (дробь) - всегда float
      f'{a} // {b} = {a // b} \n'  # 3 - целочисленное деление - то есть всегда целая часть 
      f'{a} % {b} = {a % b}')  # 1 - остаток от деления 7/2 = 3 целых и (1/2)


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = []
# КЕГЭ = []
# на следующем уроке: Чуть-чуть добить арифметику, говорим про библиотеки, условные операторы

