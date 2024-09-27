# region Домашка: ******************************************************************

'''
a = int(input())
b = int(input())
if a > b:
    if a % b == 0:
        print("Делится")
    else:
        print("Не делится")
elif a < b:
    if b % a == 0:
        print("Делится")
    else:
        print("Не делится")
else:
    print("На ноль делить нельзя!")
'''


# Разработка программы для определения вида треугольника
'''
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print("Равносторонний")
elif a != b != c != a:
    print("Разносторонний")
else:
    print("Равнобедренный")
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Цикл for отвечает на запросы: "повтори N раз", "пробеги от А до В"
'''
# range(STOP-1)
# range(START, STOP-1)
# range(START, STOP-1, STEP)

for i in range(10):  # range(start=0, STOP=10-1, step=1)
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
print()


for i in range(2, 10):  # range(START=2, STOP=10-1, step=1)
    print(i, end=' ')  # 2 3 4 5 6 7 8 9
print()


for i in range(2, 10, 2):  # range(START=2, STOP=10-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8
print()


for i in range(2, 10+1, 2):  # range(START=2, STOP=11-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10
print()


for i in range(10, 0):  # range(START=10, STOP=0-1, STEP=1)
    print(i, end=' ')  #
print()


for i in range(10, 0, -1):  # range(START=10, STOP=0-1, STEP=-1)
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1
print()


# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']

print(len(M))  # 5 - возвращает длину списка М (кол-во его элементов)

for i in range(len(M)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e
print()


for i in range(len(M)):
    M[i] = M[i] * i
print(M)  # ['', 'b', 'cc', 'ddd', 'eeee']


# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']

for x in M:
    print(x, end=' ')  # a b c d e
print()

for x in M:
    if x in 'ae':
        print(x, end=' ')  # a e
print()


s = '2345362745236427'
for x in s:
    if x in '02468':
        print(x, end=' ')  # 2 4 6 2 4 2 6 4 2 
print()
'''


# Цикл while отвечает на запросы: "пока условие верно, то выполняй", "бесконечный цикл"
'''
for i in range(2, 10+1, 2):  # range(START=2, STOP=11-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10
print()

i = 2
while i <= 10:
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
    i += 2
print()
'''

'''
n = int(input('Введите число в 10-й системе для перевода: '))
b = int(input('Введите систему счисления в которую будем переводить: '))
R = []
while n > 0:
    R.append(n % b)
    n //= b  # b = b // b
R.reverse()
print(R)

print(int('1000'))  # 1000
print(int('1000', 2))  # 8 - Перевод из 2-й системы счисления в 10-ю
'''


'''
n = int(input('Введите число в 10-й системе для перевода: '))
b = int(input('Введите систему счисления в которую будем переводить: '))
r = ''
while n > 0:
    r += str(n % b)
    n //= b  # b = b // b
r = r[::-1]  # срез в обратном порядке - разворачивает строку наоборот
print(r)

print(int(r, 2))  # 8 - Перевод из 2-й системы счисления в 10-ю
'''


# Бесконечные циклы и операторы break, continue, exit()
'''
k = 0
while True:
    k += 1
    if k % 2 != 0:
        continue  # - прерывает итерацию (шаг) цикла
    if k == 2_000_000:
        break  # - прерывает выполнение цикла в котором находится
    if k == 1_000_000:
        exit()  # - полностью прерывает выполнение программы
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
