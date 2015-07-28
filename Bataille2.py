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

#I'm adding a break if the turns go more than 50 otherwise it risks creating an infinte loop.
import random

#asking for players names
def getPlayersNames():
	playerA = raw_input("First Player's name?")
	playerB = raw_input("Second Player's name?")
	return playerA, playerB

#this dictionary holds the cards ranks, suits, and values
deckDict = {
	"Ranks": ["2","3","4","5","6","7","8","9","10",'J','Q','K','A'],
	"Suits": ["s", "h", "d", "c"], 
	"Values": [2,3,4,5,6,7,8,9,10,11,12,13,14]
}

#we are creating the deck by combining the ranks and the suits
def createDeck():
	suitsList = [n for n in deckDict['Suits']]
	deckOfCards = []
	for n in deckDict["Ranks"]:
		for x in range (len(suitsList)):
			deckOfCards.append(n + suitsList[x])
	return deckOfCards

 # for debugging
# print "The deck is %s cards\n" % len(deckOfCards)

# shuffle and deal cards
def dealCards(cards):
	deckToShuffle = random.shuffle(cards)
	playerACards = []
	playerBCards = []
	for n in range(len(cards) - 1):
		if n % 2 != 0:
			playerACards.append(cards[n])
		else:
			playerBCards.append(cards[n])
	return playerACards, playerBCards

# pick top card for each player
def pickCards(x, y):
	playerAPick = x.pop()
	playerBPick = y.pop()
	return playerAPick, playerBPick

# find index in dictionary from a rank
def indexInDict(a):
	rankIndex = deckDict["Ranks"].index(a)
	return rankIndex

def bestCard(player1, player2, x, y, z, a):
	playerACards = z
	playerBCards = a
	playerA = player1
	playerB = player2
	if x[0] == "A":
		cardRankPlayerA = x[0]
	else:
		cardRankPlayerA = x[:-1]
	if y[0] == "A":
		cardRankPlayerB = y[0]
	else:
		cardRankPlayerB = y[:-1]
	cardSuitPlayerA = x[-1:]
	cardSuitPlayerB = y[-1:]
	cardSuitPlayerAIndex = deckDict["Suits"].index(cardSuitPlayerA)
	cardSuitPlayerBIndex = deckDict["Suits"].index(cardSuitPlayerB)
	cardValuePlayerA = deckDict["Values"][indexInDict(cardRankPlayerA)]
	cardValuePlayerB = deckDict["Values"][indexInDict(cardRankPlayerB)]
	if int(cardValuePlayerA) > int(cardValuePlayerB):
		playerACards.insert(0,x)
		playerACards.insert(0,y)
		print "%s wins this round with %s vs %s" % (playerA, x,y)
		return playerACards
	elif int(cardValuePlayerB) > int(cardValuePlayerA):
		playerBCards.insert(0,x)
		playerBCards.insert(0,y)
		print "%s wins this round with %s vs %s" % (playerB, x,y)
		return playerBCards
	elif int(cardValuePlayerA) == int(cardValuePlayerB):
		if cardSuitPlayerAIndex < cardSuitPlayerBIndex:
			playerACards.insert(0,x)
			playerACards.insert(0,y)
			print "%s wins this round with %s vs %s" % (playerA, x,y)
			return playerACards
		else:
			playerBCards.insert(0,x)
			playerBCards.insert(0,y)
			print "%s wins this round with %s vs %s" % (playerB, x,y)
			return playerBCards
	else:
		return "This is not possible PlayerA's card was", x, "Player B's card was", y
	#return "Player A now has %s cards in their deck and player B has now %s cards in their deck\n" % (len(playerACards), len(playerBCards))
	#return playerACards, playerBCards

def play():
	(playerA, playerB) = getPlayersNames()
	print "Hello %s and %s. Are you ready to play? Press Y for yes or N for No" % (playerA, playerB)
	userResponse = raw_input("Y/N")
	if userResponse == "Y":
		deckOfCards = createDeck()
		print deckOfCards
		(playerACards, playerBCards) = dealCards(deckOfCards)
		round = 0
		while (len(playerACards) > 0 and len(playerBCards) > 0):
			(playerAPick, playerBPick) = pickCards(playerACards, playerBCards)
			bestCard(playerA, playerB, playerAPick, playerBPick, playerACards, playerBCards)
			round += 1
		if len(playerACards) == 0:
			print "%s won after %s rounds" % (playerB, round)
		else:
			print "%s won after %s rounds" % (playerA, round)
	else:
		print "Oh well, another time maybe"

play()
















