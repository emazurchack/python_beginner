"""
Урок 3. Функции
"""
"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
   Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""
def myDiv(x, y):
    if y == 0:
        raise ZeroDivisionError
    return x/y
print(myDiv(0, 3))
print(myDiv(5, 3))
print(myDiv(1, 3))
print(myDiv(1, 0))
"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
   имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
   Реализовать вывод данных о пользователе одной строкой.
"""
def getAccData(surName, name, patronymic, yearOfBirth = 1900, currentCity = '< не указан >', email = '< не указан >', pnone='< не указан >'):
    if surName.isdigit() or name.isdigit() or patronymic.isdigit() or currentCity.isdigit() or email.isdigit():
        raise ValueError
    if yearOfBirth == 1900:
        raise ValueError(f"Не задан параметр <Год рождения (yearOfBirth)>")
    return f"Фамилия: {surName.capitalize()}, Имя: {name.capitalize()}, Отчество: {patronymic.capitalize()}, Год рождения: {yearOfBirth}, Город проживания: {currentCity.capitalize()}, e-mail: {email}, телефон: {pnone}"
print(getAccData(surName='мазурчак', name='евгений', patronymic='владимирович', yearOfBirth=1976, email='mr.emazurchack@gmail.com'))
"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
   и возвращает сумму наибольших двух аргументов.
"""
def my_func(x=0, y=0, z=0):
    out_lst = [x, y, z]
    out_lst.sort(reverse=True)
    print(out_lst)
    return out_lst[0] + out_lst[1]
print(my_func(x=5, y=8, z=9))
"""
4. Программа принимает действительное положительное число x и целое отрицательное число y.
   Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
   При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
   Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
   Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""
def myPow(x=0,y=0):
    if x == 0:
        raise ValueError(f"Введите число: {x}")
    if y == 0:
        return 1
    if y == 1:
        return x
    if y == -1:
        return (1/x)

    if y > 0:
        return x**y
    else:
        z = (x**abs(y))
        z = 1/z
        return z
def myPow2(x=0,y=0):
    if x == 0:
        raise ValueError(f"Введите число: {x}")
    if y == 0:
        return 1
    if y == 1:
        return x
    if y == -1:
        return (1/x)
    z = 1
    for i in range(1, abs(y)+1, 1):
        #print(i)
        #print(f" {i} : {x}")
        z *= x
    if y > 0:
        return z
    else:
        z = 1/z
        return z

print(f"myPow(2, 3): {myPow(2, 3)}")
print(f"myPow2(2, 3): {myPow2(2, 3)}")
print(f"myPow(2, 0): {myPow(2, 0)}")
print(f"myPow2(2, 0): {myPow2(2, 0)}")
print(f"myPow(2, -3): {myPow(2, -3)}")
print(f"myPow2(2, -3): {myPow2(2, -3)}")
"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
   При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных
   пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
   Но если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный
   символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее
   сумме и после этого завершить программу.
"""
def myInput(stop = '@'):
    return input(f"Введите строку целых чисел через пробел (для окончания {stop}): ").split()

def interactiveSum(stop = '@'):
    res = 0
    stop_sum = False
    while True:
        num_lst = myInput(stop=stop)
        for elem in num_lst:
            stop_sum = elem.lower() == stop.lower()
            if stop_sum:
                break
            res += int(elem)
        if stop_sum:
            break
    return res

print(f"Result of interactibe SUM is: {interactiveSum()}")

"""
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
   но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое
слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
"""
def myTitle(iStr = ''):
    return iStr.capitalize()


def capitalize(iLst = input("Введите строку: ").split()):
    out_str = ''
    for element in iLst:
        out_str += myTitle(element) + ' '
    return out_str.lstrip().rstrip()

print(capitalize())
