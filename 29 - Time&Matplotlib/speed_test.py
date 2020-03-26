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
	limit = max([len(str1),len(str2)])
	try:
		for i in range(limit):
			outp+=int(str1[i] != str2[i])
	except:
			outp+= limit - i
	return outp

target = "ippopotamo"
performance = []
label = []
attempts = 0
errors = []

print("You will have to write the word", target,"for 5 times and you will see how much your speed improved.")
input("Press enter to start")

while(attempts < 5):

	t1 = t.time()
	uInput = input("> ")
	t2 = t.time()
	errors.append(strdifference(target, str.lower(uInput)))
	performance.append(round(t2-t1,2))
	label.append("Attempt " + str(attempts + 1))
	attempts+=1

if errors == 0:
	print("Well done! You didn't make any errors!")
else:
	print("You made", sum(errors),"mistakes during the exercise.")

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.set_xlabel('Attempts')
ax1.set_ylabel('Time (s)')
ax1.plot(label, performance, 'b', label='Performance') 
ax2.set_ylabel('Number of Errors')
ax2.plot(label, errors, 'r', label='Errors')

plt.title("Performance report")
plt.show()

