#coding=UTF8
from math import fsum,fabs,pow,sqrt
__author__ = 'chexov'

def calculate_x_y(x,y):
    """
    Часть параметров для расчета
    correlation_coefficient(n,x,y)  -> int,int,int
    param x список координат х
    param y список координат y
    """
    sum_xy = fsum([ _x*_y for _x,_y in zip(x,y) ])
    pow_x = fsum([_x*_x for _x in x])
    pow_y = fsum([_y*_y for _y in y])
    return sum_xy,pow_x,pow_y

def correlation_coefficient(n,x,y):
    """
    Получение корреляционного коэфициента
    correlation_coefficient(n,x,y)  -> int
    param n количество эксперементов
    param x список координат х
    param y список координат y
    """
    sum_xy,pow_x,pow_y = calculate_x_y(x,y)
    r = (n*sum_xy - fsum(x)*fsum(y))/(
        sqrt(
            (n*pow_x - pow(fsum(x),2))*
            (n*pow_y - pow(fsum(y),2))
        ))
    return r

def calculate_b_first(n,x,y):
    """
    Получение среднего значения зависимости переменной y при x = 0
    calculate_b_first(n,x,y) ->  int
    param n количество эксперементов
    param x список координат х
    param y список координат y
    """
    sum_xy,pow_x,pow_y = calculate_x_y(x,y)
    b = (n*sum_xy - fsum(x)*fsum(y))/(
        n*pow_x - pow(fsum(x),2)
        )
    return b
def calculate_b_zero(n,x,y):
    """
    Получение углового коэффициента линии регрессии (показывает, насколько в среднем
    изменяется величина y при изменении величины x на единицу своего измерения)
    calculate_b_zero(n,x,y) ->  int
    param n количество эксперементов
    param x список координат х
    param y список координат y
    """
    b_first = calculate_b_first(n,x,y)
    b = fsum(y)/n - b_first*(fsum(x)/n)
    return b
