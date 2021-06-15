"""
Урок 8. ООП. Полезные дополнения
"""
print("Задание 1")
"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». 
    В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и 
    преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, 
    месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""
class Date(object):
    def __init__(self, day=0, month=0, year=0):
        self._day = day
        self._month = month
        self._year = year
    def __str__(self):
        return str(self._day).rjust(2,'0') + ' ' + str(self._month).rjust(2,'0') + ' ' + str(self._year)
    @classmethod
    def from_string(cls, date_as_string, separator=' '):
        day, month, year = map(int, date_as_string.split(separator))
        return cls(day, month, year)
    @staticmethod
    def is_date_valid(date_as_string, separator=' '):
        day, month, year = map(int, date_as_string.split(separator))
        return day <= 31 and month <= 12 and year <= 2999

d1 = Date.from_string('11-09-2012', '-')
print(d1)
d2 = Date.from_string('12 12 2013')
print(d2)
print("{} '{}' result is: {}".format('Validate', '11-07-2012', Date.is_date_valid('11-07-2012', '-')))
print("{} '{}' result is: {}".format('Validate', '11 07 2012', Date.is_date_valid('11 07 2012')))
print("{} '{}' result is: {}".format('Validate', '11-13-2012', Date.is_date_valid('11-13-2012', '-')))

print("Задание 2")
"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. 
    Проверьте его работу на данных, вводимых пользователем. 
    При вводе пользователем нуля в качестве делителя программа должна корректно 
    обработать эту ситуацию и не завершиться с ошибкой.
"""

class ZeroByDevision(Exception):
    def __init__(self):
        self.message = 'ОШИБКА. Деление на ноль.'

a, b = map(float, input("Введите делимое и делитель через пробел: ").split())
try:
    if b == 0:
        raise ZeroByDevision
    res = a/b
except ZeroByDevision as err:
    print(err.message)
else:
    print("Деление {} на {}, результат: {}".format(a, b, res))

print("Задание 3")
"""
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. 
    Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список. 
    Класс-исключение должен контролировать типы данных элементов списка.
    Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, 
    пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”. 
    При этом скрипт завершается, сформированный список выводится на экран.
    Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. 
    При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, 
    только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) 
    и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.
"""

class InputNumberValueError(ValueError):
    pass

input_data = []
break_flag = False
while True:
    in_values = input('Введите числа через пробел: ').lower().replace(',', '.').split()
    if 'stop' in in_values:
        for val in in_values:
            try:
                if val != 'stop':
                    try:
                        if val.replace(',', '').replace('.', '').isdigit():
                            input_data.append(float(val))
                        else:
                            raise InputNumberValueError
                    except:
                        raise InputNumberValueError
                else:
                    break_flag = True

            except Exception as ex:
                print(ex.message)
    else:
        for val in  map(float, in_values):
            input_data.append(val)
    if break_flag:
        break

print("Результат: ", input_data)

print("Задание 7")
"""
7. Реализовать проект «Операции с комплексными числами».
    Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел. 
    Проверьте работу проекта, создав экземпляры класса (комплексные числа) 
    и выполнив сложение и умножение созданных экземпляров. 
    Проверьте корректность полученного результата.
"""
class Complex(object):
    def __init__(self, re, im):
        self.re = re
        self.im = im
    def __str__(self):
        return '%s + %si' % (self.re, self.im)
    def __add__(self, other):
        return Complex(self.re + other.re, self.im + other.im)
    def __sub__(self, other):
        return Complex(self.re - other.re, self.im-other.im)
    def __mul__(self, other):
        return Complex((self.re * other.re - self.im * other.im), (self.re * other.im + self.im * other.re))

a = Complex(1, 3)
b = Complex(4, 8)
print("Result [+]: ", a+b)
print("Result [-]: ", a-b)
print("Result [*]: ", a*b)
print("Задание 4,5,6")
"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. 
    А также класс «Оргтехника», который будет базовым для классов-наследников. 
    Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
    В базовом классе определить параметры, общие для приведенных типов. 
    В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. 
    Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании. 
    Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, 
    можно использовать любую подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. 
    Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
    
    Подсказка: постарайтесь по возможности реализовать в проекте 
    «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""
#import uuid
appointment = ['Для дома',  'Для оффиса', 'Промышленный']
supported_resolutions = ['300x300', '600x600', '720x720', '1200x600', '1200x1200']
supported_interfaces = ['WiFi', 'USB 1.0', 'USB 2.0', 'USB 3.0', 'USM Type-C', 'USB-mini', 'LAN', 'DVI', 'HDMI', 'RS-232', 'Bluetooth']
supported_print_format = ['A0', 'A1', 'A2', 'A3', 'A4', 'A5']

# Office equipment - Оргтехника
class OfficeEquipment(object):
    def __init__(self):
        self.Brand = None
        #модель наименование
        self.model_name = None
        #номер модели
        self.model_code = None
        #брєнд
        self.brand = None
        #назначение
        self.appointment = None
        #поддерживаемые интерфейсы
        self.supported_interfaces = None

class Printers_MFU(OfficeEquipment):
    def __init__(self):
        super().__init__()
        #
        self.supported_print_format = None
        #поддерживаемые разрешения
        self.supported_resolutions = None


#
# товар
class Product(object):
    pass

"""
Марина - извените, но банально нет времени на достойное выполнение пунктов 4, 5, 6.
Абы как - делать не хочу.
"""

