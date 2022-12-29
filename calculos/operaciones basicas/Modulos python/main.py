import add
import subtract
import multiply
import divide


def main():
    pass


def begin():
    start = int(input(
        '''
        Welcome to our calculator, our Calculator have 4 principal functions,
        add, subtract, multiply and divide, 
        lets go, 
        please type 1 to continue or 0 to exit: 
        '''))

    if start == 1:
        operationSelect = int(input('''
        i´m glad to see you here, please type which operation you need: 
            1: Add
            2: Subtract
            3: Multiply
            4: Divide
            0: exit
        '''))
        match operationSelect:
            case 1:
                print(add.add())
            case 2:
                print(subtract.subtract())
            case 3:
                print(multiply.multiply())
            case 4:
                print(divide.divide())

    else:
        exit()


if __name__ == '__main__':
    begin()
