# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

R = []
for n in range(1, 10000):
    s = convert(n, 3)
    if n % 3 == 0:
        s = s + s[-3:]
    else:
        x = (n % 3) * 3
        s = s + convert(x, 3)
    r = int(s, 3)
    if r > 150:
        R.append(n)
print(min(R))
'''

'''
def convert(n, b):
    r = ''
    while n:
        r = str(n % b) + r
        n //= b
    return r

print(convert(8, 2))

L = []
for n in range(7, 1000):
    s = convert(n, 3)
    if n % 3 == 0:
        s += s[-3] + s[-2] + s[-1]
    else:
        s = s + convert(((n % 3) * 3), 3)
    r = int(s, 3)
    if r > 150:
        L.append(n)
print(min(L))
'''



# 8
'''
n = 0
L = []
s = sorted('СБОРНИК')
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        n += 1
                        word = a + b + c + d + e + f
                        if word[0] != 'Р' and word.count('Б') == 2 and (word.count('К') == 1 or word.count('К') == 0):
                            L.append(n)
print(max(L))
'''

# 15
'''
for a in range(1, 10000):
    k = 1
    for x in range(0, 100):
        for y in range(0, 100):
            if not ((x < a) or (3 * y + 2 * x > 120) or (a > y)):
                k = 0
    if k == 1:
        print(a)
        break



def F(x, y, A):
    return (x < A) or (3 * y + 2 * x > 120) or (A > y)

for A in range(10000):
    if all(F(x, y, A) for x in range(100) for y in range(100)):
        print(A)
        break



for A in range(10000):
    if all( ((x < A) or (3 * y + 2 * x > 120) or (A > y)) for x in range(100) for y in range(100)):
        print(A)
        break
'''


# 17

M = [int(x) for x in open('files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 5]
B = [x for x in M if abs(x) % 100 == 29]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x in A) + (y in A) + (z in A) == 2:
        if (x + y + z) <= max(B):
            R.append(x + y + z)
print(len(R), max(R))










# # endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 25, 27]
# КЕГЭ = []
# на следующем уроке: 17, 12, 22, 27, 24, 26
