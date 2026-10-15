




# Цикл for отвечает на запросы: "повтори N раз", "Пробеги от А до В"


# Цикл for работает с функцией range()
'''
# range(0, STOP-1, 1)
# range(START, STOP-1)
# range(START, STOP-1, STEP)

for i in range(10):
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
print()

for i in range(10+1):
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9 10
print()

for i in range(2, 10+1):
    print(i, end=' ')  # 2 3 4 5 6 7 8 9 10
print()

for i in range(2, 10+1, 2):
    print(i, end=' ')  # 2 4 6 8 10
print()

for i in range(1, 10+1, 2):
    print(i, end=' ')  # 1 3 5 7 9
print()

for i in range(10, 0):
    print(i, end=' ')  # ...
print()

for i in range(10, 0, -1):
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1
print()


for i in range(5):  # "повтори N раз"
    print('Hello, world! ')
    # Hello, world!
    # Hello, world!
    # Hello, world!
    # Hello, world!
    # Hello, world!
'''

# А также цикл for работает с последовательностями
'''
# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']

# i  01234
s = 'abcde'



for x in M:
    print(x, end=' ')  # a b c d e
print()

s = '23iu4h23iu4h'
for x in s:
    print(x, end=' ')  # 2 3 i u 4 h 2 3 i u 4 h
print()

for x in s:
    if x in '0123456789':
        print(x, end=' ')  # 2 3 4 2 3 4
print()


print(len(M), len(s))  # 5 5


for i in range(len(M)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e
print()


for i in range(len(M)):
    M[i] = M[i] * i
print(M)  # ['', 'b', 'cc', 'ddd', 'eeee']
'''

# Цикл while отвечает на запросы: "ПОКА условие верное, делай действие", "бесконечный цикл"
'''
for i in range(2, 10+1, 2):
    print(i, end=' ')  # 2 4 6 8 10
print()

i = 2
while i <= 10:
    print(i, end=' ')
    i += 2
print()
'''

'''
n = 423908
summa = 0
while n > 0:
    summa += (n % 10)
    n //= 10
print(summa)  # 26
'''



# Бесконечный цикл и оперторы break, continue, exit()
'''
k = 0
while True:
    k += 1
    if k % 2 != 0:
        continue  # Прерывает выполнение итерации цикла (шага) 
    if k == 50_000:
        exit()  # Прерывает выполнение всей программы
    if k == 100_000:
        break  # Прерывает выполнение цикла в котором лежит
    print(k)
print('Конец работы цикла')
'''


'''
from random import randint
from time import sleep

password = 'qwerty'
count = 1
pas = input('Введите пароль: ')
while True:
    count += 1
    if pas == password:
        print('Пароль верный. ')
        break
    else:
        pas = input('Повторите попытку: ')
        if count == 3:
            print('Слишком много попыток: пройдите проверку на робота: ')
            a = randint(10, 100)
            b = randint(10, 100)
            x = int(input(f'Решите пример: {a} + {b} = '))
            if x == a + b:
                print('Проверка пройдена успешно.')
                count = 1
            else:
                print('Попробуйте через 5 минут.')
                sleep(5 * 60)

print('Добро пожаловать!')
'''


'''
n = 8

print(bin(n))  # 0b1000
print(bin(n)[2:])  # 0b1000

n = 10**8
print(bin(n)[2:])  # 101111101011110000100000000
print(int('101111101011110000100000000', 2))  # 100000000

print(oct(n)[2:])  # 575360400
print(int('575360400', 8))  # 100000000

print(hex(n)[2:])  # 5f5e100
print(int('5f5e100', 16))  # 100000000

# ValueError: int() base must be >= 2 and <= 36, or 0


n = 8
b = 2
while n > 0:
    r = n % b
    print(r, end=' ')  # 0 0 0 1
    n //= b
print()
'''


# Пробегите числа от 20 до 250 включительно и найдите все числа кратыне 3

for i in range(20, 250+1):
    if i % 3 == 0:
        print(i, end=' ')
print()


for i in range(21, 250+1, 3):
    print(i, end=' ')
print()

for x in range(5, 100, 5):
    print(x, end=' ')  # 5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95
print()





























