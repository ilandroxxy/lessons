# region Домашка: ************************************************************

'''
M = [1, 2, 3]  # list (список)
print(type(M))  # <class 'list'>

M.append(4)  # Метод - это функция для конкретного типа данных (класса)
print(M)  # [1, 2, 3, 4]
'''

# Домашнее задание 3
# Создайте класс 'Car', который имеет атрибуты:
# - 'make'' (марка автомобиля),
# - 'model' (модель автомобиля),
# - 'year' (год выпуска).
#
# Дайте им также метод 'display_info', который выводит информацию о машине (марка, модель и год).
'''
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f'Марка: {self.make}, Модель: {self.model}, Год выпуска: {self.year}')


my_car = Car('Honda', 'Civic', '2008')
my_car.display_info()
'''
# Марка: Honda, Модель: Civic, Год выпуска: 2008


# Домашнее задание 4
# Создайте родительский класс 'Animal' с атрибутами 'name' и 'species'
# Дайте им также метод 'make_sound', который выводит звук, издаваемый животными.
#
# Создайте подклассы 'Dog' и 'Cat', которые наследуют от класса 'Animal'.
# Дайте каждому из них собственный метод make_sound(),
# который выводит соответсвующий звук (Гав для собаки и Мяу для кота).
'''
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print('Животное издает звук:')


class Dog(Animal):

    def make_sound(self):
        print('Гав')


class Cat(Animal):

    def make_sound(self):
        print('Мяу')


dog = Dog('Шарик', 'Собака')
dog.make_sound()  # Гав

cat = Cat('Мурка', 'Кошка')
cat.make_sound()  # Мяу
'''


# Домашнее задание 5
'''
with open('sample.txt', mode='r') as f:
    print(f.read())
'''


# endregion Домашка: *********************************************************
# #
# #
# region Урок: ************************************************************


# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# ФИПИ = []
# КЕГЭ = []
# на следующем уроке:
