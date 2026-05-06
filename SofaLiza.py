# region Домашка: ******************************************************************



# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 12463 PRO100 ЕГЭ 29.12.23 (Уровень: Базовый)
# – в строке есть одно число, которое повторяется четыре раза,
# – есть другое число, которое повторяется дважды,
# – остальные три числа различны;
# – среднее арифметическое трёх неповторяющихся чисел строки не меньше наибольшего из повторяющихся в строке чисел
'''
cnt = 0
for s in open('files/9.txt'):
    M = [int(x) for x in s.split()]
    copied4 = [x for x in M if M.count(x) == 4]
    copied2 = [x for x in M if M.count(x) == 2]
    copied1 = [x for x in M if M.count(x) == 1]
    if len(copied4) == 4 and len(copied2) == 2 and len(copied1) == 3:
        if (sum(copied1) / 3) >= max(copied4 + copied2):
            cnt += 1
print(cnt)
'''


# № 11946 (Уровень: Средний)
# – в строке есть одно число, которое повторяется трижды, остальные четыре числа различны;
# – числа в строке расположены в порядке неубывания.
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    flag = 0
    copied3 = [x for x in M if M.count(x) == 3]
    copied1 = [x for x in M if M.count(x) == 1]
    if M == sorted(M):
        flag += 1
    if len(copied3) == 3 and len(copied1) == 4:
        flag += 1
    if flag <= 1:
        cnt += 1
print(cnt)
'''


#– в строке есть два числа, каждое из которых повторяется дважды, остальные три числа различны;
#  произведение всех повторяющихся чисел строки более чем вдвое превосходит произведение неповторяющихся чисел.
'''
from math import prod
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied2 = [x for x in M if M.count(x) == 2]
    copied1 = [x for x in M if M.count(x) == 1]
    if len(copied2) == 4 and len(copied1) == 3:  # [5, 5, 6, 7, 7, 8, 9]
        if prod(copied2) > prod(copied1) * 2:
            cnt += 1
print(cnt)
'''  # 161


'''
from itertools import permutations
summa = 0
for s in open('files/9.csv'):
    M = sorted([int(x) for x in s.split(';')])
    copied2 = [x for x in M if M.count(x) == 2]
    copied3 = [x for x in M if M.count(x) == 3]
    if len(copied2) == 4 and len(copied3) == 3:
        if any(p[0] + p[1] == p[2] + p[3] and (p[0] + p[1]) % 2 != 0 and (p[2] + p[3]) % 2 != 0 for p in permutations(M[:4], r=4)):
            summa += sum(M)
print(summa)
'''


# № 10910 (Уровень: Средний)
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied = [x for x in M if M.count(x) > 1]
    not_copied = [x for x in M if M.count(x) == 1]
    # if M.count(min(M)) == 1:
    if min(M) in not_copied:
        if len(copied) > 0:
            if max(M) + min(M) < sum(copied):
                cnt += 1
print(cnt)
'''


# № 29347 Открытый вариант 2026 (Уровень: Базовый)
'''
def F(x, a1, a2):
    B = 22 <= x <= 40
    C = 32 <= x <= 50
    A = a1 <= x <= a2
    return (not A) <= (B == C)


R = []
M = [x / 4 for x in range(10 * 4, 60 * 4)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(min(R))  # 28.0 -> 28
'''

# № 12469 (Уровень: Базовый)
'''
def F(x, a1, a2):
    D = 7 <= x <= 68
    C = 29 <= x <= 100
    A = a1 <= x <= a2
    return D <= (((not C) and (not A)) <= (not D))

R = []
M = [x / 10 for x in range(0, 120 * 10)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(min(R))  # 21.75 -> 21.8 -> 21.9 -> 22
'''


# № 20905 Апробация 05.03.25 (Уровень: Базовый)
# На числовой прямой даны два отрезка: P = [17; 58] и Q = [29; 80].
# Укажите наименьшую возможную длину такого отрезка A, что логическое выражение
# (x∈P)→(((x∈Q)∧¬(x∈A))→¬(x∈P))
# истинно (т.е. принимает значение 1) при любом значении переменной х.
'''
def F(x, a1, a2):
    P = 17 <= x <= 58
    Q = 29 <= x <= 167
    A = a1 <= x <= a2
    return P <= ((Q and (not A)) <= (not P))

RES = []
M = [x / 4 for x in range(0, 180 * 4)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            RES.append(a2 - a1)
print(min(RES))  # 29.0 -> 29
'''


# № 20961 (Уровень: Базовый)
# (М. Попков) На числовой прямой даны два отрезка: P=[15;142] и Q=[38;167].
# Укажите наименьшую возможную длину такого отрезка A, для которого логическое выражение
# ¬((x∈Q)→((¬(x∈A)∧(x∈P))→¬(x∈Q)))
# ложно (т.е. принимает значение 0) при любом значении переменной x.
'''
def F(x, a1, a2):
    P = 15 <= x <= 142
    Q = 38 <= x <= 167
    A = a1 <= x <= a2
    return (not(Q <= (((not A) and P) <= (not Q))))

R = []
M = [x / 4 for x in range(0, 190 * 4)]
for a1 in M:
    for a2 in M:
        if all(not F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(min(R))
'''

# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 25, 27]
# КЕГЭ = [6, 7, 10, 11, 12, 17]
# на следующем уроке: 17 24 27 26


# region 📖 Пробник (Вариант 2)

# Студент #Софья
# Дата: #Пятница #27Февраля2026
# ✅ Верно: 1, 2, 3, 5, 7, 8, 11, 13, 15, 16, 18, 19, 20, 21, 23, 25
# ⛔️ Неверно: 4, 6, 9, 10, 12, 14, 17, 22, 24, 26, 27
# ❔ Без ответа: Нет
# Итог: 16/29 первичных балла ~ 67 вторичных

# Студент #Лиза
# Дата: #Понедельник #02Марта2026
# ✅ Верно: 1, 2, 3, 4, 5, 7, 11, 13, 15, 16, 18, 19, 20, 21, 23, 25
# ⛔️ Неверно: 6, 8, 9, 10, 12, 14, 17, 22, 24, 26, 27
# ❔ Без ответа: Нет
# Итог: 16/29 первичных балла ~ 67 вторичных

# endregion 📖 Пробник (Вариант 2)
