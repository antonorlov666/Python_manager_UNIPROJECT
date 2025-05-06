from view import *
from model import *

def main():
    start_dialogue()

    name_table = table_name_func()
    while True:
        df = pand(name_table)
        df.set_index(df.columns[0], inplace=True)
        operation = inputs()
        if operation == 'full name':
            index_name = inputs_name()
            full_name_view(df, index_name)
        elif operation == 'job':
            filter_value = filter_input()
            column = 'Должность'
            comparison = '='
            filtered_value = filter(df, filter_value, column, comparison)
            filter_view(filtered_value)
        elif operation == 'experience':
            filter_value = filter_number_input()
            column = 'Стаж'
            comparison = filter_comparison_input()
            filtered_value = filter(df, filter_value, column, comparison)
            filter_view(filtered_value)
        elif operation == 'Marital status':
            filter_value = filter_input()
            column = 'Семейное положение'
            comparison = '='
            filtered_value = filter(df, filter_value, column, comparison)
            filter_view(filtered_value)
        else:
            ERROR()












