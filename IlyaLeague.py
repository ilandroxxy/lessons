


# Типы данных переменных
'''
a = 5  # int (integer) - целочеисленные значения
print(type(a))  # <class 'int'>


b = 5.0  # float (число с плавающей точкой) - вещественные значения (дроби)
print(4 / 2, type(4 / 2))  # 2.0 <class 'float'>

b2 = 5,0
print(b2)  # (5, 0)
print(type(b2))  # <class 'tuple'>


c = '5'  # str (string) - строковый тип данных для хранения текста и символов
print(c * 5)    # 55555
print('hello ' * 4)  # hello hello hello hello - строки при умножении на целое число дублируются

c1 = 'Hello, '
c2 = 'world!'
c = c1 + c2  # - операция конкатенации строк (склеивание)
print(c)  # Hello, world!

s = '7' + '2' * 5
print(s)  # 722222


d1 = True  # bool (основы математической логики)
d0 = False
print(4 <= 10)  # True
print(4 == 10)  # False
'''



# Типы данных коллекций (последовтельностей)

L = ['a', 'b', 'c', 'd', 'e']  # list (список)
# 1. Могут хранить неограниченное кол-во элементов
# 2. Элементы могут быть различных типов данных
# 3. Каждый элемент списка имеет свой порядковый номер - индекс
# 4. Индексы можно считать слева-навправо начиная 0 и справа-налево начиная -1
# 5. Элементы списка можно изменять через индексы (в отличие от строк и кортежей)

'''
# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
# -i -5   -4   -3   -2   -1

print(f'Первый элемент списка М: {M[0]}')
print(f'Последний элемент списка М: {M[-1]}')


M[0], M[-1] = M[-1], M[0]
print(M)  # ['e', 'b', 'c', 'd', 'a']


M = [2, '2', 2.0, True, {1, 2, 3}, [1, 2, 3]]
for x in M:
    print(type(x), x)
    # <class 'int'> 2
    # <class 'str'> 2
    # <class 'float'> 2.0
    # <class 'bool'> True
    # <class 'set'> {1, 2, 3}
    # <class 'list'> [1, 2, 3]

T = ('a', 'b', 'c', 'd', 'e')  # tuple (кортеж)

S = {'a', 'b', 'c', 'd', 'e'}  # set (множество)



# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
# -i -5   -4   -3   -2   -1

print(len(M))  # 5

for x in M:
    print(x, end=' ')  # a b c d e
print()

for x in M:
    if x in 'ae':
        print(x, end=' ')  # a e
print()


for i in range(len(M)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e
print()

for i in range(len(M)):
    M[i] = M[i] * 2
print(M)  # ['aa', 'bb', 'cc', 'dd', 'ee']
'''


# Пару слов про цикл for

# Цикл for отвечает на запросы: "повтори n раз", "пробеги от числа А до числа Б"
'''
# range(0, STOP-1, 1)
# range(START, STOP-1, 1)
# range(START, STOP-1, STEP)

for i in range(10):
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
print()

for i in range(2, 10):
    print(i, end=' ')  # 2 3 4 5 6 7 8 9
print()

for i in range(2, 10, 2):
    print(i, end=' ')  # 2 4 6 8
print()

for i in range(2, 10+1, 2):
    print(i, end=' ')  # 2 4 6 8 10
print()


for i in range(1, 10+1, 2):
    print(i, end=' ')  # 1 3 5 7 9
print()

for i in range(10, 0-1, -1):
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1 0
print()

# Работа цикла for с последовательностями

s = '22ik3j4io32j4iu23hj4'

for x in s:
    print(x, end=' ')  # 2 2 i k 3 j 4 i o 3 2 j 4 i u 2 3 h j 4
print()

for x in s:
    if x in '0123456789':
        print(x, end=' ')  # 2 2 3 4 3 2 4 2 3 4
print()


for x in s:
    if x not in '0123456789':
        print(x, end=' ')  # i k j i o j i u h j
print()


# Сумму цифр этой строки

n = '2142343'
total = 1
summa = 0
cnt = 0
for x in n:
    summa += int(x)
    cnt += 1
    total *= int(x)
print(summa, cnt)  # 19 7
print(total)
print(len(n))  # 7
'''


# Серзы списков
'''
# i  01234
s = 'abcde'

print(s[1:-1])  # 'bcd'
print(s[::2])  # ace
print(s[1::2])  # bd

print(s[::-1])  # edcba
'''



# Функции списков:
'''
M = [1, 2, 3, 3, 2, 3]

print(len(M))
print(sum(M))
print(min(M), max(M))

print(sorted(M))  # [1, 2, 2, 3, 3, 3]
print(sorted(M, reverse=True))  # [3, 3, 3, 2, 2, 1]
print(sorted(M)[::-1])  # [3, 3, 3, 2, 2, 1]

print(set(M))  # {1, 2, 3} - убирает копии элементов, то есть ищет различные элементы 
'''


# Методы списков
'''
M = [1, 2, 3]
M.append(4)
M.append(5)  # - добавляет новый элемент в конец списка (только один элемент)
print(M)  # [1, 2, 3, 4, 5]

M = M[::-1]
M.append(0)
M = M[::-1]
print(M)  # [0, 1, 2, 3, 4, 5]


# Альтернатива:

M = [1, 2, 3]
M = [0] + M + [4, 5]  # - конкатенация списков
print(M)  # [0, 1, 2, 3, 4, 5]


# Возвращает кол-во конкретного элемента 
M = [2, 2, 2, '2', '2']
print(M.count(2))  # 3
print(M.count('2'))  # 2
'''




# Генераторы списков

print([x for x in range(5)])  # [0, 1, 2, 3, 4]

print([str(x) for x in range(5)])  # ['0', '1', '2', '3', '4']

print([x ** 2 for x in range(5)])  # [0, 1, 4, 9, 16]

print([x ** 2 for x in range(10) if x % 2 == 0])  # [0, 4, 16, 36, 64]

print([x for x in range(0, 100) if len(str(x)) == 2])  # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

print([x for x in range(100) if len(str(x)) == 1])  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print([x for x in range(-100, 100) if len(str(abs(x))) == 1])  # [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# NameError: name 'x' is not defined


print([x for x in '2142343'])  # ['2', '1', '4', '2', '3', '4', '3']
print(sum([int(x) for x in '2142343']))  # 19


print(sum([int(x) for x in '21f42.3 43' if x in '0123456789']))  # 19
# ValueError: invalid literal for int() with base 10: 'f'



# На следующем уроке проговорим: допустим 8 номера






















