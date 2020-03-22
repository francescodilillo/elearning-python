################################################################################
# 
# Author: francescodilillo
# Purpose: Stores 8 names in a list, pick and print a random one
# Last Edit Date: 22-03-2020
#
#
################################################################################

import random

people = []

while len(people) < 8:

	people.append(input("Please insert the name of the next person: "))

print("The list is: ", people)


index = random.randint(0,7)

print("I picked randomly the number ", index, " which name is: ", people[index])