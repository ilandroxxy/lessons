# region Домашка: ************************************************************

# https://stepik.org/lesson/1038803/step/4?unit=1062776
'''
def F(a, b):
    if a <= b:
        return a == b
    return F(a-2, b) + F(a // 2, b)

print(F(32, 14) * F(14, 1))
'''

# endregion Домашка: *********************************************************
# #
# #
# region Урок: ************************************************************

# https://education.yandex.ru/ege/task/8f13d075-e784-4654-ae10-7d109cee90e9
'''
# Вариант 1
def F(x, y, A):
    return (3*x + y > A) and (y < x) and (x < 30)

for A in range(1000):
    flag = True
    for x in range(100):
        for y in range(100):
            if F(x, y, A) == True:
                flag = False
                break
    if flag == True:
        print(A)
        break

# Вариант 2
def F(x, y, A):
    return (3*x + y > A) and (y < x) and (x < 30)

for A in range(1000):
    k = 0
    for x in range(100):
        for y in range(100):
            if F(x, y, A) == False:
                k += 1
    if k == 10000:
        print(A)
        break

# Вариант 3
def F(x, y, A):
    return (3*x + y > A) and (y < x) and (x < 30)

for A in range(1000):
    if all(F(x, y, A) == False for x in range(100) for y in range(100)):
        print(A)
        break


# Вариант 4.1
def F(x, y, A):
    return (3*x + y > A) and (y < x) and (x < 30)

R = []
for A in range(1000):
    if all(F(x, y, A) == False for x in range(100) for y in range(100)):
        R.append(A)
print(min(R))

# Вариант 4.2
print(min([A for A in range(1000) if all(((3*x + y > A) and (y < x) and (x < 30)) == False for x in range(100) for y in range(100))]))
'''


# https://education.yandex.ru/ege/task/cf61f112-a1cf-40f3-9fef-d1a97ba29075
'''
def F(A, x):
    return (((x % A == 0) and (x % 375 == 0)) <= (x % 100 == 0)) and (A > 10)

for A in range(1, 1000):
    if all(F(A, x) for x in range(10000)):
        print(A)
        break
'''

# https://education.yandex.ru/ege/task/e4ee1ff0-c06e-478d-b397-be872b454f46
'''
def F(x, A):
    return (x & 91 == 0) or ((x & 77 == 0) <= (x & A != 0))

for A in range(0, 1000):
    if all(F(x, A) for x in range(10000)):
        print(A)
        break
'''

'''
def F(A, x):
    return ((x % 10 == 0) and (x % 26 == 0) and (x >= 300)) <= (A <= x)


for A in range(0, 1000000):
    if all(F(A, x) for x in range(10000)):
        print(A)
'''


# https://education.yandex.ru/ege/task/691e4108-0628-4175-90d1-827c5a8b5a94
'''
def F(A, x):
    B = 70 <= x <= 80
    return (x % 12 == 0) and B and (x % A != 0)


cnt = 0
for A in range(1, 1000):
    if all(F(A, x) == False for x in range(1, 10000)):
        cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/task/1452a6ee-c08b-4f20-8169-6fe1a281193d
'''
def F(x, a1, a2):
    P = 15 <= x <= 40
    Q = 21 <= x <= 63
    A = a1 <= x <= a2
    return P <= ((Q and (not A)) <= (not P))


R = []
M = [x / 4 for x in range(10 * 4, 70 * 4)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(min(R))  # 19.0
'''

# https://education.yandex.ru/ege/task/21fef5ec-ac54-4333-b360-20a22600f6c8
'''
def F(x, a1, a2):
    P = 13 <= x <= 19
    Q = 17 <= x <= 23
    A = a1 <= x <= a2
    return (not(not P) <= Q) <= (A <= ((not Q) <= P))


R = []
M = [x / 4 for x in range(10 * 4, 30 * 4)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(max(R))  # 10.0
'''

# https://education.yandex.ru/ege/task/219c0d8e-bf34-4ec2-8f11-cf4d06a6fae7

def F(x, a1, a2):
    B = 15 <= x <= 40
    C = 21 <= x <= 63
    A = a1 <= x <= a2
    return (not B) <= ((C and (not A)) <= B)


R = []
M = [x / 4 for x in range(10 * 4, 70 * 4)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(min(R))  # 22.75 -> 23


# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# ФИПИ = [2, 5, 6, 8, 12, 13, 14, 15, 16, 23, 25]
# КЕГЭ = []
# на следующем уроке:
