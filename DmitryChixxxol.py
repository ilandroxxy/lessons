# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# 📱 Давайте рассмотрим две полезные функции в Python: split() и join() #tpy
# Функции split() и join() в Python являются мощными инструментами для работы со строками.
# split() позволяет разбивать строки на части, а join() — объединять их обратно.

# 🚩 Функция split()
# Функция split() используется для разделения строки на части, создавая список.
# По умолчанию строка разбивается по пробелам, но вы также можете указать другой разделитель.
'''
# Пример 1: Разделение по пробелам
text = "Привет, мир! Как дела?"
words = text.split()  # Разделяем строку по пробелам
print(words)  # Вывод: ['Привет,', 'мир!', 'Как', 'дела?']

# Пример 2: Разделение по заданному разделителю
data = "яблоко;банан;груша"
fruits = data.split(';')  # Разделяем строку по символу ";"
print(fruits)  # Вывод: ['яблоко', 'банан', 'груша']
'''

# 🚩 Функция join()
# Функция join() объединяет элементы списка в строку, используя заданный разделитель.
'''
# Пример 1: Объединение списка слов
words = ['Привет,', 'мир!', 'Как', 'дела?']
sentence = ' '.join(words)  # Объединяем слова с пробелом
print(sentence)  # Вывод: Привет, мир! Как дела?

# Пример 2: Объединение списка с заданным разделителем
fruits = ['яблоко', 'банан', 'груша']
result = ';'.join(fruits)  # Объединяем фрукты через запятую и пробел
print(result)  # Вывод: яблоко;банан;груша
'''


# № 18133 (Уровень: Базовый)
# (В. Колчев) Все 5-буквенные слова, в составе которых
# могут быть только буквы К,О,Д,И,М,
# записаны в алфавитном порядке и пронумерованы.
# Вот начало списка:
# 1. ДДДДД
# 2. ДДДДИ
# 3. ДДДДК
# 4. ДДДДМ
# 5. ДДДДО
# …
# Под каким номером в списке идёт последнее слово, которое содержит
# ровно две буквы М и не содержит букв М, стоящих рядом?
'''
# Вариант 1
s = sorted('КОДИМ')
n = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    n += 1
                    if slovo.count('М') == 2 and 'ММ' not in slovo:
                        print(n)

# Вариант 2
from itertools import *
n = 0
for p in product(sorted('КОДИМ'), repeat=5):
    slovo = ''.join(p)
    n += 1
    if slovo.count('М') == 2 and 'ММ' not in slovo:
        print(n)


# Вариант 3
from itertools import *
for n, p in enumerate(product(sorted('КОДИМ'), repeat=5), 1):
    slovo = ''.join(p)
    if slovo.count('М') == 2 and 'ММ' not in slovo:
        print(n)
'''


# № 17799 (Уровень: Средний)
# (В. Зарянкин) Все четырёхбуквенные слова, в составе которых могут быть
# только русские буквы А, Р, Г, У, М, Е, Н, Т, записаны в алфавитном порядке и пронумерованы начиная с 1.
# Вот начало списка:
# 1. АААА
# 2. АААГ
# 3. АААЕ
# 4. АААМ
# 5. АААН
# ...
#
# Под каким номером в списке идёт последнее слово, в котором
# все буквы различны и все символы располагаются в алфавитном порядке?
'''
from itertools import *
for n, p in enumerate(product(sorted('АРГУМЕНТ'), repeat=4), 1):
    slovo = ''.join(p)
    if len(slovo) == len(set(slovo)):  # все буквы различны
        # print(slovo)  # АГЕМ
        # print(list(slovo))  # ['А', 'Г', 'Е', 'М']
        # print(sorted(slovo))  # ['А', 'Г', 'Е', 'М']
        if list(slovo) == sorted(slovo):
            print(n)
'''

# № 18042 (Уровень: Базовый)
# (Л. Шастин) Ваня составляет 5-буквенные слова, в которых
# могут быть использованы только буквы Л, Ю, С, Т, Р, А, причём
# буква Ю используется не более двух раз.
# Также слово не должно оканчиваться согласными буквами.
# Сколько существует таких слов, которые может написать Ваня?
'''
from itertools import *
cnt = 0
for p in product('ЛЮСТРА', repeat=5):
    slovo = ''.join(p)
    if slovo.count('Ю') <= 2:
        if slovo[-1] not in 'ЛСТР':
            cnt += 1
print(cnt)
'''


# № 12917 PRO100 ЕГЭ 26.01.24 (Уровень: Базовый)
# Петя составляет слова путём перестановки букв в слове ПРОСТО.
# Сколько он сможет составить слов,
# если запрещено ставить рядом две одинаковые буквы?
'''
from itertools import *
r = []
for p in permutations('ПРОСТО'):
    slovo = ''.join(p)
    if 'ОО' not in slovo:
        r.append(slovo)
print(len(set(r)))
'''


# № 17627 Основная волна 19.06.24 (Уровень: Базовый)
# Определите количество 15-ричных пятизначных чисел,
# в записи которых ровно одна цифра 8
# и не менее двух цифр с числовым значением, превышающим 9.
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
from itertools import *
cnt = 0
for p in product(alphabet[:15], repeat=5):
    num = ''.join(p)
    if num[0] != '0':
        if num.count('8') == 1:
            if len([x for x in num if x > '9']) >= 2:
                cnt += 1
print(cnt)
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 6, 8, 12]
# КЕГЭ  = []
# на следующем уроке:
