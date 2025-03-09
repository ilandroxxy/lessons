# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

"""from itertools import*
#2
def f(x,y,z,w):
    return (z<=x) and ((x and(y==(not(z)))) <= w)
for p in permutations('xyzw'):
    for q1,q2,q3,q4,q5 in product([0,1],repeat=5):
        table=[(q1,1,1,q2),
               (0,0,q3,q4),
               (q5,0,0,0)]
        if len(set(table)) == len(table):
            if [f(**dict(zip(p,r))) for r in table] == [0,0,0]:
                print(*p)
"""

'''
from string import *
alphabet = digits + ascii_uppercase

def convert(n, b):
    r = ''
    while n > 0:
        r = alphabet[n % b] + r
        n //= b
    return r

#5
k = []
for n in range(1, 1000):
    # b = bin(n)[2:]
    # b = f'{n:b}'
    b = convert(n, 2)

    if b.count('0') % 2 == 0:
        b = "1" + b + "1"
    else:
        b = "10" + b
    r = int(b, 2)
    if r < 100:
        k.append(r)
print(max(k))
'''


#8
'''
k=0
from itertools import*
for w in set(permutations('парижанка')):
    s="".join(w)
    if (s.count('иа')+s.count('аа')+s.count('ии')+s.count('аи')) == 1:
        if (s.count('иии')+s.count('ааа')+s.count('ааи')+s.count('аиа')+s.count('иаа')) == 0:
            k+=1
print(k)

from itertools import *
R = []
for w in permutations('парижанка'):
    s = "".join(w)
    word = s
    s = s.replace('и', 'а')
    if s.count('аа') == 1 and 'ааа' not in s:
        R.append(word)
print(len(set(R)))

from itertools import *
k = 0
for w in set(permutations('парижанка')):
    s = "".join(w).replace('и', 'а')
    if s.count('аа') == 1 and 'ааа' not in s:
        k += 1
print(k)
'''




#9
'''
k=s=0
for line in open('0. files/9.csv'):
    k+=1
    n=[int(x) for x in line.split(';')]
    a=[x for x in n if n.count(x) ==1]
    if len(a) == 4:
        ma=max(a)
        mi=min(a)
        sm=(ma+mi)**2
        a.remove(ma)
        a.remove(mi)
        kub=((a[0]**3)+(a[1])**3)
        if sm>kub:
            s+=k
print(s)
'''
'''
n = 0
summa = 0
for s in open('0. files/9.csv'):
    n += 1
    M = sorted([int(x) for x in s.split(';')])
    if len(M) == len(set(M)):
        if (M[0] + M[-1]) ** 2 > (M[1] ** 3 + M[2] ** 3):
            summa += n
print(summa)
'''


"""
#12
for n in range(3,10001):
    s='2'+"5"*n
    while "25" in s or "355" in s or "555" in s:
        if "25" in s:
            s=s.replace('25','5',1)
        if "355" in s:
            s=s.replace('355','522',1)
        if '555' in s:
            s=s.replace('555','3',1)
    if s.count('2') == 10:
        print(n)
        break
"""
#13
"""from ipaddress import *
net = ip_network('158.214.121.40/255.255.255.224',0)
for ad in net.hosts():
    print(ad)
"""
"""
#14
k=0
s=5*729**2024+3*243**1413-7*81**169-2*9**107+3017
while s >0:
    if s % 27 <= 25:
        if ((s % 27)%2)==0:
            k+=s%27
        s//=27
print(k)
"""
'''
from string import *
alphabet = digits + ascii_uppercase

def convert(n, b):
    r = ''
    while n > 0:
        r = alphabet[n % b] + r
        n //= b
    return r


n = 5 * 729 ** 2024 + 3 * 243 ** 1413 - 7 * 81 ** 169 - 2 * 9 ** 107 + 3017
r = convert(n, 27)
print(sum([alphabet.index(x) for x in r if x in alphabet[::2] and x <= 'P']))
'''

"""
#16
from functools import*
@lru_cache(None)
def f(n):
    if n<15: return 4
    if n >= 15 and n%3 == 0: return f(2*n//3)+n-1
    else: return f(n-1)+3
for n in range(0,1000): 
    if f(n) == 251:
        print(n)
"""
"""
#17
k=[]
n=[int(x) for x in open('17_19486.txt')]
otr=[int(x) for x in n if x<0]
pol=[int(x) for x in n if x>0]
n7=[int(x) for x in n if abs(x) % 10 == 7]
for a,b in zip(n,n[1:]):
    if (((a in otr) and (b in pol)) or ((a in pol) and (b in otr))):
        if (a+b)<len(n7):
            k.append(a+b)
print(len(k),max(k))
"""
#19-21
"""def f(s1,s2,p):
    if (s1+s2)<=100 and (p == 2 or p == 4):
        return True
    if ((s1+s2)>100 and p == 4) or ((s1+s2)<100 and (p!=2 or p!=4)):
        return False
    if p % 2 ==0:
        return  f(s1-3,s2-3,p+1) and f(s1//2,s2,p+1) and f(s1,s2//2,p+1)
    else:
        return f(s1-3,s2-3,p+1) or f(s1//2,s2,p+1) or f(s1,s2//2,p+1)
for s2 in range(53,1000):
    if f(48,s2,0) == True:
        print(s2)
"""
"""
#23
def f(n, m):
    if n >= m: return n == m
    return f(n + 2, m) + f(n + 3, m) + f(n * 2, m)
print(f(8,35) - f(8,20)*f(20,30)*f(30,35))
"""
#25
"""from functools import *
for i in range(1984,10**10+1,1984):
    if fnmatch(str(i),'[2468]9?23?*23[13579][2468]'):
        print(i,i//1984)
"""
#27
"""from math import*
clA=[[],[]]

for line in open('27_A_19647.txt'):
    x,y=[float(k) for k in line.split()]
    if x<4:
        clA[0].append([x,y])
    else:
        clA[1].append([x,y])

def center(cl):
    m=[]
    for p in cl:
        sm=sum([dist(p,p1) for p1 in cl])
        m.append([sm,p])
    return min(m)[1]

centersA =[center(cl) for cl in clA]
cA=[[2.3392, 2.6712], [5.8917, -0.0602]]
#center(cA) = [2.3392, 2.6712]
print(*[10000*x for x in center(cA)])
"""

'''
from math import*
mi = float("inf")
ma = float("-inf")
for x in [k * 0.25 for k in range(0,10000000)]:
    A = 0
    P = 52 <= x <= 105
    Q = 0 <= x <= 52
    f = ((not P) and (not Q) and (not(A))) <= (x *x > 303601)
    if f != 1:
        mi = min(mi,x)
        ma = max(ma,x)
        print(ceil(ma-mi))
'''
'''
def F(x, a1, a2):
    C = 48 <= x <= 94
    J = 83 <= x <= 100
    A = a1 <= x <= a2
    return (not(C or J)) <= (not A)

R = []
M = [x / 4 for x in range(40 * 4, 120 * 4)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(max(R))
'''





# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25]
# КЕГЭ  = []
# на следующем уроке: 15 отрезки, 22, 24,
