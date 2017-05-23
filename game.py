"""A number-guessing game."""

import random

name = raw_input("What's your name?")
print "%s, welcome to the guessing game." % (name)
number = random.randint(1, 100)
print number
while True:
    print number

    guess = raw_input("Guess a number between 1 and 100.")
    print int(guess)
    if guess > number:
        print "Guess is too high. Try again."
    elif guess < number:
        print "Guess is too low. Try again."