# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 31505 Демоверсия 2027(Уровень: Базовый)
'''
n = 0
R = []
from itertools import product
for p in product(sorted('АКЦЕНТ'), repeat=5):
    word = ''.join(p)
    n += 1
    if n % 2 == 0:
        if word[0] not in 'АЕК':
            if word.count('Т') >= 1:
                R.append(n)
print(min(R))
'''
from multiprocessing.pool import worker

# № 9363 Джобс 10.06.23(Уровень: Средний)
# Семён составляет слова путем перестановки букв в слове ХОЧУНАБЮДЖЕТ.
# Сколько слов может составить Семён, если известно, что слова
# с пятью подряд идущими гласными буквами запрещены?
'''
cnt = 0
from itertools import permutations
for p in permutations('ХОЧУНАБЮДЖЕТ'):
    word = ''.join(p)
    for x in 'ОУАЮЕ':
        word = word.replace(x, '*')
    if '*' * 5 not in word:
        cnt += 1
print(cnt)
'''


# № 8417 (Уровень: Базовый)
# Ярослав составляет коды из букв, входящих в слово ЯРОСЛАВ.
# Код должен состоять из 5 букв, буквы в коде не должны
# повторяться, согласных в коде должно быть больше, чем
# гласных, две гласные буквы нельзя ставить рядом.
# Сколько кодов может составить Ярослав?
'''
cnt = 0
from itertools import permutations
for p in permutations('ЯРОСЛАВ', r=5):
    word = ''.join(p)
    for x in 'ЯОА':
        word = word.replace(x, 'А')
    for x in 'РСЛВ':
        word = word.replace(x, 'В')
    if word.count('В') > word.count('А'):
        if 'АА' not in word:
            cnt += 1
print(cnt)
'''


# № 5553 (Уровень: Базовый)
# Сколько можно составить различных кодов, в составе которых
# встречаются две подряд идущие гласные, путём перестановки букв
# слова СОТОЧКА?
'''
R = []
from itertools import permutations
for p in permutations('СОТОЧКА'):
    word = ''.join(p)
    if 'ОА' in word or 'АО' in word or 'ОО' in word:
        R.append(word)
print(len(set(R)))


R = []
from itertools import permutations
for p in permutations('СОТОЧКА'):
    word = ''.join(p)
    w = word
    word = word.replace('А', 'О')
    if 'ОО' in word:
        R.append(w)
print(len(set(R)))
'''



# № 5488 (Уровень: Базовый)
# Полина составляет коды из букв слова ПОЛИНА.
# Код должен состоять из 8 букв, любую букву можно использовать
# произвольное число раз или не использовать вовсе.
# Полина хочет, чтобы согласных в каждом коде было больше, чем гласных.
# Сколько кодов, удовлетворяющих этому условию, она сможет составить?
'''
cnt = 0
from itertools import product
for p in product('ПОЛИНА', repeat=8):
    word = ''.join(p)
    sogl = [x for x in word if x in 'ПЛН']
    glas = [x for x in word if x not in 'ПЛН']
    if len(sogl) > len(glas):
        cnt += 1
print(cnt)
'''


# № 11201 (Уровень: Средний)
# (С. Якунин) Полина составляет слова, переставляя буквы в слове ПАЙТОН.
# Сколько слов может составить Полина, если известно, что сумма
# порядковых номеров гласных букв, в каждом из них, равна 6?
# Буквы нумеруются слева направо, начиная с единицы.
'''
cnt = 0
from itertools import permutations
for p in permutations('ПАЙТОН'):
    word = ''.join(p)
    summa = 0
    for i in range(len(word)):
        if word[i] in 'АО':
            summa += i+1
    if summa == 6:
        cnt += 1
print(cnt)
'''


# № 6892 OpenFIPI(Уровень: Базовый)
# Определите количество шестизначных чисел, записанных в шестеричной
# системе счисления, в записи которых ровно одна цифра 2,
# при этом никакая нечётная цифра не стоит рядом с цифрой 2.
'''
cnt = 0
from itertools import product
for p in product('012345', repeat=6):
    num = ''.join(p)
    if num[0] != '0':
        if num.count('2') == 1:
            for x in '135':
                num = num.replace(x, '*')
            if '*2' not in num and '2*' not in num:
                cnt += 1
print(cnt)
'''


# № 12240 ЕГКР 16.12.23(Уровень: Базовый)
# Сколько существует девятеричных пятизначных чисел, содержащих
# в своей записи ровно одну цифру 5, в которых никакие две одинаковые
# цифры не стоят рядом?
'''
cnt = 0
from itertools import product
for p in product('012345678', repeat=5):
    num = ''.join(p)
    if num[0] != '0':
        if num.count('5') == 1:
            # if all(pair not in num for pair in '00 11 22 33 44 55 66 77 88'.split()):
            if all(x * 2 not in num for x in '012345678'):
                cnt += 1
print(cnt)
'''

# № 12462 PRO100 ЕГЭ 29.12.23(Уровень: Базовый)
# Сколько существует различных трёхзначных и пятизначных чисел, записанных
# в шестнадцатеричной системе счисления, в записи которых цифры следуют
# слева направо в строго убывающем порядке?
'''
cnt = 0
from itertools import product
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

for p in product(alp[:16], repeat=5):
    num = ''.join(p)
    if num[0] != '0':
        if sorted(num)[::-1] == list(num):
            if len(num) == len(set(num)):
                print(num)
                cnt += 1


for p in product(alp[:16], repeat=3):
    num = ''.join(p)
    if num[0] != '0':
        if num[0] > num[1] > num[2]:
            cnt += 1
print(cnt)
'''


# № 13094 (Уровень: Средний)
# Сколько существует 9-значных девятеричных чисел, в записи которых
# не встречается цифра 0, любые две соседние цифры имеют разную чётность,
# и никакая цифра не повторяется больше 3 раз?
'''
cnt = 0
from itertools import product
for p in product('12345678', repeat=9):
    num = ''.join(p)
    if num[0] != '0':
        if num.count('0') == 0:
            if all(num.count(x) <= 3 for x in num):
                for x in '02468':
                    num = num.replace(x, '2')
                for x in '1357':
                    num = num.replace(x, '1')
                if '11' not in num and '22' not in num:
                    cnt += 1
print(cnt)
'''

# № 13870 (Уровень: Средний)
# (Л. Шастин) Сколько существует различных пятизначных чисел,
# записанных в восьмеричной системе счисления, в записи которых
# есть только три одинаковые цифры, причём стоящие рядом?

cnt = 0
from itertools import product
for p in product('01234567', repeat=5):
    num = ''.join(p)
    if num[0] != '0':
        if all(num.count(x) <= 3 for x in num):
            if all(num.count(x) == 1 or num.count(x) == 3 for x in num):
                if any(x*3 in num for x in num):
                    cnt += 1
print(cnt)


cnt = 0
from itertools import product
for p in product('01234567', repeat=5):
    num = ''.join(p)
    if num[0] != '0':
        copied3 = [x for x in num if num.count(x) == 3]
        copied1 = [x for x in num if num.count(x) == 1]
        if len(copied3) == 3 and len(copied1) == 2:
            if copied3[0] * 3 in num:
                cnt += 1
print(cnt)


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 8, 13, 15, 16, 19-21]
# КЕГЭ = []
# todo на следующем уроке:
