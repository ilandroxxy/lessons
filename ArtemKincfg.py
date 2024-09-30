# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Цикл for отвечает на запросы: "повтори N раз", "пробеги от А до В"
'''
# Работа с циклом for через функцию range

# range(STOP-1)
# range(START, STOP-1)
# range(START, STOP-1, STEP)

for i in range(10):  # range(start=0, STOP=10-1, step=1)
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
print()

for i in range(2, 10):  # range(START=2, STOP=10-1, step=1)
    print(i, end=' ')  # 2 3 4 5 6 7 8 9
print()

for i in range(2, 10, 2):  # range(START=2, STOP=10-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8
print()

for i in range(2, 10+1, 2):  # range(START=2, STOP=11-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10
print()

for i in range(10, 0):  # range(START=10, STOP=0-1, step=1)
    print(i, end=' ')  #
print()

for i in range(10, 0, -1):  # range(START=10, STOP=0-1, STEP=-1)
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1
print()


# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']

print(len(M))  # 5 - Возвращает длину списка (кол-во элементов в нем)

for i in range(len(M)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e
print()


for i in range(len(M)):
    M[i] = M[i] * i
print(M)  # ['', 'b', 'cc', 'ddd', 'eeee']

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

# Цикл while отвечает на запросы: "пока условие верно выполняй", "бесконечные циклы"

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

# Алгоритм через списки:
'''
n = int(input('Введите число для перевода в b-ю систему: '))
b = int(input('Введите b-ю систему: '))
R = []
while n > 0:
    R.append(n % b)  # .append() - добавляет новый элемент в конец списка
    n //= b
R.reverse()  # .reverse() - меняет порядок элементов списка
print(R)  # [1, 0, 0, 0]

print(int('1000', 2))  # 8 - Перевод из 2-й в 10-ю систему
'''


# Алгоритм через строки:
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
print(alphabet)
n = int(input('Введите число для перевода в b-ю систему: '))
b = int(input('Введите b-ю систему: '))
r = ''
while n > 0:
    r += alphabet[n % b]
    n //= b
r = r[::-1]  
print(r)  # 75BCD15

print(int(r, b))  # 123456789 - Перевод из 16-й в 10-ю систему
'''


# Бесконечные циклы и операторы break, continue, exit()
'''
k = 0
while True:
    k += 1
    if k % 2 != 0:
        continue  # Прерывает итерацию (шаг) цикла
    if k == 1_000_000:
        break  # Прерывает исполнение цикла в котором сейчас лежит
    if k == 2_000_000:
        exit()  # Прерывает полностью исполнение программы
    print(k)

print('Продолжение программы после циклы')
'''


# Консольный калькулятор систем счисления

alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

while True:
    case = input('\n'
                 'case 1: Перевод из 10-й в b-ю систему: \n'
                 'case 2: Перевод из b-й в 10-ю систему: \n'
                 'case 3: Перевод из b-й в k-ю систему: \n'
                 'case 0: Выход из программы \n')

    if case == '1':
        n = int(input('Введите число для перевода в b-ю систему: '))
        b = int(input('Введите b-ю систему: '))
        r = ''
        while n > 0:
            r += alphabet[n % b]
            n //= b
        r = r[::-1]
        print(f'Результат перевода: {r}')

    elif case == '2':
        r = input('Введите число в b-й системе счисления: ')
        b = int(input('Введите b-ю систему: '))
        print(f'Результат перевода: {int(r, b)}')

    elif case == '3':
        pass

    elif case == '0':
        print('Спасибо, что пользовались нашим калькулятором!')
        exit()

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
