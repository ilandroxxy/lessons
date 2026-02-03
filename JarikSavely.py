# region Домашка: ******************************************************************



# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
s = open('files/24.txt').readline()
s = s.split('WWF')
maxi = 0
for i in range(len(s) - 120):
    r = 'WF' + 'WWF'.join(s[i:i + 121]) + 'WW'
    if 'WSFWW' not in r:
        maxi = max(maxi, len(r))
print(maxi)
'''


'''
from itertools import permutations

table = '12 15 16 21 23 24 32 36 37 42 47 51 56 61 63 65 73 74'
graph = 'AB BA AF FA FB BF FE EF BD DB ED DE EC CE DG GD CG GC'

for per in permutations('ABCDEFG'):
    new_table = table
    for i in range(1, 7+1):
        new_table = new_table.replace(str(i), per[i-1])
    if set(new_table.split()) == set(graph.split()):
        print('1 2 3 4 5 6 7')
        print(*per)



R = []
for n in range(1 ,10000):
    s = f'{n:b}'
    if n%5 == 0:
       s = s + '11'
    else:
        s = s + f'{n//5:b}'
    r = int(s,2)
    if n % 2 != 0 and r >= 783:
        R.append(n)
print(min(R))
'''

RES = []
alp = sorted('0987654321QWERTYUIOPLKJHGFDSAZXCVBNM')
def convert(n,b):
    r = ''
    while n > 0:
        r += alp[n%b]
        n //= b
    return r[::-1]
for x in range(1, 8410):
    n = 29**293 + 29**271 - x
    r = convert(n, 29)
    RES.append(r.count('0'))
print(max(RES))

# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25, 27]
# КЕГЭ = []
# на следующем уроке: 10, 12, 24, 26
