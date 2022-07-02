from calculator_art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def power(n1, n2):
    return n1 ** n2


def operation_check(operation):
    if operation in operations:
        return operation
    else:
        print('invalid input')
        operation = input('Pick an operation above: ')
        return operation_check(operation)


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '^': power
}


def calculator():
    print(logo)
    num1 = float(input('Please enter first number: '))
    total = 0
    finished = False
    while not finished:
        for op in operations:
            print(op)
        operation_symbol = input('Pick an operation above: ')
        check_symbol = operation_check(operation_symbol)
        num2 = float(input('please enter next number: '))
        function_calc = operations[check_symbol]
        answer = function_calc(num1, num2)
        print(f'{num1} {check_symbol} {num2} = {answer}')
        exiting = 'tab anything to exit'
        ask = input(f'type "y" to continue calculating with {answer}, or type "n" to restart program or {exiting}: ')
        if ask == 'y':
            num1 = answer
        elif ask == 'n':
            finished = True
            calculator()
        else:
            finished = True
    print('Thanks for using my program\nBye')


calculator()
