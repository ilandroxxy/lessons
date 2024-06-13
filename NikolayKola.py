# region Домашка: ******************************************************************

# Три числа - три действия
'''
a = input()
b = input()
c = input()

print('razn a,b  ^', int(a) - int(b))

print('summ a,c  ^', int(a) + int(c))

print('ostat a,b  ^', int(a) % int(b))


a = int(input())
b = int(input())
c = int(input())

print(a - b)
print(a + b)
print(a % b)
'''

'''
a = (input(('число пятизначное целое')))
b = [int(a) for i in a]
print(b[0] * b[1] * b[2] * b[3] * b[4])
print('произведение   ^')
print(sum(b))
print('сумма   ^')
'''
# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Циклы for и while

# for: "Повтори n раз", "Пробеги числа от a до b"

# Цикл for - работа с функцией range():
'''
for i in range(10):  # range(START=0, STOP=10-1, STEP=1)
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
print()

for i in range(2, 10):  # range(START=2, STOP=10-1, STEP=1)
    print(i, end=' ')  # 2 3 4 5 6 7 8 9
print()

for i in range(2, 10, 2):  # range(START=2, STOP=10-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8
print()  # Все числа кратные 2, Все четные числа

for i in range(2, 10+1, 2):  # range(START=2, STOP=11-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10
print()

for i in range(10, 0, -1):
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1
print()


# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']

for i in range(len(M)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e
print()

# Через индексы мы можем изменять элементы списка
for i in range(len(M)):
    M[i] = M[i] * i
print(M)  # ['', 'b', 'cc', 'ddd', 'eeee']
'''

# Цикл for - работа с последовательностями:
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

# while: "Пока условие верно, делай действие", "Бесконечные циклы"

for i in range(2, 10+1, 2):  # range(START=2, STOP=11-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10
print()

i = 2
while i <= 10:
    print(i, end=' ')  # 2 4 6 8 10
    i += 2
print()

# 14 17555
'''
for x in range(0, 2030+1):
    n = 7**91 + 7**160 - x
    M = []  # сюда будем складывать остатки от деления
    while n > 0:
        M.append(n % 7)
        n //= 7
    M.reverse()
    if M.count(0) == 70:
        print(x)

# '20202020'.count('0') = 4  [20, 20, 20, 20].count(0) == 0

for x in range(0, 2030+1):
    n = 7**91 + 7**160 - x
    s = ''  # сюда будем складывать остатки от деления
    while n > 0:
        s += str(n % 7)
        n //= 7
    s = s[::-1]
    if s.count('0') == 70:
        print(x)
'''


# Бесконечный цикл while
'''
k = 0
while True:
    k += 1
    print(k)
'''
'''
while True:
    case = int(input('case 1:  ...\n'
                     'case 2: ... \n'
                     'case 3: ... \n'
                     'case 0: exit \n'))
    if case == 1:
        pass

    if case == 2:
        pass

    if case == 3:
        pass

    if case == 0:
        exit()
'''


# continue и break
'''
for i in range(0, 50, 2):
    print(i, end=' ')
print()

for i in range(0, 50, 2):
    if i % 2 != 0:
        continue  # Прерывает итерацию цикла (шаг)
        print('HELLO')
    if i == 30:
        print('КОНЕЦ')
        break  # Прерывает цикл
        print('КОНЕЦ')  # До сюдого мы не успеем дойти
    print(i, end=' ')
print()
'''

# КЕГЭ № 6598 Пробник ИМЦ СПб (Уровень: Базовый)
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

'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (x and (not y)) or (y == z) or (not w)
                if F == 0:
                    print(x, y, z, w)
'''

'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((y and (x == (not z))) <= w) and (z <= y)
                if F == 0:
                    print(x, y, z, w)
'''

'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (x or (not y)) and z and (not w)
                if F == 1:
                    print(x, y, z, w)
'''


print('x y z w F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((y <= w) == (x <= (not z))) and (x or w)
                print(x, y, z, w, int(F))

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2*, 3, 4, 6, 7, 9*, 10, 11, 18, 19-21]
# КЕГЭ  = [2]
# на следующем уроке:
