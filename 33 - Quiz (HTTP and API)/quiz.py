################################################################################
# 
# Author: francescodilillo
# Purpose: Quiz game connected to Open Trivia API
# Last Edit Date: 26-03-2020
#
#
################################################################################

import requests
import json
import random

def print_answers(opt_dictionary):

	index = 0
	while(index < 4):
		print(index+1, "-", opt_dictionary[index+1])
		index += 1

def incr_challenge(score):

	if score == 3:

		return 'medium'

	elif score == 7:

		return 'hard'


print("==================== Welcome to the QUIZ game ====================")
print("= You will be challenged with questions of increasing difficulty =")
input("+++ Press enter to start +++")

termination = False
score = 0
difficulty = 'easy'

while(termination == False):

	r = requests.get("https://opentdb.com/api.php?amount=1&difficulty="+difficulty+"&type=multiple")
	if(r.status_code != 200):

		print("There was an error with the connection to the database. Please restart the program.")
		termination = True

	else:
		
		print(" ")
		print(">>>> To answer the question, select the correct answer number")

		question = json.loads(r.text)['results'][0]
		options = question['incorrect_answers']+[question['correct_answer']]
		random.shuffle(options)
		indices = [1,2,3,4]

		print(question['question'].replace('&quot;','"').replace('&#039;',"'"))

		opt_dictionary = {indices[i]: options[i] for i in range(len(options))}

		print_answers(opt_dictionary)

		data_valid = False

		while(data_valid == False):
			try:
				
				user_answer = int(input("Make your selection by selecting the answer number: "))
				data_valid = True

			except:

				print("ERROR: Please provide a number between 1 and 4")

		if opt_dictionary[user_answer] == question['correct_answer']:

			score += 1
			print("Congratulation, correct!")

		else:
		
			print("Nope! The right answer was:", question['correct_answer'])	

		print("Your current score is:", score)	

		data_valid = False

		while(data_valid == False):

			cont = str.lower(input("Do you want to continue? [y/n]: "))

			if cont == 'y':

				termination = False
				data_valid = True

				if (difficulty == 'easy' and score == 3) or (difficulty == 'medium' and score == 7):
					print("SYSTEM: Let's bring the challenge to the next level!") 
					difficulty = incr_challenge(score)

			elif cont == 'n':

				termination = True
				data_valid = True
				print('Your final score is', score, '. Thank you for playing!')

			else:

				print('Only y or n are allowed answers.')
