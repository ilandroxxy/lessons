





# range(0, STOP-1)
# range(START, STOP-1)
# range(START, STOP-1, STEP)
'''
for i in range(10):
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
print()


for i in range(2, 10):
    print(i, end=' ')  # 2 3 4 5 6 7 8 9
print()


for i in range(2, 10+1, 2):
    print(i, end=' ')  # 2 4 6 8 10
print()

for i in range(1, 10+1, 2):
    print(i, end=' ')  # 1 3 5 7 9
print()
'''


'''
s = 'hello, world!'
print(s[::-1])

print(s[1:-1])
'''



# Генераторы списков

# Генератор[что_кладем откуда_берем]
# Генератор[что_кладем откуда_берем при_каком_условии]
'''
print([x for x in range(10)])  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print([x ** 2 for x in range(10)])  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print([x ** 2 for x in range(10) if x % 2 == 0])  # [0, 4, 16, 36, 64]


M = [int(x) for x in open('files/17.txt')]
print(M)
A = [x for x in M if abs(x) % 10 == 3 and len(str(abs(x))) == 4]
print(A)


x = 7658
print(len(str(x)))  # 4

x = -7658
print(len(str(x)))  # 5

x = -7658
print(len(str(abs(x))))  # 4
'''


'''
print(123 % 10)  # 3
print(123 % 100)  # 23

print(-123 % 10)  # 7
'''


'a' 'b' 'c' 'd' 'e'
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






# Несколько способов подключения библиотек

import math  # Самый простой вариант, но не эффективный, потмоу что везде придется тоскать math
print(math.sqrt(16))  # 4.0


import math as m  # Подлючение библиотеки с коротким именем (любое)
print(m.sqrt(16))


from math import sqrt, factorial  # Подключаем только определенные функции
print(sqrt(16))


from math import *  # Подключение всего содержимого
print(sqrt(16))
print(factorial(5))



# При подключении через * есть вероятность создания конфликта имен
'''
count = 0
from itertools import permutations
for p in permutations('abc'):
    count += 1  # count = count + 1
    print(count, p)
    # 1 ('a', 'b', 'c')
    # 2 ('a', 'c', 'b')
    # 3 ('b', 'a', 'c')
    # 4 ('b', 'c', 'a')
    # 5 ('c', 'a', 'b')
    # 6 ('c', 'b', 'a')

count = 0
from itertools import *
for p in permutations('abc'):
    count += 1  # count = count + 1
    print(count, p)
    # 1 ('a', 'b', 'c')
    # 2 ('a', 'c', 'b')
    # 3 ('b', 'a', 'c')
    # 4 ('b', 'c', 'a')
    # 5 ('c', 'a', 'b')
    # 6 ('c', 'b', 'a')
# TypeError: unsupported operand type(s) for +=: 'type' and 'int'
'''

s = '1010101111'  # поменять 0 и 1 местами
s = s.replace('0', '*')
s = s.replace('1', '0')
s = s.replace('*', '1')
print(s)  # 0101010000


print(len(s))  # длина строки s
print(s.count('1'))


M = [1, 2, 1, 2, 1, 2, '2']
print(M.count('2'))  # 1

M[0] = 100
print(M)  # [100, 2, 1, 2, 1, 2, '2']




# 31209
'''
print('1 2 3 4 5 6 7')
from itertools import permutations
table = '13 16 17 23 24 26 31 32 34 42 43 47 56 57 61 62 65 71 74 75'
graph = 'AF FA AC CA AD DA DG GD DE ED GC CG GE EG BE EB BC CB BF FB'
for p in permutations('ABCDEFG'):
    new_table = table
    for i in range(1, 7+1):
        new_table = new_table.replace(str(i), p[i-1])
    if sorted(new_table.split()) == sorted(graph.split()):
        print(*p)

    # 1 2 3 4 5 6 7
    # C D G E F A B
    # C E G D F B A
'''

# print('AF FA AC CA AD DA DG GD DE ED GC CG GE EG BE EB BC CB BF FB'.split())
# print('AF FA AC CA AD DA DG GD DE ED GC CG GE EG BE EB BC CB FB BF'.split())

    # i:   0    1    2    3    4    5    6
    # p: ('G', 'F', 'E', 'D', 'A', 'C', 'B')

    # '13 16 17 23 24 26 31 32 34 42 43 47 56 57 61 62 65 71 74 75'
    # 'GE GC GB ...'




# № 31108 Основная волна 18.06.26(Уровень: Базовый)

print('1 2 3 4 5 6 7 8')
from itertools import permutations
table = '12 15 18 21 27 35 36 46 48 51 53 58 63 64 67 72 76 81 84 85'
graph = 'AC CA AG GA AD DA CG GC CB BC BH HB HD DH HF FH FE EF EG GE'
for p in permutations('ABCDEFGH'):
    new_table = table
    for i in range(1, 8+1):
        new_table = new_table.replace(str(i), p[i-1])
    if sorted(new_table.split()) == sorted(graph.split()):
        print(*p)

# 1 2 3 4 5 6 7 8
# G E B D C H F A
# G E D B A H F C




# На следующем уроке проговорим: типа данных, f-строки, list, str, split() join()






