# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
import time
start = time.time()

# def divisors(x):  # 24 [1, ..., 24]
#     div = []
#     for j in range(1, x+1):
#         if x % j == 0:
#             div.append(j)
#     return div


def divisors(x):  # 24 [1, ..., 24]
    div = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x//j]
            # div.append(j)
            # div.append(x // j)
    return sorted(set(div))


print(divisors(24))
print(divisors(16))
print(divisors(100_000_000))

print(time.time() - start)  # 2.767  -> 0.00039
'''


# № 17564 Основная волна 08.06.24 (Уровень: Средний)
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):  # не считая единицы и самого числа.
        if x % j == 0:
            div += [j, x//j]
    return sorted(set(div))


k = 0
for x in range(700_000 + 1, 10**10):
    d = divisors(x)
    if len(d) >= 2:
        M = min(d) + max(d)
        if M % 10 == 4:
            print(x, M)
            k += 1
            if k == 5:
                break
'''

# № 17642 Основная волна 19.06.24 (Уровень: Базовый)
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x//j]
    return sorted(set(div))


k = 0
for x in range(800_000 + 1, 10**10):
    d = [j for j in divisors(x) if j % 10 == 9 and j != 9]
    if len(d) > 0:
        print(x, min(d))
        k += 1
        if k == 5:
            break
'''


# № 16389 ЕГКР 27.04.24 (Уровень: Базовый)



for s in open('files/9.txt'):
    M = list(map(int, s.split()))
    print(M)
# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 13, 14, 25]
# КЕГЭ  = []
# на следующем уроке:
