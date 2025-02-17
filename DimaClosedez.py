# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 19249 ЕГКР 21.12.24 (Уровень: Базовый)
M = [int(x) for x in open('0. files/17.txt')]
D = [x for x in M if abs(x) % 100 == 43 and len(str(abs(x))) == 5]
R = []
for i in range(len(M)-2):
    x, y, z = M[i:i+3]
    if (x in D) or (y in D) or (z in D):
        if (x**2 + y**2 + z**2) <= max(D)**2:
            R.append(x**2 + y**2 + z**2)
print(len(R), min(R))



# № 18176 (Уровень: Средний)
M = [int(x) for x in open('0. files/17.txt')]
D = [x for x in M if x > 0 and x % 10 == 4]
R = []
for i in range(len(M)-2):
    x, y, z = M[i:i+3]
    # s = str(abs(x)) + str(abs(y)) + str(abs(z))
    s = ''.join([str(abs(p)) for p in (x, y, z)])
    summa = sum(map(int, s))
    if summa == min(D):
        R.append(x + y + z)
print(len(R), max(R))

def result(number, answer):
    print(f'Задача: {number} \n'
          f'Ответ: {answer}')

# № 5627 (Уровень: Средний)
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    flag = 0
    if len(M) != len(set(M)):
        flag += 1
    D = sorted(set(M))
    if all(D[1] - D[0] == D[i+1] - D[i] for i in range(len(D)-1)):
        flag += 1
    if flag > 0:
        cnt += 1
result('№ 5627', cnt)


# № 20190 (Уровень: Базовый)



# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25, 26.1]
# КЕГЭ  = []
# на следующем уроке:

