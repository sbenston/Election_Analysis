# The data we need to retrieve.
# 1. The total number of votes casts
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save a file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0
# Initialize variables to hold candidate names and votes.
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open election results and read file.
with open(file_to_load) as election_data:

    # Read the file object with reader function.
    file_reader = csv.reader(election_data)
    
    # Read the header row.
    headers = next(file_reader)

    # Print each row in CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        
        # Print the candidate name from each row.
        candidate_name = row[2]

        # Test if unique
        if candidate_name not in candidate_options:
            # Add candidate_name to candidate_list.
            candidate_options.append(candidate_name)

            # Begin track that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add to vote count
        candidate_votes[candidate_name] += 1

# Determine percentage of votes for each candidate
# Interate thru candidate list
for candidate_name in candidate_votes:
    # Retieve votes of a candidate
    votes = candidate_votes[candidate_name]
    # Calculate percentage of vote count
    vote_percentage = (float(votes) / float(total_votes)) * 100
    # Print each using f-strings
    print(f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')

    # Determine winning vote count and candidate
    if (votes > winning_count) and (vote_percentage>winning_percentage):
        
        # if above expression true, set winning values to those values
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"----------------------\n"
    f"Winnner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"----------------------\n"
)
print(winning_candidate_summary)
