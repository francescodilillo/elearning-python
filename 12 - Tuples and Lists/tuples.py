################################################################################
# 
# Author: francescodilillo
# Purpose: Given a birthdate, it returns the month
# Last Edit Date: 15-03-2020
#
#
################################################################################

months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

birthdate = input("Please insert your birthdate in the format DD-MM-YYYY: ")
month_index = int(birthdate[3:5])

print("You were born in: ", months[month_index-1])