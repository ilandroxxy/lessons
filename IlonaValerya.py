# region Домашка: ******************************************************************

# https://stepik.org/lesson/1038703/step/3?unit=1062210
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
R = []
for x in alphabet[:15]:
    A = int(f'1{x}51', 15)
    B = int(f'3{x}2', 15)
    if (A - B) % 4 == 0:
        R.append((A - B) // 4)
print(max(R))
'''


# https://stepik.org/lesson/1038703/step/2?unit=1062210
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    s = ''
    while n > 0:
        s = s + alphabet[n % b]
        n = n // b
    return s[::-1]


n = 11 * 15 ** 65 + 18 * 15 ** 38 - 14 * 15 ** 17 + 19 * 15 ** 11 + 18338
f = convert(n, 15)
print(len(set(f)))
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Задание 12 https://education.yandex.ru/ege/task/6f2a579b-2ab5-401c-a218-11748d1fba61
'''
s = '5' * 30
cnt = 0
while '5' in s:
    cnt += 1
    if '555' in s:
        s = s.replace('555', '22', 1)
    else:
        s = s.replace('2222', '5', 1)
print(cnt)
'''


# Задание 12  https://education.yandex.ru/ege/task/50a1b75e-3829-4e52-96bc-44d8e024790e
'''
s = '3' * 70
while '333' in s or '77777' in s:
    if '333' in s:
        s = s.replace('333', '77', 1)
    else:
        s = s.replace('77777', '7', 1)
print(s)
print(s.count('7'))
print(sum(map(int, s)))
'''

# Задание 12 https://education.yandex.ru/ege/task/484d68ed-2e90-4596-a371-e6e4b49c443c
'''
for n in range(4, 10000):
    s = '9' + '6' * n

    while '666' in s or '9909' in s or '66' in s:
        s = s.replace('666', '999', 1)
        s = s.replace('9909', '6', 1)
        s = s.replace('66', '0', 1)
    if len(s) == 10:
        print(n)
'''


# Задание 12 https://education.yandex.ru/ege/task/b9cf27b5-87ab-4fc0-84df-719c5cd24629
'''
for n in range(4, 10000):
    s = '5' + '2' * n

    while '72' in s or '522' in s or '2222' in s:
        if '72' in s:
            s = s.replace('72', '2', 1)
        if '522' in s:
            s = s.replace('522', '27', 1)
        if '2222' in s:
            s = s.replace('2222', '5', 1)
    summa = sum(map(int, s))
    if summa == 22:
        print(n)
        break
'''




# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 12, 14]
# КЕГЭ  = []
# на следующем уроке:
