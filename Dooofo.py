


# Условные оператры if, elif, else (ветвление)

'''
n = int(input('n: '))
if n > 0:  # если
    print('Число положительное')
elif n < 0:  # иначе если
    print('Число отрицательное')
else:  # иначе
    print('Число равно 0')
'''


# x = int(input('x: '))
# y = int(input('y: '))
'''
x, y = -5, -5
if x > 0 and y > 0:
    print('Первая четверть')
elif x < 0 and y < 0:
    print('Третья четверть')
elif x < 0 and y > 0:
    print('Вторая четверть')
elif x > 0 and y < 0:
    print('Четвертая четверть')
else:
    print('Лежит на осях')
print('Конец программы')
'''


# Логические связки: and, or, not, in, not in, ==, !=
'''
a, b, c = 5, 6, 5

print(a == c)  # True
print(a != c)  # False

print(True + True + False + True)  #

if a > 0 and b > 0 and c > 0:
    print('AND - выполняются все описанные условия')
if a > 0 or b > 0 or c > 0:
    print('OR - хотя бы одно условие выполняется')


if (a > 0) + (b > 0) + (c > 0) == 3:
    print('Выполняются все описанные условия')
if (a > 0) + (b > 0) + (c > 0) >= 1:
    print('Xотя бы одно условие выполняется')
if (a > 0) + (b > 0) + (c > 0) == 1:
    print('Только одно условие')
if (a > 0) + (b > 0) + (c > 0) <= 2:
    print('Не более двух условий')


flag = True
print(not flag)  # False
print(not( not flag))  # True


s = '2r5f356rf23r65432'
for x in s:
    print(x, end=' ')  # 2 r 5 f 3 5 6 r f 2 3 r 6 5 4 3 2
print()

for x in s:
    if x in '0123456789':
        print(x, end=' ')  # 2 5 3 5 6 2 3 6 5 4 3 2
print()

for x in s:
    if x not in '0123456789':
        print(x, end=' ')  # r f r f r
print()


s = '23409878239847'
summa = 0
for x in s:
    summa += int(x)
print(summa)  # 74


print(sum([int(x) for x in s]))  # 74


s = '234fsdf098782f398wef47'
# print(sum([int(x) for x in s]))  # ValueError: invalid literal for int() with base 10: 'f'


s = '234fsdf098782f398wef47'
print(sum([int(x) for x in s if x in '0123456789']))  # 74
'''


'''
M = ['a', 'b', 'c', 'd', 'e']
for x in M:
    print(x, end=' ')  # a b c d e
print()


M = ['a', 'b', 'c', 'd', 'e']
for i in range(len(M)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e
print()

M = ['a', 'b', 'c', 'd', 'e']
for i in range(len(M)):
    M[i] = M[i] * i
print(M)  # ['', 'b', 'cc', 'ddd', 'eeee']
'''

# Функции списков
'''
M = [1, 2, 2, 3, 3, 3]
print(set(M))  # - Убирает копии
print(len(M))
print(sum(M))
print(max(M), min(M))
print(sorted(M))  # [1, 2, 2, 3, 3, 3]
print(sorted(M, reverse=True))  # [3, 3, 3, 2, 2, 1]
print(sorted(M)[::-1])  # [3, 3, 3, 2, 2, 1]
'''

# Методы списков
'''
M = [1, 2, 2, 3, 3, 3, '3']

M.append(5)
M.append(6)
print(M)  # [1, 2, 2, 3, 3, 3, '3', 5, 6]


M = [1, 2, 2, 3, 3, 3, '3']
M = [0] + M + [5, 6]
print(M)  # M = [0, 1, 2, 2, 3, 3, 3, '3']

print(M.count('3'))  # 1
print(M.count(3))  # 3
'''


# Срезы списковы
'''
# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
# -i -5   -4   -3   -2   -1

print(M[0])  # 'a'

print(M[1:3])  # ['b', 'c']
print(M[1:])  # ['b', 'c', 'd', 'e']
print(M[:3])  # ['a', 'b', 'c']

print(M[1: -1])  # ['b', 'c', 'd']

print(M[:])  # ['a', 'b', 'c', 'd', 'e']
print(M[::])  # ['a', 'b', 'c', 'd', 'e']

print(M[::2])  # ['a', 'c', 'e']
print(M[1::2]) # ['b', 'd']

print(M[::-1])  # ['e', 'd', 'c', 'b', 'a']
'''



# Генераторы списков
'''
print([x for x in range(10)])  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print([x ** 2 for x in range(4, 10)])  # [16, 25, 36, 49, 64, 81]
print([x ** 2 for x in range(10) if x % 2 == 0])  # [0, 4, 16, 36, 64]
'''


# https://stepik.org/lesson/1038670/step/5?unit=1062777

for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied1 = [x for x in M if M.count(x) == 1]
    copied3 = [x for x in M if M.count(x) == 3]
    if len(copied3) == 3 and len(copied1) == 4:
        if sum(copied1) / 4 <= copied3[0]:
            print(sum(M))








