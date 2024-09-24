# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
file = open('17.txt')
print(file)  # <_io.TextIOWrapper name='17.txt' mode='r' encoding='UTF-8'>

file = open('17.txt', mode='r')
file.close()

with open(file='17.txt', mode='r') as file:
    print(file)  # <_io.TextIOWrapper name='17.txt' mode='r' encoding='UTF-8'>
    # print(file.read())
    print(file.readline())  # Выводит только первую строку файла
    print(file.readlines())  # Выводим все содержимое файла в виде списка, где элементы списка это строки файла
'''


# Открытие 17 файла ЕГЭ:
'''
M = []
for s in open('17.txt'):  # пробегаем все строчки файла
    M.append(int(s))
print(M)


M = [int(x) for x in open('17.txt')]
print(M)
'''

# Открытие 9 файла ЕГЭ:
'''
for s in open('9.txt'):
    M = [int(x) for x in s.split()]
    print(M)
'''


# Тип 9 №51978
# Определите, сколько в таблице строк, для которых выполнены следующие условия:
# — все числа в строке различны;
# — нечётных чисел больше, чем чётных;
# — сумма нечётных чисел меньше суммы чётных.
# В ответе запишите число — количество строк, для которых выполнены эти условия.
'''
cnt = 0
for s in open('9.txt'):
    M = [int(x) for x in s.split()]
    if len(M) == len(set(M)):
        chet = [x for x in M if x % 2 == 0]
        nechet = [x for x in M if x % 2 != 0]
        if len(nechet) > len(chet):
            if sum(nechet) < sum(chet):
                cnt += 1
print(cnt)
'''
'''
cnt = 0
for s in open('9.csv'):
    M = [int(x) for x in s.split(';')]
    if len(M) == len(set(M)):
        chet = [x for x in M if x % 2 == 0]
        nechet = [x for x in M if x % 2 != 0]
        if len(nechet) > len(chet):
            if sum(nechet) < sum(chet):
                cnt += 1
print(cnt)
'''


# Тип 9 №60251
# Определите количество строк таблицы, содержащих числа, для которых выполнены оба условия:
# — в строке есть два числа, каждое из которых повторяется дважды, остальные числа различны;
# — среднее арифметическое всех повторяющихся чисел строки меньше среднего арифметического всех её чисел.
'''
cnt = 0
for s in open('9.csv'):
    M = [int(x) for x in s.split(';')]
    copied = [x for x in M if M.count(x) == 2]
    not_copied = [x for x in M if M.count(x) == 1]
    if len(copied) == 4 and len(not_copied) == 3:
        if sum(copied) / 4 < sum(M) / 7:
            cnt += 1
print(cnt)
'''


# Построение подряд идущих пар символов
'''
# M = [int(x) for x in open('17.txt')]
M = [1, 2, 3, 4, 5]   
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    print(f'{x}{y}', end=' ')
    # 12 23 34 45 
'''


# Тип 9 №58322
# Откройте файл электронной таблицы, содержащей в каждой строке четыре натуральных числа.
# Определите количество строк таблицы, содержащих числа, для которых выполнено хотя бы одно из условий:
# — квадрат наибольшего из четырёх чисел больше произведения трёх других;
# — будучи упорядоченными, четыре числа образуют арифметическую прогрессию.
'''
from math import prod
cnt = 0
for s in open('9.csv'):
    M = sorted([int(x) for x in s.split(';')])
    # if max(M) ** 2 > (M[0] * M[1] * M[2]):
    if max(M) ** 2 > (prod(M[:-1])) or all(M[1] - M[0] == M[i+1] - M[i] for i in range(len(M) - 1)):
        cnt += 1
print(cnt)
'''



# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 9, 8, 12, 13, 14, 15, 16, 23, 25]
# КЕГЭ  = []
# на следующем уроке:
