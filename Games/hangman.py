import random

# Populating a list with words we'll randomly pick
wordList = ["banana", "elephant", "music", "computer"]
randWord = wordList[random.randrange(len(wordList))]
alphabet = [n for n in 'abcdefghijklmnopqrstuvwxyz']
randWordDisplayed = "-" * len(randWord)


def resultCheck():
    results = [n for n in randWordDisplayed]
    guessedLetters = []
    turn = 0
    turnLength = random.randrange(len(randWord), 20)
    print "You have a total of ", turnLength, "turns. Good luck!"
    while turn <= turnLength:
        userGuess = raw_input("Pick a letter from the alphabet ")
        if str.lower(userGuess) not in alphabet:
            print "Pick a letter from the alphabet "
        elif str.lower(userGuess) in guessedLetters:
            print "You've already done this one, try another letter "
        elif str.lower(userGuess) in [n for n in randWord]:
            guessedLetters.append(str.lower(userGuess))
            print "This is a correct letter! "
            for x in range(len(results)):
                if [n for n in randWord][x] == str.lower(userGuess):
                    results[x] = str.lower(userGuess)
            turn += 1
            if [n for n in results] == [n for n in randWord]:
                turn = turnLength
                print "Congrats you guess the word", "".join(results)
                return results
            else:
                print "Word to guess: ", "".join(results)
        else:
            guessedLetters.append(str.lower(userGuess))
            print "This is an incorrect letter," \
                  + " you have: %d" % (turnLength - turn) \
                  + "turns left"
            print "Word to guess: ", "".join(results)
            turn += 1


print resultCheck()
