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


print("Welcome to the QUIZ game")
input("Press enter to start")

termination = False
score = 0

while(termination == False):

	r = requests.get("https://opentdb.com/api.php?amount=1&category=11&difficulty=easy&type=multiple")
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

		print(question['question'])

		opt_dictionary = {indices[i]: options[i] for i in range(len(options))}

		print_answers(opt_dictionary)

		termination = True



