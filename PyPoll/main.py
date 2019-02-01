# PyPoll
# In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)
# You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:


# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

# As an example, your analysis should look similar to the one below:
#   ```text
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
#   ```
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("PyPoll.csv", header = 'infer')
# print(df.columns)

print("Election Results")
print("-------------------------")
# Calculate the total number of votes
total_votes = df['Voter ID'].count()
print(f"Total Votes: {total_votes}")
print("-------------------------")
# print the percent of voters to the candidate khan
khan_candidate_as_true = df['Candidate'] == 'Khan'
# Create a df with only Khan
khan_df = df[khan_candidate_as_true]
# Count the number of votes Khan received
khan_votes = khan_df['Voter ID'].count()
khan_percent_votes = round(khan_votes / total_votes * 100.0, 3)
print(f"Khan: {khan_percent_votes}% ({khan_votes})")

# print the percent of voters to the candidate Correy
Correy_candidate_as_true = df['Candidate'] == 'Correy'
# Create a df with only Correy
Correy_df = df[Correy_candidate_as_true]
# Count the number of votes Correy received
Correy_votes = Correy_df['Voter ID'].count()
Correy_percent_votes = round(Correy_votes / total_votes * 100.0, 3)
print(f"Correy: {Correy_percent_votes}% ({Correy_votes})")

# print the percent of voters to the candidate Li
Li_candidate_as_true = df['Candidate'] == 'Li'
# Create a df with only Li
Li_df = df[Li_candidate_as_true]
# Count the number of votes Li received
Li_votes = Li_df['Voter ID'].count()
Li_percent_votes = round(Li_votes / total_votes * 100.0, 3)
print(f"Correy: {Li_percent_votes}% ({Li_votes})")

# print the percent of voters to the candidate O'Tooley
OTooley_candidate_as_true = df['Candidate'] == "O'Tooley"
# Create a df with only  O'Tooley
OTooley_df = df[OTooley_candidate_as_true]
# Count the number of votes  O'Tooley received
OTooley_votes = OTooley_df['Voter ID'].count()
OTooley__percent_votes = round(OTooley_votes / total_votes * 100.0, 3)
print(f"Correy: {OTooley__percent_votes}% ({OTooley_votes})")
print("-------------------------")

# Determine the winner of the popular vote by using a dictionary method
popular_vote_dict = {"Khan" : khan_votes, "Correy" : Correy_votes, "Li" : Li_votes, "O'Tooley" : OTooley_votes}
max_key = max(popular_vote_dict, key = lambda k: popular_vote_dict[k])
print(f"Winner: {max_key}")
print("-------------------------")
