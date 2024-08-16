
'''
x = int(input())
if x % 2 == 0:
    print("Чётное")
# elif x % 2 != 0:
else:
    print("Нечётное")
'''

'''
a = int(input())
b = int(input())
c = int(input())
summa = 0
if (a % 7 == 0 and a % 49 != 0) or a % 40 == 0:
    summa += a  # summa = summa + a
if (b % 7 == 0 and b % 49 != 0) or b % 40 == 0:
    summa += b
if (c % 7 == 0 and c % 49 != 0) or c % 40 == 0:
    summa += c
print(summa)
'''


'''
a = int(input())
b = int(input())
c = int(input())

if a % b == 0 and c % b == 0:
    print("Равносторонний")
elif a % b != 0 and c % b != 0 and a % c != 0:
    print("Разносторонний")
else:
    print('Равнобедренный')
'''


'''
x = int(input())
a = x // 10000
b = (x // 1000) % 10
c = (x // 100) % 10
d = (x // 10) % 10
e = x % 10
# произведение первой и третьей цифр равно сумме второй, четвертой и пятой цифр.
if a * c == b + d + e:
    print('Да')
else:
    print('Нет')
'''

'''
# range(START=0, STOP=12-1)
for x in range(12):
    print(x, end=' ')

print(2 + 4 + 6 + 8 + 10)
'''

# tоtаl = 1
# fоr i in range(2, 6):   #
#     total *= i
# рrint(total)


m = int(input())
t = 1
for j in range(1, m+1):
    if m % j == 0:
        t *= j
print(t)