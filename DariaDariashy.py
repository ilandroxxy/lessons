# region Домашка: ******************************************************************

# КЕГЭ № 4317 (Уровень: Сложный) 🌶
#
# Автомат обрабатывает натуральное число N по следующему алгоритму:
#
# 1. Строится пятеричная запись числа N.
#  2. К полученной записи дописываются разряды. Если последняя цифра в пятеричной записи четная,
#  справа дописывается 2, если нечетная – слева дописывается 2 и справа 3.
#  3. Результат переводится в десятичную систему и выводится на экран.
# В результате работы автомата на экране появилось число, меньшее 1000.
# Для какого наибольшего значения N данная ситуация возможна?
'''
alphabet = sorted('1234567890qwertyuiopasdfghjklzxcvbnm')


def convert(n, b):
    r = ''
    while n > 0:
        r = alphabet[n % b] + r
        n //= b
    return r


R = []
for n in range(1, 10000):
    s = convert(n, 5)
    # if int(s[-1]) % 2 == 0:
    if s[-1] in '02468':
        s = s + '2'
    else:
        s = '2' + s + '3'
    r = int(s, 5)
    if r < 1000:
        R.append(n)
print(max(R))
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
# from string import *
# alphbaet = digits + ascii_uppercase

alphabet = sorted('1234567890qwertyuiopasdfghjklzxcvbnm')


def convert(n, b):  # n - number, b - base
    r = ''
    while n > 0:
        # r += alphabet[n % b]
        r = alphabet[n % b] + r
        n //= b
    # return r[::-1]
    return r


print(convert(123456789, 16))  # 75bcd15
print(int('75bcd15', 16))  # 123456789
'''

# Тип 14 №9766
# Значение арифметического выражения: 9**8 + 3**8 - 2 – записали в системе счисления с основанием 3.
# Сколько цифр «2» содержится в этой записи?
'''
alphabet = sorted('1234567890qwertyuiopasdfghjklzxcvbnm')


def convert(n, b):
    r = ''
    while n > 0:
        r = alphabet[n % b] + r
        n //= b
    return r


x = 9**8 + 3**8 - 2
s = convert(x, 3)
print(s.count('2'))
'''

# Вариант 2
'''
x = 9**8 + 3**8 - 2
s = []
while x > 0:
    s.append(x % 3)
    x //= 3
s.reverse()
print(s.count(2))
'''


# № 16380 ЕГКР 27.04.24 (Уровень: Базовый)
# Определите в 25-ричной записи числа количество цифр с числовым значением, превышающим 10:
'''
x = 4*3125**2019 + 3 * 625**2020 - 2*125**2021 + 25**2022 - 4 * 5**2023 - 2024
s = []
while x > 0:
    s.append(x % 25)  
    x //= 25
s.reverse()  # .reverse() это метод списков, который разворачивает список в обратном порядке 
# s = s[::-1]
print(len([x for x in s if x > 10]))
'''

'''
alphabet = sorted('1234567890qwertyuiopasdfghjklzxcvbnm')


def convert(n, b):
    r = ''
    while n > 0:
        r = alphabet[n % b] + r
        n //= b
    return r


x = 4*3125**2019 + 3 * 625**2020 - 2*125**2021 + 25**2022 - 4 * 5**2023 - 2024
s = convert(x, 25)
print(len([x for x in s if x > 'A']))
'''


# № 17633 Основная волна 19.06.24 (Уровень: Базовый)
'''
for x in range(2030+1):
    n = 6**260 + 6**160 + 6**60 - x
    s = []
    while n > 0:
        s.append(n % 6)
        n //= 6
    s.reverse()
    if s.count(0) == 202:
        print(x)
        break
'''


# Тип 14 №48384
# Операнды арифметического выражения записаны в системах счисления с основаниями 9 и 11:
# 88x4y_9 + 7x44y_11
'''
alphabet = sorted('1234567890qwertyuiopasdfghjklzxcvbnm')
for x in alphabet[:9]:
    for y in alphabet[:9]:
        A = int(f'88{x}4{y}', 9)
        B = int(f'7{x}44{y}', 11)
        if (A + B) % 61 == 0:
            print((A + B) // 61)
'''


# Тип 14 №64899
# zxyx4 + xy658 = wzx73
'''
alphabet = sorted('1234567890qwertyuiopasdfghjklzxcvbnm')
for p in range(9, 36+1):
    for x in alphabet[:p]:
        for y in alphabet[:p]:
            for z in alphabet[:p]:
                for w in alphabet[:p]:
                    if int(z+x+y+x+'4', p) + int(x+y+'658', p) == int(f'{w}{z}{x}73', p):
                        print(int(x+y+z+w, p))
'''


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [5, 14]
# КЕГЭ  = []
# на следующем уроке:
