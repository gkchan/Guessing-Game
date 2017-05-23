"""A number-guessing game."""

import random

name = raw_input("What's your name?")
print "%s, welcome to the guessing game." % (name)
number = random.randint(1,100)
