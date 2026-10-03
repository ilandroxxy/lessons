



# Условные операторы if, elif, else (ветвление)
'''
n = int(input('n: '))
if n > 0:  # if - если
    print('Число положительное')
elif n < 0:  # elif - иначе если
    print('Число отрицательное')
else:  # else - иначе
    print('Число равно 0')
'''

'''
# x = int(input('x: '))
# y = int(input('y: '))
x, y = 5, 0
if x > 0 and y > 0:
    print('Первая четверть')
elif x < 0 and y < 0:
    print('Третья четверть')
elif x < 0 and y > 0:
    print('Вторая четверть')
elif x > 0 and y < 0:
    print('Четвертая четверть')
else:
    print('Число лежит на осях')
print('Программа закончила работу')
'''


# Логические связки: and, or, not, in, not in, ==, !=
'''
a, b, c = 5, 8, 5
print(a == c)  # True
print(a == b)  # False

print(a != c)  # False
print(a != b)  # True

# = - присваивание значения переменной
# == - сравнение двух значений

print(True + True + False + True)  # 3   (1 + 1 + 0 + 1)

if a > 0:
    if b > 0:
        if c > 0:
            print('AND - все условия выполняются')

if a > 0 and b > 0 and c > 0:
    print('AND - все условия выполняются')

if a > 0 or b > 0 or c > 0:
    print('OR - хотя бы одно условие выполняется')

if (a > 0) + (b > 0) + (c > 0) == 3:
    print('Все условия выполнялись')
if (a > 0) + (b > 0) + (c > 0) == 1:
    print('Выполняется только одно условие')
if (a > 0) + (b > 0) + (c > 0) >= 1:
    print('Хотя бы одно условие выполняется')
if (a > 0) + (b > 0) + (c > 0) <= 2:
    print('Не более двух условий выполняется')


flag = True
print(not flag)  # False
print(not(not flag))  # True

s = '34d2rt3df4r32df4rt'
for x in s:
    print(x, end=' ')  # 3 4 d 2 r t 3 d f 4 r 3 2 d f 4 r t
print()

for x in s:
    if x in '0123456789':
        print(x, end=' ')  # 3 4 2 3 4 3 2 4
print()

for x in s:
    if x not in '0123456789':
        print(x, end=' ')  # d r t d f r d f r t
print()


# Поиск суммы цифр строки

s = '2345897249738'
summa = 0
for x in s:
    # summa += int(x)
    summa = summa + int(x)
print(summa)  # 71

# s = '23egrg4589erg724erg9738'
# summa = 0
# for x in s:
#     summa += int(x)
# print(summa)  # ValueError: invalid literal for int() with base 10: 'e'

s = '23egrg4589erg724erg9738'
summa = 0
for x in s:
    if x in '0123456789':
        summa += int(x)
print(summa)  # 71
'''

# https://stepik.org/lesson/1309432/step/6?unit=1324548

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


# На следующем уроке, обговорить циклы и работу с библиотеками 

