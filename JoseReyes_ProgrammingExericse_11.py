# Jose Reyes
# Programming Exercise #11
# This program deals a five-card Poker hand and allows the player
# to replace selected cards during the draw phase.

import random


# This class creates a deck of playing cards.
class Deck:

    # This function creates and shuffles the deck before the game starts.
    def __init__(self, size):
        self.card_list = list(range(size))
        random.shuffle(self.card_list)
        self.current_card = 0

    # This function deals one card from the deck.
    def deal(self):

        # Start over with a shuffled deck if every card has been used.
        if self.current_card >= len(self.card_list):
            random.shuffle(self.card_list)
            self.current_card = 0

        # Save the next card before moving to the next position.
        card = self.card_list[self.current_card]

        # Move to the next card so the same card is not dealt twice.
        self.current_card += 1

        return card


# This function converts a card number into its rank and suit.
def get_card_name(card):

    # Store every rank found in a standard deck.
    ranks = [
        "Two", "Three", "Four", "Five", "Six", "Seven",
        "Eight", "Nine", "Ten", "Jack",
        "Queen", "King", "Ace"
    ]

    # Store every suit found in a standard deck.
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

    # Find the rank that belongs to the card.
    rank = card % 13

    # Find the suit that belongs to the card.
    suit = card // 13

    return f"{ranks[rank]} of {suits[suit]}"


# This function deals a five-card Poker hand.
def deal_hand(deck):

    # Create a list to store the player's cards.
    hand = []

    # Deal five cards because a Poker hand always has five cards.
    for _ in range(5):
        hand.append(deck.deal())

    return hand


# This function displays the player's hand.
def display_hand(hand):

    print()

    # Number each card so the player knows which cards to replace.
    for position, card in enumerate(hand, start=1):
        print(f"{position}. {get_card_name(card)}")


# This function asks the player which cards to replace.
def get_replacement_positions():

    while True:

        # Ask the player which cards should be replaced.
        user_input = input(
            "\nEnter the card numbers to replace "
            "(Example: 1, 3, 5)\n"
            "Press Enter to keep your hand: "
        )

        # Keep the current hand if the player presses Enter.
        if user_input.strip() == "":
            return []

        try:

            # Separate each card number entered by the player.
            entries = user_input.split(",")

            # Store each valid card position.
            positions = []

            # Check every card number entered.
            for entry in entries:

                position = int(entry.strip())

                # Only allow positions that exist in the hand.
                if position < 1 or position > 5:
                    raise ValueError

                # Prevent the same card from being replaced twice.
                if position not in positions:
                    positions.append(position)

            return positions

        except ValueError:
            print("\nPlease enter only numbers from 1 through 5.")


# This function replaces the selected cards.
def replace_cards(hand, deck, positions):

    # Replace each selected card with a new card from the deck.
    for position in positions:
        hand[position - 1] = deck.deal()


# This function controls the Poker game.
def main():

    print("Five-Card Poker Draw Game")
    print("-------------------------")

    # Create a standard deck of playing cards.
    deck = Deck(52)

    # Deal the player's starting hand.
    hand = deal_hand(deck)

    # Display the original hand before replacing any cards.
    print("\nOriginal Hand:")
    display_hand(hand)

    # Ask the player which cards they want to replace.
    positions = get_replacement_positions()

    # Replace the selected cards with new ones.
    replace_cards(hand, deck, positions)

    # Display the player's final hand.
    print("\nFinal Hand:")
    display_hand(hand)

    print("\nThanks for playing!")


# Start the program.
if __name__ == "__main__":
    main()