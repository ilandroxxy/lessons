# region Домашка: ******************************************************************


# https://stepik.org/lesson/1309452/step/7?unit=1324568
'''
L = [3, 7, 1, 4, 9, 2]
L[0], L[-1] = L[-1], L[0]
print(L)  # [2, 7, 1, 4, 9, 3]

s = '371492'
# s = s[-1] + s + s[0] # - дописываем элементы
s = s[-1] + s[1:-1] + s[0] # - заменяем элементы
print(s)  # 271493
'''


# https://stepik.org/lesson/1309452/step/8?unit=1324568
'''
x = int(input())
L = []
for i in range(x):
    a = int(input())
    L.append(a)


L = [int(input()) for x in range(int(input()))]
print(L)
'''

'''
x = int(input())
L = []
S = []
K = []
for i in range(x):
    a = int(input())
    if a < 0:
        K.append(a)
    elif a == 0:
        S.append(a)
    else:
        L.append(a)


for i in K + S + L:
    print(i)
'''


# https://stepik.org/lesson/1309452/step/12?unit=1324568
'''
from math import prod

a = int(input())
b = str(a)

print(b.count('2'))

print(b.count(b[-1]))

print(len([i for i in b if i in '13579']))

S = [int(i) for i in b if int(i) > 7]
print(sum(S))

if len(S) == 0:
    print(11)
elif len(S) == 1:
    print(S[0])
else:
    print(prod(S))

print(b.count('0') + b.count('4'))
'''


#  https://stepik.org/lesson/1309453/step/10?unit=1324569
'''
S = []
for i in range(100, 1000):
    if str(i) == str(i)[::-1]:
        S.append(i)
print(S)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Срезы строк - они полностью идентичны спискам
'''
L = [3, 7, 1, 4, 9, 2]
L[0], L[-1] = L[-1], L[0]
print(L)  # [2, 7, 1, 4, 9, 3]

# В отличие от списков для изменения содержимого 
# строки нам необходимо пересоздавать строку 

s = '371492'
# s = s[-1] + s + s[0] # - дописываем элементы
s = s[-1] + s[1:-1] + s[0] # - заменяем элементы
print(s)  # 271493
'''


# Функции строк
'''
s = '122333'
print(len(s))
# print(sum(s)) - строчные элементы суммировать нельзя
print(max(s), min(s))  # - Максимальный и минимальный элементы строки

print(sorted(s))  # ['1', '2', '2', '3', '3', '3']
print(sorted(s, reverse=True))  # ['3', '3', '3', '2', '2', '1']

print(sorted('2fko543EFL34'))  # ['2', '3', '3', '4', '4', '5', 'E', 'F', 'L', 'f', 'k', 'o']

alp36 = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
print(alp36[:2])  # ['0', '1']
print(alp36[:8])  # ['0', '1', '2', '3', '4', '5', '6', '7']


print(reversed(s))  # <reversed object at 0x104c4b1f0>
print(list(reversed(s)))  # ['3', '3', '3', '2', '2', '1']
print(''.join(list(reversed(s))))  # '333221'

print(s[::-1])   # '333221'

print(eval('2 + 2'))  # 4
print(eval('3 * (2 + 2)'))  # 12
'''


# 🐍 Все методы строк в Python, которые понадобятся на ЕГЭ

# 1⃣ .strip()
# Метод strip() удаляет пробелы (или другие символы) из начала и конца строки.
# Это полезно для очистки пользовательского ввода.
'''
text = "  Привет, мир!  "
cleaned_text = text.strip()
print(cleaned_text)  # "Привет, мир!"
'''

# 2⃣ .lower() и .upper()
# Эти методы позволяют изменять регистр строки. lower() преобразует строку в нижний регистр, а upper() – в верхний.
'''
text = "ПрIvEt"
print(text.lower())  # "привет"
print(text.upper())  # "ПРИВЕТ"
'''

# 3⃣ .replace()
# Метод replace(old, new, count) заменяет подстроку old на new в строке count раз.
'''
text = "Я люблю Python!"
new_text = text.replace("Python", "программирование")
print(new_text)  # "Я люблю программирование!"

s = '12321312321'
s = s.replace('2', '*')  # Сразу все 2ки заменились на *
print(s)  # 1*3*131*3*1

s = s.replace('*', '+', 2)
print(s)  # 1+3+131*3*1
'''


# 4⃣  .split()
# Метод split(separator) разделяет строку на части по указанному разделителю. Если разделитель не указан, используется пробел.
'''
text = "яблоко груша банан"
fruits = text.split()  # по умолчанию разделяет по пробелам
print(fruits)  # ['яблоко', 'груша', 'банан']

text = "яблоко    груша     банан"
fruits = text.split(' ')
print(fruits)  # ['яблоко', '', '', '', 'груша', '', '', '', '', 'банан']

text = "яблоко*груша*банан"
fruits = text.split('*')
print(fruits)  # ['яблоко', 'груша', 'банан']

# Пример использования для 9 номера
for s in open('0. files/9.csv'):
    print(s.split(','))
    M = [int(x) for x in s.split(',')]
    print(M)
'''

# 5⃣ .join()
# Метод join(iterable) соединяет элементы списка (или другого итерируемого объекта) в строку с указанным разделителем.
'''
fruits = ['яблоко', 'груша', 'банан']
result = ', '.join(fruits)
print(result)  # "яблоко, груша, банан"


id = '192.43.234.255'
print(id.split('.'))  # ['192', '43', '234', '255']

IP = ['192', '43', '234', '255']
print(','.join(IP))  # '192,43,234,255'

# Пример использования для 8 номера

from itertools import *
for p in permutations('abc'):
    s = ''.join(p)
    print(p, s)
    # ('a', 'b', 'c') abc
    # ('a', 'c', 'b') acb
    # ('b', 'a', 'c') bac
    # ('b', 'c', 'a') bca
    # ('c', 'a', 'b') cab
    # ('c', 'b', 'a') cba
'''

# 6⃣ .find()
# Метод find(substring) ищет подстроку в строке и возвращает индекс,
# с которого начинается первая встреча. Если подстрока не найдена, возвращает -1.
'''
text = "12321"
print(text.find('2'))  # 1
print(text.index('2'))  # 1

# print(text.index('5'))  # ValueError: substring not found
print(text.find('5'))  # -1

print(text.rfind('2'))  # 3
print(text.rindex('2'))  # 3
'''


# 7⃣ .count()
# Метод count(substring) возвращает количество вхождений подстроки в строку.
'''
text = "яблоко, груша, яблоко"
count = text.count("яблоко")
print(count)  # 2

M = [1, 2, 2, 3, 2, '2', '2']
print(M.count(2))  # 3
print(M.count('2'))  # 2
'''

# 8⃣ .startswith() и .endswith()
# Эти методы проверяют, начинается ли строка с указанной подстроки или заканчивается ли ею.
'''
text = "Привет, мир!"
print(text.startswith("Привет"))  # True
print(text.endswith("мир!"))  # True
'''


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************



# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = []
# КЕГЭ = []
# на следующем уроке:
