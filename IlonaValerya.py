# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# 17558
'''
M = [int(x) for x in open('0. files/17.txt')]
A = [x for x in M if abs(x) % 32 == 0]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x < 0) + (y < 0) >= 1:
        if (x + y) < len(A):
            R.append(x + y)
print(len(R), max(R))
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, 23, 25]
# КЕГЭ  = []
# на следующем уроке:
