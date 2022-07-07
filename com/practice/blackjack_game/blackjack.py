from blackjack_art import logo
import random


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards_amount):
    if sum(cards_amount) == 21 and len(cards_amount) == 2:
        return 0
    if 11 in cards_amount and sum(cards_amount) > 21:
        cards_amount.remove(11)
        cards_amount.append(1)
    return sum(cards_amount)


print(logo)
user_cards = []
computer_cards = []
is_game_over = False
for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)
print(f'your cards: {user_cards}, current score: {user_score}')
print(f'computers first card: {computer_cards[0]}')
if user_score == 0 or computer_score == 0 or user_score > 21:
    is_game_over = True
else:
    user_should_deal = input('type "y" to get another card, type "n" to pass')
    if user_should_deal == 'y':
        user_cards.append(deal_card())
    else:
        is_game_over = True
    print(user_cards)
    print(computer_cards)
    print('this is test to blackjack')
