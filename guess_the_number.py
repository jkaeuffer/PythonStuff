# Guess the number game
''' step 1: generates a random number and store it. step 2: have the user guess a number. 
step 3: decide whether it's higher, or lower. step 4 tell the user when they win '''

import random
# generate a random number

number_to_guess = random.randrange(0,501)

# ask the user to guess the number

def user_guess():
	number_guessed = int(raw_input("Enter a number:"))
	print "Your guess is %s" % number_guessed
	return number_guessed

#check against the actual number

def check_guess():
	user = user_guess()
	if user > number_to_guess:
		return "Lower"
	elif user < number_to_guess:
		return "Higher"
	else:
		return "Correct"

#print check_guess()

#play the game
def play_game():
	turns = 0
	print "You have %s turns left" % (10 - turns)
	for n in range(0,11):
		print "This is turn %s" % turns
		result = check_guess()
		#print "Your guess is %s" % user_guess()
		turns += 1
		print result
		if result == "Correct":
			print "congrats you won"
			break
	print "you lost, the result was %s" % number_to_guess

play_game() 


