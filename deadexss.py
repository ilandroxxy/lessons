


# https://stepik.org/lesson/1309432/step/10?unit=1324548
'''
n = int(input())
if n % 400 ==0:
    print('Високосный')
elif n % 4 == 0 and n % 100 != 0:
    print('Високосный')
else:
    print("Обычный")
'''


# https://stepik.org/lesson/1309432/step/6?unit=1324548
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


# https://stepik.org/lesson/1309432/step/9?unit=1324548
'''
a = int(input())
b = int(input())
if a > b:
    if a % b == 0:
        print("Делится")
    else:
        print("Не делится")
else:
    if b % a == 0:
        print("Делится")
    else:
        print("Не делится")
'''





# Цикл for отвечает на запросы: "Повтори N раз", "Пробеги от А до Б"


# Работа с циклом for через функцию range()
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

for i in range(1, 10, 2):
    print(i, end=' ')  # 1 3 5 7 9
print()

for i in range(10-1, 2-1, -1):
    print(i, end=' ')  # 9 8 7 6 5 4 3 2
print()
'''


# Работа цикла for нарямую с последовательностями
'''
# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
print(len(M))  # 5


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






# Цикл while отвечает на запросы: "Пока условие верно - делай действие", "Бесконечный цикл"
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


# Бесконечные циклы и операторы break, continue и exit()
'''
k = 0
while True:
    k += 1
    if k % 2 != 0:
        continue  # Прерывает итерацию (шаг) цикла 
    if k == 50_000:
        exit()  # Прерывает выполнение всей программы 
    if k == 100_000:
        break  # Прерывает выполнение цикла в котором сейчас лежит 
    print(k)
print('Конец программы')
'''

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


# Построим универсальную функцию перевода в b-ю систему счисления (для номеров 5 и 14).
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

print(convert(10**5, 2))  # 11000011010100000
print(convert(10**5, 3))  # 12002011201
print(convert(10**5, 8))  # 303240

print(convert(10**5, 16))  # 186A0
'''



# № 6575 (Уровень: Базовый)
# (А. Поликарпова) Значение выражения 766**66 + 15**13–22 записали в системе счисления с основанием 13.
# Сколько раз в этой записи встречается цифра С?
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

n = 766 ** 66 + 15 ** 13 - 22
n13 = convert(n, 13)
print(n13.count('C'))
'''


# № 6046 ФИПИ 04.02.23(Уровень: Базовый)
# Значение арифметического выражения 3 ∙ 102475 + 2 ∙ 25676 – 1677 – 2023 записали в системе счисления с основанием 32.
# Определите количество нулей в записи этого числа.



# № 6021 ФИПИ 03.02.23(Уровень: Базовый)

alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

n = 5 * 216 ** 155 + 4 * 36 ** 156 - 4 * 6 ** 157 - 2023
n32 = convert(n, 6)
print(n32.count('0'))  # Определите количество нулей в записи этого числа.
print(len(n32) - n32.count('0'))  # Определите количество не нулевых значений в записи этого числа.


# № 6576 (Уровень: Базовый)
# (А. Поликарпова) Значение выражения 283 ** 382 + 9 ** 15+2 ** 3 записали в системе
# счисления с основанием 14. Определите модуль разности между количеством
# цифр В и С в записи этого числа.

