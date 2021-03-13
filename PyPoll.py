# Open data set, election_results.csv
# Complete the list of candidates who received votes
# Count the total number of votes cast
# The total number of votes each candidate received.
# The percentage of votes that each candidate received of the total vote.
# The winner of the election based receiving the majority of the vote total

import csv
import os

# Create a filename variable to a direct or indirect path to the results file to read from.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file to write to.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Open the elctions results to read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    print(headers)