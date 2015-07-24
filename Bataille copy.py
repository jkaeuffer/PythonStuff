#the game of bataille takes as many turns as there as carde left in the dark. turn by turn, players will uncover a card from their randomly organized share of the deck, the highest card wins. If both cards are of the same values then nobody wins and they go another round.
#at the end of the turn, the winner takes all cards that were shown and places them at the bottom of their pile of cards.
#game is over when one player has all the cards

# Steps to follow:
# 1. create a list that has all the cards in a deck
# 2. create two players deck and assign in a random order half of the deck into their list
# 3 for each turn, take the first card in the list for that player, remove that card from the list and show it. then do the same for the other player
# 4 then compare the two cards and decide if they're equal or not. if they're not equal then look at which is the winner.
# 5 take both cards that were shown and add them to the end of the winner's' card list
# 6 if they are equal then have them go another round (to simplify we could use color suits as a tie break rule)
# 7 check if one users list is empty, if it is, this player has lost.

import random

deckOfCards = ['Ac', '2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', '10c', 'Jc', 'Qc', 'Kc', 'Ad', '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', '10d', 'Jd', 'Qd', 'Kd', 'As', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', '10s', 'Js', 'Qs', 'Ks', 'Ah', '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', '10h', 'Jh', 'Qh', 'Kh']

#shuffle and deal cards

def dealCards(cards):
	deckToShuffle = random.shuffle(cards)
	playerA = []
	playerB = []
	for n in range(len(cards) - 1):
		if n % 2 != 0:
			playerA.append(cards[n])
		else:
			playerB.append(cards[n])
	return playerA, playerB

(playerACards, playerBCards) = dealCards(deckOfCards)

cards = {
	"Player A:": playerACards,
	"Player B:": playerBCards
}

print cards




