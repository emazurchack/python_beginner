"""
Віполнение задания к уроку 2
"""
"""
1. Создать список и заполнить его элементами различных типов данных. 
   Реализовать скрипт проверки типа данных каждого элемента. 
   Использовать функцию type() для проверки типа. 
   Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""

test_list = [1, "23", 3.54, ("ff", 45), [1, 2, 3]]
for item in test_list:
  print(type(item))

"""
2. Для списка реализовать обмен значений соседних элементов, т.е.
   Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
   При нечетном количестве элементов последний сохранить на своем месте.
   Для заполнения списка элементов необходимо использовать функцию input().
"""

src_list = []
def init_list():
    out_list = []
    element = ''
    while element.lower() != "stop":
        element = input("Введите элемент списка: ")
        if element.lower() != 'stop':
            out_list.append(element)
    return out_list
def swap_elements(lst):
    j = 0
    for i in range(int(len(lst) / 2)):
        lst[j], lst[j + 1] = lst[j + 1], lst[j]
        j += 2

src_list = init_list()
print(f"Список (исходный): {src_list}")
swap_elements(src_list)
print(f"Список (после перестановки): {src_list}")

"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
   Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
   Напишите решения через list и через dict.
"""

month_list = [",1,2,12,", ",3,4,5,", ",6,7,8,", ",9,10,11,"]
seasons_list = ["зима", "весна", "лето", "осень"]
mont_seasons_dict = {",1,2,12,": "зима", ",3,4,5,": "весна", ",6,7,8,": "лето", ",9,10,11,": "осень"}
def find_seasons_from_month_l(month):
    for idx, val in enumerate(month_list):
        if (","+month+",") in val:
            return seasons_list[idx]
    return None
def find_seasons_from_month_d(month):
    for idx in mont_seasons_dict.keys():
        if ("," + month + ",") in idx:
            return mont_seasons_dict[idx]
    return None
print("Результат поиска по списку: ", find_seasons_from_month_l('5'))
print("Результат поиска по : ", find_seasons_from_month_d('5'))

"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
   Вывести каждое слово с новой строки.
   Строки необходимо пронумеровать.
   Если в слово длинное, выводить только первые 10 букв в слове.
"""

[print(f"№{idx}, значение: {el[:10]}" ) for idx, el in enumerate(list(input("Введите строку: ").split()))]

"""
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
   У пользователя необходимо запрашивать новый элемент рейтинга.
   Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""
init_raiting_list = [6, 4, 8, 2, 2, 1]
init_raiting_list.sort(reverse=True)
def findElement(raiting_element):
    for idx, element in enumerate(init_raiting_list):
        if raiting_element >= element:
            return idx
    return 0
el = ''
while el.lower() != 'stop':
    el = input("Введите значение рейтинга: ")
    if el != 'stop' and el.isdigit():
        init_raiting_list.insert(findElement(int(el)), int(el))
        print(init_raiting_list)
