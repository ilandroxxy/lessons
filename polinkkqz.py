





# Циклы while и for в python

# Цикл for отвечает на запросы: "поватори n раз", "пробеги от числа А до числа Б"

# range(0, STOP-1, 1)
# range(START, STOP-1, 1)
# range(START, STOP-1, STEP)

'''
for i in range(10):  # повтори 10 раз
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
print()

for i in range(8):
    print(i, end=' ')  # 0 1 2 3 4 5 6 7
print()

for i in range(2, 10):  # пробеги от числа А до числа Б
    print(i, end=' ')  # 2 3 4 5 6 7 8 9
print()

for i in range(2, 10, 2):
    print(i, end=' ')  # 2 4 6 8
print()

for i in range(2, 10+1, 2):
    print(i, end=' ')  # 2 4 6 8 10
print()

for i in range(10, 0, -1):
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1
print()

# С циклами for можно работать и через последовательность

# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']

print(len(M))  # 5 - возвращает длину последовательности M

for i in range(len(M)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e
print()

for i in range(len(M)):
    M[i] = M[i] * i
print(M)  # ['', 'b', 'cc', 'ddd', 'eeee']


# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']

for x in M:
    print(x, end=' ') # a b c d e
print()

for x in M:
    if x in 'ae':
        print(x, end=' ')  # a e
print()
'''


# Цикл while отвечает на запросы: "делать действие, пока условие верное", "бесконечные циклы"

'''
for i in range(2, 10+1, 2):
    print(i, end=' ')  # 2 4 6 8 10
print()

i = 2
while i <= 10:  # пока
    print(i, end=' ')  # 2 4 6 8 10 
    i += 2
print()
'''


# Пример использования цикла while при проверке паролей
'''
password = 'qwerty'
pas = input('Введите пароль: ')
while True:
    if pas == password:
        print('Пароль верный!')
        break  
    else:
        pas = input('Повторите попытку: ')

print('Добро пожаловать!')
'''


# Бесконечные циклы и операторы: break, continue и exit()
'''
k = 0
while True:
    k += 1  # k = k + 1
    if k % 2 == 1:
        continue  # - прерывание итеррации цикла (шага цикла)
    if k == 50_000:
        exit()  # - прерывает выполнение всей программы
    if k == 100_000:
        break  # - прерывает выполнение цикла
    print(k)
print('Вышли из цикла')



# ПОКА УСЛОВИЕ ВЕРНОЕ

k = 0
while k < 10:
    print(k)
'''


# n = 1234
# print(n % 10)  # 4
# n //= 10  # n = 123
# print(n % 10)  # 3
# n //= 10  # n = 12
# print(n % 10)  # 2
# n //= 10  # n = 1

'''
n = int(input())  # 1234
summa = 0
count = 0
total = 1
while n > 0:
    ostat = n % 10  # 4 3 2 1

    summa += ostat  # 0 + 4 + 3 + 2 + 1 = 10
    count += 1  # 1 2 3 4
    total *= ostat  # 1 * 4 * 3 * 2 * 1 =

    n //= 10

print(summa)
print(count)
print(total)
'''