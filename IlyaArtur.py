# region Домашка: ******************************************************************

# Проверка соотношения для пятизначного числа

# Сочетание клавиш: ctrl + alt + L
'''
z = int(input())
a = z // 10000
b = (z // 1000) % 10
c = (z // 100) % 10
d = (z // 10) % 10
e = z % 10
if a * c == b + d + e:
    print("Да")
else:
    print("Нет")
'''


# Разработка программы для определения вида треугольника
'''
a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print("Равносторонний")
elif a != b != c != a:
    print('Разносторонний')
else:
    print("Равнобедренный")
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Циклы while и for

# Цикл for отвечает на запросы: "повтори N раз", "пробеги от А до В"


# Работа с циклом for через range()
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

n = 10
for i in range(2, n+1, 2):
    print(i, end=' ')  # 2 4 6 8 10
print()

for i in range(10, 0):
    print(i, end=' ')  #
print()

for i in range(10, 0, -1):
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1
print()
'''
# Функция range() работает только с целыми числами
# for i in range(0, 10, 0.5):
#     print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1
# print()
# TypeError: 'float' object cannot be interpreted as an integer


# Работа с циклом for напрямую с последовательностью
'''
# 4. Через индексы элементов можно не только брать их значение, но и изменять его

# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']

print(len(M))  # 5 - Функция len() возвращает длину списка, то есть кол-во элементов в нем

for i in range(len(M)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e
print()

# 0 1 2 3 4
# a b c d e
for i in range(len(M)):
    print(i, M[i])
    # 0 * a = ''
    # 1 * b = 'b'
    # 2 * c = 'cc'
    # 3 * d = 'ddd'
    # 4 * e = 'eeee'
    M[i] = M[i] * i

print(M)  # ['', 'b', 'cc', 'ddd', 'eeee']
print('hello ' * 4)  # hello hello hello hello

# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']

for x in M:
    print(x, end=' ')  # a b c d e
print()

for x in M:
    if x in 'ae':
        print(x, end=' ')  # a e - Забрали все гласные элементы
print()
'''

# Цикл while отвечает на запросы: "пока условие верно мы делаем действие", "бесконечные циклы"

'''
for i in range(2, 10+1, 2):
    print(i, end=' ')  # 2 4 6 8 10
print()

i = 2
while i <= 10:
    print(i, end=' ')  # 2 4 6 8 10
    i += 2
print()
'''

# Перевод из 10-й в b-ю систему счисления
'''
n = int(input('Введите число для перевода: '))
b = int(input('Введите b-ю систему счисления: '))
r = ''
while n > 0:
    r = str(n % b) + r
    n //= b
print(r)  # 1000
'''

# Бесконечные циклы и операторы break, continue, exit()
'''
k = 0
while True:
    k += 1
    if k % 2 != 0:
        continue  # Прерываем итерацию (шаг) цикла
    if k == 1_000_000:
        break  # Прерывает цикл в котором сейчас находится
    if k == 2_000_000:
        exit()  # Прерывает выполнение программы (всей)
    print(k)

print('Продолжение программы')
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
