# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    if len(M) != len(set(M)):
        if M.count(max(M)) == 1:
            copied = [x for x in M if M.count(x) > 1]
            if sum(copied) > max(M):
                cnt += 1

print(cnt)
'''


# Тип 9 №59833
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    if len(set(M)) == len(M) - 1:
        copied = [x for x in M if M.count(x) > 1]
        not_copied = [x for x in M if M.count(x) == 1]
        if sum(copied) / len(copied) < sum(not_copied) / len(not_copied):
            cnt += 1
print(cnt)
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
