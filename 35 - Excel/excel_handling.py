################################################################################
# 
# Author: francescodilillo
# Purpose: practice with Pandas and Excel file
# Last Edit Date: 29-03-2020
#
#
################################################################################

import pandas as pd

file = pd.ExcelFile("./sales.xlsx")

print("The sheet names are:", file.sheet_names)

sales = file.parse('sales')

print(sales) 					# sheet data

print(sales.Date) 				# print only one column

print(sales.Amount.sum())		# calculate the column sum

print(sales.loc[3])				# print 3rd record

print(sales.loc[3, "Amount"])	# print only the amount of 3rd record

sales.set_index("Customer", inplace = True)		# set an index
print(sales.loc['MMC Inc.'])					# find all the rows corresponding to this customer
sales = sales.reset_index()						# reset the index

print(sales.loc[sales["Amount"]>2000])

print(sales.loc[sales["Amount"] > 1800]["Customer"].unique())