# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
M = [23, 4, 5, 3]
print(M)
print(*M)
'''


# Тип 5 №27535
'''
R = []
for n in range(2, 1000+1):
    s = f'{n:b}'  # s = bin(n)[2:]
    s = s + s[1] + s[0]
    r = int(s, 2)
    if r > 90:
        R.append(n)
print(min(R))
'''


# Тип 5 №25836
'''
R = []
for n in range(1, 1000):
    s = f'{n:b}'
    if n % 2 == 0:
        s = s + '00'
    else:
        s = s + '11'
    r = int(s, 2)
    if r < 134:
        R.append(n)
print(max(R))
'''

# Тип 5 №18785
'''
R = []
for n in range(1, 1000):
    s = f'{n:b}'
    if n % 2 == 0:
        s = '1' + s + '0'
    else:
        s = '11' + s + '11'
    r = int(s, 2)
    if r > 52:
        R.append(n)
print(min(R))
'''

# Тип 5 №47002
'''
R = []
for n in range(2, 1000+1):
    s = f'{n:b}'
    count_1 = s[1::2].count('1')
    count_0 = s[::2].count('0')
    r = abs(count_0 - count_1)
    if r == 4:
        R.append(n)
print(min(R))
'''


# Тип 5 №35894
'''
R = []
for n in range(105, 1000):
    s = f'{n:b}'
    for i in range(3):
        if s.count('0') == s.count('1'):
            s = s + s[-1]
        elif s.count('0') < s.count('1'):
            s = s + '0'
        else:
            s = s + '1'
    r = int(s, 2)
    if r % 4 == 0:
        R.append(n)
print(min(R))
'''

# № 9828 Основная волна 27.06.23 (Уровень: Средний)
'''
def convert(n, b):
    r = ''
    while n > 0:
        r = str(n % b) + r
        n //= b
    return r


R = []
for n in range(1, 1000):
    s = convert(n, 3)
    if n % 3 == 0:
        s = '1' + s + '02'
    else:
        x = (n % 3) * 4
        s = s + convert(x, 3)
    r = int(s, 3)
    if r < 199:
        R.append(n)

print(max(R))
'''


#
# № 688 Джобс 16.11.2020 (Уровень: Средний)
# Автомат обрабатывает натуральное число N (0≤N≤255) по следующему алгоритму:
# 1) Строится восьми битная двоичная запись числа N.
# 2) Удаляются средние 4 цифры.
# 3) Полученное число переводится в десятичную запись и выводится на экран.
#
# Какое наибольшее число, меньшее 110, после обработки автоматом даёт результат 7?

'''
R = []
for n in range(0, 110):
    s = f'{n:b}'.zfill(8)
    s = s[:2] + s[-2:]
    r = int(s, 2)
    if n < 100:
        if r == 7:
            R.append(n)
print(max(R))
'''
# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 14]
# КЕГЭ  = []
# на следующем уроке: 6
