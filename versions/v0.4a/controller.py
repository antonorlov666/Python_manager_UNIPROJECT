from view import *
from model import *

def main():
    start_dialogue()
    operation = inputs()
    if operation == 'start':
        start()
    elif operation == 'tn':
        table_name_func()
    else:
        ERROR()


