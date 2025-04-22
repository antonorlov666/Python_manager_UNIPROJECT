rfrom view import *

def start():
    start_dialogue()
    operation = inputs()
    if operation == 'offline':
        offline()
    elif operation == 'online':
        online()
    elif operation == 'help':
        help()
    else:
        print('ERROR')


def offline(): #функция
    df = pd.read_excel('список сотрудников.xlsx')
    operation = inputs()
    if operation == '':




def online(): #пока нет




if __name__ == "__main__":
    main()
