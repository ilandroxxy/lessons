# region Домашка: ************************************************************

# https://stepik.org/lesson/1038775/step/2?unit=1062778
'''
M = [int(x)for x in open("files/17.txt")]
R = []
for i in range(len(M)):
    for j in range(i + 1, len(M)):
        x, y = M[i], M[j]
        if ((x + y) % 18 == 0) != ((x * y) % 18 == 0):
            R.append(x+y)
print(len(R), max(R))
'''


# https://stepik.org/lesson/1038775/step/5?unit=1062778
'''
M = [int(x)for x in open("files/17.txt")]
D = [x for x in M if hex(x)[-2:] == '0f']
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x % 7 == 0) != (y % 7 == 0):
        if (x + y) % max(D) == 0:
            R.append(x+y)
print(len(R), max(R))
'''


# https://stepik.org/lesson/1038775/step/8?unit=1062778
'''
M = [int(x) for x in open("17.txt")]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x+y) % 120 == 0:
        R.append(x+y)
print(len(R), max(R))
'''

M = [int(x)for x in open("files/17.txt")]
R = []
avg = sum(M) / len(M)
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x > avg) + (y > avg) + (z > avg) >= 2:
        R.append(x + y + z)
print(len(R), max(R))



# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************


# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 7, 8, 9, 11, 12, 14, 15, 16, 17-, 18, 19-21, 22, 23, 25.1]
# КЕГЭ = [12, 17]
# на следующем уроке: 7, 9, 10,
