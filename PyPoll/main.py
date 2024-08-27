import os
import csv

# set variables
total_votes = 0
candidate = ""
votes_for_candidate = {} # dictionary for name of canidate
winning_votes = 0
winner = ""

# relative directory path
script_dir = os.path.dirname(__file__)

# Join the current directory with the relative directory
election_csv = os.path.join(script_dir,'/Users/carmendee/Desktop/python-challenge/PyPoll/Resources/election_data.csv')

# Open the CSV file in read mode
with open(election_csv, 'r') as csvfile:
    
# Create a CSV reader object
    csv_reader = csv.reader(csvfile)

# Skip the header row (if present)
    next(csv_reader)

# Process each row after skipping the header
    for row in csv_reader:
        
        # candidates name
        candidate = row[2]
        
        # Calculate votes for each candidate
        if candidate in votes_for_candidate:
            votes_for_candidate[candidate] += 1
        else: 
            votes_for_candidate[candidate] = 1
        
        # Calculate total votes
        total_votes += 1
        
# Print out the results
print(f"-----------------------------------------")
print(f"Election Results")
print(f"-----------------------------------------")
print(f"Total Votes: {total_votes:,}")
print(f"-----------------------------------------")


# Find the winner of the election
for candidate, votes in votes_for_candidate.items():
    if votes > winning_votes:
        winner = candidate
        winning_votes = votes
        
print(f"Winner: {winner}")
print(f"-------------------------------------------")

# Join the current directory with the relative directory
results_output = os.path.join(script_dir, '/Users/carmendee/Desktop/python-challenge/PyPoll/Resources/election_data.csv')

# Write the results into the PyPoll Election Results.txt file
with open(results_output, "w") as output_csv_file:
    output_csv_file.write("Election Results\n")
    output_csv_file.write("--------------------------------------------\n")
    output_csv_file.write(f"Total Votes: {total_votes:,}\n")
    output_csv_file.write("--------------------------------------------\n")

    for candidate, votes in votes_for_candidate.items():
        vote_percentage = round((votes / total_votes) * 100, 2)
        output_csv_file.write(f"{candidate}: {vote_percentage:.2f}% ({votes:,})\n") 
        
    output_csv_file.write("--------------------------------------------\n") 

    output_csv_file.write(f"Winner: {winner}\n")
    
    output_csv_file.write("--------------------------------------------\n")
