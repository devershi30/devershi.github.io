import random

class Card:
    def __init__(self, rank, suit, value):
        self.rank = rank
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.suit} of {self.rank}"
    
class Deck:
    def __init__(self):
        self.cards = []
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

        for suit in suits:
            for i in range (len (ranks)):
                self.cards.append(Card(suit, ranks[i], values[i]))

        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()
        
class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_hand_value(self):
        total_value = 0
        ace_count = 0

        for card in self.cards:
            total_value += card.value
            if card.value == 11:
                ace_count += 1
        
        while total_value > 21 and ace_count > 0:
            total_value -= 10
            ace_count -= 1

        return total_value
    
    def __str__(self):
        return ', '.join(str(card) for card in self.cards)
    
class Game:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.start_game()

    def start_game(self):
        self.player_hand.add_card(self.deck.draw_card())
        self.player_hand.add_card(self.deck.draw_card())
        self.dealer_hand.add_card(self.deck.draw_card())
        self.dealer_hand.add_card(self.deck.draw_card())

        print("\nPlayer Cards: ", self.player_hand)
        print("\nDealer Cards: ", self.dealer_hand)

        if self.player_hand.get_hand_value() == 21:
            print("\nBlackJack! Player Wins")
        else:
            self.dealer_turn()

    def dealer_turn(self):
        self.dealer_hand.add_card(self.deck.draw_card())
        print("\nDealer Cards: ", self.dealer_hand)

        if self.dealer_hand.get_hand_value() > 21 or self.player_hand.get_hand_value() > self.dealer_hand.get_hand_value():
            print("\nPlayer Wins")
        else:
            print("\nDealer Wins")

if __name__ == "__main__":
    Game()
