# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 17546 Основная волна 08.06.24 (Уровень: Базовый)
'''
R = []
for n in range(1, 12+1):
    s = f'{n:b}'  # s = bin(n)[2:]
    if n % 2 == 0:
        s = '10' + s
    else:
        s = '1' + s + '01'
    r = int(s, 2)
    R.append(r)
print(max(R))
'''


# № 16371 ЕГКР 27.04.24 (Уровень: Базовый)
'''
R = []
for n in range(1, 1000):
    s = f'{n:b}'
    if n % 3 == 0:
        s = s + s[-2:]
    else:
        x = (n % 3) * 3
        s = s + f'{x:b}'
    r = int(s, 2)
    if r >= 195:
        R.append(r)
print(min(R))
'''

'''
def convert(n, b):  # n - number, b - base
    r = ''
    while n > 0:
        r += str(n % b)
        n //= b
    return r[::-1]
'''

'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):  # n - number, b - base
    r = ''
    while n > 0:
        r = alphabet[n % b] + r
        n //= b
    return r


print(convert(213435235, 25))
'''

'''
def convert(n, b):  # n - number, b - base
    r = ''
    while n > 0:
        r = str(n % b) + r
        n //= b
    return r


for n in range(1, 1000):
    s = convert(n, 3)
    if n % 3 == 0:
        s = '1' + s + '02'
    else:
        x = (n % 3) * 4
        s = s + convert(x, 3)
    r = int(s, 3)
    if r < 199:
        print(n)
'''

'''
for b in range(1, 1000):
    n = bin(b)[2:]   # забыл [2:]
    if n.count('1') % 2 == 0:  # надо писать .count('1')
        n = n + '0'
        n = n[2:]
        n = '10' + n
        # n = '10' + n[2:] + '0'
    else:
        n = n + '1'
        n = n[2:]
        n = '11' + n
    r = int(n, 2)  # забыл ,2
    if r > 50:
        print(b)
        break
'''


# № 16381 ЕГКР 27.04.24 (Уровень: Базовый)
'''
def F(x, A):
    return (x % A != 0) <= ((x % 28 == 0) <= (x % 49 != 0))

for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)



for A in range(1, 1000):
    if all(((x % A != 0) <= ((x % 28 == 0) <= (x % 49 != 0))) for x in range(1, 10000)):
        print(A)
'''


# № 14656 Открытый курс "Слово пацана" (Уровень: Базовый)
'''
def F(x, y, A):
    return ((x > 68) or (y > 89)) or (2 * x - 7 * y < A)

for A in range(1000):
    if all(F(x, y, A) for x in range(100) for y in range(100)):
        print(A)
        break
'''


'''
def F(x, a1, a2):
    P = 15 <= x <= 40
    Q = 21 <= x <= 63
    A = a1 <= x <= a2
    return P <= ((Q and (not A)) <= (not P))




R = []
M = [x / 4 for x in range(10 * 4, 80 * 4)]
print(M)
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(min(R))
'''
# Ответ: 19.0 -> 19

'''
for x in range(2030+1):
    n = 3**100 - x
    base = 3
    M = []
    while n > 0:
        M.append(n % base)
        n //= base
    M.reverse()
    if M.count(0) == 5:
        print(x)


for x in range(2030+1):
    n = 3**100 - x
    base = 3
    M = ''
    while n > 0:
        M += str(n % base)
        n //= base
    M = M[::-1]
    if M.count('0') == 5:
        print(x)
'''

'''
n = 4 * 3125 ** 2019 + 3 * 625 ** 2020 - 2 * 125 ** 2021 + 25 ** 2022 - 4 * 5 ** 2023 - 2024
r = ''
while n > 0:
    r += str(n % 25)
    n //= 25
r = r[::-1]
print(r.count('0'))  # 2016
print(r)


n = 4 * 3125 ** 2019 + 3 * 625 ** 2020 - 2 * 125 ** 2021 + 25 ** 2022 - 4 * 5 ** 2023 - 2024
M = []
while n > 0:
    M.append(n % 25)
    n //= 25
M.reverse()
print(M)
print(M.count(0))  # 2015
'''


# № 17534 Основная волна 07.06.24 (Уровень: Базовый)
# A. Вычти 1
# B. Найти целую часть от деления на 2
# Сколько существует программ, для которых при исходном
# числе 30 результатом является число 1
# и при этом тракетория вычислений содержит число 8?
'''
def F(a, b):
    if a < b:
        return 0
    elif a == b:
        return 1
    else:
        return F(a-1, b) + F(a//2, b)

print(F(30, 8) * F(8, 1))


# Вариант 2

def F(a, b):
    if a <= b:
        return a == b
    return F(a-1, b) + F(a//2, b)

print(F(30, 8) * F(8, 1))


print(True + True + False)
'''

'''
def F(x, a1, a2):
    P = 15 <= x <= 40
    Q = 21 <= x <= 63
    A = a1 <= x <= a2
    return (P) <= (((Q) and (not A)) <= (not P))


R = []
M = [x / 4 for x in range(10 * 4, 80 * 4)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(min(R))  # 19.0 -> 19
'''

#
# № 17521 Основная волна 07.06.24 (Уровень: Базовый)
# Определите количество восьмеричных пятизначных чисел,
# которые не начинаются с нечётных цифр,
# не оканчиваются цифрами 2 или 6, а также содержат
# не более двух цифр 7.
'''
s = '01234567'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    num = a + b + c + d + e
                    if a != '0' and a not in '1357':
                        if e not in '26' and num.count('7') <= 2:
                            cnt += 1
print(cnt)
'''

'''
s = sorted('ФОКУС')
num = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    word = a + b + c + d + e
                    num += 1
                    if 'Ф' not in word and word.count('У') == 2:
                        print(num, word)
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1+, 2*+, 3, 4+, 6+, 7, 9*+, 10+, 11, 18+, 19-21, 22+]
# КЕГЭ  = [2, 5, 12, 14, 15, 16, 23]
# на следующем уроке:
