import random

class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        print("{} of {}".format(self.value, self.suit))

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["spades", "clubs", "diamonds", "hearts"]:
            for v in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
                self.cards.append(Card(s,v))

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0 , -1):
            r = random.randint(0,i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
    
    def show(self):
        for c in self.cards:
            c.show()

    def drawCard(self):
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    
    def draw(self, deck):
        self.hand.append(deck.drawCard())
        #return self

    def showHand(self):
        for card in self.hand:
            card.show()
    
    def countHand(self):
        points = 0
        for card in self.hand:
            print(card.value)
            try:
                a = int (card.value)
            except:
                if card.value == "J" or card.value == "Q" or card.value == "K":
                    a = 10
                else:
                    a = 11
            points += a

        print(points)
                    

deck = Deck()
deck.shuffle()
#deck.show()

bob = Player("Bob")
bob.draw(deck)
bob.draw(deck)
bob.showHand()
bob.countHand()