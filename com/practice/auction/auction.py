from auction_art import logo


def check_winner(auction_data):
    key = max(auction_data, key=auction_data.get)
    print(f'The winner is {key} with ${auction_data[key]}')


print(logo)
finished = False
bid_data = {}
while not finished:
    name = input('please enter name to specify you in auction\n')
    price = int(input('please enter bid price $'))
    bid_data[name] = price
    other_bids = input('is there any other participant who want to bid y/n ')
    if other_bids == 'y':
        finished = False
    else:
        finished = True

check_winner(bid_data)
