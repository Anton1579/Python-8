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