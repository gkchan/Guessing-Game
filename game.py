"""A number-guessing game."""

import random

tries = 0

name = raw_input("What's your name?")
print "%s, welcome to the guessing game." % (name)
number = random.randint(1, 100)
#print number
while True:
    #print number

    guess = int(raw_input("Guess a number between 1 and 100."))
    #print int(guess)
    tries += 1
    if guess > 100 or guess < 1:
        print "Please enter a number between 1 and 100."
    elif guess > number:
        print "Guess is too high. Try again."
    elif guess < number:
        print "Guess is too low. Try again."
    elif guess == number:
        print "Congrats! %s, you guessed the number!" % (name)
        print "It took you {} tries!" .format(tries)
    else:
        print "Error"
        