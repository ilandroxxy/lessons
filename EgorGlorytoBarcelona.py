# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
# -i -5   -4   -3   -2   -1

print(M[0])  # 'a' - Первый элемент списка М
print(M[-1])  # 'e' - Последний элемент списка М

M[0], M[-1] = 'A', 'E'
print(M)  # ['A', 'b', 'c', 'd', 'E']


# 1. Могут хранить неограниченное кол-во элементов, различных типов данных (в отличие от строк и массивов)
# 2. Каждый элемент списка имеет свой порядковый номер: индекс
# 3. Индексы можно считать слева-направо начиная с 0 или справа-налево начиная с -1
# 4. Элементы списков можно не только брать через индексы, но и изменять их значение (в отличие от строк и кортежей)


# i  01234
s = 'abcde'

print(s[0])  # 'a' - Первый элемент списка М
print(s[-1])  # 'e' - Последний элемент списка М
'''

# Срезы списков и строк
'''
# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']

# i  01234
s = 'abcde'

print(M[2:4], s[2:4])  # ['c', 'd'] cd - Взяли элементы со 2 индекса, до 4 индекса (не включая)
print(M[2:], s[2:])  # ['c', 'd', 'e'] cde - Все элементы справа от 2 индекса (включая)
print(M[:4], s[:4])  # ['a', 'b', 'c', 'd'] abcd - Все элементы слева до 4 индекса (не включая)
print(M[:], s[::])  # ['a', 'b', 'c', 'd', 'e'] abcde - Берем все элементы слева-направо с шагом 1
print(M[0::2], s[::2])  # ['a', 'c', 'e'] ace - Все элементы с четными индексами
print(M[1::2], s[1::2])  # ['b', 'd'] bd - Все элементы с не четными индексами


# Особенно важные срезы

# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']

n = 8
print(bin(n))  # 0b1000
print(bin(n)[2:])  # Взяли все элементы кроме 0, 1 индексов

print(M[1:-1])  # ['b', 'c', 'd'] - Все элементы кроме первого и последнего

print(M[::-1])  # ['e', 'd', 'c', 'b', 'a'] - Все элементы в обратном порядке
'''


# Цикл for с последовательностями
'''
M = [1, 2, 3, 2, 3, 4, 5, 2, 3]

s = '123234523'

print(len(s))  # 9 - Возвращает длину списка/строки (кол-во элементов в нем)

for i in range(len(M)):
    # print(i, end=' ')  # 0 1 2 3 4 5 6 7 8
    print(M[i], end=' ')  # 1 2 3 2 3 4 5 2 3
print()

for i in range(len(M)):
    M[i] = M[i] ** 2
print(M)  # [1, 4, 9, 4, 9, 16, 25, 4, 9]


for x in M:
    print(x, end=' ')  # 1 2 3 2 3 4 5 2 3
print()

s = '123234523'
for x in s:
    if x in '02468':
        print(x, end=' ')  # 2 2 4 2 
print()
'''

# Функции списков
'''
M = [1, 2, 3, 2, 3, 4, 5, 2, 3]

print(len(M))  # 9 - Возвращает длину списка/строки (кол-во элементов в нем)
print(sum(M))
print(min(M), max(M))
print(sorted(M))  # [1, 2, 2, 2, 3, 3, 3, 4, 5] - сортирует в порядке возрастания
print(sorted(M, reverse=True))  # [5, 4, 3, 3, 3, 2, 2, 2, 1] - сортирует в порядке убывания
print(set(M))  # {1, 2, 3, 4, 5}
'''


# Функции строке
'''
s = '123234523'
print(len(s))  # 9 - Возвращает длину списка/строки (кол-во элементов в нем)
# print(sum(s))
print(min(s), max(s))
print(sorted(s))  # ['1', '2', '2', '2', '3', '3', '3', '4', '5'] - сортирует в порядке возрастания
print(sorted(s, reverse=True))  # ['5', '4', '3', '3', '3', '2', '2', '2', '1'] - сортирует в порядке убывания
print(set(s))  # {'1', '5', '4', '2', '3'}
'''


# Все методы списков в Python, которые понадобятся на ЕГЭ
#
#
# Метод .append() используется для добавления элемента в конец списка.
'''
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Вывод: [1, 2, 3, 4]

# Можно реализовать через конкатенацию (склеивание) списков:
my_list = [1, 2, 3]
my_list += [4, 5]
print(my_list)  # Вывод: [1, 2, 3, 4, 5]
'''


# Метод .reverse() изменяет порядок элементов в списке на обратный.
'''
my_list = [1, 2, 3, 4]
my_list.reverse()
print(my_list)  # Вывод: [4, 3, 2, 1]

# Можно записать по другому через срез:
my_list = [1, 2, 3, 4]
my_list = my_list[::-1]
print(my_list)  # Вывод: [4, 3, 2, 1]
'''


# Метод .count() возвращает количество вхождений заданного элемента в список.
'''
my_list = [1, 2, 2, 3, 4, 2]
print(my_list.count(2))  # Вывод: 3
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
'''


# Метод .index() возвращает индекс первого вхождения заданного элемента в списке.
'''
my_list = [1, 2, 3, 2, 4]
print(my_list.index(2))  # Вывод: 1
'''

# Метод .sort() сортирует элементы списка по возрастанию (по умолчанию) или в
# обратном порядке, если передан аргумент reverse=True.
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
# Эти методы позволяют изменять регистр строки. lower()
# преобразует строку в нижний регистр, а upper() – в верхний.
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

text = '22222222'
text = text.replace('2', '*')
print(text)  # ********


text = '22222222'
text = text.replace('2', '*', 4)
print(text)  # ****2222
'''

# 4⃣  .split()
# Метод split(separator) разделяет строку на части по указанному разделителю.
# Если разделитель не указан, используется пробел.
'''
text = "яблоко груша банан"
fruits = text.split()  # по умолчанию разделяет по пробелам
print(fruits)  # ['яблоко', 'груша', 'банан']

text = "яблоко;груша;банан"
fruits = text.split(';')  # по умолчанию разделяет по пробелам
print(fruits)  # ['яблоко', 'груша', 'банан']
'''


# 5⃣ .join()
# Метод join(iterable) соединяет элементы списка (или другого итерируемого объекта)
# в строку с указанным разделителем.
'''
fruits = ['яблоко', 'груша', 'банан']
result = ', '.join(fruits)
print(result)  # "яблоко, груша, банан"

fruits = ['яблоко', 'груша', 'банан']
result = '**'.join(fruits)
print(result)  # "яблоко**груша**банан"
'''


# 6⃣ .find()
# Метод find(substring) ищет подстроку в строке и возвращает индекс, с которого начинается первая встреча.
# Если подстрока не найдена, возвращает -1.
'''
text = "Привет, прекрасный, мир!"
index = text.find(",")
print(index)  # 6

text = "Привет, прекрасный, мир!"
index = text.rfind(",")
print(index)  # 18


text = "Привет, прекрасный, мир!"
index = text.index(",")
print(index)  # 6

text = "Привет, прекрасный, мир!"
index = text.rindex(",")
print(index)  # 18
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

# Генераторы списков

M = [x for x in range(10)]
print(M)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

M = [x**2 for x in range(10)]
print(M)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

M = [x**2 for x in range(10) if x % 2 == 0]
print(M)  # [0, 4, 16, 36, 64]


import random
M = [random.randint(0, 100) for i in range(10)]
print(M)  # [22, 53, 3, 96, 88, 22, 76, 4, 74, 14]

chet = [x for x in M if x % 2 == 0]
print(chet)  # [22, 96, 88, 22, 76, 4, 74, 14]

nechet = [x for x in M if x % 2 != 0]
print(nechet)  # [53, 3]

copied = [x for x in M if M.count(x) > 1]
print(copied)  # [22, 22]

not_copied = [x for x in M if M.count(x) == 1]
print(not_copied)  # [53, 3, 96, 88, 76, 4, 74, 14]

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 4, 6]
# КЕГЭ  = []
# на следующем уроке:
