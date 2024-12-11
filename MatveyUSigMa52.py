# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# https://stepik.org/lesson/1038816/step/4?unit=1062780
'''
def divisors(x):
    div = []
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            div.append(i)
            div.append(x // i)
    return sorted(set(div))


for x in range(190201, 190261):
    chet = [i for i in divisors(x) if i % 2 == 0]
    if len(chet) == 4:
        print(chet[-1], chet[-2])
'''

'''
def divisors(x):
    div = []
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            div.append(i)
            div.append(x // i)
    return sorted(set(div))


k = 0
for x in range(10 ** 9 + 1, 10 ** 20):
    if str(x) == str(x)[::-1]:
        d = divisors(x)
        if len(d) > 0:
            if max(d) % 7 == 0 :
                print(x, max(d))
                k = k + 1
                if k == 5:
                    break
'''

'''
n = int(input())
if str(n) == str(n)[::-1]:
    print('Число палиндром')
else:
    print('Не палиндром')
'''

# № 2590 (Уровень: Базовый)
'''
def divisors(x):
    div = []
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            div.append(i)
            div.append(x // i)
    return sorted(set(div))


for x in range(6080068, 6080176 + 1):
    d = divisors(x)
    if len(d) == 0:
        print(x)
'''


'''
def divisors(x):
    div = []
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            div.append(i)
            div.append(x // i)
    return sorted(set(div))


k = 0
for x in range(800_000+1, 10**10):
    d = [j for j in divisors(x) if j % 10 == 9 and j != 9]
    if len(d) > 0:
        print(x, min(d))
        k += 1
        if k == 5:
            break
'''

'''
def divisors(x):
    div = []
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            div.append(i)
            div.append(x // i)
    return sorted(set(div))


k = 0
for x in range(700_000+1, 10**10):
    d = divisors(x)
    if len(d) >= 2:
        M = min(d) + max(d)
        if M % 10 == 4:
            print(x, M)
            k += 1
            if k == 5:
                break
'''


def divisors(x):
    div = []
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            div.append(i)
            div.append(x // i)
    return sorted(set(div))


k = 0
for x in range(700_000+1, 10**10):
    d = divisors(x)
    if len(d) >= 2:
        M = min(d)+max(d)
        if M%10==4:
            print(M)
            k += 1
            if k == 5:
                break
# endregion Урок: ********************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 14, 25]
# КЕГЭ  = []
# на следующем уроке:
