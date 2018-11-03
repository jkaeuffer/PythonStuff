import random

# This games takes a user's name and has them guess a randomly generated number


number_to_guess = random.randint(1, 10)


def get_user_name():
    name = raw_input("Hello! What is your name? ")
    print "Welcome " + name + "!"
    return name


user = get_user_name()

print "Well %s, I am thinking of a number between 1 and 10." % user

for guesses in range(6):
    user_guess = raw_input("Take a guess! ")
    try:
        user_guess = int(user_guess)
    except ValueError:
        print "Make sure to enter a number!"
        continue
    if user_guess == number_to_guess:
        print "Congrats! You have guessed my number in %d tries." % (guesses + 1)
        break

    elif user_guess > number_to_guess:
        print "Your guess is too high."

    else:
        print "Your guess is too low"

if user_guess != number_to_guess:
    print "Sorry, you lost! The number I was thinking of was %d." % number_to_guess





