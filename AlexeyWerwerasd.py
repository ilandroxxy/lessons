# region Домашка: ************************************************************

'''
x = int(input())
if x % 2 == 0:
    print('Чётное')
else:
    print('Нечётное')
'''

'''
number = input()  # str

if len(number) != 5:    # str != int
    print("Вы ввели не пятизначное число")
else:
    first = int(number[0])
    second = int(number[1])
    third = int(number[2])
    fourth = int(number[3])
    fifth = int(number[4])

    if first * third == second + fourth + fifth:
        print("Да")
    else:
        print("Нет")
'''

'''
number = int(input())

if 10000 <= number <= 99999: 
    number = str(number)
    first = int(number[0])
    second = int(number[1])
    third = int(number[2])
    fourth = int(number[3])
    fifth = int(number[4])

    if first * third == second + fourth + fifth:
        print("Да")
    else:
        print("Нет")
else:
    print("Вы ввели не пятизначное число")
'''

'''
num1 = int(input())
num2 = int(input())
num3 = int(input())

summa = 0

if num1 % 7 == 0 and num1 % 49 != 0 or num1 % 40 == 0:
    summa += num1

if num2 % 7 == 0 and num2 % 49 != 0 or num2 % 40 == 0:
    summa += num2

if num3 % 7 == 0 and num3 % 49 != 0 or num3 % 40 == 0:
    summa += num3

print(summa)
'''

# endregion Домашка: *********************************************************
#
# #
# region Урок: ************************************************************

# Цикл - это какое-либо повторяющееся действие

# Цикл for: отвечает на запросы: "повтори n раз", "пробеги от a до b"

# Работа с циклом for через функцию range:
'''
for i in range(10):  # range(START=0, STOP=10-1, STEP=1)
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
print()


for i in range(2, 10):  # range(START=2, STOP=10-1, STEP=1)
    print(i, end=' ')  # 2 3 4 5 6 7 8 9
print()


for i in range(2, 10, 2):  # range(START=2, STOP=10-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 - все четные числа (кратные 2)
print()


for i in range(1, 10, 2):  # range(START=1, STOP=10-1, STEP=2)
    print(i, end=' ')  # 1 3 5 7 9 - все нечетные числа (не кратные 2)
print()


for i in range(2, 10+1, 2):  # range(START=2, STOP=11-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10 - все четные числа (кратные 2)
print()


for i in range(10, 0):  # range(START=10, STOP=0-1, STEP=1)
    print(i, end=' ')  #
print()


for i in range(10, 0, -1):  # range(START=10, STOP=0-1, STEP=-1)
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1
print()


# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']

print(M[2])  # c
print(len(M))   # 5 - len() возвращает длину списка, то есть кол-во элементов в нем

for i in range(len(M)):  # range(START=0, STOP=5-1, STEP=1)
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e
print()


for i in range(len(M)):
    M[i] = M[i]
print(M)  # ['a', 'b', 'c', 'd', 'e']


for i in range(len(M)):
    M[i] = M[i] * i
print(M)  # ['', 'b', 'cc', 'ddd', 'eeee']
'''

# Работа с циклом for напрямую через элементы последовательности:
'''
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

# Цикл while: отвечает на запросы: "пока условие верно, повторяй действие", "бесконечные циклы"
'''
for i in range(2, 10+1, 2):  # range(START=2, STOP=11-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10 - все четные числа (кратные 2)
print()


i = 2
while i <= 10:
    print(i, end=' ')  # 2 4 6 8 10
    i += 2
'''

#  Перевод в base систему счисления

'''
num = 8
base = 2
r = ''
while num > 0:
    r += str(num % base)
    num //= base
r = r[::-1]
print(r)
'''

'''
num = int(input('Введите число в 10-й система для перевода: '))
base = int(input('Введите base систему счисления: '))
r = ''
while num > 0:
    r = str(num % base) + r
    num //= base
print(r)
'''


'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLXZCVBNM')
num = int(input('Введите число в 10-й система для перевода: '))
base = int(input('Введите base систему счисления: '))
r = ''
while num > 0:
    r = alphabet[num % base] + r
    num //= base
print(r)
'''


# Бесконечные циклы и операторы: break, continue, exit()

'''
cnt = 0
while True:
    cnt += 1
    if cnt % 2 != 0:
        continue  # - прерывает итерацию (шаг) цикла
    if cnt == 10000:
        exit()  # - просто прерывает всю программу
        break  # - прерывает цикл в котором он находится
    print(cnt)
print('Конец программы.')
'''

'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLXZCVBNM')
while True:
    case = int(input('\ncase 1: Перевод из 10-й в base систему счисления. \n'
                     'case 2: Перевод из base системы счисления в 10-ю. \n'
                     'case 3: Перевод из base системы счисления в n-ю. \n'
                     'case 0: exit \n'))

    if case == 1:
        num = int(input('Введите число в 10-й система для перевода: '))
        base = int(input('Введите base систему счисления: '))
        r = ''
        while num > 0:
            r = alphabet[num % base] + r
            num //= base
        print(f'Результат перевода: {r}')

    elif case == 2:
        base = int(input('Введите base систему счисления: '))
        r = input(f'Введите число в {base} системе счисления: ')
        print(f'Результат перевода: {int(r, base)}')

    elif case == 3:
        pass

    elif case == 0:
        print('Конец программы. ')
        exit()

    else:
        print('Неверная команда.')
'''

# ********************************************
'''
x = 19
print(x % 10)  # 9
x = -19
print(x % 10)  # 1


a = int(input())
b = int(input())

for i in range(a,b):
    if i % 20 == 0 or (i % 7 == 0 and i % 14 == 0) or abs(i) % 10 == 9:
        print(i)
'''

'''
s = '1234567890QWERTYUIOPASDFGHJKLZXCVBNM'
print(sorted(s))
# ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
'''

'''
n = int(input())  # 12345
summa = 0
count = 0
prodd = 1
while n > 0:
    x = n % 10
    summa += x
    count += 1
    prodd *= x
    n //= 10
print(summa)
print(count)
print(prodd)
'''

# № 16368 ЕГКР 27.04.24 (Уровень: Базовый)
# Миша заполнял таблицу истинности логической функции F=¬(x∨y)∧¬w∨¬(z∨w)∧y
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (not(x or y)) and (not w) or (not(z or w)) and y
                if F == 1:
                    print(x, y, z, w)
'''


# № 14651 Открытый курс "Слово пацана" (Уровень: Базовый)
# Логическая функция F задаётся выражением ((z→x)≡(w→y)∨(x∧w)).
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((z <= x) == (w <= y) or (x and w))
                if F == 0:
                    print(x, y, z, w)
'''

# КЕГЭ № 6598 Пробник ИМЦ СПб (Уровень: Базовый)
# Логическая функция F задаётся выражением ((x → w) ∧ (¬y → z)) → ((z ≡ x) ∨ (w ∧ ¬y)).
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((x <= w) and ((not y) <= z)) <= ((z == x) or (w and (not y)))
                if F == 0:
                    print(x, y, z, w)
'''

# Решу ЕГЭ № 18483 (Уровень: Базовый)
# Логическая функция F задаётся выражением ((y → w) ≡ (x → ¬z)) ∧ (x ∨ w).

print('x y z w F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((y <= w) == (x <= (not z))) and (x or w)
                if F == 0:
                    print(x, y, z, w, int(F))


for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((y <= w) == (x <= (not z))) and (x or w)
                if F == 1:
                    print(x, y, z, w, int(F))
# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# ФИПИ = [2]
# КЕГЭ = []
# на следующем уроке:
