# region Домашка: ******************************************************************

#№ 23763 Демоверсия 2026(Уровень: Базовый)

def divisors(x):
    d = []
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d += [i, x // i]
    return sorted(set(d))

cnt = 0
for i in range(800_000+1, 10**10):
    d = divisors(i)
    if len(d) > 0:
        M = max(d) + min(d)
        if M % 10 == 4:
            print(i, M)
            cnt += 1
            if cnt == 5:
                break


#№ 23282 Основная волна 11.06.25(Уровень: Средний)
'''
def divisors(x):
    d = []
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d += [i, x // i]
    return sorted(set(d))

cnt = 0
for i in range(5_400_000+1, 10**10):
    d = [j for j in divisors(i) if len(divisors(j)) == 0]
    if len(d) >= 2:
        M = min(d) + max(d)
        if (M > 60_000 and str(M) == str(M)[::-1]):
            print(i, M)
            cnt += 1
            if cnt == 5:
                break
'''


#№ 23382 Резервный день 19.06.25(Уровень: Средний)
'''
from itertools import product, repeat
def divisors(x):
    d = []
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d += [i, x // i]
    return sorted(set(d))

cnt = 0
for i in range(6_651_220+1, 10**10):
    d = [j for j in divisors(i) if len(divisors(j)) == 0 and str(j).count('2') == 1]
    if len(d) > 0:
        for p in product(d, repeat = 2):
            if p[0] * p[1] == i:
                print(i, max(p))
                cnt += 1
                break
        if cnt == 5:
            break
'''


#№ 28711 (Уровень: Базовый)

from itertools import permutations
def divisors(x):
    d = []
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d += [i, x // i]
    return sorted(set(d))
cnt = 0
for i in range(2_400_000+1, 10**10):
    d = [j for j in divisors(i) if len(divisors(j)) == 0 and (str(j).count('7') >= 1 or str(j).count('4') >= 1)]
    if len(d) > 0:
        for p in permutations(d, r = 3):
            if p[0] * p[1] * p[2] == i:
                print(i, max(p))
                cnt += 1
                break
        if cnt == 5:
            break



# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************





# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [5, 25]
# КЕГЭ = []
# на следующем уроке:



