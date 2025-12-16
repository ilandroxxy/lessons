# region Домашка: ******************************************************************

# https://stepik.org/lesson/1038816/step/15?unit=1062780
'''
def prime_at_divisors(x):
    d = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            d += [j, x // j]
    return sorted(set(d))

def divisors(x):
    d = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            if len(prime_at_divisors(j)) == 0 and len(prime_at_divisors(x // j)) == 0:
                if str(j).count('6') == 1 and str(x // j).count('6') == 1:
                    d += [j, x // j]
    return sorted(d)

cnt = 0
for x in range(6_086_055+1, 10**10):
    d = divisors(x)
    if len(d) >= 2:
        print(x, max(d))
        cnt += 1
        if cnt == 5:
            break
'''


# https://stepik.org/lesson/1038816/step/4?unit=1062780
'''
def div(x):
    d = []
    for j in range(1, int(x ** 0.5)+1):
        if x % j == 0:
            d += [j, x // j]
    return sorted(set(d))

for x in range(190201, 190260+1):
    d = [j for j in div(x) if j % 2 == 0]
    if len(d) == 4:
        print(d[-1], d[-2])
'''


# https://stepik.org/lesson/1038816/step/5?unit=1062780
'''
def divisors(x):
    d = []
    for j in range(2, int(x**0.5)+1):  # (отличный от 1 и самого числа)
        if x % j == 0:
            d += [j, x // j]
    return sorted(set(d))

cnt = 0
for x in range(10**9+1, 10**10):
    if str(x) == str(x)[::-1]:
        d = divisors(x)
        if len(d) > 0:
            if max(d) % 7 == 0:
                print(x, max(d))
                cnt += 1
                if cnt == 5:
                    break
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************



'''
# Открыли и считали данные для 24 номера:
s = open('0. files/24.txt').readline()

# Открыли и считали данные для 9 номера:

for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(',')]
    
# Открыли и считали данные для 27 номера:

for s in open('0. files/27A.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
'''

# Открыли и считали данные для 17 номера:
M = [int(s) for s in open('0. files/17.txt')]


# Три прототипа 17 номера:
'''
# i  0  1  2  3  4    
M = [1, 2, 3, 4, 5]

# 1. Под парой подразумевается два идущих подряд элемента последовательности
# 12 23 34 45
for i in range(len(M)-1):
    x, y = M[i], M[i+1]

# 2. Под тройкой подразумевается три идущих подряд элемента последовательности
# 123 234 345
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]

# 3. Под парой подразумевается два различных элемента последовательности
# 12 13 14 15
# 23 24 25
# 34 35
# 45
for i in range(len(M)):
    for j in range(i+1, len(M)):
        x, y = M[i], M[j]
'''


'''
print(len(str(1234)))  # 4
print(len(str(-1234)))  # 5
print(len(str(abs(-1234))))  # 4

print(123 % 100)  # 23
print(-123 % 100)  # 77
print(abs(-123) % 100)  # 23
'''


# № 25356 ЕГКР 13.12.25 (Уровень: Базовый)
'''
M = [int(s) for s in open('0. files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 4]
B = [x for x in M if abs(x) % 100 == 30]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x in A) + (y in A) + (z in A) == 0:
        if (x + y + z) > max(B):
            R.append(x + y + z)
print(len(R), max(R))
'''


# № 19249 ЕГКР 21.12.24 (Уровень: Базовый)
'''
M = [int(s) for s in open('0. files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 5 and abs(x) % 100 == 43]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x in A) + (y in A) + (z in A) >= 1:
        if (x**2 + y**2 + z**2) <= max(A) ** 2:
            R.append(x**2 + y**2 + z**2)
print(len(R), min(R))
'''






# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 8, 13, 14, 15, 16, 17, 19-21, 23, 25]
# КЕГЭ = []
# на следующем уроке: 9, 27
