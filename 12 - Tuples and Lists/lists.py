################################################################################
# 
# Author: francescodilillo
# Purpose: Append a user to a list
# Last Edit Date: 15-03-2020
#
#
################################################################################

user_list = ['User 1', 'User 2', 'User 3']

new_user = [input('Please insert your login: ')]

final_list = user_list + new_user

print("The final list of users is: ", final_list)