# region Домашка: ******************************************************************

'''
x = -123

# abs() - функция модуля числа (убирает знак минус)
if abs(x) % 10 == 3:
    print('Yes')
else:
    print('No')


print(123 % 10)  # 3
print(-123 % 10)  # 7
'''


'''
a = int(input())
L = [int(x) for x in str(a)]
if L[0] * L[2] == L[1] + L[3] + L[4]:
    print('Да')
else:
    print('Нет')
'''

# Вычисление суммы чисел по определенным условиям
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


# Разработка программы для определения вида треугольника
'''
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print("Равносторонний")
elif a != b and a != c and b != c:
    print("Разносторонний")
else:
    print("Равнобедренный")
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Цикл for отвечает на запросы: "повтори N раз", "пробеги от A до B"


# Работа цикла for с функцией range()
# range(STOP), range(START, STOP), range(START, STOP, STEP)
'''
for i in range(10):  # range(START=0, STOP=10-1, STEP=1)
    print(i, end=' ')   # 0 1 2 3 4 5 6 7 8 9
print()

for i in range(2, 10):  # range(START=2, STOP=10-1, STEP=1)
    print(i, end=' ')   # 2 3 4 5 6 7 8 9
print()

for i in range(2, 10, 2):  # range(START=2, STOP=10-1, STEP=2)
    print(i, end=' ')   # 2 4 6 8
print()

for i in range(2, 10+1, 2):  # range(START=2, STOP=11-1, STEP=2)
    print(i, end=' ')   # 2 4 6 8 10
print()

for i in range(10, 0):  # range(START=10, STOP=0-1, STEP=1)
    print(i, end=' ')   # нет вывода
print()

for i in range(10, 0, -1):  # range(START=10, STOP=0-1, STEP=-1)
    print(i, end=' ')   # 10 9 8 7 6 5 4 3 2 1
print()


# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']

print(len(M))  # 5 Функция len() возвращает длину списка (кол-во элементов в нем)

for i in range(len(M)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e
print()

for i in range(len(M)):
    M[i] = M[i] * i
print(M)  # ['', 'b', 'cc', 'ddd', 'eeee']
'''

# Цикл for может работать с последовательностями напрямую
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

# Работа с строками и словарями через цикл for
'''
s = 'abcde'  # str
for i in range(len(s)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(s[i], end=' ')  # a b c d e
print()

my_dict = {'один': 'one', 'два': 'two', 'три': 'three'}
print(my_dict.items())

for elem in my_dict.items():
    print(elem)
    # ('один', 'one')
    # ('два', 'two')
    # ('три', 'three')

for key, value in my_dict.items():
    print(key, value)
    # один one
    # два two
    # три three
'''


# Цикл while отвечает на запросы: "повторяй действия пока условие верно", "бесконечный цикл"
'''
for i in range(2, 10+1, 2):  # range(START=2, STOP=11-1, STEP=2)
    print(i, end=' ')   # 2 4 6 8 10
print()

i = 2
while i <= 10:
    print(i, end=' ')  # 2 4 6 8 10
    i += 2
print()

n = 8  # number
b = 2  # base system
res = ''
while n > 0:
    res += str(n % b)
    n //= b
res = res[::-1]  # Срез в обратном порядке
print(res)

n = 8  # number
b = 2  # base system
res = ''
while n > 0:
    res = str(n % b) + res
    n //= b
print(res)

# Срез в обратном порядке
s = 'abcde'
print(s[::-1])  # edcba
'''

'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    res = ''
    while n > 0:
        res = alphabet[n % b] + res
        n //= b
    return res


n = int(input('n: '))
b = int(input('b: '))
# Пример вызова функции:
print(convert(n, b))
'''

'''
k = 0
while True:
    k += 1
    print(k)
'''

from string import digits, ascii_uppercase
from time import sleep


alphabet = digits + ascii_uppercase  # 0123456789 + ABCDEFGHIJKLMNOPQRSTUVWXYZ
# alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')


def convert(n: int, b: int) -> str:
    """
    Функция для перевода из 10-ой в любую другую систему счисления
    :param n: Принимает число в 10-ой системе счисления
    :param b: Принимает систему счисления для перевода
    :return: Возвращает результат перевода в b-ую систему счисления
    """
    res = ''
    while n > 0:
        res = alphabet[n % b] + res
        n //= b
    return res


if __name__ == '__main__':
    while True:
        case = input('\n'
                     'case 1: Перевод из 10-й в N-ную систему счисления. \n'
                     'case 2: Перевод из N-й в 10-ную систему счисления. \n'
                     'case 3: Перевод из N-й в К-ную систему счисления. \n'
                     'case 0: Выход из программы. \n'
                     'case: ')

        if case == '1':
            n = int(input('Введите число в 10-ой системе счисления для перевода: '))
            b = int(input('Введите систему в которую хотим делать перевод: '))
            print(f'Результат перевода 10-го числа {n} в {b}-ую систему счисления: {convert(n, b)} \n')
            sleep(3)

        elif case == '2':
            b = int(input('Введите систему из которой хотим делать перевод: '))
            r = input(f'Введите число в {b}-ой системе счисления для перевода в 10-ую: ')
            print(f'Результат перевода {b}-го числа {b} в 10-ую систему счисления: {int(r, b)} \n')
            sleep(3)

        elif case == '3':
            sleep(3)
            pass

        elif case == '0':
            print('Спасибо, что воспользовались нашим калькулятором!')
            sleep(3)
            break

        else:
            print('Эта команда мне неизвестная, воспользуйтесь кнопками 1, 2, 3, 0')


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
