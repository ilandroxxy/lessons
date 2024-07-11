# region Домашка: ******************************************************************

'''
a = int(input())
b = int(input())
if a < b:
    c = 1
elif a > b:
    c = -1
for i in range(a, b + 1, c):
    print(i)
'''

'''
a = int(input())
b = int(input())
for i in range(min(a, b), max(a, b)+1):
    print(i)
'''
'''
s = '23490eriughnjreOEIJR-oirejght'
print(sorted(s))
print(min(s))  # -
print(max(s))  # u

print(max([1, 2, 3]))
print(max(1, 2, 3))

print(sum([1, 2, 3]))
# print(sum(1, 2, 3))
'''

'''
a = 129
print(a % 10)  # 9
print(-a % 10)  # 1
print(abs(-a) % 10)  # 9
'''

'''
m = int(input())
x = 1
for i in range(1, m+1):
    if m % i==0:
        x *= i
print(x)
'''

'''
import math

m = int(input())
R = []
for i in range(1, m+1):
    if m % i == 0:
        R.append(i)
print(math.prod(R))  # prod() - возвращает произведение элементов последовательности
'''

from time import time
start = time()

# m = 100_000_000
# div = []
# for i in range(1, m+1):
#     if m % i ==0:
#         div.append(i)
# print(div)


# m = 100_000_000
# div = []
# for i in range(1, int(m**1/2)+1):
#     if m % i == 0:
#         div.append(i)
#         div.append(m // i)
# print(div)

'''
def divisors(m):
    div = []
    for i in range(1, int(m ** (1 / 2)) + 1):
        if m % i == 0:
            div += [i, m // i]
            # div.append(i)
            # div.append(m // i)
            
    return sorted(set(div))


print(divisors(100_000_000))
# print(divisors(16))  # [1, 2, 4, 8, 16]


end = time()
print(end - start)  # 5.1972 -> 2.5422 -> 1.512091 -> 0.000327
'''

'''
n = int(input())
A = []
while n > 0:
    x = n % 10
    A.append(x)
    n = n // 10  # n //= 10
print(max(A))
print(min(A))


n = int(input())
maxi = 0
mini = 10**9
while n > 0:
    x = n % 10
    if maxi < x:
        maxi = x
    mini = min(mini, x)
    n //= 10
print(maxi)
print(mini)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = []
# КЕГЭ  = []
# на следующем уроке: Создать учебный репозиторий через github
