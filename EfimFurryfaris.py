# region Домашка: ************************************************************


# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************

# Максимальное, чтобы было 3 символа T
# for i in range(len(s)-3)
# for i in range(len(s)-1)
s = 'TxxxTxxxxxxTxxxTxxxxxTxxxxTxxxxxxTxxxxxxxTxxxTxxxxxT'
# ['', 'xxx', 'xxxxxx', 'xxx', 'xxxxx', 'xxxx', 'xxxxxx', 'xxxxxxx', 'xxx', 'xxxxx', '']
# 15 TxxxTxxxxxxTxxx
# 20 xxxTxxxxxxTxxxTxxxxx
# 21 xxxxxxTxxxTxxxxxTxxxx
# 21 xxxTxxxxxTxxxxTxxxxxx
# 25 xxxxxTxxxxTxxxxxxTxxxxxxx
# 23 xxxxTxxxxxxTxxxxxxxTxxx
# 24 xxxxxxTxxxxxxxTxxxTxxxxx
# 18 xxxxxxxTxxxTxxxxxT
s = s.split('T')
maxi = 0
for i in range(len(s)-3):
    r = 'T'.join(s[i:i+4])
    print(len(r), r)
    maxi = max(maxi, len(r))
print(maxi)



# Минимальное, чтобы было 3 символа T
# for i in range(len(s)-3)
# for i in range(len(s)-1)
s = 'TxxxTxxxxxxTxxxTxxxxxTxxxxTxxxxxxTxxxxxxxTxxxTxxxxxT'
# ['', 'xxx', 'xxxxxx', 'xxx', 'xxxxx', 'xxxx', 'xxxxxx', 'xxxxxxx', 'xxx', 'xxxxx', '']
# 6 TTxxxT
# 12 TxxxTxxxxxxT
# 12 TxxxxxxTxxxT
# 11 TxxxTxxxxxT
# 12 TxxxxxTxxxxT
# 13 TxxxxTxxxxxxT
# 16 TxxxxxxTxxxxxxxT
# 13 TxxxxxxxTxxxT
# 11 TxxxTxxxxxT
# 8 TxxxxxTT
s = s.split('T')
mini = 10**9
for i in range(len(s)-1):
    r = 'T' + 'T'.join(s[i:i+2]) + 'T'
    print(len(r), r)
    mini = min(mini, len(r))
print(mini)



s=open('0. files/24.txt').readline()
s=s.split('T')
mini = 10**9
for i in range(len(s)-208):
    r = 'T' + 'T'.join(s[i:i+209]) + 'T'
    mini = min(mini, len(r))
print(mini)

# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7?, 8, 9, 10?, 11?, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ = [9, 13, 22, 24, 25]
# на следующем уроке:


# Первый пробник 21.12.24:
# Ефим 12/25 -> 56 вторичных баллов +[1-4, 7, 8, 11, 14-18] -[5, 6, 9, 10, 12, 19-21, 22, 23, 24, 25]
