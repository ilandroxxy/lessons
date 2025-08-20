# region Домашка: ******************************************************************

# https://stepik.org/lesson/1309432/step/5?unit=1324548
'''
# ctrl + alt + L - форматирование кода в PEP8

a = int(input())
p = a // 10000
t = a // 100 % 10
v = a // 1000 % 10
ch = a // 10 % 10
pa = a % 10
if (p * t) == (v + ch + pa):
    print('Да')
else:
    print('Нет')
'''

# https://stepik.org/lesson/1309432/step/6?unit=1324548
'''
a = int(input())
b = int(input())
c = int(input())
summa = 0
if (a % 7 == 0 and a % 49 != 0) or a%40 == 0:
    summa += a
if (b % 7 == 0 and b % 49 != 0) or b%40 == 0:
    summa += b
if (c % 7 == 0 and c % 49 != 0) or c%40 == 0:
    summa += c
print(summa)
'''
'''
a = int(input())
b = int(input())
c = int(input())
summa = 0
for x in (a, b, c):
    if (x % 7 == 0 and x % 49 != 0) or x % 40 == 0:
        summa += x
print(summa)
'''


# https://stepik.org/lesson/1309432/step/10?unit=1324548
'''
a = int(input())
if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
    print("Високосный")
else:
    print("Обычный")
'''


# https://stepik.org/lesson/1309434/step/8?unit=1324550
'''
n = int(input())  # 283573498

ma = 0
mi = 10 ** 10

while n > 0:
    v = n % 10
    # if v > ma:
    #     ma = v
    ma = max(ma, v)

    if v < mi:
        mi = v
    n //= 10

print(ma)
print(mi)
'''


# https://stepik.org/lesson/1309434/step/11?unit=1324550
'''
m = int(input())
for i in range(1 , 10+1):
    # print(m, '*' ,i, '=', m*i)
    print(f'{m} * {i} = {m * i}')
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
n = int(input())
if n > 0:  # if - если 
    print('Положительное')
elif n == 0:  # elif - иначе если 
    print('Равно нулю')
else:  # else - иначе
    print('Отрицательное')
'''

# Пример зачем нужен elif
'''
# x = int(input('x: '))
# y = int(input('y: '))
x, y = -5, 6
if x > 0 and y > 0:
    print('Первая четверть')
elif x < 0 and y > 0:
    print('Вторая четверть')
elif x < 0 and y < 0:
    print('Третья четверть')
elif x > 0 and y < 0:
    print('Четвертая четверть')
else:
    print('Лежит на какой-то оси')

print('Продолжение программы')
'''


# Логические связки: and, or, not, in
'''
flag = True
print(not flag)  # False
print(not(not flag))  # True
'''

# ДЕЛ(х,128) → (¬ДЕЛ(х,А) → ¬ДЕЛ(х,80))
# Вариант 1
'''
def F(x, A):
    return (x % 128 == 0) <= ((x % A != 0) <= (x % 80 != 0))

for A in range(1000, 0, -1):
    flag = True
    for x in range(1, 10_000):
        if F(x, A) == False:
            flag = False
            break
    if flag == True:
        print(A)
        break
'''
# Вариант 2
'''
def F(x, A):
    return (x % 128 == 0) <= ((x % A != 0) <= (x % 80 != 0))

for A in range(1000, 0, -1):
    if all(F(x, A) for x in range(1, 10_000)):
        print(A)
        break
'''
# Вариант 3
'''
print(max([A for A in range(1000, 0, -1) if all( ((x % 128 == 0) <= ((x % A != 0) <= (x % 80 != 0))) for x in range(1, 10_000))]))
'''

'''
M = ['a', 'b', 'c', 'd', 'e']
print('a' in M)  # True
print('a' not in M)  # False
print('m' in M)  # False


a, b, c = 4, 5, 6
if a > 0 and b > 0 and c > 0:
    print('and - Все условия верные')
if a > 0 or b > 0 or c > 0:
    print('or - Хотя бы одно условие верное')


print(True + True + True)  # 3
if (a > 0) + (b > 0) + (c > 0) == 1:
    print('Только одно условие выполнилось')
if (a > 0) + (b > 0) + (c > 0) == 2:
    print('Только два условия выполнилось')
if (a > 0) + (b > 0) + (c > 0) == 3:
    print('Все три условия выполнились')
if (a > 0) + (b > 0) + (c > 0) >= 2:
    print('Не менее двух условий верны')
if (a > 0) + (b > 0) + (c > 0) >= 1:
    print('Хотя бы одно условие верно')
'''


# Функция перевода в различные системы счисления из 10-й
'''
alp = sorted('0123456789QWERTYUIOASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r


print(convert(8, 2))  # 1000
print(convert(10**8, 16))  # 5F5E100

print(int('1000'))  # 1000
print(int('1000', 2))  # 8 - перевод из 2-й в 10-ю
print(int('1000', 8))  # 512 - перевод из 8-й в 10-ю
# int() base must be >= 2 and <= 36, or 0
'''


# Бесконечные циклы и операторы: break, continue, exit()
'''
k = 0
while True:
    k += 1
    if k % 2 != 0:
        continue  # - Прерывание итерации (шаг) цикла
    if k == 50_000:
        exit()  # - Прерывает выполнение вообще всей программы
    if k == 100_000:
        break  # - Прерывает выполнение цикла в котором сейчас лежит
    print(k)

print('Продолжаем выполнение программы')
'''


# Короткий пример консольной программы "перевод в различные системы счисления"
'''
from string import digits, ascii_uppercase
alp = digits + ascii_uppercase  # 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ

def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r


while True:
    case = input('\n'
                 'case 1: Перевод из 10-й в b-ю систему \n'
                 'case 2: Перевод из b-й в 10-ю систему \n'
                 'case 3: Перевод из b-й в k-ю систему \n'
                 'case 0: Выход из программы. \n'
                 'case: ')

    if case == '1':
        n = int(input('Введите число для перевода: '))
        b = int(input('Введите систему счисления b: '))
        print(f'Результат перевода числа {n} в {b}-ю систему: {convert(n, b)}')

    elif case == '2':
        b = int(input('Введите систему счисления b: '))
        r = input(f'Введите число в {b}-й системе: ')
        print(f'Результат перевода числа {r} из {b}-й системы: {int(r, b)}')

    elif case == '3':
        pass

    elif case == '0':
        print('Спасибо, что пользовались нашим калькулятором!')
        exit()

    else:
        print('Я понимаю только команды: 1, 2, 3, 0')
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
# на следующем уроке: Ника посмотреть подключение библиотек
