def start_dialogue():#сообщение, выводимое при запуске программы
    print('hi, this is a setup program for launch the Python_manager v0.3a')


def inputs():#сообщение, выводимое после стартового
    return input("please, enter command: ")


def help():#сообщение, выводимое при команде "help"
    print('_____________________________\n'
          'list of commands:\n'
          'help - view this list\n'
          'start - start Telegram bot\n'
          'tn - enter table  name\n'
          '_____________________________')


def table_name_func():#функция для ввода названия таблицы
    return input('please, enter tabels name: ')


def ERROR():#сообщение, выводимое сообщение ошибки
    print('ERROR')