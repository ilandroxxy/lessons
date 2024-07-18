# region Домашка: ******************************************************************

'''
L = [int(x) for x in input()]
L.reverse()
for x in L:
    print(x)
'''

'''
m = int(input())  # 24
x = 0
for i in range(1, int(m**0.5) + 1):
    if m % i == 0:  # 4
        x += i
        x += m // i  # 24 // 4 = 6
print(x)
'''


'''
a = int(input())
b = int(input())
for i in range(a, b+1):
    x = i
    flag = True
    if x == 1:
        flag = False
    for j in range(2, x):
        if x % j == 0:
            flag = False
            break
    if flag == True:
        print(x)
'''

'''
def prime(x):
    if x == 1:
        return False
    for j in range(2, x):
        if x % j == 0:
            return False
    return True

a = int(input())
b = int(input())
for x in range(a, b+1):
    if prime(x):
        print(x)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = []
# КЕГЭ  = []
# на следующем уроке: Создать учебный репозиторий через github
