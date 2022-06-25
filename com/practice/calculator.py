import numbers


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def division(num1, num2):
    if num2 == 0:
        print('Divisor can not be zero')
        num1, num2 = input_()
    op_check = True
    while op_check:
        op = input('please specify float division or whole number division: enter / or //')
        if op == '/':
            return num1 / num2
        elif op == '//':
            return num1 // num2
        else:
            op_check = False
            print('you entered wrong input\nplease try again\n')


def modulo(num1, num2):
    return num1 % num2


def power(num1, num2):
    return num1 ** num2


def input_():
    num1 = check_input('Enter first number')
    num2 = check_input('Enter second number')
    return num1, num2


def is_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def check_input(message):
    value_as_string = input(message)
    while not is_float(value_as_string):
        print('Input must be float')
        value_as_string = input(message)
    return float(value_as_string)


def menu():
    input_ok = False
    while not input_ok:
        print('\tMenu')
        print('\t1. Add\n'
              '\t2. Subtract\n'
              '\t3. Multiply\n'
              '\t4. Division\n'
              '\t5. Modulo\n'
              '\t6. Power\n')
        user_selection = input('Please make selection')
        if user_selection in ('1', '2', '3', '4', '5', '6'):
            input_ok = True
        else:
            input_ok = False
    return user_selection


def user_has_finished():
    ok_to_finish = True
    user_input_accepted = False
    while not user_input_accepted:
        user_input = input('Do you want to continue y/n')
        if user_input == 'y':
            ok_to_finish = False
            user_input_accepted = True
        elif user_input == 'n':
            ok_to_finish = True
            user_input_accepted = True
        else:
            user_input_accepted = False
            print('You entered wrong input rather than y/n')
    return ok_to_finish


# Main program
finished = False
while not finished:
    print('Welcome to simple calculator')
    n1, n2 = input_()
    print('-' * 50)
    selection = menu()
    result = 0
    if selection == '1':
        result = add(n1, n2)
    elif selection == '2':
        result = subtract(n1, n2)
    elif selection == '3':
        result = multiply(n1, n2)
    elif selection == '4':
        result = division(n1, n2)
    elif selection == '5':
        result = modulo(n1, n2)
    elif selection == '6':
        result = power(n1, n2)
    else:
        print('Invalid choice')
    print('Result:', result)
    finished = user_has_finished()
print('Bye\nThanks for using my application')
