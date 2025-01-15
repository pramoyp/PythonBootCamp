import os
import copy
import random
import time

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
    print(f"\nThe dealer has the {random_card_dealer_1} of {random_suit_dealer_1} and the next card is face down.")
    time.sleep(1) # Pause for 1 second

    random_suit_player_1,random_card_player_1 = deal(deck_copy)
    random_suit_player_2,random_card_player_2 = deal(deck_copy)
    hand_player = [random_card_player_1, random_card_player_2]
    print(f"\nYou have the {random_card_player_1} of {random_suit_player_1} and the {random_card_player_2} of {random_suit_player_2}.")
    time.sleep(2) # Pause for 2 seconds

    dealer_total = calculate_total(hand_dealer_revealed)
    player_total = calculate_total(hand_player)
    print(f"\nDealer's total is {dealer_total} + face down card.")
    time.sleep(0.5)
    print(f"\nPlayer's total is {player_total}.")
    time.sleep(1.5) # Pause for 2 seconds
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
        hit_or_stand = input("\n\nWould you like to hit or stand? (h/s): ").lower()
        if hit_or_stand == 'h':
            # Add code to hit
            random_suit_player_next, random_card_player_next = deal(deck_copy) 
            player_hand.append(random_card_player_next)
            player_total = calculate_total(player_hand)
            time.sleep(1) # Pause for 1 second
            print(f"\nYou drew the {random_card_player_next} of {random_suit_player_next}.")
            time.sleep(1) 
            print(f"\nYour new total is {player_total}.")
            time.sleep(1.5) 
            if player_total > 21:
                print("\nBust! You lose.\n")
                return
            elif player_total == 21:
                print("\nBlackjack! You win!\n")
                return
           
        elif hit_or_stand == 's':
            # Add code to stand
            time.sleep(1) # Pause for 1 second
            print("\nThe dealer turns over his face down card....")
            time.sleep(1) # Pause for 1 second
            print(f"\nThe dealer's face down card is the {random_card_dealer_2} of {random_suit_dealer_2}.")
            time.sleep(1) 
            print(f"\nThe dealer's total is {dealer_total}.")
            time.sleep(1.5) 
            while dealer_total < 17:
                random_suit_dealer, random_card_dealer = deal(deck_copy)
                dealer_hand.append(random_card_dealer)
                dealer_total = calculate_total(dealer_hand)
                time.sleep(1) # Pause for 1 second
                print(f"\nThe dealer drew the {random_card_dealer} of {random_suit_dealer}.")
                time.sleep(1) 
                print(f"\nThe dealer's new total is {dealer_total}.")
                time.sleep(1) # Pause for 1 second
                if dealer_total > 21:
                    print("\nDealer busts! You win!\n")
                    return
            if dealer_total > player_total:
                print("\nDealer wins!\n")
            elif dealer_total < player_total:
                print("\nYou win!\n")
            else:
                print("\nIt's a tie!")
            break
        else:
            print("\nInvalid input. Please enter 'h' or 's'.")
            
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
            print("\nGreat! Let's play!")
            time.sleep(1) # Pause for 1 second
            random_card_dealer_1, random_card_dealer_2, random_card_player_1, random_card_player_2, random_suit_dealer_2 = intial_deal()
            play(random_card_dealer_1, random_card_dealer_2, random_card_player_1, random_card_player_2, random_suit_dealer_2)
            input("Press Enter to continue...")


        elif start_game == 'n':
            print("\nMaybe next time!\n")
            time.sleep(2) # Pause for 2 seconds
            break

        else:
            print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()





    
