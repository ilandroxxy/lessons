# region Домашка: ******************************************************************

# n = int(input())
# a = str(n)
# min = int(a[1])
# max = int(a[1])
# for i in (a):
#     if int(i) > max:
#         max = int(i)
#     if int(i) < min:
#         min= int(i)
# print(max)
# print(min)
'''
n = int(input())
a = str(n)
print(max(a))
print(min(a))
'''

'''
alphabet = sorted('1234567890QWERTYUIOPASDFGHJKLZXCVBNM')
while True:

    case = int(input(f'\n'
                     f'case 1: Перевод из 10-й в base систему счисления.\n'
                     f'case 2: Перевод из base в 10-ю систему счисления.\n'
                     f'case 3: Перевод из base в n-ю систему счисления.\n'
                     f'case 0: \n\n'))

    if case == 1:
        n = int(input('Введите число в 10-й системе: '))  # n - number
        b = int(input('Введите base систему счисления: '))  # b - base
        r = ''  # r - result
        while n > 0:
            r = alphabet[n % b] + r
            n //= b
        r = r
        print(f'Результат перевода в {b}-ю систему счисления: {r}')

    elif case == 2:
        b = int(input('Введите base систему счисления: '))
        r = input(f'Введите число в {b}-й системе: ')
        print(f'Результат перевода в 10-ю систему счисления: {int(r, b)}')
        # ValueError: int() base must be >= 2 and <= 36, or 0

    elif case == 3:
        b = int(input('Введите base систему счисления: '))
        x = input(f'Введите число в {b}-й системе: ')
        d = int(x, b)  # 10-ая система
        n = int(input('Введите n-ю систему счисления: '))
        r = ''
        while d > 0:
            r = alphabet[d % n] + r
            d //= n
        print(f'Результат перевода в {n}-ю систему счисления: {r}')

    elif case == 0:
        break

    else:
        print('Что-то я не очень понял вас. ')
'''
# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Тип 2 №27371
# Логическая функция F задаётся выражением ((x ∧ ¬y) → (¬z ∨ ¬w))∧((w→x) ∨ y).
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((x and (not y)) <= ((not z) or (not w))) and ((w <= x) or y)
                if F == 0:
                    print(x, y, z, w)
'''

# Тип 2 №18704
# Логическая функция F задаётся выражением (x ∨ ¬y) ∧ ¬(w ≡ z) ∧ w.
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (x or (not y)) and (not(w == z)) and w
                if F == 1:
                    print(x, y, z, w)
'''

# Тип 2 №18483
# Логическая функция F задаётся выражением ((y → w) ≡ (x → ¬z)) ∧ (x ∨ w)

print('x y z w F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((y <= w) == (x <= (not z))) and (x or w)
                if F == 0:
                    print(x, y, z, w, int(F))

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((y <= w) == (x <= (not z))) and (x or w)
                if F == 1:
                    print(x, y, z, w, int(F))

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2]
# КЕГЭ  = []
# на следующем уроке:
