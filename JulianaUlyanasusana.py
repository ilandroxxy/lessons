# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
a, b = 7, 2
print(a // b)  # 3
print(a / b)  # 3.5
print(a % b)  # 1
'''

# 21891 (5)
'''
def convert(n, b):
    r = ''
    while n > 0:
        r += str(n % b)
        n //= b
    return r[::-1]

for n in range(1, 1000):
    b = convert(n, 2)
    # b = f'{n:b}'
    # b = bin(b)[2:]
    b = b + str(b.count('1') % 2)
    b = b + str(b.count('1') % 2)
    r = int(b, 2)
    if r > 253:
        print(n)
        break
'''



# 21899 (13)
'''
from ipaddress import *
net = ip_network('98.81.154.195/255.252.0.0', 0)
cnt = 0
for ip in net:
    b = f'{ip:b}'
    if b.count('1') == 5:
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
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 23, 25]
# КЕГЭ = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Ульяна 5/8 -> 34 вторичных баллов +[1, 2, 4, 6, 12] -[5, 13, 14]

# Второй пробник 28.02.25:
# Ульяна 10/29 -> 51 вторичных баллов +[1-4, 6, 10, 13, 15, 16, 23] -[5, 8, 9, 12, 14, 17, 25]
