# region Домашка: ******************************************************************

# https://stepik.org/lesson/1309432/step/8?unit=1324548
'''
a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print('Равносторонний')
elif a != b != c != a:
    print('Разносторонний')
else:
    print('Равнобедренный')
'''


# https://stepik.org/lesson/1309432/step/9?unit=1324548
'''
a = int(input())
if a > 80:
    print('Почва пересыщена')
elif 60 < a <= 80:
    print ('Уровень влажности оптимален')
elif 30 < a <= 60:
    print ('Уровень влажности умеренный')
else:
    print('Почва слишком сухая')
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Цикл for отвечает на запросы: "повтори N раз", "пробеги от А до В"

# Работа цикла for c функцией range()
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

for i in range(10, 0, -1):
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1
print()

# Работа цикла for напрямую с последовательностями

# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']

print(len(M))  # 5 - Возвращает длину списка (кол-во элементов в нем)

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
    M[i] = M[i] * i
print(M)  # ['', 'b', 'cc', 'ddd', 'eeee']
'''


# Цикл while отвечает на запросы: "пока условие верно, делаем действие", "бесконечный цикл"
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


# Переводы в различные системы счисления
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
n = 10**8
b = 16
r = ''
while n > 0:
    r = alp[n % b] + r
    n //= b
print(r)  # 5F5E100


# Встроенная функция обратного перевода
print(int('1000', 2))  # 8
print(int('10', 8))  # 8
print(int('8', 16))  # 8
# ValueError: int() base must be >= 2 and <= 36, or 0
'''

# Универсальная функция перевода в различные системы счисления
'''
def convert(n, b):
    alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r


print(convert(10**8, 16))  # 5F5E100
print(int('5F5E100', 16))  # 10**8

print(convert(8, 2))  # 1000
print(int('1000', 2))  # 8
'''


# Бесконечные циклы и операторы: break, continue, exit()

k = 0
while True:
    k += 1
    if k % 2 != 0:
        continue  # Прерывание шага цикла (итерации цикла)
    if k == 100_000:
        break  # Прерываем выполнение цикла
    if k == 50_000:
        exit()  # Прерываем выполнение программы
    print(k)

print('Добро пожаловать.')


'''
password = 'qwerty'
pas = input('Введите пароль: ')
while True:
    if pas == password:
        print('Пароль верный!')
        break
    else:
        pas = input('Пароль неверный, повторите попытку: ')


print('Добро пожаловать.')
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
