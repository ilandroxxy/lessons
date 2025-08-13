# region Домашка: ******************************************************************

# https://stepik.org/lesson/1309431/step/13?unit=1324547
'''
k = input()
l = 2*k
y = 3*k
summa = int(k) + int(y)+ int(l)
print(f"Сумма чисел: {summa}")


k = int(input())  # 4 * 11 -> 44
summa = k + k * 11 + k * 111
print(f"Сумма чисел: {summa}")
'''


# https://stepik.org/lesson/1309432/step/8?unit=1324548
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


'''
a = int(input())
b = int(input())
if a > b:
    if a % b == 0:
        print("Делится")
    else:
        print("Не делится")
else:
    if b % a == 0:
        print("Делится")
    else:
        print("Не делится")
'''


# "Ночь" — если время с 00:00 до 05:29.
# "Утро" — если время с 05:30 до 12:14.
# "День" — если время с 12:15 до 17:44.
'''
H = int(input())
M = int(input())

if 0 <= H <= 4:
    print("Ночь")
elif H == 5:
    if 0 <= M <= 29:
        print('Ночь')
    else:
        print('Утро')
elif 6 <= H <= 11:
    print('Утро')
elif H == 12:
    if 0 <= M <= 14:
        print('Утро')
    else:
        print('День')
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Цикл for отвечает на запросы: "Повтори 5 раз", "Пробеги числа от 10 до 100", "Пробежать все элементы последовательности"
'''
for _ in range(10):  # Повтори N раз без создания переменной 
    print('Повторяю десять раз')
'''

# Работа цикла for с функцией range()
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
'''

# Работа цикла for с последовательностями: list, str, tuple, ..
'''
# i   0    1    2    3    4
L = ['a', 'b', 'c', 'd', 'e']
T = ('a', 'b', 'c', 'd', 'e')
s = 'abcde'

print(len(L))  # 5 - Функция len() возвращает длину списка (кол-во элементов внутри)
'''

# Если нужно изменять элементы списков, то лучше использовать range(len())
'''
for i in range(len(L)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(L[i], end=' ')  # a b c d e
print()

for i in range(len(L)):
    L[i] = L[i] * i
print(L)  # ['', 'b', 'cc', 'ddd', 'eeee']
'''

# Если нужно просто пробежать элементы или фильтровать их, то лучше пробегать напрямую через in
'''
L = ['a', 'b', 'c', 'd', 'e']

for x in L:
    print(x, end=' ')  # a b c d e
print()

for x in L:
    if x in 'aeo':
        print(x, end=' ')  # a e
print()
'''

# Цикл while отвечает на запросы: "Пока условие верно - делай действие", "Бесконечные циклы"
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
n = 8
b = 2
r = ''
while n > 0:
    r = str(n % b) + r
    n //= b
print(r)
'''

# Универсальная функция перевода из 10-й в b-ю систему счисления:
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r


print(convert(8, 2))
print(convert(8, 4))
print(convert(10**6, 16))  # F4240
'''


# Бесконечные циклы и операторы: break, continue, exit()
'''
k = 0
while True:
    k += 1
    if k % 2 != 0:
        continue  # прерывает итерацию (шаг) цикла
    if k == 50_000:
        exit()  # прерывает (останавливает) выполнение программы
    if k == 100_000:
        break  # прерывание цикла в котором break описан
    print(k)

print('Продолжение программы')
'''

# Простейшая программы на бесконечном цикле
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r


while True:
    case = input('\ncase 1: Перевод из 10-й в B-ю систему счисления \n'
                 'case 2: \n'
                 'case 3: \n'
                 'case 0: Выход из программы. \n'
                 'case: ')

    if case == '1':
        n = int(input('Введите число для перевода: '))
        b = int(input('Введите систему счисления: '))
        print(f'Результат перевода числа {n} в {b}-ю систему счисления: {convert(n, b)}')

    elif case == '2':
        pass

    elif case == '3':
        pass

    elif case == '0':
        print('Спасибо, что пользовались нашим калькулятором!')
        exit()

    else:
        print('Я не понимаю никаких команд, кроме: case 1, 2, 3, 0')
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
