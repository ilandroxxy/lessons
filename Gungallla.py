# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
№1
from itertools import permutations
print('1 2 3 4 5 6 7')
t='16 17 23 25 26 32 34 37 43 45 52 54 56 61 62 65 71 73'
g='AC CA CG GC GB BG BD DB DE ED EA AE CF FC FG GF FE EF'
for p in permutations('ABCDEFG'):
    new_t=t
    for i in range(1, 8):
        new_t=new_t.replace(str(i), p[i-1])
    if set(new_t.split())==set(g.split()):
        print(*p)
print(17+88)
105
'''

'''
№2
print('x y z w')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                F=((not x) and z and (not y) and (not w)) or ((not x) and z and y and (not w)) or ((not x) and z and y and w)
                if F==1:
                    print(x, y, z, w)
x,y,w,z
'''

'''
№4
19
'''

'''
№5
a=[]
for n in range(1, 1000):
    s=f'{n:b}'
    if n%5==0:
        s=s+'11'
    else:
        s=s+f'{(n//5):b}'
    r=int(s, 2)
    if r>=783:
        if n%2!=0:
            a.append(n)
print(min(a))
49
'''


# Номер 6
'''
print(16 * 24 + 253 * 399 - 19*13)

import turtle as t
t.lt(90)
t.screensize(5000, 5000)
t.tracer(0)
size = 15
for i in range(7):
    t.fd(15 * size)
    t.rt(90)
    t.fd(23 * size)
    t.rt(90)
t.up()
t.fd(3 * size)
t.rt(90)
t.fd(5 * size)
t.lt(90)
t.down()
for i in range(7):
    t.fd(252 * size)
    t.rt(90)
    t.fd(398 * size)
    t.rt(90)
t.up()
for x in range(-100, 100):
    for y in range(-100, 100):
        t.goto(x * size, y * size)
        t.dot(3, 'purple')
t.update()
t.done()
'''


# №8
'''
from itertools import product
cnt = 0
for p in product('0123456789ABCDE', repeat=4):
    num = ''.join(p)
    if num[0] != '0':
        if num.count('8') == 1:
            if all(x not in num for x in '00 11 22 33 44 55 66 77 88 99 AA BB CC DD EE'.split()):
                cnt += 1
print(cnt)
'''



# №9
# – в строке минимальное число встречается два или три раза, остальные числа без повторений;
# – сумма квадратов минимального и максимального из неповторяющихся
# чисел не больше квадрата суммы других неповторяющихся.
'''
cnt = 0
for s in open('0. files/9.csv'):
    a = [int(x) for x in s.split(',')]
    copied1 = [x for x in a if a.count(x) == 1]
    if (a.count(min(a)) == 2 and len(copied1) == 6) or (a.count(min(a)) == 3 and len(copied1) == 5):
        if (min(copied1) ** 2 + max(copied1) ** 2) <= (sum(copied1) - max(copied1) - min(copied1)) ** 2:
                cnt += 1
print(cnt)
'''


'''
№10
73
'''


# №13
'''
k=0
from ipaddress import *
net=ip_network('167.66.136.176/255.254.0.0', 0)
for ip in net:
    print(ip)
    k+=1
    if k==3:
        break
print(167+66+0+1)
'''

'''
№14
b=[]
alf='0123456789qwertyuiopasdfghjklzxcvbnm'
for x in range(1, 1000):
    n=29**293+29**271-x
    a=''
    while n>0:
        a=alf[n%29]+a
        n=n//29
    b.append(a.count('0'))
print(max(b))
24
'''

'''
№15
a=[]
def f(x, y):
    return (y>A) or (152!=2*y+3*x) or (A<x)
for A in range(1, 1000):
    if all(f(x, y) for x in range(1, 100) for y in range(1, 100)):
        a.append(A)
print(max(a))
30
'''

'''
№16
from sys import *
setrecursionlimit(10**6)
def f(n):
    if n<=10:
        return n
    if n>10:
        return n-12+f(n-21)
print(int((f(224356)-f(224272))/f(59)))
12125
'''

'''
№17
c=[]
a=[int(x) for x in open('17.txt')]
b=[int(x) for x in a if x<0 and len(str(abs(x)))==3 and abs(x)%6==0]
for i in range(len(a)-1):
    x, y = a[i], a[i+1]
    if (x<0)+(y<0)==1:
        if (x+y)>max(b):
            c.append(x**2+y**2)
print(len(c), max(c))
2553 19701728317
'''

'''
№18
6060 2522
'''

'''
№19-21
from math import floor
def f(s, n):
    if s<=505:
        return n%2==0
    if n==0:
        return 0
    h=[f(s-3, n-1), f(floor(s/5), n-1)]
    return any(h) if (n-1)%2==0 else any(h)
print([s for s in range(506, 1000) if f(s, n=2)])
print([s for s in range(506, 1000) if f(s, n=3) and not f(s, n=1)])
print([s for s in range(506, 1000) if f(s, n=4) and not f(s, n=2)])
12649
2533, 2534
2536
'''


# №23
'''
def f(a, b):
    if a > b:
        return 0
    elif a == b:
        return 1
    else:
        return f(a + 1, b) + f(a * 2, b) + f(a * 3, b)


print(f(6, 14) * f(14, 48))
print(f(6, 18) * f(18, 48))
print(f(6, 14) * f(14, 18) * f(18, 48))
print(45 + 48 - 24)  # 93 - 24 = 69
'''


# №25
'''
def f(x):
    div = []
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            div += [i, x // i]
    return sorted(set(div))

k = 0
for x in range(1324999, 1, -1):
    b = [i for i in f(x) if len(f(i)) == 0]
    if len(b) != 0:
        s = sum(b)
        if s <= 30000:
            if s % 5 == 0:
                print(x)
                k += 1
                if k == 5:
                    break
'''

'''
def f(x, y, A):
    return (x * y < A) or (y >= x) or (x > 12)

R = []
for A in range(1, 10000):
    if all(f(x, y, A) for x in range(1, 100) for y in range(1, 100)):
        R.append(A)
print(min(R))

'''

R = []
for n in range(1, 10000):
    s = f'{n:o}'
    if s[-1] == '5':
        s = s.replace('4', '2')
        s = '25' + s
    else:
         s = s + '33'
    r = int(s, 8)
    if r < 2600:
        R.append(r)
        if r == 2587:
            print(n)
print(max(R))

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 4, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19-21, 23, 25]
# КЕГЭ  = []
# на следующем уроке:
