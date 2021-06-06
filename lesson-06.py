"""
Урок 6. Объектно-ориентированное программирование
"""
import itertools
import time
import datetime

print("Задание 1")
"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). 
    Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый. 
    Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. 
    Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). 
    Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
class ListCycleIterator(object):

    def __init__(self, lst, limit = 10):
        self.counter = 0
        self.limit = limit
        if len(lst) == 0:
            raise ValueError("Задайте список элементов для повторения.")
        self.Cycler = itertools.cycle(lst)

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.Cycler.__next__()
        else:
            raise StopIteration

    def counter(self):
        return self.counter

    def limit(self):
        return self.limit

TRAFIC_LIGHT_RED = 0
TRAFIC_LIGHT_YELLOW = 1
TRAFIC_LIGHT_GREEN = 2
TrafficLightColorsOrder = (TRAFIC_LIGHT_RED, TRAFIC_LIGHT_YELLOW, TRAFIC_LIGHT_GREEN)
TrafficLightState = {TRAFIC_LIGHT_RED: "Red", TRAFIC_LIGHT_YELLOW: "Yellow", TRAFIC_LIGHT_GREEN: "Green"}
#
traffic_light_rule = {TRAFIC_LIGHT_RED: 7, TRAFIC_LIGHT_YELLOW: 2, TRAFIC_LIGHT_GREEN: 15}
print("TrafficLightRule: ", traffic_light_rule)

class TrafficLight(object):
    def __init__(self, traffic_light_rule, printing_state = True, repeat_cycle = 10):
        super().__init__()
        self.repeat_cycle = repeat_cycle
        self.current_cycle = 0
        self.stop = False
        self.printing_state = printing_state
        self.color = TRAFIC_LIGHT_RED
        self.traffic_light_rule = traffic_light_rule
        self.cycler = None

    def CurrentState(self):
        return "{}, current light: {}, time lighting {} sec".format(time.ctime(), TrafficLightState[self.color], self.traffic_light_rule[self.color])

    def printCurrentState(self):
        if self.printing_state:
            print(self.CurrentState())

    def Start(self):
        self.stop = False
        self.current_cycle = 1
        self.cycler = itertools.cycle(TrafficLightColorsOrder)
        for color in self.cycler:
            if not self.stop or (self.current_cycle <= self.repeat_cycle):
                self.color = color

                self.printCurrentState();
                time.sleep(self.traffic_light_rule[self.color])
                self.current_cycle += 1
            else:
                break

    def Stop(self):
        self.stop = True
        self.current_cycle = self.repeat_cycle

# test TrafficLight
"""
tl = TrafficLight(traffic_light_rule)
tl.Start()
"""
print("Задание 1")
"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
    Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
    Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
    Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число см толщины полотна.
    Проверить работу метода.
Например: 20м * 5000м * 25кг * 0.05м = 125т

class XXX:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x
"""
class Road(object):
    def __init__(self, length, width):
        self._length = length
        self._width = width
    @property
    def length(self):
        return self._length
    @length.setter
    def length(self, value):
        self._length = value
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        self._width = value
    # расчет массы асфальта: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число см толщины полотна
    def calc_mass_of_asphalt(self, ma_on_one_metter_by_one_cm, number_cm_blade_thickness):
        return self._length * self._width * ma_on_one_metter_by_one_cm * number_cm_blade_thickness
#test
rd = Road(1000, 12)
print(f"{rd.calc_mass_of_asphalt(32, 10)}")

"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
    Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
    оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
    В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
    Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""
print("Задание 3")
class Worker(object):
    def __init__(self, name, surname, day_birthday, month_birthday, year_birthday):
        self._name = name
        self._surname = surname
        self._day_birthday = day_birthday
        self._month_birthday = month_birthday
        self._year_birthday = year_birthday
        try:
            db = datetime.date(self._year_birthday, self._month_birthday, self._day_birthday)
        except:
            raise ValueError("Укажите число, месяц и год рождения.")
    @property
    def birthday_day(self):
        return self._day_birthday
    @birthday_day.setter
    def birthday_day(self, value):
        self._day_birthday = value

    @property
    def birthday_month(self):
        return self._month_birthday
    @birthday_month.setter
    def birthday_month(self, value):
        self._month_birthday = value

    @property
    def birthday_year(self):
        return self._year_birthday
    @birthday_year.setter
    def birthday_year(self, value):
        self._year_birthday = value

    def get_age(self):
        today = datetime.date.today()
        return today.year - self._year_birthday - ((today.month, today.day) < (self._month_birthday, self._day_birthday))
    def get_full_name(self):
        return "{} {}".format(self._name, self._surname)

class Position(Worker):
    def __init__(self, name, surname, day_birthday, month_birthday, year_birthday, position, wage, bonus):
        super().__init__(name, surname, day_birthday, month_birthday, year_birthday)
        self._position = position
        self._income = {"wage": wage, "bonus": bonus}
    @property
    def position(self):
        return self._position
    @position.setter
    def position(self, value):
        self._position = value

    @property
    def wage(self):
        return self._income["wage"]
    @wage.setter
    def position(self, value):
        self._income["wage"] = value

    @property
    def bonus(self):
        return self._income["bonus"]
    @bonus.setter
    def bonus(self, value):
        self._income["bonus"] = value

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

pos = Position("Евгений", "Мазурчак", 2, 2, 1976, "Водитель", 5600.45, 1034)
print(pos.get_full_name())
print(pos.get_age())
print(pos.get_total_income())

print("Задание 4")
"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
    А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
    Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
    Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
    Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
    должно выводиться сообщение о превышении скорости.
    Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
    Выполните вызов методов и также покажите результат.
"""
DIRECTION_LEFT = 0
DIRECTION_RIGHT = 1
DIRECTION_INFO = {DIRECTION_LEFT: 'lrft', DIRECTION_RIGHT: 'right'}

class Car(object):
    def __init__(self, speed, color, name, is_police):
        self.name = name
        self.color = color
        self.is_police = is_police
        self.speed = speed
    def show_speed(self):
        print("car [{}] speed is: {}".format(self.name, self.speed))
    def go(self):
        print("{} is go".format(self.name))
    def stop(self):
        print("{} is stoped".format(self.name))
    def turn(self, direction):
        if direction not in (DIRECTION_LEFT, DIRECTION_RIGHT):
            raise ValueError("Error direction value.")
        print("{} is turn to the {}".format(self.name, DIRECTION_INFO[direction]))

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("car [{}] WARNING: {}".format(self.name, 'the permissible speed is exceeded'))
        else:
            super().show_speed()
class SportCar(Car):
    pass
class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("car [{}] WARNING: {}".format(self.name, 'the permissible speed is exceeded'))
        else:
            super().show_speed()
class PoliceCar(Car):
    pass

tc = TownCar(78, 'red', 'Mazda CX2', False)
tc.show_speed()

sc = SportCar(110, 'blue', 'AUDI Coupe', False)
sc.show_speed()

wc = WorkCar(45, 'blue', 'MAN 2367', False)
wc.show_speed()

print("Задание 5")
"""
5. Реализовать класс Stationery (канцелярская принадлежность).
    Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
    Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
    В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
    Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""
STATIONERY_PEN    = 0
STATIONERY_PENCIL = 1
STATIONERY_HANDLE = 2
STATIONERY_TYPE = {STATIONERY_PEN: "PEN", STATIONERY_PENCIL: "PENCIL", STATIONERY_HANDLE: "HANDLE"}

class Stationery(object):
    def __init__(self, title):
        self.stationery_type = None
        self.title = title
    def draw(self):
        print("{} start draw {} type stationery".format(self.title, STATIONERY_TYPE[self.stationery_type]))

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
        self.stationery_type = STATIONERY_PEN
class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
        self.stationery_type = STATIONERY_PENCIL
class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
        self.stationery_type = STATIONERY_HANDLE
pen = Pen("BIG")
pen.draw()

handle = Handle("CentroPen")
handle.draw()