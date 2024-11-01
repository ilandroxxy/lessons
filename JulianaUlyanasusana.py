# region Домашка: ******************************************************************

# «Второе» число
'''
n = int(input())
M = []
for i in range(n):
    x = int(input())
    M.append(x)
print(M)
M = sorted(M)  # Функция sorted() сортирует по возрастанию
del M[-1]
print(max(M))
'''


# Чётный список
'''
n = int(input())  # 4
M = []
for i in range(n):
    x = int(input())
    if x % 2 == 0:
        M.append(x)
print(M)
'''

# Не оканчивайся на «5»
'''
n = int(input())
M = []
for i in range(n):
    x = int(input())
    if x % 2 != 0 and x % 10 != 5:
        M.append(x ** 2)
print(M)
'''


# Распредели числа
'''
n = int(input())
A = []
B = []
C = []
for i in range(n):
    x = int(input())
    if x < 0:
        A.append(x)
    elif x > 0:
        C.append(x)
    else:
        B.append(x)

M = A + B + C
for x in M:
    print(x)
'''


# Вычисли всё!
'''
n = int(input())
M = [int(x) for x in str(n)]
print(M.count(2))
print(M.count(M[-1]))
nechet = [x for x in M if x % 2 != 0]
print(len(nechet))
M_7 = [x for x in M if x > 7]
print(sum(M_7))
if len(M_7) == 0:
    print(11)
elif len(M_7) == 1:
    print(M_7[0])
else:
    total = 1
    for x in M_7:
        total *= x
    print(total)
print(M.count(0) + M.count(4))
'''

'''
n = int(input())
M = []
for i in range(n):
    x = int(input())
    M.append(x)

R = []
for x in M:
    if M.count(x) == 1:
        R.append(x)

if len(R) == 0:
    print("Уникальных элементов нет")
else:
    for x in R:
        print(x)
'''
# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


'''
# i  01234
s = 'abcde'
print(s[0])  # Первый элемент строки
print(s[-1])  # Последний элемент строки

# Срезы в строках работают точно так же как и в списках:

print(s[2:])  # cde - все, что справа начиная с 2
print(s[1:-1])  # bcd - все кроме первого и последнего
print(s[::-1])  # edcba - все в обратном порядке
'''


# Функции стрко
'''
s = '123213'

print(len(s))  # Длина строки
# print(sum(s)) - такой функции у строк нет
print(min(s), max(s))  # - минимальыне и максимальные элементы 
print(sorted(s))
print(sorted(s, reverse=True))
print(set(s))  # Убирает копии элементов 
'''


# Методы строк

s = '2187342sadsahdjkasASJHD'

print(s.count('2'))  # кол-во вхождений элементов в строку

print(s.index('2'))  # 0 - находит индекс первого слева элемента
print(s.rindex('2'))  # 6 - находит индекс последнего элемента

print(s.upper())  # 2187342SADSAHDJKASASJHD
print(s.lower())  # 2187342sadsahdjkasasjhd

for x in s:
    if x.isdigit():  # проверяет элемент строки на цифру
        print(x, end=' ')  # 2 1 8 7 3 4 2
print()

print(s)  # 2187342sadsahdjkasASJHD
s = s.replace('a', '*')  # Заменить все буквы 'a' на '*'
print(s)  # 2187342s*ds*hdjk*sASJHD

s = s.replace('*', 'a', 2)  # Заменить только первые две '*' на 'a'
print(s)  # 2187342sadsahdjk*sASJHD

# Методы split() и join()


# Функция split() используется для разделения строки
# на части, создавая список. По умолчанию строка
# разбивается по пробелам, но вы также можете указать
# другой разделитель.

# Пример 1: Разделение по пробелам
text = "Привет, мир ! Как дела?"
words = text.split()  # Разделяем строку по пробелам
print(words)  # Вывод: ['Привет,', 'мир!', 'Как', 'дела?']

# Пример 2: Разделение по заданному разделителю
data = "яблоко;банан;груша"
fruits = data.split(';')  # Разделяем строку по символу ";"
print(fruits)  # Вывод: ['яблоко', 'банан', 'груша']


# Функция join() объединяет элементы списка в строку, используя заданный разделитель.

# Пример 1: Объединение списка слов
words = ['Привет,', 'мир!', 'Как', 'дела?']
sentence = ' '.join(words)  # Объединяем слова с пробелом
print(sentence)  # Вывод: Привет, мир! Как дела?

# Пример 2: Объединение списка с заданным разделителем
fruits = ['яблоко', 'банан', 'груша']
result = ', '.join(fruits)  # Объединяем фрукты через запятую и пробел
print(result)  # Вывод: яблоко, банан, груша


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
