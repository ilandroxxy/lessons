
# PEP8 - ctrl + alt + L | cmnd + opt + L
# Отформатирует текст проствив пробелы


# Напишите программу, которая проверяет выполнение следующего
# соотношения для введенного пятизначного числа: произведение
# первой и третьей цифр равно сумме второй, четвертой и пятой цифр.
#
# Для решения этой задачи необходимо извлечь отдельные цифры из
# пятизначного числа и выполнить необходимые арифметические операции.

'''
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print('Равносторонний')
elif a != b != c != a:
    print('Разносторонний')
else:
    print('Равнобедренный')
'''


# Цикл for отвечает на запросы: "Повтори n раз", "Пробеги от А до Б"

# Работа цикла for с функцией range()

# range(0, STOP-1, 1)
# range(START, STOP-1, 1)
# range(START, STOP-1, STEP)
'''
for i in range(10):
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
print()

for i in range(2, 10):
    print(i, end=' ')  # 2 3 4 5 6 7 8 9
print()

for i in range(2, 10, 2):
    print(i, end=' ')  # 2 4 6 8
print()

for i in range(5, 30, 5):
    print(i, end=' ')  # 5 10 15 20 25
print()

for i in range(5, 30+1, 5):
    print(i, end=' ')  # 5 10 15 20 25 30
print()

for i in range(10, 0, -1):
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1
print()
'''

# Работа цикла for c последовательностями
'''
# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']

for x in M:
    print(x, end=' ')  # a b c d e
print()

for x in M:
    if x in 'aeuo':
        print(x, end=' ')  # a e
print()


print(len(M))  # 5

for i in range(len(M)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e
print()

# i           0    1    2    3    4
print(M)  # ['a', 'b', 'c', 'd', 'e']
for i in range(len(M)):
    M[i] = M[i] * i
print(M)  # ['', 'b', 'cc', 'ddd', 'eeee']
'''


# Цикл while отвечает на запросы: "Выполняй действие, пока условие верное", "Бесконечные циклы"

for i in range(2, 10+1, 2):
    print(i, end=' ')  # 2 4 6 8 10
print()

i = 2
while i <= 10:
    print(i, end=' ')  # 2 4 6 8 10
    i += 2
print()


# Бесконечные циклы и операторы break, continue, exit()

k = 0
while True:
    k += 1
    if k % 2 != 0:
        continue  # Прерывает итеррацию цикла
    if k == 50_000:
        exit()  # Это функция прерывания всей программы
    if k == 100_000:
        break  # Прерывает выполнение цикла
    print(k)
print('Продолжение программы')


# Добавить пример с переводом в различные системы счисления (5 и 14 номера)
# Добавить пример с подбором паролей.