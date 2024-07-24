# region Домашка: ******************************************************************

'''
from itertools import permutations
R = []
for per in permutations(['1' * 20, '2' * 15, '3' * 40]):
    s = '>' + ''.join(per) + '<'
    while '><' not in s:
        s = s.replace('>1', '3>', 1)
        s = s.replace('>2', '2>', 1)
        s = s.replace('>3', '1>', 1)
        s = s.replace('3<', '<1', 1)
        s = s.replace('2<', '<3', 1)
        s = s.replace('1<', '<2', 1)
    summa = sum(int(i) for i in s if i.isdigit())
    R.append(summa)
print(R)
print(max(R))
'''

'''
s = '>' + "1"*11 + '2'*12 + '3'*30
while '>1' in s or '>2' in s or '>3' in s:
    if '>1' in s:
        s = s.replace('>1', '22>', 1)
    if '>2' in s:
        s = s.replace('>2', '222>', 1)
    if '>3' in s:
        s = s.replace('>3', '1>', 1)
print(sum(int(i) for i in s if i.isdigit()))
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Тип 8 №18789
# Все четырёхбуквенные слова, составленные из букв С, Е, Н, О, записаны
# в алфавитном порядке и пронумерованы, начиная с 1. Начало списка выглядит так:
# 1. ЕЕЕЕ
# 2. ЕЕЕН
# 3. ЕЕЕО
# 4. ЕЕЕС
# 5. ЕЕНЕ
# Под каким номером в списке идёт первое слово, которое начинается с буквы С?
'''
s = sorted('СЕНО')
num = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                slovo = a + b + c + d
                num += 1
                if a == 'С':
                    print(num, slovo)
                    exit()
'''
'''
from itertools import product
num = 0
for per in product(sorted('СЕНО'), repeat=4):
    slovo = ''.join(per)
    num += 1
    if slovo[0] == 'С':
        print(num, slovo)
        exit()
'''


# Тип 8 №16037
# Вася составляет 5- буквенные слова, в которых есть только буквы З, И, М, А,
# причём в каждом слове есть ровно одна гласная буква и она встречается ровно 1 раз.
# Сколько существует таких слов, которые может написать Вася?
'''
from itertools import product
cnt = 0
for per in product('ЗИМА', repeat=5):
    s = ''.join(per)
    if s.count('И') + s.count('А') == 1:
        cnt += 1
print(cnt)
'''

# Тип 8 №58235
# Сколько существует различных трёхзначных чисел, записанных в четверичной
# системе счисления, в записи которых сумма первой и последней цифры
# строго больше цифры стоящей по середине?
'''
from itertools import product
cnt = 0
for per in product('0123', repeat=3):
    num = ''.join(per)
    if num[0] != '0':
        if int(num[0]) + int(num[2]) > int(num[1]):
            cnt += 1
print(cnt)
'''

# Тип 8 №59741
# Сколько существует чисел, восьмеричная запись которых содержит 5 цифр,
# причем в записи нет цифры 1.
# Также все цифры записи различны и никакие две чётные и две нечётные
# цифры не стоят рядом.

from itertools import permutations
cnt = 0
for per in permutations('0234567', 5):
    num = ''.join(per)
    if num[0] != '0':
        num = num.replace('0', '2').replace('4', '2').replace('6', '2')
        num = num.replace('5', '3').replace('7', '3')
        if '22' not in num and '33' not in num:
            cnt += 1
print(cnt)






# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 14]
# КЕГЭ  = []
# на следующем уроке:
