"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
fName = 'user_input.txt'
"""
1. Создать программно файл в текстовом формате, записать в него построчно данные,
    вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""

with open(fName, 'a') as fl:
    while True:
        ui = input('Введите строку файла (для окончания ввода - нажмите Enter): ')
        if ui.lstrip().rstrip() != '':
            fl.write(ui+'\n')
        else:
            break

"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
    выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open(fName, 'r') as fl:
    for i, el in enumerate(fl.readlines()):
        print(f"line: {i}, words: {len(el.split())}")

"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
    Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. В
    ыполнить подсчет средней величины дохода сотрудников.
"""

def read_file(file_name, data):
    import os.path
    if os.path.exists(file_name):
        with open(file_name) as fl:
            data.extend(el.split() for el in fl.readlines())

def write_file(file_name, data):
    with open(file_name, 'w') as fl:
        for el in data:
            fl.write(f'{el[0]} {el[1]}\n')

fName = 'employee_data.txt'
emp_data = []
read_file(fName, emp_data)
while True:
    usr_input = input("Введите через пробел фамилию и оклад сотрудника (stop - для окончания): ").lower().lstrip().rstrip()
    if usr_input != 'stop':
        emp_data.append(usr_input.split())
    else:
        break
write_file(fName, emp_data)
print(f"Salary < 20000: {' '.join([el[0] for el in filter(lambda item: float(item[1]) < 20000, emp_data)]).rstrip().lstrip()}")
print(f"AVG salary: {sum([float(el[1]) for el in emp_data])/len(emp_data)}")

"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

def read_file(file_name, data):
    import os.path
    if os.path.exists(file_name):
        with open(file_name) as fl:
            data.extend(el.split() for el in fl.readlines())

def write_file(file_name, data):
    with open(file_name, 'w') as fl:
        for el in data:
            fl.write(f'{el[0]} {el[1]} {el[2]}\n')
            
def eng_to_rus_numerals(item):
    item[0] = rus_numerals[item[2]]
    return item

fName = 'eng_numerals.txt'
eng_numerals = []
rus_numerals = {'0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'}
# read data
read_file(fName, eng_numerals)
#print(*eng_numerals)
#print(*map(eng_to_rus_numerals, eng_numerals))
fName = 'rus_numerals.txt'
write_file(fName, map(eng_to_rus_numerals, eng_numerals))

"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

class NumericIterator:
    def __iter__(self):
        return self

    def __init__(self, start, step, limit):
        self.limit = limit
        self.step = step
        self.counter = 0
        self.prev = start - step
        self.start = start

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            self.prev = self.start
            self.start += self.step
            return self.start
        else:
            raise StopIteration

    def current(self):
        return self.start

    def prev(self):
        return self.prev

    def counter(self):
        return self.counter

    def limit(self):
        return self.limit

#print(functools.reduce(sum, numeric))
def read_file(file_name, data):
    import os.path
    if os.path.exists(file_name):
        with open(file_name) as fl:
            for el in fl.readlines():
                for ff in el.split():
                    data.append(float(ff))

def write_file(file_name, data):
    with open(file_name, 'w') as fl:
        fl.write(' '.join(data))

in_data = []
out_data = []

numeric = NumericIterator(456.1, 1.58, 59)
for flt in numeric:
    out_data.append(round(flt, 4))
print(out_data)
write_file('ex_5.txt', map(str, out_data))
print(f"SUM (from list): {round(sum(out_data), 4)}")

read_file('ex_5.txt', in_data)
print(in_data)
print(f"SUM (from file): {round(sum(in_data), 4)}")

"""
6. Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
fName = 'subjects.txt'

in_subjects = {}
out_subjects = {}

def read_file(file_name, data):
    import os.path
    if os.path.exists(file_name):
        with open(file_name) as fl:
            for el in fl.readlines():
                #print(el)
                key = ''
                data = el.split(':')
                key = data[0].capitalize()

                lectures = 0
                practice = 0
                laboratorn = 0
                for ff in data[1].split():

                    if ff.lower().count('(л)') > 0:
                        lectures = int(ff.lower().replace('(л)', ''))
                    elif ff.lower().count('(пр)') > 0:
                        practice = int(ff.lower().replace('(пр)', ''))
                    elif ff.lower().count('(лаб)') > 0:
                        laboratorn = int(ff.lower().replace('(лаб)', ''))
                #print(key, ' ', lectures, ' ', practice, ' ', laboratorn)
                in_subjects[key.capitalize()] = {'lectures': lectures, 'practice': practice, 'laboratorn': laboratorn, 'all': lectures + practice + laboratorn}

def write_file(file_name, data):
    with open(file_name, 'w') as fl:
        fl.write(' '.join(data))
read_file(fName, in_subjects)
print('Входные данные: ', in_subjects)
print('Выходные данные: ', {el: in_subjects[el]['all'] for el in in_subjects.keys()})
