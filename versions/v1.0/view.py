def start_dialogue():#сообщение, выводимое при запуске программы
    print('hi, this is a setup program for launch the Python_manager v1.0\n'
          '')


def inputs():#функция для ввода команд
    return input("please, enter command: ")


def inputs_name():#функция для ввода ФИО
    return input('please, enter a name: ')


def table_name_func():#функция для ввода названия таблицы
    return input('please, enter tabels name: ')


def ERROR():#сообщение, выводимое при ошибке
    print('ERROR')


def full_name_view(df, index):#функция для вывода по ФИО
    print(df.loc[[index]])


def filter_view(filtred_jobs):#фенкция для вывода фильтрованных сотрудников
    print(filtred_jobs)





