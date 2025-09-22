# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Найдите сумму цифр числа (или строки)
'''
n = 12345  # i 01234
s = str(n)  # '12345'

summa1 = 0
for x in s:
    summa1 += int(x)
print(summa1)

# summa2 = s.count('1') + s.count('2') * 2 + s.count('3') * 3 ..

summa2 = 0
for i in range(0, 9+1):
    summa2 += s.count(str(i)) * i
print(summa2)


# summa3 = sum([int(x) for x in s])
summa3 = sum([int(x) for x in s if x.isdigit()])
print(summa3)

summa4= sum(map(int, s))
print(summa4)
'''


'''
print('x y z w F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (x or y) and (not(y == z)) and (not w)
                if F == 1:
                    print(x, y, z, w, int(F))
'''


# № 23548 Пересдача 03.07.25 (Уровень: Базовый)
'''
print('x y z w F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((x or y) <= z) or (y == w) or z
                if F == 0:
                    print(x, y, z, w, int(F))
'''


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, ]
# КЕГЭ = []
# на следующем уроке:
