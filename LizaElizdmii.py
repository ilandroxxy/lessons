# region Домашка: ******************************************************************
'''
b = []
counter = []
for i in range(int(input())):
    n = int(input())
    b.append(n)

for elem in b:
    count = b.count(elem)
    if count == 1:
        counter.append(elem)

if len(counter) > 0:
    print(*counter, sep='\n')
else:
    print("Уникальных элементов нет")
'''


# Сумма строки вариант 1
'''
summa = 0
a = input()
for i in range(0, len(a)):
    summa += int(a[i])
print(summa)
'''

# Сумма строки вариант 2
'''
summa = 0
a = input()
for x in a:
    summa += int(x)
print(summa)
'''

# Сумма строки вариант 3
'''
a = input()
summa = sum([int(x) for x in a])
print(summa)
'''

# Сумма строки вариант 4
'''
a = input()
summa = sum(map(int, a))
print(summa)
'''


# Поиск длинного слова
'''
a = input()
maxi = 0
for word in a.split():
    if len(word) > maxi:
        maxi = len(word)
print(maxi)
'''


'''
from string import *
alphabet = digits + ascii_uppercase
# 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ

alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):  # n - number, b - base
    r = ''
    while n > 0:
        r = alphabet[n % b] + r
        n //= b
    return r


n = int(input())
b = 3
'''

'''
L = []
for x in range(100, 1000):
    if str(x)[0] == str(x)[-1]:
        L.append(x)
print(L)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Дана программа для редактора:
# ПОКА НЕ нашлось (00)
#   заменить (011, 20)
#   заменить (022, 10)
#   заменить (01, 220)
#   заменить (02, 110)

# Известно, что исходная строка A содержала ровно два нуля — на первом
# и на последнем месте, а также поровну единиц и двоек.
# После выполнения данной программы получилась строка B, содержащая 47 единиц
# и меньше 70 двоек.
#
# Какое наибольшее количество двоек может быть в строке B?
'''
for n in range(1000):
    s = '0' + '1' * n + '2' * n + '0'
    while '00' not in s:
        s = s.replace('011', '20', 1)
        s = s.replace('022', '10', 1)
        s = s.replace('01', '220', 1)
        s = s.replace('02', '110', 1)
    if s.count('1') == 47 and s.count('2') < 70:
        print(s.count('2'))
'''


# Тип 12 №46970
# Дана программа для редактора:
# ПОКА НЕ нашлось (00)
#   заменить (01, 210)
#   заменить (02, 3101)
#   заменить (03, 2012)

# Известно, что исходная строка начиналась с нуля и заканчивалась нулём,
# а между ними содержала только единицы, двойки и тройки.
# После выполнения данной программы получилась строка,
# содержащая 70 единиц, 56 двоек и 23 тройки.
# Сколько цифр было в исходной строке?
'''
for x in range(50):
    for y in range(50):
        for z in range(50):
            s = '0' + '1' * x + '2' * y + '3' * z + '0'
            while '00' not in s:
                s = s.replace('01', '210', 1)
                s = s.replace('02', '3101', 1)
                s = s.replace('03', '2012', 1)
            if s.count('1') == 70 and s.count('2') == 56 and s.count('3') == 23:
                print(2 + x + y + z)
'''


# Тип 12 №26957
# Определите сумму числовых значений цифр строки,
# получившейся в результате выполнения программы.
'''
s = '>' + '1' * 26 + '2' * 10 + '3' * 14
while '>1' in s or '>2' in s or '>3' in s:
    if '>1' in s:
        s = s.replace('>1', '22>', 1)
    if '>2' in s:
        s = s.replace('>2', '2>', 1)
    if '>3' in s:
        s = s.replace('>3', '1>', 1)
print(sum(map(int, s[:-1])))
print(sum(map(int, s.replace('>', ''))))
print(sum([int(x) for x in s if x.isdigit()]))
'''
# ValueError: invalid literal for int() with base 10: '>'


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 6, 12]
# КЕГЭ  = []
# на следующем уроке:
