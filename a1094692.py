


# Основные свойства списков:
'''
# i   0    1    2    3    4
L = ['a', 'b', 'c', 'd', 'e']  # list (список)
# -i -5   -4   -3   -2   -1

print(f'Первый элемент списка L: {L[0]}')
print(f'Последний элемент списка L: {L[4]}')
print(f'Последний элемент списка L: {L[-1]}')

# 1. Могут хранить неограниченное кол-во элементов
# 2. Элементы могут быть различных типов данных (в отличие от массивов)
# 3. Каждый элемент списка имеет свой порядковый номер - индекс
# 4. Индексы можно считать слева-направо начиная с 0 или справа-налево начиная с -1
# 5. Элементы списка можно изменять через индексы

L[0], L[-1] = L[-1], L[0]
print(L)  # ['e', 'b', 'c', 'd', 'a']

L[0] = L[0].upper()
L[-1] = L[-1].upper()
print(L)  # ['E', 'b', 'c', 'd', 'A']


M = [2, '2', 2.0, True, 7/2, [1, 2, 3]]
for x in M:
    print(type(x), x)
    # <class 'int'> 2
    # <class 'str'> 2
    # <class 'float'> 2.0
    # <class 'bool'> True
    # <class 'float'> 3.5
    # <class 'list'> [1, 2, 3]


T = ('a', 'b', 'c', 'd', 'e')  # tuple (кортеж)
# 1. Полностью идентичны спискам, кроме: изменять элементы кортежа нельзя


S = {'a', 'b', 'c', 'd', 'e'}  # set (множество)
# 1. Не могут хранить копии элементов, а значит копии удаляются

M = [1, 2, 3, 2, 3, 2, 2]
print(len(set(M)))  # 3 - кол-во различных элементов списка М
'''


# Срезы списков и других последовательностей
'''
# i   0    1    2    3    4
L = ['a', 'b', 'c', 'd', 'e']
# -i -5   -4   -3   -2   -1

# СРЕЗ[START:STOP-1]
# СРЕЗ[START:STOP-1:STEP]

print(L[1:3])  # ['b', 'c']
print(L[:3])  # ['a', 'b', 'c']
print(L[1:])  # ['b', 'c', 'd', 'e']

print(L[2:])  # ['c', 'd', 'e'] - все элементы кроме первых двух
print(L[-2:])  # ['d', 'e'] - последние два элемента
print(L[-3:])  # ['c', 'd', 'e'] - последние три элемента

print(L[1:-1])  # ['b', 'c', 'd'] - все элементы кроме первого и последнего

print(L[:])  # ['a', 'b', 'c', 'd', 'e']
print(L[::])  # ['a', 'b', 'c', 'd', 'e']

print(L[0::2])  # ['a', 'c', 'e']
print(L[1::2])  # ['b', 'd']

print(L[::-1])  # ['e', 'd', 'c', 'b', 'a'] - все элементы в обратном порядке 
'''


# Функции списков
'''
M = [1, 3, 3, 2, 3, 2]

print(len(M))  # - возвращает кол-во элементов в списке
print(sum(M))
print(min(M), max(M))

print(sorted(M))  # [1, 2, 2, 3, 3, 3]
print(sorted(M, reverse=True))  # [3, 3, 3, 2, 2, 1]
print(sorted(M)[::-1])  # [3, 3, 3, 2, 2, 1]

print(set(M))  # - убирает копии элементов 
'''


# Методы списков - это функции направленные на определенный тип данных
'''
# .append() - добавляет элемент в конец списка

M = [1, 2, 3]
M.append(4)
M.append(5)
print(M)  # [1, 2, 3, 4, 5]


M = [1, 2, 3]
M = [0] + M + [4, 5]
print(M)  # [0, 1, 2, 3, 4, 5]


# .count() - возвращает кол-во вхождений опредленного элемента
M = [2, 2, '2', '2', 2]
print(M.count('2'))  # 2
print(M.count(2))  # 3

s = '20302130234'
print(s.count('0')) # Сколько нулей?
print(len(s) - s.count('0')) # Сколько ненулевых значений?
'''


# Работа цикла for с последовательностями

# Цикл for отвечает на два запроса: "повтори N раз", "пробеги от А до В"

# Цикл for может работать через функцию range()
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

for i in range(2, 10+1, 2):
    print(i, end=' ')  # 2 4 6 8 10
print()

for i in range(10, 0):
    print(i, end=' ')  # ....
print()

for i in range(10, 0-1, -1):
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1 0
print()
'''

# А так же цикл for работает с последовательностями
'''
# i   0    1    2    3    4
L = ['a', 'b', 'c', 'd', 'e']

for i in range(len(L)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(L[i], end=' ')  # a b c d e
print()

for x in L:
    print(x, end=' ')  # a b c d e
print()

for x in L:
    if x in 'ae':
        print(x, end=' ')  # a e
print()

for i in range(len(L)):
    L[i] = L[i] * i
print(L)  # ['', 'b', 'cc', 'ddd', 'eeee']


s = '34sd289gr374'

for x in s:
    print(x, end=' ')  # 3 4 s d 2 8 9 g r 3 7 4
print()

for x in s:
    if x in '01223456789':
        print(x, end=' ')  # 3 4 2 8 9 3 7 4
print()

summa = 0
for x in s:
    if x in '01223456789':
        summa += int(x)
        print(x, end=' ')  # 3 4 2 8 9 3 7 4
print()
print(summa)  # 40


for x in s:
    if x not in '01223456789':
        print(x, end=' ')  # s d g r 
print()
'''


# Генераторы списков

# генератор[что_кладем откуда_берем]
# генератор[что_кладем откуда_берем при_каком_условии]
'''
print([x for x in range(10)])  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print([x for x in range(10) if x % 2 == 0])  # [0, 2, 4, 6, 8]

print([x ** 2 for x in range(10) if x % 2 == 0])  # [0, 4, 16, 36, 64]

M = [int(x) for x in open('files/17.txt')]

print([x for x in M if abs(x) % 3 == 0])

print([x for x in M if x % 2 == 0])

print([x for x in M if abs(x) % 10 == 3])
print([x for x in M if abs(x) % 100 == 33])

print([x for x in M if len(str(abs(x))) == 3])

print([x for x in M if len(str(abs(x))) == 4])
'''





