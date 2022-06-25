import random


def input_num():
    num1 = input("please enter number to play")
    while not num1.isnumeric():
        print('Your input is not positive number')
        num1 = input('please enter number to play\n')
    return int(num1)


def check_game(player_num, computer_num, tries1, tries2):
    while player_num != computer_num:
        if player_num > computer_num:
            print("your number greater than guessed number\n")
        else:
            print('your number is lower than guessed number')
        print('please guess again you have {} attempts\n'.format(tries2))
        tries2 -= 1
        player_num = input_num()
        tries1 += 1
        if tries1 == 4 or player_num == computer_num:
            break
    if player_num == computer_num:
        print('You win the game')
    else:
        print('Game over! You lost')


question = 'y'
while question == 'y':
    number_of_tries = 1
    tries = 3
    computer = random.randint(1, 10)
    num = input_num()
    print(computer)
    check_game(num, computer, number_of_tries, tries)
    question = input('Do you want to play again y/n\n')
print("Thanks for playing\n Game over! Bye")
