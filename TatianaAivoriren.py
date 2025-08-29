# region Домашка: ******************************************************************

'''
n = int(input())
b = 3
r = ''
while n > 0:
    r += str(n % b)
    n //= b
print(r[::-1])
'''


n = 293048390248
b = 16
# 8 6 5 4 9 14 12 15
# 10 -> A
# 11 -> B
# 12 -> C
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]


print(convert(8, 2))  # 1000
print(int('1000', 2))  # 8

print(convert(8, 3))  # 22
print(int('22', 3))  # 8

print(convert(10**8, 16))  # 5F5E100
print(int('5F5E100', 16))  # 10**8

# Функция int - делает обратный перевод из b-ой системы в 10-ю
'''

'''
s = input()
digit = False
for char in s:
    if char.isdigit():
        digit = True
        print('Да')
        break
if digit == False:
    print('Нет')
'''


# Встроенные функции перевода из 10-й системы
'''
n = 8

# Перевод в 2-ю систему счисления
print(bin(n))  # 0b1000
print(bin(n)[2:])  # 1000
print(f'{n:b}')  # 1000

# Перевод в 8-ю систему счисления
print(oct(n)[2:])  # 10
print(f'{n:o}')  # 10


# Перевод в 16-ю систему счисления
print(hex(n)[2:])  # 8
print(f'{n:x}')  # 8 
'''


# https://stepik.org/lesson/1309455/step/8?unit=1324571
'''
text = list(input())
while '@' in text:
    text.remove('@')
print(''.join(text))
'''



# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 23754 Демоверсия 2026 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

for x in range(1, 3000):
    n = 9 * 11**210  + 8 * 11**150 - x
    r = convert(n, 11)
    if r.count('0') == 60:
        print(x)
'''

# № 21709 ЕГКР 19.04.25 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

R = []
for x in range(1, 3000):
    n = 4**210 + 4**110 - x
    r = convert(n, 4)
    R.append(r.count('0'))
    if r.count('0') == 105:
        print(x)
        break
print(max(R))
'''


# № 17869 Демоверсия 2025 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

n = 3 * 3125  8 + 2 * 625  7 - 4 * 625  6 + 3 * 125  5 - 2 * 25 ** 4 - 2025
r = convert(n, 25)
print(r.count('0'))
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


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = []
# КЕГЭ  = []
# на следующем уроке: