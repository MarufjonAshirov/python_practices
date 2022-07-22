from art import logo
import random


def difficulty(dif):
    if dif == 'hard':
        return 5
    elif dif == 'easy':
        return 10
    else:
        print('wrong input')
        dif = input('choose the difficulty type hard or easy: ').lower()
        return difficulty(dif)


random_num = random.randint(1, 100)
print(logo)
diff = input('choose the difficulty type hard or easy: ').lower()
attempts = difficulty(diff)
while attempts != 0:
    num = int(input('I am thinking of the number between 1 and 100\nGuess my number: '))
    if random_num != num:
        attempts = attempts - 1
        print(f'You have {attempts} attempts')
        if random_num > num:
            print('Too low')
        else:
            print('Too high')
    else:
        print('you got the number\nyou win')
        break
if attempts == 0:
    print('You run out of attempts')
    print(f'My number is {random_num}')
