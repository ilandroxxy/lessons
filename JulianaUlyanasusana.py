# region Домашка: ******************************************************************

'''
for s in open('0. files/9.csv'):
    M = sorted([int(x) for x in s.split(',')])
    copied2 = [x for x in M if M.count(x) == 2]
    not_copied = [x for x in M if M.count(x) == 1]
    if len(copied2) == 4 and len(not_copied) == 2:
        if M.count(max(M)) == 1:
            if M[0] * M[-1] > sum(M[1:-1]):
                print(sum(M))
                break
'''


cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(',')]
    if (sum(M)//7) in M:
        cnt+=1
print(cnt)

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
# ФИПИ = [2, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, 23, 25]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Ульяна 5/8 -> 14 вторичных баллов +[1, 2, 4, 6, 12] -[5, 13, 14]
