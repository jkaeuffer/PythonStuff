# The game of bataille takes as many turns as there as cards left in the deck.
# Turn by turn, players take a card from their deck, the highest card wins.
# If both cards are of the same values then nobody wins.
# At end of turn, winner takes all shown cards.
# The game is over when one player has all the cards
import random


# Asking for players names
def getPlayersNames():
    playerA = raw_input("First Player's name? ")
    playerB = raw_input("Second Player's name? ")
    return playerA, playerB


# This dictionary holds the cards ranks, suits, and values
deckDict = {
    "Ranks": ["2", "3", "4", "5", "6", "7",
              "8", "9", "10", 'J', 'Q', 'K', 'A'],
    "Suits": ["s", "h", "d", "c"],
    "Values": [2, 3, 4, 5, 6, 7, 8,
               9, 10, 11, 12, 13, 14]
}


# We are creating the deck by combining the ranks and the suits
def createDeck():
    suitsList = [n for n in deckDict['Suits']]
    deckOfCards = []
    for n in deckDict["Ranks"]:
        for x in range(len(suitsList)):
            deckOfCards.append(n + suitsList[x])
    return deckOfCards

# For debugging
# print "The deck is %s cards\n" % len(deckOfCards)


# Shuffle and deal cards
def dealCards(cards):
    random.shuffle(cards)
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
    cardRankPlayerA = x[:-1]
    cardRankPlayerB = y[:-1]
    cardSuitPlayerA = x[-1:]
    cardSuitPlayerB = y[-1:]
    cardSuitPlayerAIndex = deckDict["Suits"].index(cardSuitPlayerA)
    cardSuitPlayerBIndex = deckDict["Suits"].index(cardSuitPlayerB)
    cardValuePlayerA = deckDict["Values"][indexInDict(cardRankPlayerA)]
    cardValuePlayerB = deckDict["Values"][indexInDict(cardRankPlayerB)]
    if int(cardValuePlayerA) > int(cardValuePlayerB):
        playerACards.insert(0, x)
        playerACards.insert(0, y)
        print "%s wins this round with %s vs %s" % (playerA, x, y)
        return playerACards
    elif int(cardValuePlayerB) > int(cardValuePlayerA):
        playerBCards.insert(0, x)
        playerBCards.insert(0, y)
        print "%s wins this round with %s vs %s" % (playerB, y, x)
        return playerBCards
    elif int(cardValuePlayerA) == int(cardValuePlayerB):
        if cardSuitPlayerAIndex < cardSuitPlayerBIndex:
            playerACards.insert(0, x)
            playerACards.insert(0, y)
            print "%s wins this round with %s vs %s" % (playerA, x, y)
            return playerACards
        else:
            playerBCards.insert(0, x)
            playerBCards.insert(0, y)
            print "%s wins this round with %s vs %s" % (playerB, y, x)
            return playerBCards


def play():
    playerA, playerB = getPlayersNames()
    print "Hello {p1} and {p2}.".format(p1=playerA, p2=playerB) \
          + " Are you ready to play?" \
          + " Press Y for yes or N for No"
    userResponse = raw_input("> ")
    if userResponse == "Y":
        deckOfCards = createDeck()
        (playerACards, playerBCards) = dealCards(deckOfCards)
        rounds = 0
        while (len(playerACards) > 0 and len(playerBCards) > 0):
            (playerAPick, playerBPick) = pickCards(playerACards, playerBCards)
            bestCard(playerA, playerB, playerAPick,
                     playerBPick, playerACards, playerBCards)
            rounds += 1
        if len(playerACards) == 0:
            print "%s won after %s rounds" % (playerB, rounds)
        else:
            print "%s won after %s rounds" % (playerA, rounds)
    else:
        print "Oh well, another time maybe"
    return rounds


def playForScripting():
    (playerA, playerB) = ("Josephine", "X")
    userResponse = "Y"
    if userResponse == "Y":
        deckOfCards = createDeck()
        (playerACards, playerBCards) = dealCards(deckOfCards)
        rounds = 0
        while (len(playerACards) > 0 and len(playerBCards) > 0):
            (playerAPick, playerBPick) = pickCards(playerACards, playerBCards)
            bestCard(playerA, playerB, playerAPick,
                     playerBPick, playerACards, playerBCards)
            rounds += 1
        if len(playerACards) == 0:
            print "%s won after %s rounds" % (playerB, rounds)
        else:
            print "%s won after %s rounds" % (playerA, rounds)
    else:
        print "Oh well, another time maybe"
    return rounds


if __name__ == "__main__":
    play()
