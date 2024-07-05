# region Домашка: ******************************************************************

'''
A = input()
print(A)
a = int(A[0])
b = int(A[1])
c = int(A[2])
d = int(A[3])
e = int(A[4])
if (a*c) == (b+d+e):
    print('Да')
else:
    print('Нет')
'''


'''
print(83241 // 100)  # 832
print(83241 % 100)  # 41

# Число n оканчивается на 9
n = int(input('n: '))  # 129
print(n % 10 == 9)  # True
print(-n % 10 == 9)  # False
print(-129 % 10)  # 1
print(abs(-129) % 10)  # 9 – abs() - взятие модуля от числа 
'''

'''
x = int(input())  # 83241
a = x // 10000
b = (x // 1000) % 10
c = (x // 100) % 10
d = (x % 100) // 10
e = x % 10
if (a*c) == (b+d+e):
    print('Да')
else:
    print('Нет')
'''

# print(sum([int(x) for x in input('Введите три числа: ').split() if (int(x) % 7 == 0 and int(x) % 49 != 0) or (int(x) % 40 == 0)]))
# Метод .split() – разбивает строку на список строк (в данном случае по пробелам)

'''
a = int(input())
b = int(input())
if max(a, b) % min(a, b) == 0:
    print('Делится')
else:
    print('Не делится')
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Циклы - это просто повторяющееся действие

# for - отвечает на вопрос: "повтори n раз", "пробеги от a до b"
'''
# Работа с циклом for через функцию range()

for i in range(10):  # range(START=0, STOP=10-1, STEP=1)
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
print()


for i in range(2, 10):  # range(START=2, STOP=10-1, STEP=1)
    print(i, end=' ')  # 2 3 4 5 6 7 8 9
print()

for i in range(2, 10, 2):  # range(START=2, STOP=10-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 – пробежали все четные (или кратные 2) элементы
print()


for i in range(1, 10, 2):  # range(START=2, STOP=10-1, STEP=2)
    print(i, end=' ')  # 1 3 5 7 9  – пробежали все нечетные (или некратные 2) элементы
print()


for i in range(2, 10+1, 2):  # range(START=2, STOP=11-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10
print()

for i in range(10, 0):
    print(i, end=' ')  # пусто
print()

for i in range(10, 0, -1):
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1
print()


# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
print(len(M))  # 5 - Функция len() возвращает длину последовательности

for i in range(len(M)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e
print()


for i in range(len(M)):
    M[i] = M[i]  # ['a', 'b', 'c', 'd', 'e']
print(M)


for i in range(len(M)):
    M[i] = M[i] * i  # ['', 'b', 'cc', 'ddd', 'eeee']
print(M)

# Работа с циклом for напрямую через последовательности

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

# while - отвечает на вопрос: "выполняется пока условие истинно", "бесконечные циклы"
'''
for i in range(2, 10+1, 2):  # range(START=2, STOP=11-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10
print()

i = 2
while i <= 10:
    print(i, end=' ')  # 2 4 6 8 10
    i += 2
print()
'''

alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

n = int(input('Введите 10-е число: '))  # 123456789
b = int(input('Введите base систему счисления: '))  # 16
r = ''
while n > 0:
    r += alphabet[n % b]
    n //= b
r = r[::-1]
print(r)  # 75BCD15





# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = []
# КЕГЭ  = []
# на следующем уроке: Создать учебный репозиторий через github
