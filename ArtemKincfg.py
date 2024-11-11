# region Домашка: ******************************************************************
import readline

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Задание 5 https://education.yandex.ru/ege/task/5b677bd9-1e15-4e6d-a760-b33b081773a3
'''
M = []
for n in range(1, 1000):
    s = f'{n:b}'  # s = bin(n)[2:]
    if s.count('1') % 2 == 0:
        s = '10' + s[2:] + '0'
    else:
        s = '11' + s[2:] + '1'
    r = int(s, 2)  # Перевод из 2-й в 10-ю
    if r > 40:
        M.append(n)
print(min(M))
'''


# Задание 5 https://education.yandex.ru/ege/task/326fe818-6354-4d1c-b1ff-3d8d646f1705
'''
M = []
for n in range(1, 1000):
    s = f'{n:b}'
    if n % 3 == 0:
        s = s + s[-3:]
    else:
        x = (n % 3) * 3
        s = s + f'{x:b}'
    r = int(s, 2)  # Строку s переводим из 2-ой в 10-ю
    # ValueError: int() base must be >= 2 and <= 36, or 0
    if r > 151:
        M.append(r)
print(min(M))
'''


# Задание 5 https://education.yandex.ru/ege/task/57ff1917-d44e-4cf3-89a6-097323fd9717

# i                0123456789
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

for n in range(100, 1000):
    S = list(f'{n:X}')  # s = list(hex(n)[2:].upper())
    for i in range(len(S)):
        if S[i] != 'F':
            S[i] = alphabet[alphabet.index(S[i]) + 1]
    s = ''.join(S)[::-1]
    r = int(s, 16)
    summa = sum([int(x) for x in str(r)])
    if summa == 12:
        print(n)
        break




# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6]
# КЕГЭ  = []
# на следующем уроке: Закрываем вопросы по str, смотрим еще раз 5 и возможно 12 номера
