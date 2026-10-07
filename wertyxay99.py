
# 2.
'''
from itertools import*
def f(x,y,z,w):
    return (x and (not z) and (not w))or(x and (not z)and y)
for i in product([0,1], repeat=7):
    table = [(1,i[0],i[1],i[2]),(0,i[3],1,i[4]),(i[5],i[6],0,0)]
    for p in permutations('xyzw'):
        if len(table)==len(set(table)):
            if [f(**dict(zip(p,row))) for row in table]==[1,1,1]:
                print(p)
'''
from xxsubtype import bench

# 5.
'''
def f(n,base):
    s = ''
    while n > 0:
        s = str(n % base) + s
        n //= base
    return s

def s(n):
    return n.count('1')+n.count('2')*2

ans = []
for N in range(1,10000):
    n = f(N,3)
    if N%3==0:
        n+= n[-2:]
    else:
        n+= f((s(n)*2),3)
    r = int(n,3)
    if r>520 and r%2!=0:
        ans.append(r)
print(min(ans))
'''


# 6. ВОПРОС



# 8.
'''
from itertools import*
words = product(sorted('СИМВОЛ'),repeat = 5)
c= 0
for w in words:
    c+=1
    if w[0]!='С' and w[0] != "О":
        if w.count('В')==1:
            if w.count('С')<=1:
                if c%2!=0:
                    print(w,c)
'''


# 9.
'''
f = open('9.txt')
c = 0
for  i in f:
    lst = [int(x) for x in i.split()]
    if lst == sorted(set(lst)):
        if lst[0]+lst[-1]<= sum(lst)-(lst[0]+lst[-1]):
            c+=1
print(c)
'''


# 13. ВОПРОС


# 14.
'''
d = '0123456789ABCDEFGHIJKLM'
ans = []
for x in range(23):
    n = int('761'+d[x]+'035',23)+int('338'+str(x)+'932',23)
    if n%22==0:
        ans.append(n//22)
print(min(ans))
'''

'''
from string import digits, ascii_uppercase
alp = digits + ascii_uppercase
print(alp)  # 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ

alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
print(alp)  # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
print(alp[:2])  # ['0', '1']
print(alp[:8])  # ['0', '1', '2', '3', '4', '5', '6', '7']


ans = []
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alp[:23]:
    n = int(f'761{x}035', 23) + int(f'338{x}932', 23)
    if n % 22 == 0:
        ans.append(n // 22)
print(min(ans))  # 70045642
'''





# 16. ВОПРОС


# 17.
'''
ans = []
lst = [int(x) for x in open('files/17.txt')]
m3 = [x for x in lst if len(str(abs(x))) == 3]
m28 = [x for x in lst if abs(x) % 100 == 28]
for i in range(len(lst) - 2):
    a, b, c = lst[i:i+3]
    if (a in m3) + (b in m3) + (c in m3) >= 1:
        avg = (a + b + c) / 3
        if avg > 0 and avg < max(m28):
            ans.append(a + b + c)
print(len(ans), max(ans))
'''


# 19-21.
'''
def f(s,n):

    if s>=124:return n%2==0
    if n==0:return 0
    h = [f(s+1,n-1),f(s+5,n-1),f(s*3,n-1)]
    return any(h) if (n-1)%2==0 else all(h)
print([s for s in range(1,124)if f(s,2)])
print([s for s in range(1,124)if not f(s,1) and f(s,3)])
print([s for s in range(1,124)if not f(s,2) and f(s,4)])
'''


# 22. ВОПРОС


# 23.
'''
def f(a, b):
    if a <= b or a == 73:
        return a == b
    return f(a - 3, b) + f(a - 8, b) + f(a // 2, b)
print(f(76, 41) * f(41, 12))
'''

# № 31510 Демоверсия 2027(Уровень: Базовый)
# A. Прибавь 1
# B. Поменяй местами
# Первая из этих команд увеличивает число на экране на 1.
# Вторая команда применяется только к числу, у которого
# цифра в разряде десятков по значению меньше цифры,
# стоящей в разряде единиц, и действует, заменяя число
# на экране числом, в котором цифры двух младших разрядов
# поменялись местами.

# Сколько существует программ, для которых при исходном
# числе 100 результатом является число 141?
'''
def F(a, b):
    if a >= b:
        return a == b

    if str(a)[1] < str(a)[2]:
        return F(a + 1, b) + F( int(str(a)[0] + str(a)[-1] + str(a)[-2])  , b)
    else:
        return F(a + 1, b)

print(F(100, 141))
'''

'''
M = ['a', 'b', 'c', 'd', 'e']
M[0], M[-1] = M[-1], M[0]
print(M)  # ['e', 'b', 'c', 'd', 'a']

s = 'abcde'
s = s[-1] + s[1:-1] + s[0]
print(s)  # ebcda
'''



# 25. ВОПРОС
#
# 27. ВОПРОС
'''
clusterA = [[],[]]
clusterB  = [[],[],[]]
for i in open('27_A.txt'):
    x,y = [float(x) for x in i.split()]
    if y>15:
        clusterA[0].append([x,y])
    else:
        clusterA[1].append([x,y])
for i in open('27_B.txt'):
    x,y = [float(x) for x in i.split()]
    if y>23:
        clusterB[0].append([x,y])
    elif x<25:
        clusterB[1].append([x,y])
    else:
        clusterB[2].append([x,y])

def dist(p1,p2):
    x1,y1=p1
    x2,y2=p2
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def center(cl):
    lst =[]
    for p in cl:
        s = sum(dist(p,p1) for p1 in cl)
        lst.append([s,p])
    return min(lst)[1]
'''



# № 8696 (Уровень: Средний)
# Пусть M – сумма всех натуральных делителей целого числа, не считая единицы и самого числа. Если число простое, тогда M = 0.
#
# Напишите программу, которая перебирает целые числа, большие 1 273 547,
# в порядке возрастания и ищет среди них такие, для которых значение M при
# делении на 100 000 даёт в остатке простое число. Вывести первые 5 найденных
# чисел и соответствующие им значения M.
#
# Формат вывода: для каждого из 5 таких найденных чисел в отдельной строке
# сначала выводится само число, затем – значение М. Строки выводятся в
# порядке возрастания найденных чисел.
'''
def divisors(x):
    d = []
    # for j in range(1, int(x ** 0.5)+1):  # (не считая единицы и самого числа) - если нет
    for j in range(2, int(x ** 0.5)+1):  # (не считая единицы и самого числа) - если есть
        if x % j == 0:
            d += [j, x // j]
    return sorted(set(d))

cnt = 0
for x in range(1_273_547+1, 10**10):
    d = divisors(x)
    if len(d) > 0:
        M = sum(d)
        if len(divisors(M % 100_000)) == 0:
            print(x, M)
            cnt += 1
            if cnt == 5:
                break
'''

# № 31134 Основная волна 18.06.26(Уровень: Средний)
'''
def divisors(x):
    d = []
    for j in range(2, int(x ** 0.5)+1):
        if x % j == 0:
            d += [j, x // j]
    return sorted(set(d))

cnt = 0
for x in range(8_007_494_154+1, 10**10):
    d = [j for j in divisors(x) if len(divisors(j)) == 0 and str(j).count('567') == 1]
    if len(d) >= 2:
        M = min(d) + max(d)
        if M > 80_000 and len(divisors(M)) == 0:
            print(x, M)
            cnt += 1
            if cnt == 5:
                break
'''
# 8007495062 615679
# 8007495772 5671033
# 8007531302 856789
# 8007532410 5679103
# 8007559070 1567039



# № 31130 Основная волна 18.06.26(Уровень: Средний)

def divisors(x):
    d = []
    for j in range(1, int(x ** 0.5)+1):
        if x % j == 0:
            d += [j, x // j]
    return sorted(set(d))

cnt = 0
from itertools import product
for x in range(2_626_695_891+1, 10**10):
    d = [j for j in divisors(x) if len(divisors(j)) == 2 and str(j).count('67') == 1]
    if len(d) > 0:
        for p in product(d, repeat=2):
            if p[0] * p[1] == x:
                print(x, min(p))
                cnt += 1
                break
        if cnt == 5:
            break






