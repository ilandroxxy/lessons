


# Проверка длины слова
'''
s = input()
if len(s) >= 10 or len(s) % 2 == 0:
    print('ДА')
else:
    print('НЕТ')
'''


# Проверка возможности образования треугольника
'''
a = int(input())
b = int(input())
c = int(input())

if a < b + c and b < a + c and c < a + b:
    print('ДА')
else:
    print('НЕТ')
'''


# Цикл for отвечает на запросы: "повтори N раз", "пробеги от А до В"

# Цикл for работает через функцию range()

# range(0, STOP-1, 1)
# range(START, STOP-1, 1)
# range(START, STOP-1, STEP)

for i in range(10):  # 0 1 2 3 4 5 6 7 8 9
    print(i, end=' ')
print()

for i in range(2, 10):  # 2 3 4 5 6 7 8 9
    print(i, end=' ')
print()

for i in range(2, 10, 2):  # 2 4 6 8
    print(i, end=' ')
print()

for i in range(2, 10+1, 2):  # 2 4 6 8 10
    print(i, end=' ')
print()

for i in range(1, 10+1, 2):  # 1 3 5 7 9
    print(i, end=' ')
print()

for i in range(10, 0):
    print(i, end=' ')
print()

for i in range(10-1, -1, -1):
    print(i, end=' ')  # 9 8 7 6 5 4 3 2 1 0
print()


# Цикл for работает и с последовательностями
'''
# i  01234
s = 'abcde'

s = '84sfd7sfd923'

for x in s:
    print(x, end=' ')  # 8 4 s f d 7 s f d 9 2 3
print()

for x in s:
    if x in '0123456789':
        print(x, end=' ')  # 8 4 7 9 2 3
print()

for x in s:
    if x not in '0123456789':
        print(x, end=' ')  # s f d s f d
print()

# i  0123456789
s = '84sfd7sfd923'
print(len(s))  # 12


r = ''
for i in range(len(s)):
    # print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9 10 11
    print(s[i], end=' ')  # 8 4 s f d 7 s f d 9 2 3
    if s[i] in '0123456789':
        r += s[i]
print()
print(r)  # 847923
'''


# Правильный порядок
'''
a = int(input())
b = int(input())
if a < b:
    for i in range(a, b+1):
        print(i)
else:
    for i in range(a, b-1, -1):
        print(i)
'''


# Числа с условиями

a = int(input())
b = int(input())
for i in range(a, b+1):
    if (i % 20 == 0) and (i % 7 == 0 and i % 14 == 0) and (i % 10 == 9):
        print(i)






# Цикл while отвечает на запросы: "ПОКА условие верное - делаем действие", "бесконечные циклы"


