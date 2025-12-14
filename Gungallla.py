# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# 6
'''
import turtle as t
t.left(90)
t.screensize(2000, 2000)
t.tracer(0)
size= 40
t.rt(90)
for i in range(3):
    t.rt(45)
    t.fd(10*size)
    t.rt(45)
t.rt(315)
t.fd(10*size)
for i in range(2):
    t.rt(90)
    t.fd(10*size)
t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x*size, y*size)
        t.dot(2, 'purple')
t.update()
t.done()
'''
# print(7*14+6*13)


# 8
'''
k=0
from itertools import *
for p in product('0123456789abcdef', repeat=3):
    a=''.join(p)
    if a[0] != '0':
        cop1=[x for x in a if a.count(x)==1]
        if len(cop1)==3:
            for i in '02468ace':
                a = a.replace(i, 'n')
            for i in '13579bdf':
                a = a.replace(i, 'm')
            if 'nn' not in a and 'mm' not in a:
                k+=1
print(k)


k=0
from itertools import *
for p in permutations('0123456789abcdef', r=3):
    a=''.join(p)
    if a[0] != '0':
        for i in '02468ace':
            a = a.replace(i, 'n')
        for i in '13579bdf':
            a = a.replace(i, 'm')
        if 'nn' not in a and 'mm' not in a:
            k+=1
print(k)
'''



# 13
'''
a=[]
from ipaddress import *
for mask in range(1, 32):
    net=ip_network(f'213.168.83.190/{mask}', 0)
    print(net, mask, 32-mask, net.netmask)
    if '213.168.64.0' in str(net):
        a.append(32 - mask)
print(max(a))
'''


# 14 нет
'''
alf= sorted('0123456789qwertyuiopasdfghjklzxcvbnm')
for x in alf[:23]:
    a=int(f'7{x}38596', 23)
    b=int(f'14{x}36', 23)
    c=int(f'61{x}7', 23)
    d=a+b+c
    if d%22==0:
        print(x, d//22)
'''



# 17
'''
R = []
a = [int(x) for x in open('0. files/17.txt')]
b = [x for x in a if len(str(abs(x)))==4]
c = [x for x in b if str(x)[-2:]=='39']
for i in range(len(a)-1):
    x, y = a[i], a[i+1]
    if (x in b) + (y in b) == 1:
        if (x+y)**2 <= max(c)**2:
            R.append(x+y)
print(len(R), max(R))
'''







'''27
from math import dist
ca=[[],[]]
cb=[[],[],[]]
for s in open('27A.txt'):
    s=s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
    if x<0:
        ca[0].append([x, y])
    else:
        ca[1].append([x, y])
for s in open('27B.txt'):
    s=s.replace(',', '.')
    if x<-4 and y>5:
        cb[0].append([x, y])
    if x<-4 and y<5:
        cb[1].append([x, y])
    if x>-4:
        cb[2].append([x, y])
def f(cl):
    r=[]
    for p in cl:
        summa=0
        for g in cl:
            summa+=dist(p, g)
            r.append([summa, p])
    return min(r)[1]

centersa=[f(cl) for cl in ca]
print('a:', centersa)
pxa=(-2.8545062803277164+6.428377908701726)/2*1000
pya=(-0.013407659019377058-8.612117644536346)/2*1000
print(int(abs(pxa)), int(abs(pya)))

centersb=[f(cl) for cl in cb]
print('b:', centersb)
pxb=()/3*1000
pyb=()/3*1000
print(int(abs(pxb)), int(abs(pyb)))

1786 4312
'''


# 8, 9, 13, 14, 17, 27

# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 4, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19-21, 23, 25, 27]
# КЕГЭ  = []
# на следующем уроке:
