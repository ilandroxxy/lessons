# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 20814 Апробация 05.03.25 (Уровень: Базовый)
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):  # не считая единицы и самого числа.
        if x % j == 0:
            div += [j, x // j]  # x = 24, j = 4, 24 // 4 = 6
    return sorted(set(div))


cnt = 0
for x in range(500_000+1, 10**10):
    div = divisors(x)
    R = sum(div)
    if R % 10 == 9:
        print(x, R)
        cnt += 1
        if cnt == 5:
            break
'''

'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x // j]  # x = 24, j = 4, 24 // 4 = 6
    return sorted(set(div))


cnt = 0
for x in range(600_000+1, 10**10):
    div = [j for j in divisors(x) if j != 9 and j % 10 == 9]
    if len(div) > 0:
        print(x, min(div))
        cnt += 1
        if cnt == 5:
            break
'''


# № 19775 (Уровень: Средний)
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):  # не считая самого числа.
        if x % j == 0:
            div += [j, x // j]  # x = 24, j = 4, 24 // 4 = 6
    return sorted(set(div))


cnt = 0
for x in range(32_500_000+1, 10**10):
    div = [j for j in divisors(x) if len(divisors(j)) == 0]
    S = sum(div)
    if S != 0 and S % 145 == 0:
        print(x, S)
        cnt += 1
        if cnt == 7:
            break
'''

# № 19778 (Уровень: Средний)
'''
def divisors(x):
    div=[]
    for j in range(2,int(x**0.5)+1):
        if x%j==0:
            div+=[j,x//j]
    return sorted(set(div))


cnt=0
for x in range(9_500_000+1,10**10):
    div=[j for j in divisors(x) if len(divisors(j))==0]
    if len(div)>0:
        F=sum(div)//len(div)
        if F%813==0:
            print(x,F)
            cnt+=1
            if cnt==5:
                break
'''


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 3, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, 23, 25]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Лиза 11/29 -> 54 вторичных баллов +[1-2, 4, 5, 10, 12-14, 16, 23, 25] -[3, 6, 8]

# Второй пробник 28.02.25:
# Лиза 17/29 -> 70 вторичных баллов +[1-17, 23, 25] -[]
