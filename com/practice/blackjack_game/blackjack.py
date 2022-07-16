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


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"

    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


print(logo)
user_cards = []
computer_cards = []
is_game_over = False
for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)
while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f'your cards: {user_cards}, current score: {user_score}')
    print(f'computers first card: {computer_cards[0]}')
    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_should_deal = input('type "y" to get another card, type "n" to pass: ')
        if user_should_deal == 'y':
            user_cards.append(deal_card())
        else:
            is_game_over = True
while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

print(f"Your final hand: {user_cards}, your score {user_score}")
print(f"Computer;s hand: {computer_cards}, computer's score: {computer_score}")
print(compare(user_score, computer_score))
