################################################################################
# 
# Author: francescodilillo
# Purpose: Measure the speed and count the errors of the user, then show him the chart
# Last Edit Date: 25-03-2020
#
#
################################################################################

import time as t
import matplotlib.pyplot as plt

def strdifference(str1, str2):
	outp = 0
	try:
		for i in range(len(str1)):
			outp+=int(str1[i] != str2[i])
	except:
			outp+= abs(len(str1) - len(str2))
	return outp

target = "ippopotamo"
performance = []
label = []
attempts = 0
errors = []

print("You will have to write the word", target,"for 5 times and you will see how much your speed improved.")
print("Press enter to start")

while(attempts < 5):

	t1 = t.time()
	uInput = input("> ")
	t2 = t.time()
	errors.append(strdifference(target, str.lower(uInput)))
	performance.append(round(t2-t1,2))
	label.append("Attempt " + str(attempts + 1))
	attempts+=1

if errors == 0:
	print("Well done! You didn't do any errors!")
else:
	print("You made", sum(errors),"mistakes during the exercise.")

plt.plot(label, performance, 'b', label='Performance in s') 
plt.plot(label, errors, 'r', label='Errors')
plt.xlabel('Attempts')
plt.ylabel('Values')
plt.legend(loc='lower right')
plt.title("Performance report")
plt.show()

