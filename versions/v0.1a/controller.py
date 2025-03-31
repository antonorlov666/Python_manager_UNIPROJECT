from view import *

def main():
    while True:
        operation = inputs()
        try:
            if operation == 'help':
                help()

        except:
            print('ERROR')


if __name__ == "__main__":
    main()