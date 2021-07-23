import numpy as np
"""
1. Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого кредитного скоринга (ks): 
    zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110], 
    ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]. 
    Используя математические операции, посчитать коэффициенты линейной регрессии, 
    приняв за X заработную плату (то есть, zp - признак), 
    а за y - значения скорингового балла (то есть, ks - целевая переменная). 
    Произвести расчет как с использованием intercept, так и без.
    
2. В каких случаях для вычисления доверительных интервалов и проверки статистических гипотез 
    используется таблица значений функции Лапласа, а в каких - таблица критических точек распределения Стьюдента?
"""
