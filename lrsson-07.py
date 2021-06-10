"""
Урок 7. ООП. Продвинутый уровень
"""
from abc import ABC, abstractmethod

print("Задание 2")
"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды. 
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название. 
К типам одежды в этом проекте относятся пальто и костюм. 
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). 
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). 
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. 
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, 
проверить на практике работу декоратора @property.
"""
class Сlothes(ABC):
    def __init__(self, type_name, collection, model_name):
        self._type_name = type_name
        self._collection = collection
        self._model_name = model_name
    @property
    def type_name(self):
        return self._type_name
    @type_name.setter
    def length(self, value):
        self._type_name = value
    @property
    def collection(self):
        return self._collection
    @collection.setter
    def collection(self, value):
        self._collection = value
    @property
    def model_name(self):
        return self._model_name
    @model_name.setter
    def model_name(self, value):
        self._model_name = value

    @abstractmethod
    def get_tissue_consumption(self):
        pass
#пальто - coat
class Coat(Сlothes):
    def __init__(self, collection, model_name, size):
        super().__init__("Coat", collection, model_name)
        self._size = size
    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, value):
        self._size = value

    def get_tissue_consumption(self):
        return (self.size/6.5 + 0.5)

    @property
    def tissue_consumption(self):
        return self.get_tissue_consumption()

#костюм - costume
class Costume(Сlothes):
    def __init__(self, collection, model_name, height):
        super().__init__("Costume", collection, model_name)
        self._height = height
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        self._height = value

    def get_tissue_consumption(self):
        return (2 * self.height + 0.3)

    @property
    def tissue_consumption(self):
        return self.get_tissue_consumption()


ct = Coat("2021", "Синий бриз", 5)
print(ct.tissue_consumption)
cm = Costume("2021", "Синий бриз", 8)
print(cm.tissue_consumption)

print("Задание 3")
"""
3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. 
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число). 
В классе должны быть реализованы методы перегрузки арифметических операторов: 
сложение (__add__()), 
вычитание (__sub__()), 
умножение (__mul__()), 
деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, 
умножение и обычное (не целочисленное) деление клеток, соответственно. 
В методе деления должно осуществляться округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, 
    иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. 
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу. 
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.

Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.
"""
class Cell(object):
    def __init__(self, size):
        if size % 1 > 0:
            #print(size % 1)
            raise NotImplementedError("Размер клетки должен представляться целым числом.")
        self.size = size
    def __repr__(self):
        return "<Cell> Размер клетки: {}".format(self.size)
    # +
    def __add__(self, other):
        return Cell(self.size + other.size)
    # -
    def __sub__(self, other):
        if (other.size + 1) <= self.size:
            return Cell(self.size - other.size)
        else:
            raise ValueError("Не возможно выполнить операцию. Результат операции не корректен. Размер клетки не может быть меньше, либо равен нулю.")
    # *
    def __mul__(self, other):
        if other.size > 0:
            return Cell(self.size * other.size)
        else:
            raise ValueError("Результирующая клетка не может быть нулевой.")
    # /
    def __truediv__(self, other):
        if self.size // other.size > 0:
            return Cell(self.size // other.size)
        else:
            raise ZeroDivisionError("Результирующая клетка не может быть нулевой.")
    #
    def make_order(self, row_cell):
        if row_cell % 1 > 0:
            #print(size % 1)
            raise NotImplementedError("Параметр [row_cell] должен представляться целым числом.")
        whole_part = self.size // row_cell
        fractional_part = self.size % row_cell
        base_lst = []
        for i in range(1, whole_part+1):
            base_lst.append('*'*row_cell)
        base_lst.append('*' * fractional_part)
        print("Результат по {} клет(ки/ок) в ряду: \n{}".format(row_cell, '\n'.join(base_lst)))

c1 = Cell(8)
c2 = Cell(3)
print(c1)
print(c2)
#

print("Сумма: (c1+c2) ", c1+c2)
print("Разность: (c1-c2) ", c1-c2)
#print("Разность: (c2-c1)", c2-c1)
print("Деление: (c1/c2) ", c1/c2)
#print("Деление: (c2/c1) ", c2/c1)

c2.make_order(2)
c2.make_order(4)
(c1+c2).make_order(5)

"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), 
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). 
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем 
с первым элементом первой строки второй матрицы и т.д.

"""
print("Задание 1")
from copy import deepcopy

class Matrix:
    def __init__(self, matrix):
        self.matrix = list()
        self.matrix = deepcopy(matrix)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, lst)) for lst in self.matrix])

    def size(self):
        return len(self.matrix), len(self.matrix[0])

    def __add__(self, other):
        if isinstance(other, Matrix):
            row = []
            if self.size() != other.size():
                raise ArithmeticError("Размерности объектов не совпадают.")
            for i in range(len(self.matrix)):
                col = []
                for j in range(len(self.matrix[0])):
                    col.append(self.matrix[i][j] + other.matrix[i][j])
                row.append(col)
            return Matrix(row)
        else:
            return None


m1 = Matrix([[1,2,3], [4,5,6], [7,8,9]])
print(m1.size())
print(m1)
m2 = Matrix([[1,1,1], [1,1,1], [1,1,1]])
print(m2.size())
print(m2)
m3 = m1 + m2
print("result: ")
print(m3)
