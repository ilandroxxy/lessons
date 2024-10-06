# region Домашка: ******************************************************************

'''
a = int(input())
b = int(input())
c = int(input())
summa = 0
if (a % 7 == 0 and a % 49 != 0) or a % 40 == 0:
    summa += a
if (b % 7 == 0 and b % 49 != 0) or b % 40 == 0:
    summa += b
if (c % 7 == 0 and c % 49 != 0) or c % 40 == 0:
    summa += c
print(summa)
'''


'''
a = int(input())
b = int(input())
if a % b == 0 or b % a == 0:
    print('Делится')
else:
    print('Не делится')
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Цикл for отвечает на запросы: "Повтори N раз", "Пробеги от A до В"
'''
# Работа с циклом for через функцию range:

# range(STOP-1)
# range(START, STOP-1)
# range(START, STOP-1, STEP)

for i in range(10):  # range(start=0, STOP=10-1, step=1)
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
print()


for i in range(2, 10):  # range(start=2, STOP=10-1, step=1)
    print(i, end=' ')  # 2 3 4 5 6 7 8 9
print()


for i in range(2, 10, 2):  # range(start=2, STOP=10-1, step=2)
    print(i, end=' ')  # 2 4 6 8
print()


for i in range(2, 10+1, 2):  # range(start=2, STOP=10-1, step=2)
    print(i, end=' ')  # 2 4 6 8 10
print()


for i in range(10, 0):  # range(start=10, STOP=0-1, step=1)
    print(i, end=' ')  #
print()


for i in range(10, 0, -1):  # range(start=10, STOP=0-1, step=1)
    print(i, end=' ')  #
print()


# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']

print(len(M))  # 5 - Возвращает длину списка (кол-во элементов в нем)

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
'''

# Цикл while отвечает на запросы: "ПОКА условие верно, делаем", ""
'''
for i in range(2, 10+1, 2):  # range(start=2, STOP=10-1, step=2)
    print(i, end=' ')  # 2 4 6 8 10
print()


i = 2
while i <= 10:
    print(i, end=' ')  # 2 4 6 8 10 
    i += 2
print()
'''
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

n = int(input('Введите число в 10-й системе: '))
b = int(input('Введите b-ю систему для перевода: '))
r = ''
while n > 0:
    r += alphabet[n % b]
    n //= b
r = r[::-1]  # Разворачиваем содержимое строки в обратном порядке
print(f'Результат перевода: {r}')
'''

'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    r = ''
    while n > 0:
        r += alphabet[n % b]
        n //= b
    return r[::-1]


n = int(input('Введите число в 10-й системе: '))
b = int(input('Введите b-ю систему для перевода: '))
print(f'Результат перевода: {convert(n, b)}')
'''


# Бесконечные циклы и операторы break, continue, exit()
'''
k = 0
while True:
    k += 1
    if k % 2 != 0:
        continue  # Прерывает итерацию (шаг) цикла
    if k == 1_000_000:
        break  # Прерывает выполнение циклы в котором лежит
    if k == 2_000_000:
        exit()  # Прерывает выполнение всей программы
    print(k)

print('Продолжение программы')
'''


from string import digits, ascii_uppercase

alphabet = digits + ascii_uppercase
# 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ

def convert(n, b):
    r = ''
    while n > 0:
        r += alphabet[n % b]
        n //= b
    return r[::-1]


while True:
    case = int(input('\n'
                     'case 1: Перевод из 10-й в b-ю систему счисления \n'
                     'case 2: Перевод из b-й в 10-ю систему счисления \n'
                     'case 3: Перевод из b-й в k-ю систему счисления\n'
                     'case 0: Выход из программы\n'
                     'case: '))

    if case == 1:
        n = int(input('Введите число в 10-й системе: '))
        b = int(input('Введите b-ю систему для перевода: '))
        r = convert(n, b)
        print(f'Результат перевода числа {n} из 10-й в {b}-ю систему: {r}')

    elif case == 2:
        b = int(input('Введите b-ю систему: '))
        r = input(f'Введите число в {b}-й системе: ')
        n = int(r, b)
        print(f'Результат перевода числа {r} из {b}-й в 10-ю систему: {n}')

    elif case == 3:
        b = int(input('Введите b-ю систему: '))
        r = input(f'Введите число в {b}-й системе: ')
        k = int(input('Введите k-ю систему для перевода: '))
        n = int(r, b)
        new_r = convert(n, k)
        print(f'Результат перевода числа {r} из {b}-й в {k}-ю систему: {new_r}')

    elif case == 0:
        print('Спасибо, что пользовались нашим калькулятором!')
        break

    else:
        print('Я не понимаю такой команды, воспользуйтесь: 1, 2, 3, 0')


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
