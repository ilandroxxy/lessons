# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
n = 8
b = 2
r = ''
while n > 0:
    r += str(n % b)
    n //= b
r = r[::-1]
print(r)
'''

'''
def convert(n, b):
    r = ''
    while n > 0:
        r += str(n % b)
        n //= b
    return r[::-1]


print(convert(8, 2))  # 1000
'''


# № 9774 Основная волна 20.06.23 (Уровень: Средний)
'''
def convert(n, b):
    r = ''
    while n > 0:
        r += str(n % b)
        n //= b
    return r[::-1]


R = []
for n in range(1, 10000):
    s = convert(n, 3)
    if n % 3 == 0:
        s = s + s[-2:]
    else:
        x = (n % 3) * 5
        s = s + convert(x, 3)
    r = int(s, 3)
    if r > 133:
        R.append(r)

print(min(R))
'''

'''
def convert(n, b):
    r = ''
    while n > 0:
        r += str(n % b)
        n //= b
    return r[::-1]


z = []
for n in range(1, 1000):
    s = convert(n, 2)
    s = s.replace('0', '*').replace('1', '0').replace('*', '1')
    s = '1' + s
    if s.count('1') % 2 != 0:
        s = s + '1'
    else:
        s = s + '0'
    r = int(s, 2)
    if r > 180:
        z.append(n)
print(min(z))
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# todo Разобрать, как решить авторскую задачку
'''
cnt = 0
for n in range(10**8, 10**9+1):
    s = f'{n:b}'
    for _ in range(3):
        summa = sum([int(x) for x in str(int(s, 2))])
        if summa % 2 != 0:
            s += '1'
        else:
            s += '0'
    r = int(s, 2)
    if 987_654_321 <= r <= 2_123_456_789:
        cnt += 1
        print(cnt)
'''

# Тип 5 №15818
'''
R = []
for n in range(1, 10000):
    s = f'{n:b}'
    s += str(s.count('1') % 2)
    s += str(s.count('1') % 2)
    r = int(s, 2)
    if r > 93:
        R.append(r)
print(min(R))
'''

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6]
# КЕГЭ  = []
# на следующем уроке:
