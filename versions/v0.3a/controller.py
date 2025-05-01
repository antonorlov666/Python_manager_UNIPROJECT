from view import *
from model import *

def main():
    while True:
        operation = inputs()
        if operation == 'help':
            help()
        if operation == 'start':
            start()
        if operation == 'tn':
            table_name_func()
        else:
            ERROR()


