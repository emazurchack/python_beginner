"""
Урок 4. Полезные инструменты


7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
    При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
    Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""
import random
import functools
import itertools
"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
    В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
    Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
print("Задание 1")
import L04_EX_1

print(L04_EX_1.get_employee_payroll(9, 45.67, 123))
"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""
print("Задание 2")
in_list_count = 40
in_list = list(random.randint(1, 20) for _ in range(in_list_count))
print("Исходный список: ", in_list)
print("Элементы исходного списка, значения которых больше предыдущего элемента: ", [in_list[i] for i in range(len(in_list)) if i > 0 and in_list[i] > in_list[i-1]])
"""
3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.
"""
print("Задание 3")
print("Результат (кратные 20 или 21, для чисел в пределах от 20 до 240): ", list(i for i in range(241) if (i >= 20) and ((i % 20 == 0) or (i % 21 == 0))))
#from itertools import count
#iterator = (count(start=20, step=1))
#print( list(i for i in (next(iterator) for _ in range(221)) if ((i % 20 == 0) or (i % 21 == 0))))

"""
4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
    Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести в порядке их следования в исходном списке.
    Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""
print("Задание 4")
in_list_count = 40
in_list = list(random.randint(1, 20) for _ in range(in_list_count))
print("Исходный список: ", in_list)
print("Список уникальных элементов: ", [i for i in in_list if in_list.count(i) == 1])

print("Задание 5")
"""
5. Реализовать формирование списка, используя функцию range() и возможности генератора.
    В список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
print("Результат: ", functools.reduce(lambda a, b: a * b, [i for i in range(1001) if i >= 100 and i % 2 == 0]))
"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание,
    что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
    Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""
print("Задание 6")
print("а) итератор, генерирующий целые числа, начиная с указанного")
class WholeNmberIterator(object):

    def __init__(self, start = 1, step = 1, limit = 1000):
        self.counter = 0
        self.limit = limit
        if step % 1:
            raise ValueError("Шаг должен быть целым числом.")
        if start % 1:
            raise ValueError("Стартовый элемент должен быть целым числом.")
        self.step = step
        self.start = start
        self.current = self.start
        self.Counter = itertools.count(self.start, self.step)

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            self.current = self.Counter.__next__()
            return self.current
        else:
            raise StopIteration

    def current(self):
        return self.current

    def prev(self):
        return (self.current, self.current - self.step)[self.current > self.start]

    def counter(self):
        return self.counter

    def limit(self):
        return self.limit
# test WholeNmberIterator
wni = WholeNmberIterator(6, 1, 100)
print(wni)
print([list(i for i in wni)])

print("б) итератор, повторяющий элементы некоторого списка, определенного заранее")
class ListCycleIterator(object):

    def __init__(self, limit = 10, lst = []):
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

# test ListCycleIterator
lci = ListCycleIterator(10, [66, 77, 88, 99])
print(lci)
print([list(i for i in lci)])
