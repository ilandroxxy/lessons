# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
from itertools import product

alf = '0123456789abcdef'

c = 0


def f(z):
    d = [int(i, 16) for i in z]

    if (d[0] + d[1]) % 2 != 0 and (d[1] + d[2]) % 2 != 0:
        return 1
    return 0


for i in product(alf, repeat=3):
    z = list(i)
    u1 = len(z) == len(set(z))

    if u1 and f(z):
        c += 1

print(c)

ответ: 896
'''

#
'''
from itertools import *
from string import *
alphabet = digits + ascii_uppercase
# 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ

# alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
cnt = 0
for p in permutations(alphabet[:16], r=3):
    num = ''.join(p)
    if num[0] != '0':
        for x in alphabet[:16:2]:
            num = num.replace(x, '2')
        for x in alphabet[1:16:2]:
            num = num.replace(x, '1')
        if '11' not in num and '22' not in num:
            cnt += 1
print(cnt)
'''


'''
f=open('9.csv')
KKK=[]

c=0

for s in f:
    c+=1
    s1=s.strip()

    z=[int(i) for i in s1.split(';')]

    d=[z.count(i) for i in z]

    u1=d.count(2)==4 and d.count(1)==3

    u2 = z.count(max(z)) == 1

    if u1 and u2:
        print((c,sum(z)))

        #break

ответ: 787
'''


'''
f=open('0. files/9.csv')
KKK=[]

c=0

for s in f:
    c+=1
    s1=s.strip()

    z=[int(i) for i in s1.split(';')]

    d=[z.count(i) for i in z]

    u1=d.count(2)==4 and d.count(1)==3

    u2 = z.count(max(z)) == 1

    if u1 and u2:
        print((c, sum(z)))

        #break
'''

'''
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied2 = [x for x in M if M.count(x) == 2]
    not_copied = [x for x in M if M.count(x) == 1]
    if len(copied2) == 4 and len(not_copied) == 3:
        if max(M) in not_copied:
            print(sum(M))
            break

'''

'''
c=0

f=open('17.txt')

z=[]
for s in f:
    s1=s.strip()

    n=int(s1)
    z+=[n]

mx_39_4=-100000000000000

for i in z:
    if i>mx_39_4 and abs(i)%100==39:
        mx_39_4=i


for i in range(len(z)-1):
    a=z[i]
    b=z[i+1]

    u1=(len(str(abs(a))) == 4 and len(str(abs(b))) != 4) or (len(str(abs(a))) != 4 and len(str(abs(b))) == 4)

    u2=(a+b)**2<=mx_39_4**2

    if u1 and u2:
        c+=1

print(c)

ответ:2300
'''

'''
M = [int(x) for x in open('0. files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 4]
B = [x for x in A if abs(x) % 100 == 39]
R = []  # c=0, mx_39_4=-100000000000000
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x in A) + (y in A) == 1:
        if (x + y) ** 2 <= max(B) ** 2:
            R.append(x + y)
print(len(R), max(R))
'''

'''
from fnmatch import *
for x in range(2025, 10**8, 2025):
    if fnmatch(str(x), '12*34?5'):
        print(x, x // 2025)
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
