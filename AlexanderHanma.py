# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Задача 17
'''
M = [int(x) for x in open('files/17.txt')]
D = [x for x in M if abs(x) % 100 == 43 and len(str(abs(x))) == 5]
D2 = [x for x in M if str(x)[-2:] == '43' and 10000 <= abs(x) <= 99999]
R = []
for i in range(len(M)-2):
    x, y, z = M[i:i+3]  # i, i+1, i+2
    if (x in D) or (y in D) or (z in D):
        if (x**2 + y**2 + z**2) <= max(D)**2:
            R.append(x**2 + y**2 + z**2)
print(len(R), min(R))
'''


from ipaddress import *
net = ip_network(f'218.194.82.148/255.255.255.192', 0)
for ip in net:
    print(ip)


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Александр 19/25 -> 75 вторичных баллов +[1-5, 7, 9-10, 12, 14-16, 18-22, 24, 25] -[6, 8, 11, 13, 17, 23]
# Саша
