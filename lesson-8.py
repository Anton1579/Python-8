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

# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад
# и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц
# оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.

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
print(xerox.__dict__)
print(printer.__dict__)
print(scanner.__dict__)


# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем
# данных. Например, для указания количества принтеров, отправленных на склад, нельзя использовать
# строковый тип данных.

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



name = input('Название товара Xerox: ')
quantity = int(input('количество: '))
price = int(input('цена: '))
xerox = Xerox(name, quantity, price)
name = input('Название товара Printer: ')
quantity = int(input('количество: '))
price = int(input('цена: '))
printer = Printer(name, quantity, price)
name = input('Название товара Scanner: ')
quantity = int(input('количество: '))
price = int(input('цена: '))
scanner = Scanner(name, quantity, price)
xerox.papers()
print(printer.papers())
print(scanner.ink_1())
print(xerox.__dict__)
print(printer.__dict__)
print(scanner.__dict__)

# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.


class ComplexNumber:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        self.suma_x = self.x + other.x
        self.suma_y = self.y + other.y

    def __mul__(self, other):
        self.mult_x = self.x * other.x - self.y * other.y
        self.mult_y = self.y * other.x + self.x * other.y


x = float(input('x = : '))
y = float(input('y = : '))
a = ComplexNumber(x, y)
x = float(input('x = : '))
y = float(input('y = : '))
b = ComplexNumber(x, y)
a + b
a * b
print('Сумма:   %.2f + %.2f' % (a.suma_x, a.suma_y))
print('Произв.: %.2f + %.2f' % (a.mult_x, a.mult_y))