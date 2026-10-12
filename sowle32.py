



# Цикл for отвечает на запросы: "Повтори N раз", "Пробеги от числа А до числа В"

# Цикл for работает с функцией range()
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
    print(i, end=' ')  #
print()

for i in range(10, 0-1, -1):
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1 0
print()
'''

# Или цикл for работает с последовательностями
'''
s = 'abcde'
for x in s:
    print(x, end=' ')  # a b c d e
print()

L = ['a', 'b', 'c', 'd', 'e']
for x in L:
    print(x, end=' ')  # a b c d e
print()

s = 'u32h4j2u3hj423ui42'
for x in s:
    print(x, end=' ')  # u 3 2 h 4 j 2 u 3 h j 4 2 3 u i 4 2
print()

s = 'u32h4j2u3hj423ui42'
for x in s:
    if x in '0123456789':
        print(x, end=' ')  # 3 2 4 2 3 4 2 3 4 2
print()

s = 'u32h4j2u3hj423ui42'
for x in s:
    if x in '02468':
        print(x, end=' ')  # 2 4 2 4 2 4 2
print()




# i   0    1    2    3    4
L = ['a', 'b', 'c', 'd', 'e']

print(len(L))  # 5 - Возвращает кол-во элементов

for i in range(len(L)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(L[i], end=' ')  # a b c d e
print()

for i in range(len(L)):
    L[i] = L[i] * i
print(L)  # ['', 'b', 'cc', 'ddd', 'eeee']



# i   0    1    2    3    4
L = ['a', 'b', 'c', 'd', 'e']
for i in range(len(L)):
    if i % 2 == 0:
        L[i] = L[i] * i
    else:
        L[i] = L[i] * 3
print(L)  # ['', 'bbb', 'cc', 'ddd', 'eeee']


s = 'u32h4j2u3hj423ui42'
for x in s:
    if x in '02468':
        print(x, end=' ')  # 2 4 2 4 2 4 2
print()

s = 'u32h4j2u3hj423ui42'
for i in range(len(s)):
    if s[i] in '02468':
        print(s[i], end=' ')  # 2 4 2 4 2 4 2
print()
'''


# Цикл while отвечает на запросы: "Пока условие верно - делать действие", "Бесконечные циклы"
'''
for i in range(2, 10+1, 2):
    print(i, end=' ')  # 2 4 6 8 10
print()


i = 2
while i <= 10:
    print(i, end=' ')  # 2 4 6 8 10 
    i = i + 2
print()
'''



# Бесконечные циклы и операторы break, continue и exit()
'''
password = 'qwerty'
pas = input('Введите пароль: ')
while True:
    if pas == password:
        print('Пароль верный.')
        break
    else:
        pas = input('Пароль неверный, повторите попытку: ')

print('Добро пожаловать!')
'''

FirstName = 'ilya'
first_name = 'ilya'


k = 0
while True:
    k += 1
    if k % 2 != 0:
        continue  # прерывает итеррацию цикла (шаг)
    if k == 100_000:
        break   # прерывает выполнение цикла
    if k == 50_000:
        exit()  # прерывает выполнение программы
    print(k)


print('Выход из цикла')











