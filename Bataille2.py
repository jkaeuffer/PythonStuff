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


#asking for players names
def getPlayersNames():
	playerA = raw_input("First Player's name?")
	playerB = raw_input("Second Player's name?")

(playerA, playerB) = getPlayersNames

#this dictionary holds the cards ranks, suits, and values
deckVersion2 = {
	"Ranks": ["2","3","4","5","6","7","8","9","10",'J','Q','K','A'],
	"Suits": 'shdc', 
	"Values": [2,3,4,5,6,7,8,9,10,11,12,13,14]
}

#we are creating the deck by combining the ranks and the suits
def createDeck():
	suitsList = [n for n in deckVersion2['Suits']]
	deckOfCards = []
	for n in deckVersion2["Ranks"]:
		for x in range (len(suitsList)):
			deckOfCards.append(n + suitsList[x])
	return deckOfCards

#assigning the newly created deck to "deckOfCards" variable, this way a new deck is created, and we're re-using just the variable in
#the other functions
deckOfCards = createDeck()

 # for debugging
print "The deck is %s cards\n" % len(deckOfCards)

suitsOrder = ["s", "h", "d", "c"]

# shuffle and deal cards
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

# pick top card for each player

def pickCards(x, y):
	playerAPick = x.pop()
	playerBPick = y.pop()
	return playerAPick, playerBPick

(playerAPick, playerBPick) = pickCards(playerACards, playerBCards)

# for debugging
# print deckVersion2["Ranks"].index("J")

# find index in dictionary from a rank
def indexInDict(a):
	rankIndex = deckVersion2["Ranks"].index(a)
	return rankIndex

# for debugging
# print deckVersion2["Values"][indexInDict(playerAPick[:-1])]

# check best card
dealCards(deckOfCards)
print "Player A has %s cards in their deck\n" % len(playerACards)
print "Player B has %s cards in their deck\n" % len(playerBCards)

def bestCard(x, y):
	# finding the card's rank
	cardRankPlayerA = x[:-1]
	cardRankPlayerB = y[:-1]
	# find the card's suit
	cardSuitPlayerA = x[-1:]
	cardSuitPlayerB = y[-1:]
	cardSuitPlayerAIndex = suitsOrder.index(cardSuitPlayerA)
	cardSuitPlayerBIndex = suitsOrder.index(cardSuitPlayerB)
	#find the value equivalent to the card's rank
	cardValuePlayerA = deckVersion2["Values"][indexInDict(cardRankPlayerA)]
	cardValuePlayerB = deckVersion2["Values"][indexInDict(cardRankPlayerB)]
	# comparing the card's values first, assuming they're not equal to each other
	# we'll get to the "equal to each other" part later
	if int(cardValuePlayerA) > int(cardValuePlayerB):
		# if player wins, they get both cards to their deck
		playerACards.append(x)
		playerACards.append(y)
		print "Player A wins this round"
	elif int(cardValuePlayerB) > int(cardValuePlayerA):
		playerBCards.append(x)
		playerBCards.append(y)
		print "Player B wins this round"
	# now let's look at if the cards ranks are the same, then the values win over. We have a list
	# suitsOrder that tracks the order of suits 
	elif int(cardValuePlayerA) == int(cardValuePlayerB):
		# if the INDEX is lower that means it's earlier in the list	
		if cardSuitPlayerAIndex < cardSuitPlayerBIndex:
			playerACards.append(x)
			playerACards.append(y)
			print "Player A wins this round"
		else:
			playerBCards.append(x)
			playerBCards.append(y)
			print "Player B wins this round"
	else:
		return "This is not possible PlayerA's card was", x, "Player B's card was", y
	return "Player A now has %s cards in their deck and player B has now %s cards in their deck\n" % (len(playerACards), len(playerBCards))



#printing everything for debugging
print "Cards are %s \n" % deckOfCards
print "Player A's cards are %s \n" % playerACards
print "Player B's cards are %s \n" % playerBCards
print "Player A's pick is %s \n" % playerAPick
print "Player B's pick is %s \n" % playerBPick
print bestCard(playerAPick, playerBPick)















