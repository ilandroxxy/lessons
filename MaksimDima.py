# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Логические связки: and, or, not, in, ==, !=, ^
'''
flag = True
print(not flag)
print(not(not flag))

s = '2wre34we234tr'
for x in s:
    # if x.isdigit():
    if x in '0123456789':
        print(x, end=' ')  # 2 3 4 2 3 4
print()

a = '126732109'
for x in a:
    if x in '02468':
        print(x, end=' ')  # 2 6 2 0
print()

A = [int(x) for x in '126732109']
A = [1, 2, 6, 7, 3, 2, 1, 0, 9]
for x in A:
    # if str(x) in '02468':
    if x % 2 == 0:
        print(x, end=' ')  # 2 6 2 0
print()


a, b, c = 4, -5, 6
if a > 0 and b > 0:
    print('and')  # Гарантирует, что оба (все) условия будут выполняться
if a > 0 or b > 0:
    print('or')  # Говорит о том, что хотя бы одно условие выполняется
if (a > 0) ^ (b > 0):
    print('^')  # Говорит о том, что только одно условие выполняется (либо 1, либо 2)
if (a > 0) != (b > 0):
    print('!=')  # Говорит о том, что только одно условие выполняется (либо 1, либо 2)


print(True + False + True)  # 2

#   True      False     True
if (a > 0) + (b > 0) + (c > 0) == 2:
    print('Только два условия истинны')
if (a > 0) + (b > 0) + (c > 0) >= 2:
    print('Хотя бы два условия истинны')
'''

'''
# i   0    1    2    3    4
A = ['a', 'b', 'c', 'd', 'e']   # list (список)
# -i -5   -4   -3   -2   -1

print(A[0])  # Первый элемент списка A
print(A[-1])  # Последний элемент списка A
print(A[1:-1])  # ['b', 'c', 'd'] - Все элементы, кроме первого и последнего

A[0], A[-1] = 'A', 'E'
print(A)  # ['A', 'b', 'c', 'd', 'E']

# 1. Могут хранить в себе неограниченное кол-во элементов, различных значений (в отличие от массивов и строк)
# 2. Каждый элемент списка имеет свой порядковый номер, индекс
# 3. Индексы можно считать слева-направо начиная с 0 или справа-налево начиная с -1
# 4. Через индексы мы можем не только брать элементы списка, но и ИЗМЕНЯТЬ их значения (в отличие от кортежей и строк)
'''

# Срезы списков и строк
'''
# i   0    1    2    3    4
A = ['a', 'b', 'c', 'd', 'e']

# i  01234
s = 'abcde'

# СРЕЗ [START : STOP - 1 : STEP]

print(A[2:4])  # ['c', 'd']
print(A[:4])  # Все элементы до 4 по индексу (не включительно)
print(A[2:])  # ['c', 'd', 'e'] - Все элементы от 2 по индексу (включительно)
print(A[:])
print(A[::])  # ['a', 'b', 'c', 'd', 'e'] - Все элементы
print(A[0::2])  # ['a', 'c', 'e'] - Все элементы по четным индексам
print(A[1::2])  # ['b', 'd'] - Все элементы на нечетных индексах

print(s[0::2])  # ace - Все элементы по четным индексам
print(s[1::2])  # bd - Все элементы на нечетных индексах

# Особенно полезные срезы:

n = 8
print(bin(n))  # 0b1000
print(bin(n)[2:])  # 1000 - Все элементы, кроме первых двух

print(A[1:-1])  # ['b', 'c', 'd'] - Все элементы кроме первого и последнего

print(A[::-1])  # ['e', 'd', 'c', 'b', 'a'] - Все элемнты в обратном порядке
'''


# Работа цикла for с списками
'''
# i   0    1    2    3    4
A = ['a', 'b', 'c', 'd', 'e']


print(len(A))  # Выводит длину списка (кол-во символов)

for i in range(len(A)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(A[i], end=' ')  # a b c d e
print()

for i in range(len(A)):
    A[i] = A[i] * i
print(A)  # ['', 'b', 'cc', 'ddd', 'eeee']


A = ['a', 'b', 'c', 'd', 'e']

for x in A:
    print(x, end=' ')  # a b c d e
print()

for x in A:
    if x in 'ae':
        print(x, end=' ')  # a e
print()
'''


# Работа цикла while с списками
'''
n = 8
b = 2
R = []
while n > 0:
    R.append(n % b)
    n //= b
R.reverse()  # R = R[::-1]
print(R)  # [1, 0, 0, 0]

n = 8
b = 2
r = ''
while n > 0:
    r = str(n % b) + r
    n //= b
print(r)  # 1000
'''

# Функции списков
'''
M = [1, 2, 3, 2, 3, 4]
print(len(M))
print(sum(M))
print(min(M), max(M))
print(sorted(M))  # [1, 2, 2, 3, 3, 4] - Сортировка по возрастанию
print(sorted(M, reverse=True))  # [4, 3, 3, 2, 2, 1] - Сортировка по убыванию
print(set(M))  # {1, 2, 3, 4} - Удаляет копии элементов
'''

# Функции строк
'''
s = '123234'
print(len(s))
# print(sum(s))  # не работает
print(min(s), max(s))
print(sorted(s))  # ['1', '2', '2', '3', '3', '4'] - Сортировка по возрастанию
print(sorted(s, reverse=True))  # ['4', '3', '3', '2', '2', '1'] - Сортировка по убыванию
print(set(s))  # {'4', '3', '1', '2'} - Удаляет копии элементов
'''


# Методы - это функции направленные только на один тип данных

# Все методы списков в Python, которые понадобятся на ЕГЭ

# Метод .append() используется для добавления элемента в конец списка.
'''
my_list = [1, 2, 3]
my_list.append(4)
my_list.append(5)
print(my_list)  # Вывод: [1, 2, 3, 4, 5]

# Можно реализовать через конкатенацию (склеивание) списков:
my_list = [1, 2, 3]
# my_list += [4, 5]
my_list = [0] + my_list + [4, 5]
print(my_list)  # Вывод: [0, 1, 2, 3, 4, 5]
'''


# Метод .reverse() изменяет порядок элементов в списке на обратный.
'''
my_list = [1, 2, 3, 4]
my_list.reverse()
print(my_list)  # Вывод: [4, 3, 2, 1]

my_list = [1, 2, 3, 4]
my_list = list(reversed(my_list))  # <list_reverseiterator object at 0x10236ff40>
print(my_list)  # Вывод: [4, 3, 2, 1]

# Можно записать по другому через срез:
my_list = [1, 2, 3, 4]
my_list = my_list[::-1]
print(my_list)  # Вывод: [4, 3, 2, 1]
'''


# Метод .count() возвращает количество вхождений заданного элемента в список.
'''
my_list = [1, 2, 2, 3, 4, 2]
count_of_twos = my_list.count(2)
print(count_of_twos)  # Вывод: 3


s = 'uh5ui43h5ui3h45'
cnt = 0
for x in s:
    if x.isdigit():
        cnt += 1
print(f'Кол-во цифр в строке: {cnt}')

print(len([x for x in s if x.isdigit()]))  # 7

print([x*2 for x in s if x.isdigit()])  # ['55', '44', '33', '55', '33', '44', '55']
'''

# Метод .remove() удаляет первое вхождение указанного элемента из списка.
'''
my_list = [1, 2, 3, 2, 4]
my_list.remove(2)  # первая найденная двойка
print(my_list)  # Вывод: [1, 3, 2, 4]

# Можно удалить элемент через его индекс используя del:
my_list = [1, 2, 3, 2, 4]
del my_list[1]  # индекс удаляемого элемента
print(my_list)  # Вывод: [1, 3, 2, 4]

my_list = [1, 2, 3, 2, 4]
while 2 in my_list:
    my_list.remove(2)
print(my_list)  # [1, 3, 4]


my_list = [1, 2, 3, 2, 4]
for _ in range(my_list.count(2)):
    my_list.remove(2)
print(my_list)  # [1, 3, 4]
'''


# Метод .index() возвращает индекс первого вхождения заданного элемента в списке.
'''
my_list = [1, 2, 3, 2, 4]
index_of_two = my_list.index(2)
print(index_of_two)  # Вывод: 1
'''

# Метод .sort() сортирует элементы списка по возрастанию (по умолчанию) или в обратном порядке,
# если передан аргумент reverse=True.
'''
my_list = [4, 1, 3, 2]
my_list.sort()
print(my_list)  # Вывод: [1, 2, 3, 4]

my_list.sort(reverse=True)
print(my_list)  # Вывод: [4, 3, 2, 1]

# Скажу честно я не любитель этого метода, считаю, что удобнее будет использовать функцию sorted():
my_list = [4, 1, 3, 2]
my_list = sorted(my_list)
print(my_list)  # Вывод: [1, 2, 3, 4]

my_list = sorted(my_list, reverse=True)
print(my_list)  # Вывод: [4, 3, 2, 1]
'''


# Все методы строк в Python, которые понадобятся на ЕГЭ

# 1⃣ .strip()
# Метод strip() удаляет пробелы (или другие символы) из начала и конца строки.
# Это полезно для очистки пользовательского ввода.
'''
text = " Привет, мир!  "
cleaned_text = text.strip()
print(cleaned_text)  # "Привет, мир!"
'''

# 2⃣ .lower() и .upper()
# Эти методы позволяют изменять регистр строки. lower() преобразует
# строку в нижний регистр, а upper() – в верхний.
'''
text = "ПрIvEt"
print(text.lower())  # "прivet"
print(text.upper())  # "ПРIVET"
'''

# 3⃣ .replace()
'''
# Метод replace(old, new, count) заменяет подстроку old на new в строке count раз.
text = "Я люблю Python!"
new_text = text.replace("Python", "программирование")
print(new_text)  # "Я люблю программирование!"

text = '21321321321312'
text = text.replace('2', '*')  # Заменили сразу все '2'
print(text)  # *13*13*13*131*

text = text.replace('*', '2', 3)  # Заменили первые 3 звездочки на '2'
print(text)  # 213213213*131*
'''


# 4⃣  .split()
# Метод split(separator) разделяет строку на части по указанному разделителю.
# Если разделитель не указан, используется пробел.
'''
text = "яблоко груша банан"
fruits = text.split()  # по умолчанию разделяет по пробелам
print(fruits)  # ['яблоко', 'груша', 'банан']

for s in open('files/9.csv'):
    print(s)  # '43,90,148,130,1'
    M = [int(x) for x in s.split(',')]
    print(M)  # [43, 90, 148, 130, 1]
'''

# 5⃣ .join()
# Метод join(iterable) соединяет элементы списка (или другого итерируемого объекта)
# в строку с указанным разделителем.
'''
fruits = ['яблоко', 'груша', 'банан']
result = ', '.join(fruits)
print(result)  # "яблоко, груша, банан"

result = '***'.join(fruits)
print(result)  # "яблоко***груша***банан"
'''


# 6⃣ .find()
# Метод find(substring) ищет подстроку в строке и возвращает индекс, с которого начинается первая встреча.
# Если подстрока не найдена, возвращает -1.
'''
text = "212222212"

index = text.find("1")
print(index)  # 1

index = text.index("1")
print(index)  # 1

index = text.rfind("1")
print(index)  # 7

index = text.rindex("1")
print(index)  # 7

index = text.find("3")
print(index)  # -1 - Если элемента не найдется, то вернет -1

index = text.index("3")
print(index)  # ValueError: substring not found
'''

# 7⃣ .count()
# Метод count(substring) возвращает количество вхождений подстроки в строку.
'''
text = "яблоко, груша, яблоко"
count = text.count("яблоко")
print(count)  # 2
'''

# 8⃣ .startswith() и .endswith()
# Эти методы проверяют, начинается ли строка с указанной подстроки или заканчивается ли ею.
'''
text = "Привет, мир!"
print(text.startswith("Привет"))  # True
print(text.endswith("мир!"))  # True
'''

# Генераторы списков:
'''
M = [int(x) for x in open('files/17.txt')]
# -2536

# Найдите все элементы, которые оканчиваются на 36

D = [x for x in M if abs(x) % 100 == 36]
print(D)  # [-2536, -8336, 1536, 1436, -9736, 236

D = [x for x in M if str(x)[-2:] == '36']
print(D)  # [-2536, -8336, 1536, 1436, -9736, 236

D = [x for x in M if str(x).endswith('36')]
print(D)  # [-2536, -8336, 1536, 1436, -9736, 236


M = [x for x in range(10)]
print(M)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

M = [x for x in range(10) if x % 2 == 0]
print(M)  # [0, 2, 4, 6, 8]

M = [x**2 for x in range(10) if x % 2 == 0]
print(M)  # [0, 4, 16, 36, 64]

from random import randint
M = [randint(0, 100) for _ in range(10)]
print(M)  # [53, 60, 95, 50, 2, 62, 50, 93, 43, 19]

chet = [x for x in M if x % 2 == 0]
print(chet)  # [60, 50, 2, 62, 50]

nechet = [x for x in M if x % 2 != 0]
print(nechet)  # [53, 95, 93, 43, 19]

copied = [x for x in M if M.count(x) > 1]
print(copied)  # [50, 50]

not_copied = [x for x in M if M.count(x) == 1]
print(not_copied)  # [53, 60, 95, 2, 62, 93, 43, 19]


# Определите длину самой длинной последовательности, состоящей из символов Y.
s = open('files/24.txt').readline()
s = s.replace('X', ' ').replace('Z', ' ')
print(len(sorted(s.split())[-1]))  # 10
print(max([len(x) for x in s.split()]))  # 10
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = []
# КЕГЭ  = []
# на следующем уроке:
