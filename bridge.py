"""Bridge Simulator"""

###########################################
# Phase 1: Card Deck and Creation of Hands#
###########################################


import collections
from random import choice   # Used to randomly deal out cards (akin to shuffling the deck)

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:

	# Initialize the deck
	ranks = [str(n) for n in range(2, 11)] + list('JQKA')
	suits = 'spades diamonds clubs hearts'.split()


	# Initialize the cards
	def __init__(self):
		self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

		self.north = []
		self.east = []
		self.south = []
		self.west = []

		self.players = [self.north, self.east, self.south, self.west]

	def __len__(self):
		return len(self._cards)

	def __getitem__(self, position):
		return self._cards[position]

class Dealer(FrenchDeck):

	def deal():
		while len(deck._cards) != 0:
			for p in deck.players:
				if len(p) == 13:
					continue
				else:
					pick_card = choice(deck)
					p.append(pick_card)
					deck._cards.remove(pick_card)
					print(len(deck._cards))
		for i, p in enumerate(deck.players):
			print("Hand {}:".format(i))
			print(p)

class Play(FrenchDeck)






class Hands(FrenchDeck): 

	def __init__(self):
		self.suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

	def sort_hands():
		for p in deck.players:
			

	def spades_high(card):
		rank_value = FrenchDeck.ranks.index(card.rank)
		return rank_value * len(self.suit_values) + self.suit_values[card.suit]

	def points(hand):
		temp_value = 0
		for card in hand:
			if 

	for p in players:
		p.append(points(p))

# class Display(FrenchDeck):


deck = FrenchDeck()
# print(choice(deck))
# print(list(deck))
Dealer.deal()
# Hands.sort_hands()
