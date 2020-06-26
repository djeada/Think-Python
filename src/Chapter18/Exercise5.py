'''
Exercise 5
The following are the possible hands in poker, in increasing order of value (and decreasing order of probability):

pair:
two cards with the same rank
two pair:
two pairs of cards with the same rank
three of a kind:
three cards with the same rank
straight:
five cards with ranks in sequence (aces can be high or low, so Ace-2-3-4-5 is a straight and so is 10-Jack-Queen-King-Ace, but Queen-King-Ace-2-3 is not.)
flush:
five cards with the same suit
full house:
three cards with one rank, two cards with another
four of a kind:
four cards with the same rank
straight flush:
five cards in sequence (as defined above) and with the same suit
The goal of these exercises is to estimate the probability of drawing these various hands.

1. Download the following files from http://thinkpython.com/code:
Card.py
: A complete version of the Card, Deck and Hand classes in this chapter.
PokerHand.py
: An incomplete implementation of a class that represents a poker hand, and some code that tests it.
2. If you run PokerHand.py, it deals seven 7-card poker hands and checks to see if any of them contains a flush. Read this code carefully before you go on.
3. Add methods to PokerHand.py named has_pair, has_twopair, etc. that return True or False according to whether or not the hand meets the relevant criteria. Your code should work correctly for “hands” that contain any number of cards (although 5 and 7 are the most common sizes).
4. Write a method named classify that figures out the highest-value classification for a hand and sets the label attribute accordingly. For example, a 7-card hand might contain a flush and a pair; it should be labeled “flush”.
5. When you are convinced that your classification methods are working, the next step is to estimate the probabilities of the various hands. Write a function in PokerHand.py that shuffles a deck of cards, divides it into hands, classifies the hands, and counts the number of times various classifications appear.
6. Print a table of the classifications and their probabilities. Run your program with larger and larger numbers of hands until the output values converge to a reasonable degree of accuracy. Compare your results to the values at http://en.wikipedia.org/wiki/Hand_rankings.
Solution: http://thinkpython.com/code/PokerHandSoln.py.
'''

import random

class Card():
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

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
        
class Deck():
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
            for i in range(len(self.cards)-1):
                if self.cards[i] > self.cards[i+1]:
                    temp = self.cards[i]
                    self.cards[i] = self.cards[i+1]
                    self.cards[i+1] = temp

    def deal_hands(self, num_hands, num_cards):
        if (num_hands * num_cards) > len(self.cards):
            print('Ich habe keine mehr!')
            return
        else:
            lista = []
            for x in range(num_hands):
                    hand = Hand()
                    for y in range(num_cards):
                        hand.cards.append(self.cards.pop())
                    lista.append(hand)
            return lista
    

class Hand():
    def __init__(self, label=''):
        self.cards = []
        self.label = label

    def __str__(self):
        return ', '.join(str(x) for x in self.cards)


def find_defining_class(obj, method_name):
    for ty in type(obj).mro():
        if method_name in ty.__dict__:
            return ty
    return None


class PokerHand(Hand):

    def suit_hist(self):
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def has_flush(self):
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def rank_hist(self):
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has_two_of_a_kind(self):
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 2:
                return True
        return False

    def has_three_of_a_kind(self):
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 3:
                return True
        return False


    def has_straight(self):
        self.rank_hist()
        if 1 in self.ranks.keys():
            self.ranks[14] = 1

        for card in self.cards:
            count = 0
            for i in xrange(5):
                if card.rank + i in self.ranks.keys():
                    count += 1
            if count >= 5:
                return True
        return False


    def has_full_house(self):
        self.rank_hist()

        for item in self.cards:
            print(item)

        for x in self.ranks.values():
            for y in self.ranks.values():
                if x >= 3 and y >= 2:
                    return True
        return False


    def has_four_of_a_kind(self):
        self.rank_hist()
        for val in self.ranks.keys():
            if val == 4:
                return True
        return False


    def has_straight_flush(self):
        if not self.has_straight() and not self.has_flush():
            return False

        for card in self.cards:
            if card.rank == 1:
                high_ace = Card(card.suit, 14)
                self.cards.append(high_ace)

        for card in self.cards:
            count = 0
            for i in xrange(5):
                for y in self.cards:
                    if y.rank == card.rank + i and y.suit == card.suit:
                        count += 1
            if count >= 5:
                return True
        return False

    def classify(self):
        self.has_hands = []
        best_hand = PokerHand.types_of_hands[0]

        for type in PokerHand.types_of_hands[1:]:
            x = getattr(self, type)
            if x():
                self.has_hands.append(type)

        for item in self.has_hands:
            if self.types_of_hands.index(item) > self.types_of_hands.index(best_hand):
                best_hand = item

        self.label = best_hand


def find_probabilities(num_of_decks):
    probability_histo = {}
    total_num_hands = num_of_decks * 7

    for num in xrange(num_of_decks):
        deck = Deck()
        deck.shuffle()

        for i in range(7):
            hand = PokerHand()
            deck.move_cards(hand, 7)
            hand.classify()
            for item in hand.has_hands:
                probability_histo[item] = probability_histo.get(item, 0) + 1

    for type_hand in probability_histo.keys():
        probability_histo[type_hand] = str(probability_histo[type_hand] / float(total_num_hands) * 100) + " %"

    print(probability_histo)

deck1 = Deck()
deck1.shuffle()
for x in deck1.deal_hands(5,5):
    print(x)
    
