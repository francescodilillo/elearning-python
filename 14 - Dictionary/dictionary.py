################################################################################
# 
# Author: francescodilillo
# Purpose: practice with dictionaries
# Last Edit Date: 18-03-2020
#
#
################################################################################

person = {"name": "Francesco", "gender": "M", "age": 27, "address": "15 Rue de Ville, Luxembourg", "phone": 34566112233}

request = input("What info would you need to learn about the person? ").lower()

output = person.get(request, "The request can't be fulfilled since there is no field " + request)

print(request, ": ", output)