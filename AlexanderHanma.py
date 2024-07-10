# region Домашка: ******************************************************************
'''
n = int(input())
summ = 0
for i in range(1, n + 1):
    v = i ** 3
    if v % 10 == 3 or v % 10 == 5 or v % 10 == 9:
        summ += i
print(summ)
'''

'''
a = int(input())
b = int(input())
for i in range(a, b + 1):
    flag = True
    for g in range(2, i):
        if i % g == 0:
            flag = False
            break
    if flag == True:
        print(i)
'''
# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (w <= x) and ((y <= z) == (x <= y))
                if F == 1:
                    print(x, y, z, w)
'''


# Тип 2 №68503

print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F=(x==(y<=z)) and ((not w )<=(x==y))
                if F == 1:
                    print(x, y, z, w)

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = []
# КЕГЭ  = []
# на следующем уроке:
