# region Домашка: ************************************************************

# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************


# 20808
'''
maxi = 0
for x in range(1, 2030+1):
    n = 7**170 + 7**100 - x
    M = []
    while n > 0:
        M.append(n % 7)
        n //= 7
    M.reverse()
    if M.count(0) >= maxi:
        maxi = M.count(0)
        print(x, maxi)
'''


# 20809
'''
def F(a, x):
    b = 60 <= x <= 80
    return (x % a == 0) or (b <= (x % 22 != 0))
R = []
for a in range(1, 10000):
    if all(F(a, x) for x in range(1,10000)):
        R.append(a)
print(max(R))
'''


# 20814
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            div.append(j)
            div.append(x // j)
    return sorted(set(div))


for x in range(500_000+1, 10**10):
    div = divisors(x)
    R = sum(div)
    if R % 100 == 99:
        print(x, R)
        input()
'''


# № 19778 (Уровень: Средний)

def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            div.append(j)
            div.append(x // j)
    return sorted(set(div))


for x in range(9_500_000+1, 10**10):
    div = [j for j in divisors(x) if len(divisors(j)) == 0]
    if len(div) > 0:
        F = sum(div) // len(div)
        if F % 813 == 0:
            print(x, F)
            input()

# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 7, 8, 9, 11, 12, 14, 15, 16, 17-, 18, 19-21, 22, 23, 25.1]
# КЕГЭ = [7, 11, 12, 17]
# на следующем уроке: 9, 10,


# Первый пробник 21.12.24:
# 4/8 -> 29 вторичных баллов +[1, 10, 16, 23] -[2, 4, 12, 15]

# Второй пробник 28.02.25:
# 10/29 -> 48 вторичных баллов +[1, 2, 4, 10, 12, 14, 15, 16, 23, 25] -[11]
