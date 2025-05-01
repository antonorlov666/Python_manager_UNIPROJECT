def start_dialogue():#сообщение, выводимое при запуске программы
    print('_____________________________\n'
          'hi, this is a setup program for launch the Python_manager v0.4a\n'
          '_____________________________\n'
          'list of commands:\n'
          'start - start Telegram bot\n'
          'tn - enter table  name\n'
          '_____________________________\n'
          'Thats all I wanted to tell you, you can use this app now\n'
          '_____________________________')


def inputs():#сообщение, выводимое после стартового
    return input("please, enter command: ")



def table_name_func():#функция для ввода названия таблицы
    return input('please, enter tabels name: ')


def ERROR():#сообщение, выводимое при ошибке
    print('ERROR')