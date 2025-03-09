# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


def is_cube(n):
    root = round(n * (1/3))
    return root * 3 == n


def divisors(n):
    div=[]
    for j in range(2, int(n**0.5)+1):
        if n%j==0:
            div+=[j, n//j]
    div+=[n]
    return sorted(set(div))


for x in range(228224, 531136):
    d = [j for j in divisors(x) if j % 2 != 0 and is_cube(j)]

    if len(d) >= 4:
        print(d)
        print(len(d), max(d))


'''
def divisors(n):
    div=[]
    for j in range(2, int(n**0.5)+1):
        if n%j==0:
            div+=[j, n//j]
    div+=[n]
    return sorted(set(div))

# Генерация кубов нечетных чисел
cubes = {x*3 for x in range(1, int(531135*(1/3)) + 1) if x % 2 != 0}
print(cubes)
'''
# Перебор чисел в заданном диапазоне
# for num in range(228224, 531136):
#     div = divisors(num)
#     cube_divisors = [j for j in div if j in cubes]
#     if len(cube_divisors) >= 4:
#         print(len(cube_divisors), max(cube_divisors))


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14, 15, 16, 23, 25]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Egor 7/10 -> 40 вторичных баллов +[1, 4, 5, 10, 12, 13] -[2, 6, 8]

# Второй пробник 28.02.25:
# Egor 12/16 -> 56 вторичных баллов +[1-4, 6, 7, 11-14, 16, 23] -[5, 8, 10, 15]
