# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Тип 14 №8664
'''
print(bin(8**2020 + 4**2017 + 26 - 1)[2:].count('1'))
print(f'{(8**2020 + 4**2017 + 26 - 1):b}'.count('1'))
'''

# Тип 14 №26988
'''
x = 16**8 * 4**20 -4**5 - 64
R = []
while x > 0:
    R.append(x % 4)
    x //= 4
R.reverse()
print(R.count(3))
'''

'''
alphabet = sorted('1234567890QWERTYUIOPASDFGHJKLZXCVBNM')
print(alphabet[20])

print([0, 10, 20].count(0))  # 1
print('01020'.count('0'))  # 3
print('0AK'.count('0'))  # 1
'''


# № 16380 ЕГКР 27.04.24 (Уровень: Базовый)
'''
x = 4*3125**2019+3*625**2020 - 2*125**2021 + 25**2022 -4*5**2023-2024
R = []
while x > 0:
    R = [x % 25] + R
    x //= 25

# Вариант 1
print(len([i for i in R if i > 10]))

# Вариант 2
cnt = 0
for i in R:
    if i > 10:
        cnt += 1
print(cnt)
'''


# № 17633 Основная волна 19.06.24 (Уровень: Базовый)
'''
for x in range(2030+1):
    num = 6**260 + 6**160 + 6**60 - x
    R = []
    while num > 0:
        R.append(num % 6)
        num //= 6
    R.reverse()
    if R.count(0) == 202:
        print(x)
        break
'''


'''
alphabet = sorted('1234567890QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:16]:
    A = int(f'8{x}84{x}', 16)
    B = int(f'78{x}34', 16)
    if (A + B) % 23 == 0:
        print((A + B) // 23)
'''

# Тип 14 №48388
# Операнды арифметического выражения записаны в системах счисления с основаниями 12 и 14:
# x231y_12 + 78x98y_14.
'''
alphabet = sorted('1234567890QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:12]:
    for y in alphabet[:12]:
        A = int(f'{x}231{y}', 12)
        B = int(f'78{x}98{y}', 14)
        if (A + B) % 99 == 0:
            print((A + B) // 99)
'''
# 41428


# Сделаем проверку на "полный квадрат числа"
'''
n = int(input('n: '))
if n ** 0.5 == int(n**0.5):
    print('Есть полный квадрат')
else:
    print('Нет')
'''

# Тип 14 №55631
# В системе счисления с основанием p выполняется
# равенство y4y + y65 = xz33.
# Буквами x, y и z обозначены некоторые цифры из алфавита системы счисления с основанием p.
# Определите значение числа xyzp и запишите это значение в десятичной системе счисления.
'''
alphabet = sorted('1234567890QWERTYUIOPASDFGHJKLZXCVBNM')
for p in range(7, 36+1):
    for x in alphabet[:p]:
        for y in alphabet[:p]:
            for z in alphabet[:p]:
                if int(f'{y}4{y}', p) + int(f'{y}65', p) == int(f'{x}{z}33', p):
                    print(int(x+y+z, p))
'''


# Тип 14 №63030
'''
def my_int(num: list, base: int):
    return sum([x*base**i for i, x in enumerate(num[::-1])])

for x in range(40):
    for y in range(40):
        A = my_int([5, 7, x, 6, 9, 2, y, 1, 9], 40)
        B = my_int([y, x], 40)
        if A % 39 == 0 and (B**0.5 == int(B ** 0.5)):
            print(x, y, B)
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
