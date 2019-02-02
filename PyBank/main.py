# # PyBank
# ![Revenue](Images/revenue-per-lead.jpg)
#   * In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)
#   * Your task is to create a Python script that analyzes the records to calculate each of the following:
#   * The total number of months included in the dataset
#   * The net total amount of "Profit/Losses" over the entire period
#   * The average of the changes in "Profit/Losses" over the entire period
#   * The greatest increase in profits (date and amount) over the entire period
#   * The greatest decrease in losses (date and amount) over the entire period
#   * As an example, your analysis should look similar to the one below:

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


print("Financial Analysis")
print("------------------------------")
total_months = pybank['Date'].count()
print(f"Total Months: {total_months}")
total_amount = pybank['Profit/Losses'].sum()
print(f"Total: ${total_amount}")
# average_change = round(pybank['Profit/Losses'].mean(), 2)
# print(f"Average Change: ${average_change}")

# This block of code converts the Date column into the index
pybank.index = pybank['Date']
pybank2 = (pybank['Profit/Losses'].astype(int))
pybank2_index = (pybank['Date'])

# Extracts the profit/loss column into a series and assigns it to the following variable
# Create a list that will hold the change values
profit_losses_series = []
profit_losses_index = []
i = 1
for i in range(len(pybank2)-1):
    first_val = pybank2[i]
    second_val = pybank2[i + 1]
    index_val2 = pybank2_index[i + 1]
    change_value = second_val - first_val
    profit_losses_series.append(change_value)
    profit_losses_index.append(index_val2)

# Calculate the average change in the list using numpy mean and then rouding to 2 decimals
average_change = round(np.mean(profit_losses_series),2)
print(f"Average  Change: ${average_change}")

# Determines the date that had the highest change in profit that is stored in the series
max_change_in_profit = max(profit_losses_series)
# Determine the corresponding index (date) that had the highest change in profit
max_change_index = profit_losses_series.index(max_change_in_profit)
maxDate = profit_losses_index[max_change_index]
print(f"Greatest Increase in Profits: {maxDate} (${max_change_in_profit})")

# Determine the date that had the greatest loss of profit stored in the profit loss series
min_change_in_profit = min(profit_losses_series)
min_change_index = profit_losses_series.index(min_change_in_profit)
minDate = profit_losses_index[min_change_index]
print(f"Greatest Decrease in Profits: {minDate} (${min_change_in_profit})")

pybank.to_csv('pybank_result.txt', header = None, sep = ' ', mode = 'a')