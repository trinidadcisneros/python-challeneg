# # PyBank

# ![Revenue](Images/revenue-per-lead.jpg)

# * In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

# * Your task is to create a Python script that analyzes the records to calculate each of the following:

#   * The total number of months included in the dataset

#   * The net total amount of "Profit/Losses" over the entire period

#   * The average of the changes in "Profit/Losses" over the entire period

#   * The greatest increase in profits (date and amount) over the entire period

#   * The greatest decrease in losses (date and amount) over the entire period

# * As an example, your analysis should look similar to the one below:

#   ```text
#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)
#   ```

# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.

import pandas as pd
import numpy as np

pybank = pd.read_csv("PyBank.csv", header = 'infer', parse_dates=False)

# # print(pybank)

# max_profit = pybank['Profit/Losses'].max()
# # max_index = pybank.loc[max_profit]

# index = pybank['Profit/Losses'] == 1170593
# print(f"Greatest Increase in Profits: (${max_profit})")

print("Financial Analysis")
print("------------------------------")
# print the total number of months
total_months = pybank['Date'].count()
print(f"Total Months: {total_months}")
# # print the sum of column 'profit/losses'
# total = pybank['Profit/Losses'].sum()
# print(f"Total: ${total}")

# # Identify the index that Date = Feb-2012
feb2012_increase = pybank['Date'] == 'Feb-2012'
# print(feb2012_increase)
# Determine the index

maximum_profit = pybank['Profit/Losses'].max()

date_of_max_profit = pybank['Profit/Losses'][pybank['Date'] == 'Feb-2012']
print(f"Greatest Increase in Profits: {date_of_max_profit} + (${maximum_profit})")

decreased_profit = pybank['Profit/Losses'].min()
date_of_decreased_profit = pybank['Profit/Losses'][pybank['Profit/Losses'] == decreased_profit]
print(f"Greatest Decrease in Profits : {date_of_decreased_profit} (${decreased_profit})")

pybank.to_csv('pybank_result.txt', header = None, sep = ' ', mode = 'a')