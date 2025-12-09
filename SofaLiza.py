# region Домашка: ******************************************************************

# https://stepik.org/lesson/1038667/step/2?unit=1062772
'''
n = 0
s = sorted('АЕКНС')
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        word = a + b + c + d + e + f
                        n += 1
                        if word == 'СЕНЕКА':
                            print (n)
'''


# https://stepik.org/lesson/1038667/step/8?unit=1062772
'''
R = []
from itertools import permutations
for p in permutations('СОТОЧКА'):
    word = ''.join(p)
    if any(pair in word for pair in 'АО ОА ОО'.split()):
        R.append(word)
print(len(set(R)))
'''


# https://stepik.org/lesson/1038667/step/3?unit=1062772
'''
cnt = 0
from itertools import permutations
for p in permutations('ЯРОСЛАВ', r=5):  # буквы в коде не должны повторяться
    word = ''.join(p)
    sogl = [x for x in word if x in 'РСЛВ']
    glas = [x for x in word if x in 'ЯОА']
    if len(sogl) > len(glas):  # согласных в коде должно быть больше, чем гласных
        if all(pair not in word for pair in 'ЯО ОЯ АО ОА ЯА АЯ'.split()):
            cnt += 1
print(cnt)
'''


# https://stepik.org/lesson/1038667/step/4?unit=1062772
'''
RES = []
n = 0
from itertools import product
for p in product(sorted('МАРКСЛ'), repeat=6):
    word = ''.join(p)
    n += 1
    if word.count('КС') == 0 and 'СК' not in word:
        # одна буква повторяется трижды, а остальные не повторяются?
        copied3 = [x for x in word if word.count(x) == 3]
        copied1 = [x for x in word if word.count(x) == 1]
        if len(copied3) == 3 and len(copied1) == 3:
            RES.append(n)
print(max(RES))
'''

# Все четырехбуквенный слова, в составе которых могут быть
# только буквы П, Я, Т, Ь, Д, Н, Е, Й, записаны в алфавитном
# порядке и пронумерованы начиная с 1.
#
# Ниже приведено начало списка:
# 1. ДДДД
# 2. ДДДЕ
# 3. ДДДЙ
# 4. ДДДН
# 5. ДДДП
# 6. ДДДТ
# 7. ДДДЬ
# 8. ДДДЯ
#
# Под каким номером в списке идёт последнее слово, которое
# не содержит ни одной гласной и все буквы в нем различны?

RES = []
n = 0
from itertools import product

for p in product(sorted('ПЯТЬДНЕЙ'), repeat=4):
    word = ''.join(p)
    n += 1
    if word.count('Я') == 0 and word.count('E') == 0:
        if len(word) == len(set(word)):
            RES.append(n)

print(max(RES))

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************



# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 8, 13, 14, 15, 16, 19-21, 23]
# КЕГЭ = []
# на следующем уроке: 25, 17, 9, 27
