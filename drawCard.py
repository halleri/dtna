import random, itertools, sys


class Card(object):

    def cards(self):
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        rank = ['Ace','2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        deck = list(' of '.join(card) for card in itertools.product(rank, suits))

        random.shuffle(deck)

        while deck:
            card_shown = deck.pop()
            print(card_shown)
            if True:
                response = raw_input("Press the Enter key to draw another card")
                if response == 'y':
                    print (card_shown)
                if response == 'n':
                    sys.exit()
                if not deck:
                    print("Deck is now empty!")



if __name__ == '__main__':
    card = Card()
    card.cards()







