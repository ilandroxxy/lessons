# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# i  01234
s = 'abcde'

print(f'Первый элемент строки s: {s[0]}')
print(f'Последний элемент строки s: {s[-1]}')

# Срезы строк
'''
print(s[2:4])  # cd
print(s[:4])  # abcd
print(s[2:])  # cde
print(s[0::2])  # ace
print(s[1::2])  # bd
print(s[::-1])  # edcba
print(s[1:-1])  # bcd - все элементы кроме первого и последнего 
'''


# Функции строк:
'''
s = '122233345'
print(len(s))   # 9 - Возвращает длину строки
print(min(s), max(s))  # 1 5
print(max('aAbB'))  # a
print(sorted(s))  # ['1', '2', '3', '4', '5']
print(sorted(s, reverse=True))  # ['1', '2', '3', '4', '5']
print(set(s))  # {'3', '4', '2', '5', '1'}
print(eval('((2+2) * 5) / 2'))  # 10.0 - решает арифметические примеры
'''


# Методы строк
'''
s = 'jiUHkjikIHiu'
print(s.lower())  # jiuhkjikihiu
print(s.upper())  # JIUHKJIKIHIU

s = '1231253213213'
s = s.replace('2', '*')  # Заменить все '2' на '*' разом
print(s)  # 1*31*53*13*13

s = s.replace('*', '+', 3)  # Заменить только первые три '*' на '+'
print(s)  # 1+31+53+13*13
'''

'''
id = '45.87.234.255'
print(id.split('.'))  # ['45', '87', '234', '255'] - Разбить строку на список по символу '.'
print(id.split('4'))  # ['', '5.87.23', '.255']

s = '34 57  897  34    123'
print(s.split(' '))  # ['34', '57', '', '897', '', '34', '', '', '', '123']
print(s.split())  # ['34', '57', '897', '34', '123']

M = ['34', '57', '897', '34', '123']
new_s = ''.join(M)
print(new_s)  # 345789734123

new_s = ','.join(M)
print(new_s)  # 34,57,897,34,123

new_s = '***'.join(M)
print(new_s)  # 34***57***897***34***123
'''


# Работа с циклами
'''
for i in range(len(s)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(s[i], end=' ')  # a b c d e
print()

for x in s:
    print(x, end=' ')  # a b c d e
print()
'''


# Задание 12 https://education.yandex.ru/ege/task/0a80339b-a1c9-4b63-8e60-313bc5ef8710
# ПОКА нашлось(0) ИЛИ нашлось(01)
#    ЕСЛИ нашлось(01)
#       ТО заменить(01, 10)
#    ИНАЧЕ заменить(0, 111)
'''
s = '0' + '1' * 45
while '0' in s or '01' in s:
    if '01' in s:
        s = s.replace('01', '10', 1)
    else:
        s = s.replace('0', '111', 1)
print(s)  # 111111111111111111111111111111111111111111111111
print(s.count('1'))  # 48
'''


'''
for n in range(1, 1000):
    s = '3' * 15 + '2' * 18 + '1' * n

    while '31' in s or '33' in s or '21' in s:
        if '31' in s:
            s = s.replace('31', '123', 1)
        if '33' in s:
            s = s.replace('33', '211', 1)
        if '21' in s:
            s = s.replace('21', '1', 1)
    summa = sum([int(x) for x in s])
    if summa > 24:
        print(n)
        break
'''

# https://education.yandex.ru/ege/task/56888dcf-39cf-4282-8bf7-5fec144e945c
'''
maxi = 0
for n in range(4, 10000):
    s = '3' + '5' * n

    while '333' in s or '555' in s:
        if '555' in s:
            s = s.replace('555', '3', 1)
        else:
            s = s.replace('333', '5', 1)

    summa = sum([int(x) for x in s])
    if maxi < summa:
        maxi = summa
        print(maxi)
'''


# https://education.yandex.ru/ege/task/b3c1add0-9671-42f4-b405-20b7927c3234
'''
for n in range(10, 1000):
    s = '3' + '5' * n

    while '25' in s or '355' in s or '555' in s:
        if '25' in s:
            s = s.replace('25', '32', 1)
        if '355' in s:
            s = s.replace('355', '25', 1)
        if '555'in s:
            s = s.replace('555', '3', 1)
    summa = sum([int(x) for x in s])
    if summa % 25 == 0:
        print(n)
        break
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 12, 14]
# КЕГЭ  = []
# на следующем уроке:
