print (" Welcome to Guess the Number! ")

import random
from random import randint
number = randint(1, 100)
guesses = 1
guess = int(input (" Guess a number between 1 and 100: "))

while guess !=number:
    if guess < number:
      print (" You need to guess higher. Try again ")
      guess = int(input(" \nGuess a number between 1 and 100: "))
      guesses = guesses + 1
    else:
      print (" You need to guess lower.Try again ")
      guess  = int(input(" \nGuess a number between 1 and 100: "))
      guesses = guesses + 1
  
