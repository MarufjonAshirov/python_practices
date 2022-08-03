from art import logo, vs
from game_data import data
import random


def format_data(account):
    """ formatting account data"""
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f'{account_name}, a {account_description}, from {account_country}'


def check_answer(guess_w, a_followers, b_followers):
    if a_followers > b_followers:
        return guess_w == 'a'
    else:
        return guess_w == 'b'


def check_guess(guess1):
    if guess1 == 'a' or guess1 == 'b':
        return guess1
    else:
        print('Input is invalid')
        guess1 = input('Who has more followers: Type A or B->').lower()
        check_guess(guess1)


print(logo)
score = 0
is_finished = True
account_b = random.choice(data)

while is_finished:
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f'Compare A: {format_data(account_a)}')
    print(vs)
    print(f'Compare B: {format_data(account_b)}')

    guess = input('Who has more followers: Type A or B->').lower()
    check_guess(guess)
    a_follower = account_a['follower_count']
    b_follower = account_b['follower_count']

    is_correct = check_answer(guess, a_follower, b_follower)
    if is_correct:
        score += 1
        print(f'You are right, your score: {score}')
    else:
        is_finished = False
        print(f'Sorry, that is wrong.\nFinal score: {score}')
    print('-' * 80)
