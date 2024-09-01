# region Домашка: ******************************************************************

'''
L = [3, 7, 1, 4, 9, 2]
# print(L[1:-1])  # [7, 1, 4, 9]
# print(L[0])  # 3
L = [L[-1]] + L[1:-1] + [L[0]]
print(L)
'''

'''
from string import punctuation

print(punctuation)
s = input()
for x in punctuation:
    s = s.replace(x, '')
print(max([len(x) for x in s.split()]))
'''
# [1, 2, 3, 4]
# [1, 2, 4, 3, 5, 6]

# '123456'
# '1243'
# print(max('123456', '1243'))


# Распредели числа
'''
start, mid, end = [], [], []
n = int(input())
for i in range(n):
    x = int(input())
    if x < 0:
        start.append(x)
    elif x == 0:
        mid.append(x)
    else:
        end.append(x)
for x in start + mid + end:
    print(x)
'''

'''
from math import prod


def my_prod(L: list):
    r = 1
    for x in L:
        r *= x
    return r


n = int(input())
N = [int(x) for x in str(n)]
print(N.count(2))
print(N.count(N[-1]))
print(len([x for x in N if x % 2 != 0]))
print(sum([x for x in N if x > 7]))
N89 = [x for x in N if x > 7]

if len(N89) == 0:
    print(11)
elif len(N89) == 1:
    print(N89[0])
else:
    print(my_prod(N89))
    # print(prod(N89))

print(N.count(0) + N.count(4))
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Строковый тип данных - он похож на списки, так как каждый элемент строки имеет порядковый номер (индекс)
'''
# i  01234
s = 'abcde'
print(s[0])  # первый элемент строки
print(s[-1])  # последний элемент строки
print(s[2:4])  # cd
print(s[::-1])  # вывели элементы строки в обратном порядке
# Срезы работают точно так же как и в списках

for x in s:
    print(x, end=' ')  # a b c d e
print()

for i in range(len(s)):
    print(s[i], end=' ')  # a b c d e
print()

# Два основных отличия от списков:
# 1. Элементы всегда строчные
# 2. Нельзя изменять элементы строки (то есть, если мы захотим изменить строку, то ее придется пересоздать)

s = 'abcde'  # Допустим мы хотим заменить элемент 'c' на '*'
s = s[:2] + '*' + s[3:]
print(s)  # ab*de
'''

# Функции строк
'''
s = '12321abcdefABCDE.,?!'
print(len(s))  # возвращает длину строки
# print(sum(s)) - такой функции нет
print(max(s))
print(min(s))
print(sorted(s))  # ['!', ',', '.', '1', '1', '2', '2', '3', '?', 'A', 'B', 'C', 'D', 'E', 'a', 'b', 'c', 'd', 'e', 'f']
print(set(s))  # {'D', '2', ',', '.', '1', 'e', 'f', '!', 'a', '3', 'b', 'A', 'd', 'B', 'E', '?', 'c', 'C'}
# set - удаляет копии элементов строки и меняет тип данных на множество set()
'''

# Методы строк
'''
s = '2143213124321412'

print(s.count('2'))  # 5 - возвращает кол-во вхождений элементов в строке
print(s.index('2'))  # 0 - возвращает индекс первого найденного элемента
print(s.find('2'))  # 0 - возвращает индекс первого найденного элемента

print(s.rindex('2'))  # 15 - возвращает индекс последнего найденного элемента
print(s.rfind('2'))  # 15 - возвращает индекс последнего найденного элемента

# print(s.index('5'))  # print(s.index('5'))  ValueError: substring not found
print(s.find('5'))  # -1 - просто таким образом сигнализирует, что элемент не найден

# print(s.rindex('5'))  # print(s.rindex('5'))  ValueError: substring not found
print(s.rfind('5'))  # -1 - просто таким образом сигнализирует, что элемент не найден

s = s.replace('2', '*')  # - пересоздаем строку заменя все двойки на '*'
print(s)  # *143*131*43*141*

s = s.replace('*', '2', 3)  # - пересоздаем строку заменя первые три '*' на двойки
print(s)  # 21432131243*141*


id = '213.34.23.54'
# print(int('11111111', 2))  # 255
int_id = [int(x) for x in id.split('.')]
print(int_id)  # [213, 34, 23, 54]

id = '213.34.23.54'
str_id = id.split('.')
print(str_id)  # ['213', '34', '23', '54']

print(''.join(str_id))  # 213342354
print('*'.join(str_id))  # 213*34*23*54
print('**'.join(str_id))  # 213**34**23**54
print(' + '.join(str_id))  # 213 + 34 + 23 + 54
print(', '.join(str_id))  # 213, 34, 23, 54
'''

'''
# i  0123456789
s = 'SdamEge_2024'
print(s[0])  # S
print(s[-3])  # 0
print(len(s))  # 12
print(s.index('a'))  # 2
# s = '00' + s  - добавить '00' слева
# s += '00' - добавить '00' справа
print(int(s[-1]) + int(s[-4]))  # 6
print(s.replace('_', '!'))  # SdamEge!2024
print(s)  # SdamEge_2024
print(s.split('_'))  # ['SdamEge', '2024']
'''

s = '32849!7'
summa = 0
for x in s:
    if x.isdigit():
        summa += int(x)
print(summa)

summa = sum([int(x) for x in s if x.isdigit()])
print(summa)

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 6]
# КЕГЭ  = []
# на следующем уроке:
