# region Домашка: ******************************************************************

'''
a = int(input())
print(a ** 3)
print(6 * a ** 2)
'''


# Разработка программы для определения вида треугольника
'''
a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print("Равносторонний")
elif a != b != c != a:  # 2 4 3
    print("Разносторонний")
else:
    print("Равнобедренный")
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Цикл for отвечает на запросы: "повтори N раз", "пробеги от А до В"

# Функция range() это функция диапазона только целых чисел
# range(STOP-1)
# range(START, STOP-1)
# range(START, STOP-1, STEP)
'''
for i in range(10):  # range(start=0, STOP=10-1, step=1)
    # print(i, end='**')  # 0**1**2**3**4**5**6**7**8**9**
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
print()


for i in range(2, 10):  # range(START=2, STOP=10-1, step=1)
    print(i, end=' ')  # 2 3 4 5 6 7 8 9
print()


for i in range(2, 10, 2):  # range(START=2, STOP=10-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8
print()


for i in range(2, 10+1, 2):  # range(START=2, STOP=10-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10
print()


for i in range(10, 0+1):  # range(START=10, STOP=0, step=1)
    print(i, end=' ')  #
print()

for i in range(10, 0, -1):  # range(START=10, STOP=0, STEP=-1)
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1
print()


# Через цикл for мы можем перебирать все элементы списка
M = ['a', 'b', 'c', 'd', 'e']
for x in M:
    print(x, end=' ')  # a b c d e
print()

# Функция len(M) - возвращает длину (кол-во элементов) последовательности M

# Через цикл for мы можем перебирать все элементы списка по индексам

# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
for i in range(len(M)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e 
print()
'''

# Цикл while отвечает на запросы: "пока условие верно, делаем действие", "бесконечные циклы"
'''
for i in range(2, 10+1, 2):  # range(START=2, STOP=10-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10
print()

i = 2
while i <= 10:
    print(i, end=' ')
    i += 2  # 0 1 2 3 4 5 6 7 8 9 
print()
'''


# Функция перевода из 10-й в b-ю систему счисления
'''
n = int(input('Введите число для перевода: '))
b = int(input('Введите b-ю систему счисления: '))
r = ''
while n > 0:
    r = str(n % b) + r
    n //= b
print(r)
'''

# Универсальная функция перевода
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
n = int(input('Введите число для перевода: '))
b = int(input('Введите b-ю систему счисления: '))
r = ''
while n > 0:
    r = alphabet[n % b] + r
    n //= b
print(r)  
'''

# Бесконечные циклы и операторы break, continue, exit()
'''
k = 0
while True:
    k += 1
    if k % 2 != 0:  # нечетное
        continue  # - Прерывает итерацию (шаг) цикла
    if k == 1_000_000:
        break  # - Прерывает цикл в котором он находится
    if k == 2_000_000:
        exit()  # - Полностью прерывает программу
    print(k)


print('Продолжение программы')
'''


# Калькулятор систем счисления

from string import *
alphabet = digits + ascii_uppercase


def convert(n, b):
    r = ''
    while n > 0:
        r = alphabet[n % b] + r
        n //= b
    return r


while True:
    case = input('\n'
                 'case 1: Перевод из 10-й в b-ю систему. \n'
                 'case 2: Перевод из b-й в 10-ю систему. \n'
                 'case 3: Перевод из b-й в k-ю систему. \n'
                 'case 0: Выход из программы. \n')

    if case == '1':
        n = int(input('Введите число для перевода: '))
        b = int(input('Введите b-ю систему счисления: '))
        r = convert(n, b)
        print(f'Результат перевода числа {n} в {b}-ю систему: {r}')

    elif case == '2':
        b = int(input('Введите b-ю систему счисления: '))
        r = input(f'Введите число в {b}-й системе: ')
        n = int(r, b)
        print(f'Результат перевода числа {r} из {b}-ю системы: {n}')

    elif case == '3':
        pass

    elif case == '0':
        print('Спасибо, что пользовались нашим калькулятором')
        exit()

    else:
        print('Я понимаю только команды 1, 2, 3, 0.')




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
