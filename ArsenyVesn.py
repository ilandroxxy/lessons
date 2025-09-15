# region Домашка: ******************************************************************

'''
a = input()
if a in ('Информатика', 'Программирование', 'ИКТ'):
    print('Петя берёт с собой компьютер')
else:
    print('Петя берёт с собой тетрадь')
'''
from time import process_time_ns

# Сочетание клавиш ctrl + alt + L
'''
a = input()
if len(a) >= 10 or len(a) % 2 == 0:
    print('ДА')
else:
    print('НЕТ')
'''

'''
a = int(input())
b = int(input())
if max(a, b) % min(a, b)== 0:
    print('Делится')
else:
    print('Не делится')
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Циклы for отвечает на запросы: "повтори n раз", "пробеги от А до В"

# Цикл for вместе с функцией range()
'''
# range(0, STOP-1, 1)
# range(START, STOP-1, 1)
# range(START, STOP-1, STEP)

for i in range(10):
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
print()

for i in range(2, 10):
    print(i, end=' ')  # 2 3 4 5 6 7 8 9
print()

for i in range(2, 10, 2):
    print(i, end=' ')  # 2 4 6 8
print()

n = 10
for i in range(2, n+1, 2):
    print(i, end=' ')  # 2 4 6 8 10
print()


for i in range(10, -1, -1):
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1 0
print()
'''

# Цикл for вместе с последовательностями
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


for i in range(len(M)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e
print()


for i in range(len(M)):
    M[i] = M[i] * i
print(M)  # ['', 'b', 'cc', 'ddd', 'eeee']
'''


# Циклы while отвечает на запросы: "Пока условие верное - делай действие", "Бесконечные циклы"

'''
for i in range(2, 10+1, 2):
    print(i, end=' ')  # 2 4 6 8 10
print()

i = 2
while i <= 10:
    print(i, end=' ')  # 2 4 6 8 10
    i += 2
print()
'''


# Переводы в различные системы счисления
'''
n = 10000

# Перевод в двоичную систему счисления
print(bin(n)[2:])  # 10011100010000
print(f'{n:b}')  # 10011100010000

# Перевод из двоичной в 10-ю
print(int('10011100010000', 2))  # 10000
# ValueError: int() base must be >= 2 and <= 36, or 0



# Перевод в восьмеричную систему счисления
print(oct(n)[2:])  # 23420
print(f'{n:o}')  # 23420

# Перевод из восьмеричной в 10-ю
print(int('23420', 8))  # 10000



# Перевод в шестнадцатеричную систему счисления
print(hex(n)[2:])  # 2710
print(f'{n:x}')  # 2710

# Перевод из шестнадцатеричной в 10-ю
print(int('2710', 16))  # 10000
'''

'''
n = 8
b = 2
r = ''
while n > 0:
    r = r + str(n % b)
    n //= b
print(r[::-1])  # 1000



n = 8
b = 2
r = ''
while n > 0:
    r = str(n % b) + r
    n //= b
print(r)

alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r

x = convert(8, 2)
print(x)  # 1000

x = convert(8, 8)
print(x)  # 10

x = convert(10**6, 16)
print(x)  # F4240
'''


# Бесконечный цикл и операторы: break, continue, exit()
'''
k = 0
while True:
    k += 1
    if k % 2 != 0:
        continue   # Прерывает итерацию (шаг) цикла
    if k == 50_000:
        exit()  # Прерывание всей программы
    if k == 100_000:
        break  # Прерывание цикла в котором сейчас находимся
    print(k)

print('Продолжение программы')
'''


# Простая програмка переводов в различные системы счисления
'''
from string import digits, ascii_uppercase

alp = digits + ascii_uppercase  # '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r


while True:
    case = input('\n\n'
                 'case 1: Перевод из 10-й в b-ю систему \n'
                 'case 2: Перевод из b-й в 10-ю систему \n'
                 'case 3: Перевод из b-й в k-ю систему \n'
                 'case 0: Выход из программы. \n'
                 'case: ')

    if case == '1':
        n = int(input('\nВведите число в 10-й системе: '))
        b = int(input('Введите систему счисления: '))
        r = convert(n, b)
        print(f'Результат перевода числа {n} в {b}-ю систему: {r}')

    elif case == '2':
        b = int(input('\nВведите систему счисления: '))
        r = input(f'Введите число в {b}-й системе: ')
        n = int(r, b)
        print(f'Результат перевода числа {r} из {b}-й системы в 10-ю: {n}')

    elif case == '3':
        pass

    elif case == '0':
        print('Спасибо, что пользовались нашей программой!')
        exit()

    else:
        print('Я понимаю только команды: 0, 1, 2, 3')
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
# на следующем уроке:
