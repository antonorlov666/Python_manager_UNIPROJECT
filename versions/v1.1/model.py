from view import *

import pandas as pd



def pand(name):
    return pd.read_excel(name)

def filter(df, filter_value, column, comparison):#уневирсальная функция для фильтрации значений по столбцам
    if comparison == '=':#если comparison равно "=", то стравниваем фильтруемый столбец с фильтратом(filter_value)
        filtered_value = df[df[column] == filter_value]
    elif comparison == '<':#если comparison равно "<", то выбираем все значения меньше фильтрата
        filtered_value = df[df[column] < filter_value]
    elif comparison == '>':#если comparison равно ">", то выбираем все значения больше фильтрата
        filtered_value = df[df[column] > filter_value]
    else:
        ERROR()
        return

    if filtered_value.empty:#фильтрация несуществующих значений
        ERROR()
    else:
        return filtered_value


