
'''
from math import prod
m = int(input())
d = []
for i in range(1, m + 1):
    if m % i == 0:
        d.append(i)
print(prod(d))
'''



cnt = 0
for x in range(10, 100):
    if (x % 2 != 0) and (not(x > 67)):
        cnt += 1
print(cnt)


# 11 13 14 .. 67



