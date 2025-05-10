# region Домашка: ******************************************************************
from sys import base_prefix
from zoneinfo import reset_tzpath


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************
'''
def divi(x):
    div=[]
    for i in range(1,(int(x**0.5)+1)):
        if x%i==0:
            div+=[i,x//i]
    return sorted(set(div))


cnt=0
for i in range(500_001,10**9):
    d=divi(i)
    if len(d)!=0:
        R = sum(d)
        if R%10==6:
            cnt+=1
            print(i,R)
            if cnt==5:
                break
'''

'''
def divi(x):
    div=[]
    for i in range(2,(int(x**0.5)+1)):
        if x%i==0:
            div+=[i,x//i]
    return sorted(set(div))

cnt=0
for x in range(1125000+1,10**9):
    d=[i for i in divi(x) if i%10==7 and i!=7]
    if len(d)!=0:
        cnt+=1
        print(x, min(d))
        if cnt==5:
            break
'''

'''
def divi(x):
    div=[]
    for i in range(2,(int(x**0.5)+1)):
        if x%i==0:
            div+=[i,x//i]
    return sorted(set(div))

cnt=0
for x in range(1273547+1,10**9):
    d=divi(x)
    if len(d)!=0:
        M=sum(d)
        if len(divi(M % 100_000)) == 0:
            cnt+=1
            print(x,M)
            if cnt==5:
                break
'''

'''
from fnmatch import *

def divi(x):
    div=[]
    for i in range(1,(int(x**0.5)+1)):
        if x%i==0:
            div+=[i,x//i]
    return sorted(set(div))

cnt=0
for x in range(10**7):
    if fnmatch(str(x),'*2?2*'):
        if str(x) == str(x)[::-1]:
            if x%53==0 :
                d=divi(x)
                if len(d)>30:
                    print(x,sum(d))
'''

'''
from fnmatch import *
def divi(x):
    div=[]
    for i in range(2,(int(x**0.5)+1)):
        if x%i==0:
            div+=[i,x//i]
    return sorted(set(div))

for x in range(10**7):
    if fnmatch(str(x),'3*52?'):
        d=divi(x)
        if len(d)%2!=0:
            print(x,max(d))
'''

'''
def divi(x):
    div=[]
    for i in range(2,(int(x**0.5)+1)):
        if x%i==0:
            div+=[i,x//i]
    return sorted(set(div))

cnt=0
for x in range(220_000+1,10**9):
    d=divi(x)
    if len(d) > 0:
        M=min(d)+max(d)
        if M%10==4:
            cnt+=1
            print(x,M)
            if cnt==5:
                break
'''

'''
def divi(x):
    div=[]
    for i in range(2,(int(x**0.5)+1)):
        if x%i==0:
            div+=[i,x//i]
    return sorted(set(div))

cnt=0
for x in range(460_000_000+1,10**9):
    d=divi(x)
    if len(d)>=5:
        M=d[-5]
        if M > 0:
            cnt+=1
            print(M)
            if cnt==5:
                break
'''

# № 2685 Пробный 02.2022 /dev/inf Base level (Уровень: Средний)
'''
def divi(x):
    div=[]
    for i in range(2,(int(x**0.5)+1)):
        if x%i==0:
            div+=[i,x//i]
    return sorted(set(div))

cnt=0
for x in range(1_200_000, 1, -1):
    d=divi(x)
    if len(d)>=2:
        S=d[0] + d[1]
        if S!=0 and S%2022==0:
            cnt+=1
            print(x,S)
            if cnt==5:
                break
'''

'''
def divi(x):
    div=[]
    for i in range(2,(int(x**0.5)+1)):
        if x%i==0:
            div+=[i,x//i]
    return sorted(set(div))

cnt=0

for x in range(400_000_000+1,10**9):
    d=divi(x)
    if len(d)>=5:
        P=d[0]*d[1]*d[2]*d[3]*d[4]
        if P%100==17 and P < x:
            cnt+=1
            print(P, d[4])
            if cnt==5:
                break
'''

'''
def divi(x):
    div=[]
    for i in range(1,(int(x**0.5)+1)):
        if x%i==0:
            div+=[i,x//i]
    return sorted(set(div))

for x in range(190201,190260+1):
    d=[i for i in divi(x) if i%2==0]
    if len(d)==4:
        print(d[-1], d[-2])
'''

'''
def divi(x):
    div=[]
    for i in range(1,(int(x**0.5)+1)):
        if x%i==0:
            div+=[i,x//i]
    return sorted(set(div))

cnt=0
for x in range(500_000+1,10**9):
    d=[i for i in divi(x) if i%10==8 and i!=8 and i!=x]
    if len(d)>0:
        cnt+=1
        print(x, min(d))
        if cnt==5:
            break
'''

# endregion Урок: ********************************************************************
# #
# #
# region Разобрать: ********************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25, 26.1]
# КЕГЭ  = [5, 9, 14, 15, 16, 17, 22, 23]
# на следующем уроке:


# Первый пробник 21.12.24:
# Александр 19/25 -> 75 вторичных баллов +[1-5, 7, 9-10, 12, 14-16, 18-22, 24, 25] -[6, 8, 11, 13, 17, 23]

# Второй пробник 28.02.25:
# Александр 24/25 -> 88 вторичных баллов +[1-10, 12-25] -[11]
# Саша 10/25 -> 51 вторичных баллов +[1, 2, 4, 12, 14-16, 19, 23, 25] -[3, 5, 6-10, 11, 13, 17, 18, 20-22, 24]
