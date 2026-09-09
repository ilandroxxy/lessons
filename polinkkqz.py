
# int(), str(), float()
'''
n = int(input())
n = str(n)
print(max(n))
print(min(n))
'''


# print(min(23,432,4 ,3245,34,543,5))

# https://stepik.org/lesson/1309434/step/8?unit=1324550
'''
n = int(input())
maxi, mini = 0, 10**8
while n > 0:
    ostat = n % 10

    if ostat > maxi:
        maxi = ostat

    mini = min(mini, ostat)

    n //= 10
print(maxi)
print(mini)
'''

'''
n = int(input())  # 897236
cnt2 = 0
cnt1 = 0
while n > 0:
    x = n % 10

    if x % 2 == 0:
        cnt2 += 1
    else:
        cnt1 += 1

    n //= 10

print(cnt2)
print(cnt1)
'''

# https://stepik.org/lesson/1309434/step/10?unit=1324550
'''
n = int(input())
cnt1, cnt2 = 0, 0
for i in range(n):
    x = int(input())
    if x % 2 == 0:
        cnt2 += 1
    else:
        cnt1 += 1
print(cnt2)
print(cnt1)
'''

# https://stepik.org/lesson/1309435/step/10?unit=1324551
'''
summa = 0
n = int(input())  # 220000004
for j in range(1, n+1):
    if n % j == 0:
        summa += j
print(summa)
'''

'''
a = int(input())
b = int(input())
for n in range(a, b+1):
    cnt = 0
    for j in range(1, n+1):
        if n % j == 0:
            cnt += 1
    if cnt == 2:
        print(n)
'''

# -2 -1 0 1 2 3 4 - целые числа
# 1 2 3 4 5 6 7 8 - натуральные
# 2 3 5 7 11 13 - простые числа


# https://stepik.org/lesson/1309434/step/10?unit=1324550
