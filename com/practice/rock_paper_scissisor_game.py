import random

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game = [rock, paper, scissor]
question = 'y'
ans1 = 'You win'
ans2 = 'You lose\nComputer wins'
while question == 'y':
    print('Welcome to rock paper scissor game!!!')
    choice = int(input('please enter 0 for rock, 1 for paper and 2 for scissor'))
    guess = random.randint(0, 3)
    print(game[choice])
    print('Computer choose:\n' + game[guess])
    if choice == guess:
        print('Draw')
    elif choice == 0 and guess == 1:
        print(ans2)
    elif choice == 0 and guess == 2:
        print(ans1)
    elif choice == 1 and guess == 0:
        print(ans1)
    elif choice == 1 and guess == 2:
        print(ans2)
    elif choice == 2 and guess == 0:
        print(ans2)
    elif choice == 2 and guess == 1:
        print(ans1)
    else:
        print('Invalid input')
    question = input('Do you want to play again y/n\n')
print('Game over!!!\n Bye')
