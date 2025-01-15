import copy
import random

deck = {
    'Hearts': ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'],
    'Diamonds': ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'],
    'Clubs': ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'],
    'Spades': ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
}

deck_copy = copy.deepcopy(deck)

card_values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A' : 11
}

def reset_deck():
    global deck_copy
    deck_copy = copy.deepcopy(deck)

def calculate_total(hand):
    total = sum(card_values[card] for card in hand)
    if total > 21 and 'A' in hand:
        total -= 10  # Convert one Ace from 11 to 1
    return total

def deal(deck):
    suit = random.choice(list(deck.keys()))
    card = random.choice(deck[suit])
    deck[suit].remove(card)
    return suit, card

def intial_deal():
    dealer_hand = [deal(deck_copy)[1] for _ in range(2)]
    player_hand = [deal(deck_copy)[1] for _ in range(2)]
    print(f"Dealer's hand: {dealer_hand}")
    print(f"Player's hand: {player_hand}")
    return dealer_hand, player_hand

def play(dealer_hand, player_hand):
    dealer_total = calculate_total(dealer_hand)
    player_total = calculate_total(player_hand)

    while True:
        hit_or_stand = input("Would you like to hit or stand? (h/s): ").lower()
        if hit_or_stand == 'h':
            _, card = deal(deck_copy)
            player_hand.append(card)
            player_total = calculate_total(player_hand)
            print(f"You drew {card}. Your total is now {player_total}.")
            if player_total > 21:
                print("Bust! You lose.")
                return
            elif player_total == 21:
                print("Blackjack! You win!")
                return
        elif hit_or_stand == 's':
            print(f"Dealer's total is {dealer_total}.")
            while dealer_total < 17:
                _, card = deal(deck_copy)
                dealer_hand.append(card)
                dealer_total = calculate_total(dealer_hand)
                print(f"Dealer drew {card}. Total is now {dealer_total}.")
                if dealer_total > 21:
                    print("Dealer busts! You win!")
                    return
            break
        else:
            print("Invalid input. Please enter 'h' or 's'.")

    if dealer_total > player_total:
        print("Dealer wins!")
    elif dealer_total < player_total:
        print("You win!")
    else:
        print("It's a tie!")

def main():
    print("Welcome to Blackjack!")
    while True:
        start_game = input("Would you like to play a hand of Blackjack? (y/n): ").lower()
        if start_game == 'y':
            reset_deck()
            dealer_hand, player_hand = intial_deal()
            play(dealer_hand, player_hand)
        elif start_game == 'n':
            print("Maybe next time!")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == '__main__':
    main()


