# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(num, base):
    res = ''
    while num > 0:
        res = alphabet[num % base] + res
        num //= base
    return res


x = convert(123456789, 16)
print(x)  # 75BCD15
print(int(x, 16))  # 123456789
# ValueError: int() base must be >= 2 and <= 36, or 0
'''


# № 17611 Резервный день 19.06.2024 (Сибирь)
'''
with open('17.txt', 'r') as file:
    M = [int(x) for x in file]


M = [int(x) for x in open('17.txt')]
# D = [x for x in M if abs(x) % 10 == 7 and 1000 <= abs(x) <= 9999]
D = [x for x in M if str(x)[-1] == '7' and len(str(abs(x))) == 4]
R = []
for i in range(len(M)-2):
    # x, y, z = M[i], M[i+1], M[i+2]
    x, y, z = M[i:i+3]
    if (x in D) + (y in D) + (z in D) >= 2:  # хотя бы два элемента из трех оканчиваются на 7
        if (x + y + z) > max(D):
            R.append(x + y + z)
print(len(R), max(R))
'''


# № 17615 Резервный день 19.06.2024 (Сибирь)
'''
def F(a, b):
    if a < b or a == 16:  # ДОП условие: И не содержит 16
        return 0
    elif a == b:
        return 1
    else:
        return F(a-2, b) + F(a//2, b)

print(F(32, 8) * F(8, 1))



def F(a, b):
    if a <= b or a == 16:  # ДОП условие: И не содержит 16
        return a == b
    return F(a-2, b) + F(a//2, b)

print(F(32, 8) * F(8, 1))
'''


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
