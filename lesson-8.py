# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать
# дату в виде строки формата «день-месяц-год». В рамках класса реализовать
# два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
# год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


class Date:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year


    def display(self):
        return f'{self.day}-{self.month}-{self.year}'


    @classmethod
    def date_class(cls, day, month, year):
        return cls(day, month, year)

    @staticmethod
    def date_static(day, month):
        return Date(day, month, 2019) # year для примера

date = Date(9, 11, 2018)
date_1 = Date.date_class(25, 12, 1990)
date_2 = Date.date_static(21, 1)

print(date.display())
print(date_1.display())
print(date_2.display())


# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
# в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class ZeroDivisionError:
    def __init__(self, x):
        self.x = x


    def __truediv__(self, y):
        try:
            return round(self.x / y)
        except:
            return ('ZeroDivisionError')


number = ZeroDivisionError(50)
print(number / 5)
print(number / 0)

# 2 --------------------------
class ZeroDivisionError:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def truediv(x, y):
        try:
            return (x / y)
        except:
            return ('ZeroDivisionError')


number = ZeroDivisionError(25, 4)
print(ZeroDivisionError.truediv(10, 5))
print(ZeroDivisionError.truediv(10, 2))
print(number.truediv(100, 0))

