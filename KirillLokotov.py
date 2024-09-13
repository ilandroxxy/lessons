# region Домашка: ************************************************************

'''
a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print("Равносторонний")
elif a != b != c != a:
    print("Разносторонний")
else:
    print("Равнобедренный")
'''

# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************

# Цикл - это некоторое повторяющееся действие

'''
# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']

print(len(M))  # 5 - Функция len() возвращает длину списка (кол-во элементов в нем)

for i in range(5):
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e 
'''

# Простое число: число которое делится на 1 и на само число
'''
print()  # В каждой функции print() содержится переход на новую строку '/n'


for i in range(10):
    print(i, end='*&*')  # 0*&*1*&*2*&*3*&*4*&*5*&*6*&*7*&*8*&*9*&*
print()


def prime(n):
    if n <= 1:
        return False
    for j in range(2, n):
        if n % j == 0:
            return False
    return True


for n in range(1, 100):
    if prime(n):
        print(n, end=' ')
print()

for n in range(1, 100):
    flag = True
    if n == 1:
        flag = False
    for j in range(2, n):  # n = 10
        if n % j == 0:
            flag = False
            break
    if flag == True:
        print(n, end=' ')
'''


# Цикл for, отвечает на вопросы: "повтори n раз", "пробеги числа от a до b"

# range(START, STOP, STEP)
'''
for i in range(10):  # range(START=0, STOP=10-1, STEP=1)
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
print()

for i in range(2, 10):  # range(START=2, STOP=10-1, STEP=1)
    print(i, end=' ')  # 2 3 4 5 6 7 8 9
print()

for i in range(2, 10, 2):  # range(START=2, STOP=10-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8
print()

for i in range(2, 10+1, 2):  # range(START=2, STOP=11-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10
print()

for i in range(10, 0):  # range(START=10, STOP=0-1, STEP=1)
    print(i, end=' ')  #
print()

for i in range(10, 0, -1):  # range(START=10, STOP=0-1, STEP=-1)
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1
print()

# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']

for i in range(len(M)):
    M[i] = M[i] * i
print(M)  # ['', 'b', 'cc', 'ddd', 'eeee']


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


# Цикл while, отвечает на вопросы: "пока условие верно выполняем действие", "бесконечный цикл"
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

# Перевод в различные системы счисления
'''
n = 8
base = 2
R = []
while n > 0:
    R.append(n % base)
    n //= base  # n = n // base
R.reverse()  # R = R[::-1]
print(R)  # [1, 0, 0, 0]
'''

'''
n = 8
base = 2
r = ''
while n > 0:
    r += str(n % base)
    n //= base
r = r[::-1]
print(r)  # 1000
'''


# Перевод из 10_сс в base_сс при base > 10
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
print(alphabet)
# ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
n = int(input('Введите число для перевода: '))
base = int(input('Введите систему счисления: '))
r = ''
while n > 0:
    r += alphabet[n % base]
    n //= base
r = r[::-1]
print(r)  # 1000
'''


# Операторы break, continue, exit()
'''
k = 0
while True:
    k += 1
    if k % 2 != 0:
        continue  # continue - прерывает итерацию (шаг) цикла в которой сейчас находится
    print(k)
    if k == 5000:
        exit()
    if k == 10000:
        break  # break - прерывает цикл в котором сейчас находится
print('Конец программы.')
'''

'''
from string import digits, ascii_uppercase

alphabet = digits + ascii_uppercase
# alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

while True:
    case = input('\n'
                 'case 1: Перевод из 10-й в N-ю систему счисления \n'
                 'case 2: Перевод из N-й в 10-ю систему счисления \n'
                 'case 3: Перевод из N-й в K-ю систему счисления  \n'
                 'case 0: exit() \n'
                 'case: ')

    if case == '1':
        n = int(input('Введите число для перевода: '))
        base = int(input('Введите систему счисления: '))
        r = ''
        while n > 0:
            r += alphabet[n % base]
            n //= base
        r = r[::-1]
        print(f'Результат перевода: {r}')

    elif case == '2':
        pass

    elif case == '3':
        pass

    elif case == '0':
        break
print('Спасибо, что воспользовались нашим калькулятором! ')
'''

# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = []
# КЕГЭ = []
# на следующем уроке:
