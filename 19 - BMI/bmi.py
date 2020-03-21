################################################################################
# 
# Author: francescodilillo
# Purpose: Calculate BMI given weight and height
# Last Edit Date: 21-03-2020
#
#
################################################################################

print("This program will ask you your weight and height in order to calculate your BMI")
altFlag = str.lower(input("Are you going to input weight in kg and height in m? [y/n/exit] "))

if(altFlag == 'y' or altFlag == 'n'):

	weight = round(float(input("Please input your weight: ")),2)
	height = round(float(input("Please input your height: ")),2)

	if(altFlag == 'y'):

		BMI = round(weight/(height**2),2)

	else:

		BMI = round((weight/(height**2)) * 703,2)	

	if(BMI <= 18.5):

		category = 'Underweight'

	elif(18.5 < BMI <= 24.9):

		category = 'Normal weight'

	elif(24.9 < BMI <= 29.9):

		category = 'Overweight'

	else:

		category = 'Obesity'

	print("Your weight is: ", weight, " your height is: ", height, "Your BMI is ", BMI, " and your category is ", category)

else:

	print("Program exited successfully")