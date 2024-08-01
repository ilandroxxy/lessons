# region Домашка: ******************************************************************

'''
L = [4, 5, 6, 9]
L[1] = 14
L += [1, 2, 5]
del L[0]
L *= 3
L.insert(4, 45)
print(L)
'''

'''
L = [3, 7, 1, 4, 9, 2]
# L[0], L[-1] = L[-1], L[0]
x = L[0]
L[0] = L[-1]
L[-1] = x
print(L)
'''

'''
L = [3, 7, 1, 4, 9, 2]
L = [L[-1]] + L[1:-1] + [L[0]]
print(L)
'''

'''
s = input().split()
print(max([len(x) for x in s]))
'''

'''
L = [60, 50, -30, 6]
L.sort()  # L = sorted(L)
print(L)  # [-30, 6, 50, 60]
print(L[-2])
'''

'''
L = [9, 2, 7, 14, 5, 8, 11, 22, 15, 10]
print([x for x in L if x % 2 == 0])  # [2, 14, 8, 22, 10]
'''

'''
my_list = []
n = int(input())
for i in range(n):
    x = int(input())
    if x % 2 == 0:
        my_list.append(x)

print(my_list)
'''

'''
A, B, C = [], [], []
s = int(input())
for _ in range(s):
    i = int(input())
    if i < 0:
        A.append(i)
    elif i > 0:
        B.append(i)
    else:
        C.append(i)
W = A + C + B
# print(*W, sep='\n')
for x in W:
    print(x)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
s = 'hello, world'

# i  01234
s = 'abcde'

print(s[1])  # b
print(f'Последний элемент строки s: {s[-1]}')  # e
print('Последний элемент строки s: ' + s[-1])

L = [1, 2, 3, 4, 5]
L[0] = 'A'
print(L)  # ['A', 2, 3, 4, 5]

s = '12345'
# s[0] = 'A'
s = 'A' + s[1:]
print(s)  # A2345
'''

# Срезы строк
'''
# s[STOP], s[START:STOP], s[START:STOP:STEP]

# i  01234
s = 'abcde'

print(s[1:4])  # bcd
print(s[:3])  # abc - все элементы слева до третьего (не включая)
print(s[2:])  # cde - все элементы справа от второго (включая)
print(s[:])  # abcde - все элементы слева-направо
print(s[:-1])  # abcd
print(s[::-1])  # edcba - все элементы в обратном порядке
print(s[0::2])  # ace - все элементы стоящие на четных индексах
print(s[1::2])  # bd - все элементы стоящие на нечетных индексах 

L = [1, 2, 3]
L.reverse()

L = L[::-1]

s = '123'
s = s[::-1]
'''


# Функции строк str()
'''
s = '5' * 10
print(s)  # 5555555555

print('5' + '2')  # 52

print(len('12345'))  # 5 - len() - возвращает длину строки
print(max('hello,world'))  # w
print(min('hello,world'))  # ,
print(sorted('23 >,! ijuu EUH'))
# [' ', ' ', ' ', '!', ',', '2', '3', '>', 'E', 'H', 'U', 'i', 'j', 'u', 'u']
print(sorted('hello,world'))
# [',', 'd', 'e', 'h', 'l', 'l', 'l', 'o', 'o', 'r', 'w']
print(set('hello,world'))  # {'e', 'r', ',', 'h', 'd', 'l', 'w', 'o'}
'''

# Методы строк str()

s = 'hello, world'
print(s.count('l'))  # 3

L = [2, 2, '2', 3, '3', '3']
print(L.count(3))  # 1
print(L.count('3'))  # 2


print(s.index('l'))  # 2
print(s.rindex('l'))  # 10

s = 'hello, world'
s = s.replace('l', '*')
print(s)  # he**o, wor*d
s = s.replace('*', 'l', 2)
print(s)  # hello, wor*d

'''
id = '12.43.234.128'
x = '11111111'
print(int(x, 2))  # 255
print(id.split('.'))  # ['12', '43', '234', '128']
ID = [int(x) for x in id.split('.')]
print(ID)  # [12, 43, 234, 128]
for x in ID:
    if not (0 <= x <= 255):
        print('Плохой ID')
        break
print('ID хороший')
'''

ID = ['12', '43', '234', '128']
s = '*'.join(ID)
print(s)  # 12*43*234*128

s = '++'.join(ID)
print(s)  # 12++43++234++128

s = ''.join(ID)
print(s)  # 1243234128

s = ' '.join(ID)
print(s)  # 12 43 234 128



# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 6]
# КЕГЭ  = []
# на следующем уроке:
