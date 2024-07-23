# region Домашка: ******************************************************************

'''
alphabet = sorted('1234567890qwertyuiopasdfghjklzxcvbnm')

def convert(n, b):
    r = ''
    while n > 0:
        r = alphabet[n % b] + r
        n //= b
    return r


x = 766**66 + 15**13 - 22
s = convert(x, 13)
print(s.count('c'))
'''

'''
x = 766**66 + 15**13 - 22
M = []
while x > 0:
    M.append(x % 13)
    x //= 13
M.reverse()
print(M.count(12))
'''

'''
R = []
for x in range(2031):
    n = 7**91 + 7**160 - x
    s = []
    while n > 0:
        s.append(n % 7)
        n //= 7
    s.reverse()
    if s.count(0) == 70:
        R.append(x)
print(max(R))
'''

'''
R = []
alphabet = sorted('1234567890qwertyuiopasdfghjklzxcvbnm')
for x in alphabet[:15]:
    A = int(f'97531{x}19', 15)
    B = int(f'3{x}519', 15)
    if (A + B) % 11 == 0:
        R.append((A + B) // 11)

print(min(R))
'''

'''
alphabet = sorted('1234567890qwertyuiopasdfghjklzxcvbnm')
R = []
for y in alphabet[:15]:
    for x in alphabet[:15]:
        A = int(f'123{x}5', 15)
        B = int(f'67{y}9', 17)
        if (A + B) % 131 == 0 and y < x:
            print(y, x, (A + B) // 131)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Операторы break, continue и функция exit()
'''
k = 0
while True:  # бесконечный цикл
    k += 1
    if k == 10000:
        exit()  # - функция прерывает выполнение программы
    if k == 5000:
        break  # - прерывает цикл в котором он находится
    if k % 2 == 0:
        continue  # - прерывает текущую итерацию цикла (шаг)
    print(k)

for x in range(10):
    for y in range(10):
        if y == 5:
            break
        print(x, y)
'''



# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [5, 14]
# КЕГЭ  = []
# на следующем уроке:
