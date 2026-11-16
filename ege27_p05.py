# region Домашка: ******************************************************************



# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


#
# № 24629 (Уровень: Базовый)
# (М. Рубцова) Значение арифметического выражения
# 14**1402 + 28**501 - 14**51 - 1400  записали в системе счисления
# с основанием 14. Определите в 14-ричной записи числа
# количество цифр с числовым значением, равным С.
'''
alp = sorted("0123456789QWERTYUIOPASDFGHJKLZXCVVBBNM")
def convert(n, b):
    r = ""
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

n = 14**1402 + 28**501 - 14**51 - 1400
n14 = convert(n, 14)
print(n14.count('C'))
'''


# № 23752 Демоверсия 2026(Уровень: Базовый)
'''
alp = sorted("0123456789QWERTYUIOPASDFGHJKLZXCVVBBNM")
def convert(n, b):
    r = ""
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

n = 2 * 2187**2020 + 729 ** 2021 - 2 * 243 ** 2022 + 81 ** 2023 - 2 * 27 ** 2024 - 6561
n27 = convert(n, 27)
print(len([x for x in n27 if x not in '0123456789']))
print(len( [x for x in n27 if x > '9'] ))
'''


# № 22067 (Уровень: Средний)
'''
alp = sorted("0123456789QWERTYUIOPASDFGHJKLZXCVBNM")
def convert(n, b):
    r = ""
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

n = 3 * 17 ** 777 + 15 * 17 ** 250 - 6 * 17 ** 100 + 2
n17 = convert(n, 17)
print(len(set([x for x in n17 if int(x, 17) % 2 == 0])))
print(len(set([x for x in n17 if x in alp[0::2]])))
'''

# № 21900 Открытый вариант 2025(Уровень: Базовый)
'''
alp = sorted("0123456789QWERTYUIOPASDFGHJKLZXCVBNM")
def convert(n, b):
    r = ""
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

for x in range(1, 2300):
    n = 7 ** 350 + 7 ** 150 - x
    n7 = convert(n, 7)
    if n7.count('0') == 200:
        print(x)
'''


# № 20808 Апробация 05.03.25(Уровень: Средний)
'''
alp = sorted("0123456789QWERTYUIOPASDFGHJKLZXCVBNM")
def convert(n, b):
    r = ""
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

R = []
for x in range(1, 2030):
    n = 7 ** 170 + 7 ** 100 - x
    n7 = convert(n, 7)
    if n7.count('0') == 73:
        print(x)
#     R.append(n7.count('0'))
# print(max(R))  # 73
'''



# № 31511 Демоверсия 2027(Уровень: Базовый)

alp = sorted("0123456789QWERTYUIOPASDFGHJKLZXCVBNM")
for x in alp[:22]:
    A = int(f'27{x}98876', 22)
    B = int(f'26{x}51', 22)
    C = int(f'711{x}5', 22)
    if (A + B + C) % 21 == 0:
        print((A + B + C) // 21)




# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [5, 13, 14, 15, 16, 19-21, 23]
# КЕГЭ = []
# todo на следующем уроке:
