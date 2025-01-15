import os
import copy
import random

# Define clear_screen function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

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

def calculate_total(hand):
    total = sum(card_values[card] for card in hand)
    if total > 21 and 'A' in hand:
        total -= 10  # Convert one Ace from 11 to 1
    return total


def intial_deal():
    # Add code to deal the cards
    random_suit_dealer_1,random_card_dealer_1 = deal(deck_copy)
    random_suit_dealer_2,random_card_dealer_2 = deal(deck_copy)
    hand_dealer = [random_card_dealer_1, random_card_dealer_2]
    hand_dealer_revealed = [random_card_dealer_1]
    print(f"The dealer has the {random_card_dealer_1} of {random_suit_dealer_1} and the next card is face down.")

    random_suit_player_1,random_card_player_1 = deal(deck_copy)
    random_suit_player_2,random_card_player_2 = deal(deck_copy)
    hand_player = [random_card_player_1, random_card_player_2]
    print(f"You have the {random_card_player_1} of {random_suit_player_1} and the {random_card_player_2} of {random_suit_player_2}.")

    dealer_total = calculate_total(hand_dealer_revealed)
    player_total = calculate_total(hand_player)
    print(f"Dealer's total is {dealer_total} + face down card.")
    print(f"Player's total is {player_total}.")
    return random_card_dealer_1, random_card_dealer_2, random_card_player_1, random_card_player_2, random_suit_dealer_2

def deal(deck):
    suit = random.choice(list(deck.keys()))
    card = random.choice(deck[suit])
    deck[suit].remove(card)
    return suit, card


def play(random_card_dealer_1, random_card_dealer_2, random_card_player_1, random_card_player_2, random_suit_dealer_2):
    # Add code to play the game
    dealer_hand = [random_card_dealer_1, random_card_dealer_2]
    player_hand = [random_card_player_1, random_card_player_2]
    dealer_total = calculate_total(dealer_hand)
    player_total = calculate_total(player_hand)


    while True:
        hit_or_stand = input("Would you like to hit or stand? (h/s): ").lower()
        if hit_or_stand == 'h':
            # Add code to hit
            random_suit_player_next, random_card_player_next = deal(deck_copy) 
            player_hand.append(random_card_player_next)
            player_total = calculate_total(player_hand)
            print(f"You drew the {random_card_player_next} of {random_suit_player_next}.")
            print(f"Your new total is {player_total}.")
            if player_total > 21:
                print("Bust! You lose.")
                return
            elif player_total == 21:
                print("Blackjack! You win!")
                return
           
        elif hit_or_stand == 's':
            # Add code to stand
            print(f"The dealer's face down card is the {random_card_dealer_2} of {random_suit_dealer_2}.")
            print(f"The dealer's total is {dealer_total}.")
            while dealer_total < 17:
                random_suit_dealer, random_card_dealer = deal(deck_copy)
                dealer_hand.append(random_card_dealer)
                dealer_total = calculate_total(dealer_hand)
                print(f"The dealer drew the {random_card_dealer} of {random_suit_dealer}.")
                print(f"The dealer's new total is {dealer_total}.")
                if dealer_total > 21:
                    print("Dealer busts! You win!")
                    return
            if dealer_total > player_total:
                print("Dealer wins!")
            elif dealer_total < player_total:
                print("You win!")
            else:
                print("It's a tie!")
            break
        else:
            print("Invalid input. Please enter 'h' or 's'.")
            
def reset_deck():
    global deck_copy
    deck_copy = copy.deepcopy(deck)

def main():
    # define blackjack function
    while True:
        clear_screen()
        start_game = input("\nWould you like to play a hand of Blackjack? (y/n): ").lower()
        if start_game == 'y':
            reset_deck()
            print("Great! Let's play!")
            random_card_dealer_1, random_card_dealer_2, random_card_player_1, random_card_player_2, random_suit_dealer_2 = intial_deal()
            play(random_card_dealer_1, random_card_dealer_2, random_card_player_1, random_card_player_2, random_suit_dealer_2)
            input("Press Enter to continue...")


        elif start_game == 'n':
            print("Maybe next time!")
            break

        else:
            print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()





    
