from blackjack_art import logo
import random


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(user_score):
    if sum(user_score) == 21 and len(user_score) == 2:
        return 0
    if 11 in user_score and sum(user_score) > 21:
        user_score.remove(11)
        user_score.append(1)
    return sum(user_score)


print(logo)
user_cards = []
computer_cards = []
for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
