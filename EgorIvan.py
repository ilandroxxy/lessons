# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Статград 23.10.25 вариант 2 (https://disk.yandex.ru/i/6Z6cTKKeb8lQNQ) Номер 7
'''
# V_music = a * b * c * t
a = 2
b = 56000
c = 15
t = 27 * 60 + 27
V_music = a * b * c * t

U = 367_217_732  # бит/с
T = 332  # с
V_all = U * T

print(V_all - V_music)   # 28 заголовков
print((V_all - V_music) / 28)  # 1 заголовок в бит
print(((V_all - V_music) / 28) / 2**13)  # 1 заголовок в бит
'''


# Статград 23.10.25 вариант 2 (https://disk.yandex.ru/i/6Z6cTKKeb8lQNQ) Номер 11
'''
sym = 128
byte = 29 * 2**20 / 335_793
print(byte)  # 90.557 -> 90 (отведено не более 29 Мбайт)
bit = 90 * 8
i = bit / sym
print(i)  # 5.625 -> 5 (отведено не более 29 Мбайт)
print(f'Максимально возможную мощность алфавита: {2 ** 5}')
print(f'Минимальная возможную мощность алфавита: {2 ** (5 - 1) + 1}')
'''


# Статград 23.10.25 вариант 2 (https://disk.yandex.ru/i/6Z6cTKKeb8lQNQ) Номер 14
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

L = []
for x in range(1, 7290+1):
    n = 27 ** 298 + 27 ** 269 - x
    s = convert(n, 27)
    L.append(s.count('0'))
print(max(L))
'''

# натуральное число range(1, ...)
# целое неотрицательное число range(0, ...)
# целое положительное число range(1, ...)


# Статград 23.10.25 вариант 2 (https://disk.yandex.ru/i/6Z6cTKKeb8lQNQ) Номер 9
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied1 = [x for x in M if M.count(x) == 1]
    if 3 <= M.count(max(M)) <= 4 and 4 <= len(copied1) <= 5:
        if max(copied1) + min(copied1) <= sum(copied1) - max(copied1) - min(copied1):
            cnt += 1
print(cnt)
'''

# Статград 23.10.25 вариант 2 (https://disk.yandex.ru/i/6Z6cTKKeb8lQNQ) Номер 25
'''
def divisors(x):
    d = []
    for j in range(2, int(x ** 0.5)+1):  # не считая самого числа.
        if x % j == 0:
            d.append(j)
            d.append(x // j)
    return sorted(set(d))

cnt = 0
for x in range(1_475_000-1, -1, -1):
    d = [j for j in divisors(x) if len(divisors(j)) == 0]
    if len(d) > 0:
        S = sum(d)
        if S != 0 and S <= 42000 and S % 6 == 0:
            print(x)
            cnt += 1
            if cnt == 5:
                break
'''


# Статград 23.10.25 вариант 2 (https://disk.yandex.ru/i/6Z6cTKKeb8lQNQ) Номер 17
'''
M = [int(x) for x in open('files/17.txt')]
A = [x for x in M if x < 0 and abs(x) % 9 == 0 and len(str(abs(x))) == 4]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i + 1]
    # в которых есть только одно отрицательное число
    if (x < 0) + (y < 0) == 1:
        if (x + y) > max(A):
            R.append(x ** 2 + y ** 2)
print(len(R), min(R))
'''


# # endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 25, 27]
# КЕГЭ = []
# на следующем уроке: 9, 17, 12, 22, 27
