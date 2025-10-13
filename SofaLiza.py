# region Домашка: ******************************************************************

# https://stepik.org/lesson/1038432/step/2?unit=1060804
# № 6903 (Уровень: Базовый)
'''
RES = []
for n in range(1, 10000):
    s = bin(n)[2:]  # str()

    # Пункт 2 повторяется ещё раз к записи, полученной после второго пункта.

    # Если сумма цифр в двоичной записи числа чётная
    for i in range(2):
        if s.count('1') % 2 == 0:
            s = '11' + s[2:] + '00'  # два левых разряда заменяются на 11
        else:
            s = '10' + s[2:] + '11'


    r = int(s, 2)
    if n < 100:
        RES.append(r)
print(max(RES))
'''


# № 6779 (Уровень: Базовый)
'''
RES = []
for n in range(1, 10000):
    s = bin(n)[2:]
    summa = sum(map(int, s))
    if summa % 2 == 0:
        s = '101' + s[3:] + '0'
    else:
        s = '10' + s[2:] + '11'
    r = int(s, 2)
    if r > 68:
        RES.append(n)
print(min(RES))


# Если просят найти минимальный n
for n in range(1, 10000):
    s = bin(n)[2:]
    r = int(s, 2)
    if r > 100:
        print(n)
        break


# Если просят найти максимальный n
for n in range(10000, -1, -1):
    s = bin(n)[2:]
    r = int(s, 2)
    if r > 100:
        print(n)
        break
        
        
# Если просят найти минимальное/максимальное r

RES = []
for n in range(1, 10000):
    s = bin(n)[2:]
    r = int(s, 2)
    if r > 100:
        RES.append(r)
print(min(RES), max(RES))
'''

'''
RES = []
for n in range(1, 10000):
    s = bin(n)[2:]
    if n % 2 == 0:
        s = '1' + s + '0'
    else:
        s = '11' + s + '11'
    r = int(s, 2)
    if r > 225:
        RES.append(r)
print(min(RES))
'''

# https://stepik.org/lesson/1038432/step/10?unit=1060804
'''
RES = []
for n in range(1, 10000):
    s = bin(n)[2:]
    if n % 2 == 0:
        s = '10' + s
    else:
        s = '1' + s + '01'
    r = int(s, 2)
    if n <= 12:
        RES.append(r)
print(max(RES))
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************



'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r


# Проверки, что функция переписана верно 
print(convert(8, 2))  # 1000
print(len(set(alp)))  # 36
'''


# № 23752 Демоверсия 2026 (Уровень: Базовый)
'''
def convert(n, b):
    alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r

n = 2*2187**2020 + 729**2021 - 2*243**2022 + 81**2023 - 2*27**2024 - 6561
s = convert(n, 27)
print(s.count('0'))  # Сколько значащих нулей
print(s.count('0') + s.count('1'))  # Сколько значащих нулей и единиц
print(len(s) - s.count('0'))  # Сколько ненулевых символов
print(len(set(s)))  # Сколько различных значений
print(len([x for x in s if x > '9']))  # Количество цифр с числовым значением, превышающим 9.
'''


# № 23754 Демоверсия 2026 (Уровень: Базовый)
'''
def convert(n, b):
    alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r

# где x – целое положительное число, не превышающее 3000
RES = []
for x in range(1, 3000):
    n = 9 * 11**210 + 9 * 11**150 - x
    s = convert(n, 11)
    if s.count('0') == 60:
        RES.append(x)
print(max(RES))
'''


# № 23753 Демоверсия 2026 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alp[:29]:
    A = int(f'923{x}874', 29)
    B = int(f'524{x}6152', 29)
    if (A + B) % 28 == 0:
        print((A + B) // 28)
'''


# https://inf-ege.sdamgia.ru/problem?id=48393
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alp[:8]:
    for y in alp[:8]:
        A = int(f'{y}04{x}5', 11)
        B = int(f'253{x}{y}', 8)
        if (A + B) % 117 == 0:
            print((A + B) // 117)
'''


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 14]
# КЕГЭ = []
# на следующем уроке:
