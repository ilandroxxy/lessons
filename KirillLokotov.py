# region Домашка: ************************************************************

# № 227 (Уровень: Базовый)
# https://stepik.org/lesson/1038703/step/12?unit=1062210
'''
print(bin(4 ** 2015 + 2 ** 2015 - 15)[2:].count('1'))

# i  012345
s = '345678'

# СРЕЗ [ START : STOP-1 :  STEP ]
print(s[:2])  # 34
print(s[2:])  # 5678
'''


# № 17555 Основная волна 08.06.24 (Уровень: Базовый)
# https://stepik.org/lesson/1038703/step/10?unit=1062210
'''
z = []
for x in range(2030+1):
    n = 7 ** 91 + 7 ** 160 - x
    b = 7
    R = []
    while n > 0:
        R.append(n % b)
        n //= b
    R = R[::-1]
    if R.count(0) == 70:
        z.append(x)
print(max(z))
'''


# № 6575 (Уровень: Базовый)
# https://stepik.org/lesson/1038703/step/7?unit=1062210
'''
R = []
n = 766**66 + 15 ** 13 - 22
b = 13
while n > 0:
    R.append(n % b)
    n //= b
R = R[::-1]
print(R.count(12))
'''

# 9 - 9
# 10 - A
# 11 - B
# 12 - C

# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************


# Задание 14 https://education.yandex.ru/ege/task/08f6e0f1-0ce1-42d4-a73e-2e9d1e334a55
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:17]:  # 0 1 2 3 4 5 6 7 8 9 A B C D E F G
    A = int(f'5432{x}67', 17)
    B = int(f'302{x}', 17)
    if (A + B) % 19 == 0:
        print(A + B)
'''


# Задание 14 https://education.yandex.ru/ege/task/376fdf5f-fe0f-49fe-873c-698126bf1ccd
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:24]:
    A = int(f'4M{x}F', 24)
    B = int(f'265AFDN{x}', 24)
    C = int(f'N4{x}931B3L', 24)
    D = int(f'NG{x}4F', 24)
    E = int(f'FKJB5{x}IK', 24)
    if (A + B + C + D + E) % 23 == 0:
        print((A + B + C + D + E) // 23)
'''


# Задание 14 https://education.yandex.ru/ege/task/ae1e6ebd-512c-4ea3-9bb6-6862096652d8
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
R = []
for z in alphabet[:35]:
    for y in alphabet[:19]:
        A = int(f'3B{z}4C', 35)
        B = int(f'A12F{y}', 19)
        if (A + B) % 7 == 0:
            R.append(alphabet.index(z) + alphabet.index(y))
print(max(R))


print(int('23423', 40))
# ValueError: int() base must be >= 2 and <= 36, or 0
'''



# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 14]
# КЕГЭ = []
# на следующем уроке:
