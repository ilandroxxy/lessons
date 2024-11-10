# region Домашка: ******************************************************************

# № 7718
'''
M = [int(x) for x in open('files/17.txt')]
R = []
for i in range(len(M)):
    for j in range(i + 1, len(M)):
        x, y = M[i], M[j]
        if ((x + y) % 18 == 0) != ((x * y) % 18 == 0):
            R.append(x + y)
print(len(R), max(R))
'''
# 12040019971


'''
A = True
B = False

if A and B:
    print('Выполняются оба условия')
if A or B:
    print(' Выполняется хотя бы один')
if (A) != (B):  
    print('Выполняется либо 1, либо 2 (только один)')
'''


# Встроенные функции перевода:
'''
n = 125
print(bin(n))  # 0b1111101
print(f'{n:b}')  # 1111101
print(bin(n)[2:])  # 1111101
print(int('1111101', 2))  # 125

print(oct(n))  # 0o175
print(f'{n:o}')  # 175
print(oct(n)[2:])  # 175
print(int('175', 8))  # 125

print(hex(n))  # 0x7d
print(f'{n:x}')  # 7d
print(f'{n:X}')  # 7D
print(hex(n)[2:])  # 7d
print(int('7d', 16))  # 125
'''


# № 8954
'''
M = [int(x) for x in open('files/17.txt')]
D = [x for x in M if hex(x)[-2:] == '0f']

R = []
for i in range(len(M)-1):
    x, y = M[i], M[i + 1]
    if (x % 7 == 0) != (y % 7 == 0):
        if (x + y) % max(D) == 0:
            R.append(x + y)
print(len(R), max(R))
'''
# 29487


# № 2491 (Уровень: Базовый)
'''
M = [int(x) for x in open('files/17.txt')]
avg = sum(M) / len(M)
R = []
for i in range(len(M)-2):
    if any(p < avg for p in M[i:i+3]):
        if all('9' in str(p) for p in M[i:i+3]):
            R.append(sum(M[i:i+3]))
print(len(R), max(R))
'''
# 34517460


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Тип 9 https://education.yandex.ru/ege/task/cecbe39b-e6f6-479b-b23b-b0261ac504fe
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied = [x for x in M if M.count(x) == 2]
    not_copied = [x for x in M if M.count(x) == 1]
    print(copied, not_copied)
    if len(copied) == 4 and len(not_copied) == 3:
        # [76, 96, 76, 96] [51, 23, 19]
        if sum(copied) / len(copied) < sum(M) / len(M):
            cnt += 1
print(cnt)
'''

# Задание 9 https://education.yandex.ru/ege/task/96c09be1-da8c-4460-b91f-05f352ddaa78
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(',')]
    nechet = [x for x in M if x % 2 != 0]
    if (len(M) != len(set(M))) != (len(nechet) == 3):
        cnt += 1
print(cnt)
'''


# Задание 9 https://education.yandex.ru/ege/task/c255edb8-3ff7-4c2a-bf66-03487b499649
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    if any(M.count(x) == 3 for x in M):
        if len(set(M)) == 5:  # в строке ровно 5 различных значений
            if sum(M) < 502:
                cnt += 1
print(cnt)
'''


# Задание 9 https://education.yandex.ru/ege/task/d62dc568-941a-44da-870b-b8cc21faee9f
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(',')]
    flag = 0
    chet = [x for x in M if x % 2 == 0]
    nechet = [x for x in M if x % 2 != 0]
    if sum(nechet) > sum(chet):
        flag += 1
    if len(set(M)) == len(M) - 1:
        flag += 1
    if flag == 1:
        cnt += 1
print(cnt)


cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(',')]
    chet = [x for x in M if x % 2 == 0]
    nechet = [x for x in M if x % 2 != 0]
    if (sum(nechet) > sum(chet)) != (len(set(M)) == len(M) - 1):
        cnt += 1
print(cnt)
'''

# Задание 9 https://education.yandex.ru/ege/task/22cf7ea4-d582-409f-b6ab-8fe3b9fe4728

cnt = 0
for s in open('files/9.csv'):
    M = sorted([int(x) for x in s.split(',')])

    if len(set(M)) < 4:
        if (2 * M[0] ** 2) > (M[1] * M[2]):
            if M[1] != max(M) and M[2] != max(M):
                print(M)
                cnt += 1
print(cnt)


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
