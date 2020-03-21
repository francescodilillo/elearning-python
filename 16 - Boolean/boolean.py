################################################################################
# 
# Author: francescodilillo
# Purpose: practice with boolean and conditions
# Last Edit Date: 19-03-2020
#
#
################################################################################

age = 27

oAge = float(input("How old are you? "))

if(age < oAge):
	print("You are older than me!")
elif(age == oAge):
	print("We have the same age!")
else:
	print("I'm older than you!")