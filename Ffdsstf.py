







# Цикл for отвечает на запросы: "пробеги от числа А до числа Б", "Повторите N раз"
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

for i in range(2, 10+1, 2):
    print(i, end=' ')  # 2 4 6 8 10
print()

for i in range(1, 10+1, 2):
    print(i, end=' ')  # 1 3 5 7 9
print()

for i in range(10-1, 0-1, -1):  # 9 8 7 6 5 4 3 2 1 0
    print(i, end=' ')
print()

for i in range(5):
    print('Hello, world!')
    # Hello, world!
    # Hello, world!
    # Hello, world!
    # Hello, world!
    # Hello, world!


# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
print(len(M))  # 5


for x in M:
    print(x, end=' ')  # a b c d e
print()

for x in M:
    if x in 'ae':
        print(x, end=' ')
print()  # a e


for i in range(len(M)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e
print()


for i in range(len(M)):
    M[i] = M[i] * i
print(M)  # ['', 'b', 'cc', 'ddd', 'eeee']
'''



# Цикл while отвечает на запросы: "Пока условие верное - делаем действие", "Бесконечный цикл"
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


# Бесконечные циклы и операторы: break, continue, exit()
'''
k = 0
while True:
    k += 1
    if k % 2 != 0:
        continue  # Прерывает итеррацию цикла (шаг цикла)
    if k == 50_000:
        break  # Прерывание выполнения цикла
    if k == 100_000:  # Полностью прерывали выполнение программы
        exit()
    print(k)
print('Конец выполнения программы')
'''


# Пример использования бесконечныйх циклов
'''
from random import randint
from time import sleep

password = 'qwerty'
pas = input('Введите пароль: ')
count = 0
while True:
    if pas == password:
        print('Пароль верный. ')
        break
    count += 1
    if count == 3:
        a = randint(0, 100)
        b = randint(0, 100)
        x = int(input(f'Пройдите проверку на робота: {a} + {b} = '))
        if x == a + b:
            count = 0
            print('Проверка пройдена успешно.')
        else:
            print('Повторите попытку через 5 минут.')
            sleep(5 * 60)
    pas = input('Пароль неверный, повторите попытку: ')

print('Добро пожаловать!')
'''



# Перевод в различные системы счисления
'''
n = 10000
print(bin(n))   # 0b10011100010000
print(bin(n)[2:])   # 10011100010000
print(oct(n)[2:])   # 23420
print(hex(n)[2:])   # 2710

print(hex(10**8)[2:])  # 5f5e100

print(int('5f5e100', 16))  # 100000000
print(int('1000', 2))  # 8 - обратный перевод из любой b-й системы в 10-ю


n = 10000
print(f'{n:b}')  # 10011100010000
print(f'{n:o}')  # 23420
print(f'{n:x}')  # 2710
'''


# № 31502 Демоверсия 2027(Уровень: Базовый)
#
# На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом.
# 1. Строится двоичная запись числа N.
# 2. Далее эта запись обрабатывается по следующему правилу:
# а) если число N чётное, то к этой записи справа и слева дописываются по две единицы;
# б) если число N нечётное, то в конец двоичной записи (справа) дописываются два нуля,
# а в начало (слева) дописывается единица.
# 3. Результат переводится в десятичную систему и выводится на экран.

# Укажите наименьшее число R, превышающее 95, которое может быть результатом работы данного алгоритма.
# В ответе запишите это число в десятичной системе счисления.
'''
RES = []
for n in range(1, 10000):
    n2 = bin(n)[2:]
    if n % 2 == 0:
        n2 = '11' + n2 + '11'
    else:
        n2 = '1' + n2 + '00'
    r = int(n2, 2)
    if r > 95:
        RES.append(r)
print(min(RES))
'''

alp = sorted(set('01223456789QWERTYUIOPASDFGHJKLZXCVBBNM'))
def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

print(convert(8, 2))  # 1000
print(convert(10**8, 16))  # 5F5E100

print(int('5F5E100', 16))  # 100000000
# ValueError: int() base must be >= 2 and <= 36, or 0
















