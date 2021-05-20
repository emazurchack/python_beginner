"""
1. Поработайте с переменными, создайте несколько, выведите на экран,
   запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
"""

firstVar = None
secondVar = None
print(firstVar)
print(secondVar)

firstVar = input('Input first Var')
secondVar = input('Input second Var')

firstVar = float(firstVar) if firstVar.isnumeric() else firstVar
print(firstVar.isnumeric())
print(firstVar.isdigit())
print(firstVar.isalnum())
print(firstVar.isdecimal())

secondVar = float(secondVar) if secondVar.isnumeric() else secondVar

print(f"Var [firstVar] value [{firstVar}], type [{type(firstVar)}]")
print(f"Var [secondVar] value [{secondVar}], type [{type(secondVar)}]")

"""
2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды 
   и выведите в формате чч:мм:сс. Используйте форматирование строк.
"""
def time_from_sec(seconds):
    minutes = seconds // 60
    hours = minutes // 60
    minutes = minutes % 60
    seconds = seconds % 60
    return [hours, minutes, seconds]

sec = input('Enter time in seconds: ')
if not sec.isdigit():
    raise ValueError
hours, minutes, seconds = time_from_sec(int(sec))

print("%02d:%02d:%02d"%(hours, minutes, seconds))
print("%02d:%02d" % (minutes, seconds))

"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369. 
"""

num = input('Enter an integer: ')
if not num.isdigit():
    raise ValueError
print(f"result is: {int(num) + int(num*2) + int(num*3)}")

"""
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. 
   Для решения используйте цикл while и арифметические операции.
"""
num = input('Введите целое положительное число: ')
if not num.isdigit():
    raise ValueError
lnum = list(num)
nMax = 0
for n in lnum:
    nMax = int(n) if int(n) > nMax else nMax
print(f"Max: {nMax} digit in {num}")
"""
5. Запросите у пользователя значения выручки и издержек фирмы. 
   Определите, с каким финансовым результатом работает фирма 
   (прибыль — выручка больше издержек, или убыток — издержки больше выручки). 
   Выведите соответствующее сообщение. 
   Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). 
   Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""

#выручка
proceeds = 0.0
#издержки
costs = 0.0
#численность сотрудников
count_of_employees = 0

proceeds = input('Введите выручку (nnnnnn.nn): ')
if not proceeds.replace('.', '').replace(',', '').isdigit():
    raise ValueError
proceeds = float(proceeds.replace(',', '.'))
proceeds = round(proceeds, 2)
print(f'Выручка: {proceeds}')

costs = input('Введите издержки (nnnnnn.nn): ')
if not costs.replace('.', '').replace(',', '').isdigit():
    raise ValueError
costs = float(costs.replace(',', '.'))
costs = round(costs, 2)
print(f'Издержки: {costs}')

print(f"Фирма сработала с {('УБЫТКОМ', 'ПРИБЫЛЬЮ')[proceeds>costs]} в {round((proceeds-costs), 2)}")
#Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
if proceeds>costs:
    rentability = (proceeds-costs)/proceeds
    print(f"Рентабельность: {round(rentability, 2)}")
#Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
    count_of_employees = input('Введите численность сотрудников (nnnnnn): ')
    if not count_of_employees.isdigit():
        raise ValueError
    count_of_employees = int(count_of_employees)
    print(f"Численность сотрудников : {count_of_employees}")
    print(f"Прибыль фирмы в расчете на одного сотрудника: {round(((proceeds-costs)/count_of_employees), 2)}")

"""
6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил [a] километров. 
   Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. 
   Требуется определить номер дня, на который общий результат спортсмена составить не менее [b] километров. 
   Программа должна принимать значения параметров [a] и [b] и выводить одно натуральное число — номер дня.
"""

day_optimal_result=1
start_result = input('Введите результат пробежки 1го дня (км) [целое число]: ')
if not start_result.isdigit():
    raise ValueError
start_result = int(start_result)
optimal_result = input('Введите количество (км) для оптимального результата [целое число]: ')
if not optimal_result.isdigit():
    raise ValueError
optimal_result = int(optimal_result)
if optimal_result <= start_result:
    print('ЧАВО???')
else:
    day_result = start_result
    print(f"{day_optimal_result}(й) день.    Результат: {round(day_result, 2)}(км)")
    while day_result < optimal_result:
        day_optimal_result += 1
        day_result += (day_result*0.1)
        print(f"{day_optimal_result}(й) день.    Результат: {round(day_result, 2)}(км)")
    print(f"оптимальный результат будет достигнут на {day_optimal_result} день.")
