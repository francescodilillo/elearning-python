################################################################################
# 
# Author: francescodilillo
# Purpose: Use error handling and data validation into the example from the past units
# Last Edit Date: 22-03-2020
#
#
################################################################################

validExam1 = False
validExam2 = False
validClasses = False
validAbs = False

try:

	while validExam1 == False:

		exam1 = float(input("Insert the score for the first exam: "))

		if 0.0 <= exam1 <= 10.0:

			validExam1 = True

		else:

			print('The score has to be between 0 and 10.')


	try:

		while validExam2 == False:

			exam2 = float(input("Insert the score for the second exam: "))

			if 0.0 <= exam2 <= 10.0:

				validExam2 = True

			else:

				print('The score has to be between 0 and 10.')

		try:

			while validClasses == False:

				classes = int(input("Insert the total number of classes: "))

				if classes>=0:

					validClasses = True

				else:

					print('The number of classes has to be greater than 0.')


			try:

				while validAbs == False:

					absences = int(input("Insert the total number of absences: "))

					if absences >= 0 and absences <= classes:

						validAbs = True

					else:

						print('The number of absences has to be greater than 0 and less than', classes)

				avgGrade = round((exam1+exam2)/2,2)
				attendance = (classes-absences)/classes

				print("The average grade is:", avgGrade)
				print("The attendance is:", attendance)

				if avgGrade >= 6 and attendance >= 0.8:
					print("The student has been approved")
				elif avgGrade < 6 and attendance < 0.8:
					print("The student failed due to", avgGrade, "not being sufficient and attendance (",attendance,") less than 80%")
				elif avgGrade < 6 and attendance > 0.8:
					print("The student failed due to", avgGrade, "not being sufficient")
				else:
					print("The student failed due to attendance (",attendance,") less than 80%")

			except:

				print('The number of absences is not a valid number.')


		except:

			print('The number of classes is not a valid number')


	except:

		print("The second score is not a valid number")

except:

	print("The first score is not a valid number")