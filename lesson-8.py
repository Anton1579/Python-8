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


# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на
# наличие только чисел. Проверить работу исключения на реальном примере. Необходимо запрашивать
# у пользователя данные и заполнять список. Класс-исключение должен контролировать типы данных
# элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь
# сам не остановит работу скрипта, введя, например, команду “stop”. При этом скрипт завершается,
# сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и
# вносить его в список, только если введено число. Класс-исключение должен не позволить пользователю
# ввести текст (не число) и отобразить соответствующее сообщение. При этом работа скрипта
# не должна завершаться.

class Error:
    def __init__(self, list_1):
        self.list_1 = list_1
        self.list_1 = []

    def my_list(self):
        while True:
            try:
                number_1 = int(input('Введите число: '))
                self.list_1.append(number_1)
                print(self.list_1)
            except:
                print('Вы вели не число. Остановить? Y/N')
                number_2 = input('Введите число: ')

                if number_2 == 'N' or number_2 == 'n':
                    print(conclusion.my_list())
                elif number_2 != 'N' or number_2 != 'n':
                    return 'Вы вышли'
                else:
                    return 'Вы вышли'


conclusion = Error(1)
print(conclusion.my_list())


# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс
# «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники
# (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class Warehouse:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price


class Printer(Warehouse):
    def __init__(self, name, quantity, price):
        super().__init__(name, quantity, price)
        self.paper = 30

    def papers(self):
        return f'Название товара-{self.name} количество-{self.quantity} цена-{self.price} ' \
               f'Количество бумаги-{self.paper} листов'


class Scanner(Warehouse):
    def __init__(self, name, quantity, price):
        super().__init__(name, quantity, price)
        self.ink = 70

    def ink_1(self):
        return f'Название товара-{self.name}, количество-{self.quantity} цена-{self.price} ' \
               f'Количество чернил-{self.ink} %'


class Xerox(Warehouse):

    def __init__(self, name, quantity, price):
        super().__init__(name, quantity, price)
        self.paper = 25

    def papers(self):
        print(f'Название товара-{self.name} количество-{self.quantity} цена-{self.price} '
              f' Количество листов-{self.paper}')




xerox = Xerox('Philips', 23, 2000)
printer = Printer('Hp', 20, 2000)
scanner = Scanner('Sony', 24, 1900)
xerox.papers()
print(printer.papers())
print(scanner.ink_1())
