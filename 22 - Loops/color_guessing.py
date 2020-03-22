################################################################################
# 
# Author: francescodilillo
# Purpose: Color guessing game
# Last Edit Date: 22-03-2020
#
#
################################################################################

import random

colors = ['red', 'yellow', 'blue', 'orange', 'pink', 'green', 'violet']

selector = 'yes'

while selector == 'yes':

	print("Your possible choices are: ", colors)
	choice = ''
	winner = colors[random.randint(0, len(colors)-1)]

	while winner != choice:

		choice = input("Try to guess the color: ")

		if winner == choice:

			print("CONGRATULATIONS! You won, you guessed the right color!")

		else:

			print("Sorry, you lost! Try again to guess the color!")

	selector = str.lower(input("Do you want to play again? [yes/no] "))


print("Thank you for playing!")

