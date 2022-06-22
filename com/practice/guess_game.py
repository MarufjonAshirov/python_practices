import random

question = 'y'
while question == 'y':
    number_of_tries = 1
    tries = 3
    guess = random.randint(1, 10)
    num = input('please enter number to play\n')
    while not num.isnumeric():
        print('Your input is not positive number')
        num = input('please enter number to play\n')
    num = int(num)
    while num != guess:
        if num > guess:
            print("your number greater than guessed number\n")
        else:
            print('your number is lower than guessed number')
        print('please guess again you have {} attempts\n'.format(tries))
        tries -= 1
        num = int(input('please enter number to play\n'))
        number_of_tries += 1
        if number_of_tries == 4 or num == guess:
            break
    if num == guess:
        print('You win the game')
    else:
        print('Game over! You lost')
    question=input('Do you want to play again y/n\n')
print("Thanks for playing\n Game over! Bye")
