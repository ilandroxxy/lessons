# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

#пробник

'''from itertools import *
print('1 2 3 4 5 6 7')
t='16 17 23 25 26 32 34 37 43 45 52 54 56 61 62 65 71 73'
g='ac ca cg gc gb bg bd db de ed ea ae cf fc fg gf fe ef'
for p in permutations('abcdefg'):
    nt=t
    for i in range(1, 8):
        nt=nt.replace(str(i), p[i-1])
    if set(nt.split())==set(g.split()):
        print(*p)
print(17+88)'''

'''print('x y z w')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f=((not x) and z and (not y) and (not w)) or ((not x) and z and y and (not w)) or ((not x) and z and y and w)
                if f==1:
                    print(x, y, z, w)
print('x,y,w,z')'''

'''print(2+2+3+2+4+3+3)'''

'''for n in range(1, 1000):
    s=f'{n:b}'
    if n%5==0:
        s=s+'11'
    else:
        s=s+f'{n//5:b}'
    r=int(s, 2)
    if r>=783:
        if n%2!=0:
            print(n)
            break'''

'''import turtle as t
t.left(90)
t.screensize(2000, 2000)
t.tracer(0)
size=10
for i in range(7):
    t.fd(15*size)
    t.rt(90)
    t.fd(23*size)
    t.rt(90)
t.up()
t.fd(3*size)
t.rt(90)
t.fd(5*size)
t.lt(90)
t.down()
for i in range(7):
    t.fd(252*size)
    t.rt(90)
    t.fd(398*size)
    t.rt(90)
t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x*size, y*size)
        t.dot(3, 'purple')
t.update()
t.done()
print(253*399+3*24+5*13)'''

'''from math import *
a=4
b=33000
c=37
t=41*60+33
v=363956352
I1=a*b*c*t
I2=v*307
I3=I2-I1
Iz=I3/30
print(ceil(Iz/2**13))'''

'''n=0
from itertools import *
for p in product('0123456789abcde', repeat=4):
    a=''.join(p)
    if a[0]!='0':
        if a.count('8')==1:
            if all(str(i)!=str(i+1) and i in '0123456789' for i in a):
                n+=1
print(n)'''

'''n=0
for s in open('9.csv'):
    a=[int(x) for x in s.split(';')]
    b=[x for x in a if a.count(x)==1]
    if a.count(min(a))==2 or a.count(min(a))==3:
       if len(set(b))==6 or len(set(b))==5:
           if max(b)**2+min(b)**2<=(sum(b)-max(b)-min(b))**2:
               n+=1
print(n)'''

'''from math import *
I=53*2**23
I1=I/282952
i=I1/102
print(floor(2**i))'''

'''k=0
from ipaddress import *
net=ip_network('167.66.136.176/255.254.0.0', 0)
for ip in net:
    print(ip)
    k+=1
    if k==5:
        break
print(167+66+1)'''

'''b=[]
alf=sorted('0123456789qwertyuiopasdfghjklzxcvbnm')
for x in range(1, 8410):
    n=29**293+29**271-x
    a=''
    while n>0:
        a=alf[n%29]+a
        n=n//29
    b.append(a.count('0'))
print(max(b))'''

'''a=[]
def f(x, y):
    return (y>A) or (152!=2*y+3*x) or (A<x)
for A in range(1, 1000):
    if all(f(x, y) for x in range(1, 100) for y in range(1, 100)):
        a.append(A)
print(max(a))'''

'''from functools import *
from sys import *
setrecursionlimit(10000)
@lru_cache(None)
def f(n):
    if n<=10:
        return n
    else:
        return n-12+f(n-21)
for i in range(10, 224360):
    f(i)
print((f(224356)-f(224272))/f(59))'''

'''d=[]
a=[int(x) for x in open('17.txt')]
b=[x for x in a if x<0]
c=[x for x in b if len(str(abs(x)))==3 and x%10==6]
for i in range(len(a)-1):
    x, y = a[i], a[i+1]
    if (x in b)+(y in b)==1:
        if x+y>max(c):
            d.append(x**2+y**2)
print(len(d), max(d))'''

'''from math import floor
def f(s, n):
    if s<=505:
        return n%2==0
    if n==0:
        return 0
    h=[f(s-3, n-1), f(floor(s/5), n-1)]
    return all(h) if (n-1)%2==0 else all(h)
print([s for s in range(506, 5000) if f(s, n=2)])
print([s for s in range(506, 5000) if f(s, n=3) and not f(s, n=1)])
print([s for s in range(506, 5000) if f(s, n=4) and not f(s, n=2)])'''

'''def f(a, b):
    if a>b:
        return 0
    elif a==b:
        return 1
    else:
        return f(a+1, b)+f(a*2, b)+f(a*3, b)
print(f(6, 14)*f(14, 48))
print(f(6, 18)*f(18, 48))
print(45+48)'''

'''s=open('24.txt').readlinr()
reg=r'[1-9](+[1-9])+'''

'''
k=0
def f(x):
    div=[]
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            div+=[i, x//i]
    return sorted(set(div))
for x in range(1324999, 1, -1):
    a=f(x)
    b=[x for x in a if len(f(x))==0]
    if len(b)!=0:
        if sum(b)<=30000:
            if sum(b)%5==0:
                print(x)
                k+=1
                if k==5:
                    break
'''

'''from math import dist
clsA=[[],[]]
clsB=[[],[],[]]
for s in open('27_A.txt'):
    s=s.replace(',','.')
    x, y = [float(i) for i in s.split()]
    if y>90:
        clsA[0].append([x, y])
    if y<90:
        clsA[1].append([x, y])
for s in open('27_B.txt'):
    s=s.replace(',','.')
    x, y = [float(i) for i in s.split()]
    if y>41 and x>15:
        clsB[0].append([x, y])
    if 32<y<41:
        clsB[1].append([x, y])
    if y<32 and x>15:
        clsB[2].append([x, y])
def c(cl):
    r=[]
    for p in cl:
        s=0
        for g in cl:
            s+=dist(p, g)
        r.append([s, p])
    return max(r)[1]
acA=[c(cl) for cl in clsA]
print(acA)
print(len(clsA[0]), len(clsA[1]))
print('p1 =', int((16.99841482246666+95.6727515672738)*10000))
print('p2 =', int((63.94062638636294+87.77751031781972)*10000))

acB=[c(cl) for cl in clsB]
print(acB)
print(dist([0, 0], [21.38834573144159, 48.899310705252915]))
print(dist([0, 0], [22.1707588150025, 39.65891347675987]))
print(dist([0, 0], [23.329917580199655, 26.41328219493777]))
print('q1 =', int(21.38834573144159*10000))
print('q2 =', int(26.41328219493777*10000))'''



# Разбираем на уроке:

# Номер 8
'''
n=0
from itertools import *
for p in product('0123456789abcde', repeat=4):
    a=''.join(p)
    if a[0]!='0':
        if a.count('8')==1:
            # if all(a[i] != a[i+1] for i in range(len(a)-1)):
            # if all(p not in a for p in '00 11 22 33 44 55 66 77 88 99 aa bb cc dd ee'.split()):
            if all(p*2 not in a for p in '0123456789abcde'):
                n+=1
print(n)
'''

# Номер 11
'''
sym = 102

byte = 53*2**20 / 282952
print(byte)  # 196.4097 -> 196 (отведено не более 53 Мбайт)
bit = 196 * 8

i = bit / sym
print(i)  # 15.372 -> 15 (отведено не более 53 Мбайт)

i = 15
print(2 ** 15)
'''


# Номер: 17
'''
d = []
a = [int(x) for x in open('files/17.txt')]
b = [x for x in a if x < 0]
c = [x for x in b if len(str(abs(x))) == 3 and abs(x) % 10 == 6]
for i in range(len(a) - 1):
    x, y = a[i], a[i + 1]
    if (x in b) + (y in b) == 1:
        if x + y > max(c):
            d.append(x ** 2 + y ** 2)
print(len(d), max(d))
'''



# 19. 2544 -
# 20. 2533, 2534 +
# 21. 2536 +
'''
from math import floor
def f(s, n):
    if s<=505:
        return n%2==0
    if n==0:
        return 0
    h=[f(s-3, n-1), f(floor(s/5), n-1)]
    return any(h) if (n-1)%2==0 else all(h)
print(max([s for s in range(506, 20000) if f(s, n=2)]))
print([s for s in range(506, 5000) if f(s, n=3) and not f(s, n=1)])
print([s for s in range(506, 5000) if f(s, n=4) and not f(s, n=2)])
'''


# Номер 23
'''
def f(a, b):
    if a>b:
        return 0
    elif a==b:
        return 1
    else:
        return f(a+1, b)+f(a*2, b)+f(a*3, b)

print(f(6, 14) * f(14, 18) * f(18, 48))  # 24
print(f(6, 14)*f(14, 48))  # 45
print(f(6, 18)*f(18, 48))  # 48
print(45+48-24)  # 69
'''


from re import *



# 1. 105 +
# 2. xywz +
# 3. -
# 4. 19 +
# 5. 49 +
# 6. 101084 +
# 7. 405106 +
# 8. -
# 9. 752 +
# 10. 104 -
# 11. 43378 -
# 12. -
# 13. 234 +
# 14. 24 +
# 15. 30 +
# 16. 12125 +
# 17. 2563, 19701728317 -+
# 18. 6653, 2522 +
# 19. 2544 -
# 20. 2533, 2534 +
# 21. 2536 +
# 22. 130 +
# 23. 93 -
# 24. -
# 25. 1324994 +
#        1324992
#        1324991
#        1324986
#        1324980
#
# 26. -
# 27. 1126711, 1517181 +
#        213883, 264132 +



# ------------------------

'''print('x y z w')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f=(x or (not y)) and (not(y==z)) and (not w)
                if f==1:
                    print(x,y,z,w)
print('x,z,y,w')'''

'''def f(n):
    a=''
    while n>0:
        a=str(n%3)+a
        n=n//3
    return a
for n in range(1, 100):
    s=f(n)
    if n%3==0:
        s=s+s[-3:]
    else:
        s=s+f((n%3)*3)
    r=int(s, 3)
    if r>150:
        print(n)
        break'''

'''import turtle as t
t.left(90)
t.screensize(2000, 2000)
t.tracer(0)
size=20
for i in range(4):
    t.fd(10*size)
    t.rt(270)
t.up()
t.fd(3*size)
t.rt(270)
t.fd(5*size)
t.rt(90)
t.down()
for i in range(2):
    t.fd(10*size)
    t.rt(270)
    t.fd(12*size)
    t.rt(270)
t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x*size, y*size)
        t.dot(5, 'purple')
t.update()
t.done()
print(13*11+11*11-6*8)'''

'''p=1024*512
i=32
v=32768
I=p*i
print(I/v)'''

'''b=[]
n=0
from itertools import *
for p in product(sorted('сборник'), repeat=6):
    a=''.join(p)
    n+=1
    if a[0]!='р':
        if a.count('б')==2:
            if a.count('к')<=1:
                b.append(n)
print(max(b))'''

'''k=0
for s in open('9.csv'):
    a=[int(x) for x in s.split(';')]
    cop2=[x for x in a if a.count(x)==2]
    cop1=[x for x in a if a.count(x)==1]
    if len(cop2)==4:
        if len(cop1)==3:
            if sum(cop2)/len(cop2)<sum(cop1)/len(cop1):
                k+=1
print(k)'''

'''alf=16
i=4
sim=32
I1=32*4
I1B=I1/8
print(I1B, 'Б')
I=I1B*16384
print(I, 'Б')
print(I/1024, 'КБ')'''

'''from ipaddress import *
for mask in range(1, 33):
    net=ip_network(f'111.118.179.50/{mask}', 0)
    for ip in net:
        if ip=='111.118.178.0':
            print(mask)'''

'''alf=sorted('0123456789qwertyuiopasdfghjklzxcvbnm')
for x in alf[:19]:
    a=int(f'83{x}916', 19)
    b=int(f'123{x}45', 19)
    c=int(f'67{x}89', 19)
    d=a+b+c
    if d%17==0:
        print(x, d//17)
        break'''

'''def f(x, y):
    return (x<A) or (3*y+2*x>120) or (A>y)
for A in range(1, 1000):
    if all(f(x, y) for x in range(1, 100) for y in range(1, 100)):
        print(A)
        break'''

'''from sys import *
setrecursionlimit(10000)
def f(n):
    if n==1:
        return 1
    if n>1:
        return n-1+f(n-1)
print(f(2024)-f(2022))'''

'''d=[]
a=[int(x) for x in open('17.txt')]
b=[x for x in a if len(str(abs(x)))==5]
c=[x for x in a if x%100==29]
for i in range(len(a)-2):
    x, y, z = a[i], a[i+1], a[i+2]
    if (x in b)+(y in b)+(z in b)==2:
        if x+y+z<=max(c):
            d.append(x+y+z)
print(len(d), max(d))'''

'''def f(s, n):
    if s>=473:
        return n%2==0
    if n==0:
        return 0
    h=[f(s+1, n-1), f(s+5, n-1), f(s*4, n-1)]
    return any(h) if (n-1)%2==0 else all(h)
print([s for s in range(1, 473) if f(s, n=2)])
print([s for s in range(1, 473) if f(s, n=3) and not f(s, n=1)])
print([s for s in range(1, 473) if f(s, n=4) and not f(s, n=2)])'''

'''def f(a, b):
    if a>b or a==13:
        return 0
    elif a==b:
        return 1
    else:
        return f(a+1, b)+f(a+2, b)+f(a*3, b)
print(f(3, 8)*f(8, 18))'''

'''m=10**10
s=open('24.txt').readline()
s=s.split('T')
for i in range(len(s)-110):
    a='T'.join(s[i:i+111])
    m=min(m, len(a))
print(m)'''

'''k=0
from fnmatch import *
for x in range(1, 10**8+1):
    if fnmatch(str(x), '2*1?71'):
        if x%2023==0:
            print(x, x//2023)
            k+=1
            if k==5:
                break'''

'''from math import dist
clustersA=[[],[]]
clustersB=[[],[],[],[]]
for s in open('27A.txt'):
    s=s.replace(',','.')
    x, y = [float(i) for i in s.split()]
    if y<-6:
        clustersA[0].append([x, y])
    if y>-6:
        clustersA[1].append([x, y])
for s in open('27B.txt'):
    s=s.replace(',','.')
    x, y = [float(i) for i in s.split()]
    if x<-6:
        clustersB[0].append([x, y])
    if x>-6 and y<-6:
        clustersB[1].append([x, y])
    if x>-6 and -2.2>y>-6:
        clustersB[2].append([x, y])
    if y>-2.2:
        clustersB[3].append([x, y])
def c(cl):
    r=[]
    for p in cl:
        s=0
        for g in cl:
            s+=dist(p, g)
        r.append([s, p])
    return min(r)[1]
cA=[c(cl) for cl in clustersA]
#print(cA)
print('px1 =', int(10000*((-10.905880705597788-8.200449737762538)/2)))
print('py1 =', int(10000*((-10.204709977756867+0.6389817096874344)/2)))
cB=[c(cl) for cl in clustersB]
#print(cB)
print('px2 =', int(10000*((-7.802625235535932-3.524536597344898-2.227181886935543-2.0077768651389816)/4)))
print('py2 =', int(10000*((-6.109460942632754-7.61967069886266-3.794469655185359-0.8902897197106308)/4)))'''


# Номер 13 Пробник №2
'''
from ipaddress import *
for mask in range(1, 33):
    net=ip_network(f'111.118.179.50/{mask}', 0)
    if '111.118.178.0' in str(net):
            print(net.netmask)  # 255.255.254.0
'''

# Номер 14 Пробник №2
'''
alf = sorted('0123456789qwertyuiopasdfghjklzxcvbnm')
for x in alf[:19]:
    a = int(f'83{x}916', 19)
    b = int(f'123{x}45', 19)
    c = int(f'67{x}89', 19)
    d = a + b + c
    if d % 17 == 0:
        print(d // 17)
        break
'''

# Номер 19-21 Пробник №2
'''
def f(s, n):
    if s >= 473:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [f(s + 1, n - 1), f(s + 5, n - 1), f(s * 4, n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)


print([s for s in range(1, 473) if f(s, n=2)])
print([s for s in range(1, 473) if f(s, n=3) and not f(s, n=1)])
print([s for s in range(1, 473) if f(s, n=4) and not f(s, n=2)])
'''


# Номер 25 Пробник №2
'''
from fnmatch import *
for x in range(2023, 10**8+1, 2023):
    if fnmatch(str(x), '2*1?71'):
        print(x, x//2023)
'''


# Номер 24 Пробник №2
'''
m = 10 ** 10
s = open('files/24.txt').readline()
s = s.split('T')
for i in range(len(s) - 208):
    a = 'T' + 'T'.join(s[i:i + 209]) + 'T'
    m = min(m, len(a))
print(m)
'''


# Определите максимальное количество идущих подряд символов,
# среди которых символ T встречается ровно 3 раза.

s = 'xxxTxxxxxTxxTxxxxxxxTxxxxTxTxxxxxxxxxxxxTxxxx'
# ['xxx', 'xxxxx', 'xx', 'xxxxxxx', 'xxxx', 'x', 'xxxxxxxxxxxx', 'xxxx']
# xxxTxxxxxTxxTxxxxxxx
# xxxxxTxxTxxxxxxxTxxxx
# xxTxxxxxxxTxxxxTx
# xxxxxxxTxxxxTxTxxxxxxxxxxxx
# xxxxTxTxxxxxxxxxxxxTxxxx
maxi = 0
s = s.split('T')
for i in range(len(s) - 3):
    a = 'T'.join(s[i:i + 4])
    maxi = max(maxi, len(a))
print(maxi)


# Определите минимальное количество идущих подряд символов,
# среди которых символ T встречается ровно 3 раза.

mini = 10 ** 10
s = 'xxxTxxxxxTxxTxxxxxxxTxxxxTxTxxxxxxxxxxxxTxxxx'
# ['xxx', 'xxxxx', 'xx', 'xxxxxxx', 'xxxx', 'x', 'xxxxxxxxxxxx', 'xxxx']
# TxxxxxTxxT
# TxxTxxxxxxxT
# TxxxxxxxTxxxxT
# TxxxxTxT
# TxTxxxxxxxxxxxxT
s = s.split('T')
for i in range(len(s) - 1):
    a = 'T' + 'T'.join(s[i:i + 2]) + 'T'
    print(a)
    mini = min(mini, len(a))
print(mini)

# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 25, 27]
# КЕГЭ = [17, ]
# на следующем уроке: 24, 10

# Пробник №2
# Дата: #Вторник #24Февраля2026
# ✅ Верно: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 16, 17, 18, 21, 23, 27
# ⛔️ Неверно: 13, 14, 19, 20, 22, 24, 25, 26
# ❔ Без ответа: Нет
#
# Итог: 22/29 первичных балла ~ 78 вторичных


# Топ номеров 11.02.26
# 1. 19-21
# 2. 1
# 3. 2
# 4. 4
# 5. 5
# 6. 9
# 7. 17
# 8. 6
# 9. 23
# 10. 15
# 11. 14
# 12. 13
# 12. 25
# 13. 27
# 14. 18
# 15. 22
# 16. 7
# 17. 11
# 18. 16
# 19. 10