
import pandas as pd
import numpy as np

pybank = pd.read_csv("PyBank.csv", header = 'infer', parse_dates=False)

print("Financial Analysis")
print("------------------------------")
total_months = pybank['Date'].count()
print(f"Total Months: {total_months}")
total_amount = pybank['Profit/Losses'].sum()
print(f"Total: ${total_amount}")
average_change = round(pybank['Profit/Losses'].mean(), 2)
print(f"Average Change: ${average_change}")
profit_losses_series = (pybank['Profit/Losses'])

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

pybank.to_csv('pybank_result_with_just_pandas.txt', header = None, sep = ' ', mode = 'a')