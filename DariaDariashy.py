# region Домашка: ******************************************************************

# № 7594 Досрочная волна 2023 (Уровень: Базовый)
'''
def F(x, A):
    return (x & 39 == 0) or ((x & 11 == 0) <= (x & A != 0))

R = []
for A in range(1000):
    if all(F(x, A) for x in range(1, 10000)):
        R.append(A)
print(min(R))
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
ip = '32.4.23.43'
print(ip.split('.'))  # ['32', '4', '23', '43']

s = '34 98     12 34      54'
print(s.split(' '))  # ['34', '98', '', '', '', '', '12', '34', '', '', '', '', '', '54']

s = '34 98     12 34      54'
print(s.split())  # ['34', '98', '12', '34', '54']
'''

s = '44;48;86;20;44'
print(s.split(';'))  # ['44', '48', '86', '20', '44']
for x in s.split(';'):
    print(x)

# for s in open('files/9.csv'):
#     print(s)  # 44;48;86;20;44
#     M = [int(x) for x in s.split(';')]
#     print(M)

for s in open('files/9.txt'):
    M = [int(x) for x in s.split()]

# 44;48;86;20;44
s = '44;48;86;20;44'
print(s.split(';'))  # ['44', '48', '86', '20', '44']
print(''.join(s.split(';')))  # 4448862044



# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 13, 14, 15, 16, 17, 23, 25]
# КЕГЭ  = []
# на следующем уроке:
