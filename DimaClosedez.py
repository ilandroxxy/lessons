# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Тип 24 №27692
# Определите максимальное количество идущих подряд символов B.
'''
# Вариант 1 - через ctrl + F поиск по строке 'BBBBB...'
s = open('files/24.txt').readline()
print(s)

# Вариант 2 - ака как в 17 номере
#    11
s = 'BBBBBBBBXBBBB'

s = open('files/24.txt').readline()
count = 1  # Длина промежуточной последовательности
maxi = 0  # Длина максимальной длиный последовательности
for i in range(len(s)-1):
    # if s[i] == 'B' and s[i+1] == 'B':
    if s[i:i+2] == 'BB':
        count += 1
        # if maxi < count:
        #     maxi = count
        maxi = max(maxi, count)
    else:
        count = 1
print(maxi)


# Вариант 3
s = open('files/24.txt').readline()
s = s.replace('A', ' ').replace('C', ' ')
print(max([len(x) for x in s.split()]))
'''

s = 'ikjijiEijijE Eokokok'


# Тип 24 №46982
# Определите количество групп из идущих подряд не менее 12 символов,
# которые начинаются и заканчиваются буквой E и
# не содержат других букв E (кроме первой и последней) и букв F.
'''
s = open('files/24.txt').readline()
s = s.replace('E', 'E E')
print(len([len(x) for x in s.split() if len(x) >= 12 and 'F' not in x]))
'''


# Тип 24 №58327
# Определите максимальное количество идущих подряд цифр,
# расположенных в невозрастающем порядке.
'''
s = open('files/24.txt').readline()
count = 1
maxi = 0
for i in range(len(s)-1):
    if s[i] >= s[i+1]:
        count += 1
        maxi = max(maxi, count)
    else:
        count = 1
print(maxi)
'''
# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


s = open('files/24.txt').readline()
print(s.count('XXXX'))
s = s.replace('XXXX', '*')
print(s.count('*'))
for x in 'XYZ':
    s = s.replace(x, ' ')
print(s.count('*'))

s = open('files/24.txt').readline()
cnt = 0
for i in range(len(s)-3):
    if s[i:i+4] == "XXXX":
        cnt += 1
print(cnt)

cnt = 0
s = open('files/24.txt').readline()
for i in range(len(s) - 3):
    if s[i] + s[i + 1] + s[i+2] + s[i + 3] == 'XXXX':
        cnt += 1
print(cnt)

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке:
