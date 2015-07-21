
# to make a game of hangman we first need to generate a random word and now display it, intead we need to display a select (and random) set of letters, and dashes for the missing letters.
# players should also be able to know which letters they have tried to guess already and which ones are left. That will come in a V2
# if a player guesses a letter then we show all the letters he guessed.

import random

wordList = ["banana", "elephant", "music", "computer"] # populating a list with words we'll randomly pick

randWord =  wordList[random.randrange(len(wordList))]
alphabet = [n for n in 'abcdefghijklmnopqrstuvwxyz']
randWordDisplayed = "-" * len(randWord)

print randWord
print randWordDisplayed


# write a function that takes the user input for 10 turns, gives results to the user, and eventually when the turn is over print the restuls

def resultCheck():
	results = [n for n in randWordDisplayed] # placeholder of the word with the dashes and the random letter
	guessedLetters = []
	turn = 0
	while turn <=5:
		userGuess = raw_input("Pick a letter from the alphabet")
		if str.lower(userGuess) not in alphabet:
			print "Pick a letter from the alphabet"
		elif str.lower(userGuess) in guessedLetters:
			print "you've already done this one, try another letter"
		elif str.lower(userGuess) in [n for n in randWord]:
			guessedLetters.append(str.lower(userGuess))
			print "this is a correct letter!"
			for x in range(len(results)):
				if [n for n in randWord][x] == str.lower(userGuess):
					results[x] =  str.lower(userGuess)
			turn += 1
			if [n for n in results] == [n for n in randWord]:
				turn = 11
				print "Congrats you guess the word", "".join(results)
			else:
				print "word to guess: ", "".join(results)
		else:
			guessedLetters.append(str.lower(userGuess))
			print "this is an incorrect letter,  you have: ", 5 - turn, "turns left"
			print "word to guess: ", "".join(results)
			turn += 1


print resultCheck()




