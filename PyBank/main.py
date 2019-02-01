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

pybank = pd.read_csv("PyBank.csv", header = 'infer', parse_dates=False)


print("Financial Analysis")
print("------------------------------")
total_months = pybank['Date'].count()
print(f"Total Months: {total_months}")
total_amount = pybank['Profit/Losses'].sum()
print(f"Total: ${total_amount}")
average_change = round(pybank['Profit/Losses'].mean(), 2)
print(f"Average Change: ${average_change}")

# This block of code converts the Date column into the index
pybank.index = pybank['Date']
pybank2 = pybank[['Profit/Losses']]


# Extracts the profit/loss column into a series and assigns it to the following variable
profit_losses_series = pybank2['Profit/Losses']

# The following block will determine the date with the greatest profit
# Determines which value in the profit/loss series has the highest value
max_profit = profit_losses_series.max()
# Determines the index (the date) of the max profit and assigns the value to the profit date variable
profit_date = str(profit_losses_series.index[profit_losses_series == max_profit].values)
# Since the output of profit date is a string in a list, the following 
# removes the brakets and quotation mark so that the date can be printed without these characters
formatted_profit_date = str(profit_date)[2:-2]
print(f"Greatest Increase in Profits: {formatted_profit_date} $({max_profit})")

# The following block will determine the date with the lowest profts
decreased_profit = profit_losses_series.min()
# Determines the index (the date) with the greatest loss of profit and assigns 
# the value to the profit decreased_profit_date variable
decreased_profit_date = str(profit_losses_series.index[profit_losses_series == decreased_profit].values)
# Formats date of decreased profit value so that the braket and quotation is not in the output
formatted_decreased_profit_date = str(decreased_profit_date)[2:-2]
print(f"Greatest Decrease in Profits: {formatted_decreased_profit_date} $({decreased_profit})")

pybank.to_csv('pybank_result.txt', header = None, sep = ' ', mode = 'a')