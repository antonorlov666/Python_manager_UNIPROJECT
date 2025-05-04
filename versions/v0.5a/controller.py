from view import *
from model import *

def main():
    start_dialogue()
    operation = inputs()
    if operation == 'start':
        start()
        bot_status = start()
    elif operation == 'tn':
        table_name_func()
    else:
        ERROR()


    if bot_status == 1:
        print('bot started')
    elif bot_status == 0:
        print('bot wasnt started')


    name_table = table_name_func()
    while True:
        df = pand(name_table)
        operation = inputs()
        if operation == 'string':
            df.set_index(df.columns[0], inplace=True)
            index_name = inputs_name()
            string_view(df, index_name)
        else:
            ERROR()












