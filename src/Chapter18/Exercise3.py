"""
Exercise 3
Write a Deck method called deal_hands that takes two parameters, the number of hands and
the number of cards per hand, and that creates new Hand objects, deals the appropriate
number of cards per hand, and returns a list of Hand objects.
"""

import random


class Card:
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [
        None,
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    ]

    def __str__(self):
        return "%s of %s" % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __gt__(self, other):
        if self.suit < other.suit:
            return False
        if self.suit == other.suit:
            if self.rank < other.rank:
                return False
        return True

    def __ls__(self, other):
        if self.suit > other.suit:
            return False
        if self.suit == other.suit:
            if self.rank > other.rank:
                return False
        return True


class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return "\n".join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        for j in range(len(self.cards)):
            for i in range(len(self.cards) - 1):
                if self.cards[i] > self.cards[i + 1]:
                    temp = self.cards[i]
                    self.cards[i] = self.cards[i + 1]
                    self.cards[i + 1] = temp

    def deal_hands(self, num_hands, num_cards):
        if (num_hands * num_cards) > len(self.cards):
            print("Ich habe keine mehr!")
            return
        else:
            lista = []
            for x in range(num_hands):
                hand = Hand()
                for y in range(num_cards):
                    hand.cards.append(self.cards.pop())
                lista.append(hand)
            return lista


class Hand:
    def __init__(self, label=""):
        self.cards = []
        self.label = label

    def __str__(self):
        return ", ".join(str(x) for x in self.cards)


deck1 = Deck()
deck1.shuffle()
for x in deck1.deal_hands(5, 5):
    print(x)
