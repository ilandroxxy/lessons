# region Домашка: ******************************************************************


'''
from ipaddress import *
net = ip_network('136.36.240.16/255.255.255.248')
cnt = 0
for ip in net:
    if '101' not in f'{ip:b}':
        cnt += 1
print(cnt)
'''


# Тип 25 №29673
'''
def divisors(x):
    div = []
    for j in range(2, int(x ** 0.5) + 1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


# print(divisors(24))  # [2, 3, 4, 6, 8, 12] 6
# print(divisors(16))  # [2, 4, 8] 3
# print(divisors(36))  # [2, 3, 4, 6, 9, 12, 18]

cnt = 0
for x in range(123456789, 223456789 + 1, 1):
    if (x ** 0.5) == int(x ** 0.5):
    # if (x ** 0.5).is_integer():
        if len(divisors(x)) == 3:
            cnt += 1
            print(x, max(divisors(x)))
            if cnt == 10:
                break
'''

'''
from ipaddress import *
for A in range(256):
    net = ip_network(f'183.192.{A}.0/255.255.252.0', 0)
    if all(f'{ip:b}'[16:].count('1') > 3 for ip in net):
        print(A)
        break
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# 1 бит - минимальная единица измерения
# 1 байт = 8 бит = 2**3 бит
# 1 Кбайт = 1024 байт = 2**10 байт = 2**13 бит
# 1 Мбайт = 1024 Кбайт = 2**20 байт = 2**23 бит
# 1 Гбайт = 1024 Мбайт = 2**30 байт = 2**33 бит

# Тип 11 №6803
'''
symbols = 15
alphabet = 9
i = 4  # 2**i >= alphabet - бит на один символ
bit = symbols * i
# byte = bit / 8  # 7.5 -> 8
byte = 8  # байт на один пароль
print(byte * 25)
'''
# Ответ: 200


# Тип 11 №26956
'''
symbols = 9
alphabet = 26
i = 5  # 2**i >= alphabet
bit = symbols * i
print(bit / 8)  # 5.625 -> 6
byte = 6
I = 300 / 15  # Вес одного пользователя
print(I - byte)  # Вес пользователя - пароль = доп информация
'''


# Тип 11 №59804
'''
symbols = 85
alphabet = 10 + 2000
i = 11  # 2**i >= alphabet
bit = symbols * i
print(bit / 8)  # 116.875 -> 117
byte = 117
print((byte * 46080) / 2**10)
'''
# Ответ: 5265


# Тип 11 №55598
'''
symbols = 9
alpahbet = 26
i = 5
bit = symbols * i
print(bit / 8)  # 5.625 -> 6
byte = 6

symbols2 = 50
alphabet2 = 1984
i2 = 11
bit2 = symbols2 * i2
print(bit2 / 8)  # 68.75 -> 69
byte2 = 69

I = (4 * 2**20) / 32768
print(I - byte - byte2)
'''

'''
alphabet = 10 + 26 + 450
i = 9
I = (213 * 2**10) / 708
bit = I * 8
print(bit)
symbols = bit / i
print(symbols)  # 273.83 -> 274   # отведено более 213*
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 4, 5, 6, 8, 9, 11, 12, 13, 14, 15, 16, 17, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке:
