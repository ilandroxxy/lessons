# region Домашка: ******************************************************************

'''
c = 0
M = [int(s) for s in open("files/17.txt")]
R = []
cnt = 0
l = []
a = []
for i in range(len(M) - 1):
    x, y = M[i], M[i + 1]
    if (str(x)[-1] == '1') != (str(y)[-1] == '1'):
        l.append((x + y) / 2)
        a.append(min(x, y))

for i in range(len(M) - 1):
    x, y = M[i], M[i + 1]
    if (str(x)[-1] == '1') != (str(y)[-1] == '1'):
        if x < max(l) and y < max(l):
            cnt += 1
            if x == min(a) or y == min(a):
                c = max(c, max(x, y))
print(cnt, c)
'''

'''
M = [int(s) for s in open("files/17.txt")]
L = [(M[i], M[i+1]) for i in range(len(M) - 1) if (str(M[i])[-1] == '1') != (str(M[i+1])[-1] == '1')]
cnt, c = 0, 0
for i in range(len(M) - 1):
    x, y = M[i], M[i + 1]
    if (str(x)[-1] == '1') != (str(y)[-1] == '1'):
        if max(x, y) < max([sum(pair) / 2 for pair in L]):
            cnt += 1
            D = min([min(pair) for pair in L])
            if (x == D) or (y == D):
                c = max(c, max(x, y))
print(cnt, c)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
for s in open('files/9.txt'):
    M = [int(x) for x in s.split()]
    print(M)
'''

# Тип 9 №61355
# В каждой строке электронной таблицы записаны шесть натуральных чисел.
# Определите количество строк таблицы, содержащих числа, для которых
# одновременно выполнены все следующие условия:
# — все числа в строке различны;
# — среднее арифметическое наибольшего и наименьшего чисел в
# строке больше среднего арифметического всех остальных чисел.
#
# В ответе запишите число — количество строк, удовлетворяющих заданным условиям.
'''
cnt = 0
for s in open('files/9.csv'):
    M = sorted([int(x) for x in s.split(';')])
    if len(M) == len(set(M)):
        if (M[0] + M[-1]) / 2 > sum(M[1:-1]) / 4:
            cnt += 1
print(cnt)


cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    if len(M) == len(set(M)):
        if (min(M) + max(M)) / 2 > (sum(M) - (min(M) + max(M))) / 4:
            cnt += 1
print(cnt)
'''


# Тип 9 №58517
'''
cnt = 0
for s in open('files/9.txt'):
    M = [int(x) for x in s.split()]
    if M.count(min(M)) == 1:  # — минимальное число встречается в строке ровно один раз;
        if any(M.count(x) > 1 for x in M):  # — хотя бы одно число в строке повторяется более одного раза;
            if max(M) > ((sum(M) - max(M)) / 5) * 3:  # — максимальное число в строке превышает среднее арифметическое остальных пяти чисел этой строки более чем в три раза.
                cnt += 1
print(cnt)
'''


# Тип 9 №59780
'''
cnt = 0
for s in open('files/9.txt'):
    M = [int(x) for x in s.split()]
    copied_4 = [x for x in M if M.count(x) == 4]
    copied = [x for x in M if M.count(x) > 1]
    if len(copied_4) == 4:
        if sum(copied) / len(copied) < sum(M) / 7:
            cnt += 1
print(cnt)
'''

'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied = [x for x in M if M.count(x) == 2]
    not_copied = [x for x in M if M.count(x) == 1]
    if len(copied) == 2 and len(not_copied) == 4:
        if sum(copied) / 2 < sum(not_copied) / 4:
            cnt += 1
print(cnt)
'''


cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    if len(M) == len(set(M)):
        chet = [x for x in M if x % 2 == 0]
        nechet = [x for x in M if x % 2 != 0]
        if len(nechet) > len(chet):
            if sum(nechet) < sum(chet):
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
