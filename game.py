"""A number-guessing game."""

import random
import math
    

tries = 0

name = raw_input("What's your name?")
print "%s, welcome to the guessing game." % (name)
number = random.randint(1, 100)
#print number
while True:
    #print number
    try:
        if guess_1.isdigit
            guess_1 = raw_input("Guess a number between 1 and 100.")
        if guess_1 != 
            guess_2 = math.floor(guess_1)
            print "If your number is not an integer we are rounding it down!"
        else:
            print "Error"
    except TypeError:
        print "Please enter an integer between 1 and 100."
        continue
    tries += 1
    # if guess_2 > 100 or guess_2 < 1:
    #     print "Please enter a number between 1 and 100."
    # elif guess_2 > number:
    #     print "Guess is too high. Try again."
    # elif guess_2 < number:
    #     print "Guess is too low. Try again."
    # else:
    #     print "Congrats! %s, you guessed the number!" % (name)
    #     print "It took you {} tries!" .format(tries)
   