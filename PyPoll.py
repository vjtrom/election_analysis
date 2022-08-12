#Overview - Who won the election
#   Pull in the data - might be more than one file
#   Cleanse and order the data as needed
#   Identify the data fields needed to perform the objective - candidates ranking
#   Data input needed:
#       total votes cast
#       list of candidtates
#       total numbe of votes each candidiate received
#   Data output:
#       total num of votes each candidate received as a percentage of total votes cast
#       proper formatting
#
# Begin Coding

x = "hello"
print(x)

# # Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Create candidate options list
candidate_options = []

# Declare a 'votes' dictionary
candidate_votes = {}

# Track the winning candidate, vote count, and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0.00

# # # Open the election results and read the file.
election_data = open(file_to_load, 'r')
#with open(file_to_load) as election_data:
file_reader = csv.reader(election_data)

# Read the header row.
headers = next(file_reader)
print(headers)

# Print each row in the CSV file.
for row in file_reader:

   # Add to the total vote count.
    total_votes += 1

# Get the candidiate_name from each row.
    candidate_name = row[2]

# If the candidate does not match any existing candidate...
    if candidate_name not in candidate_options:

        # add it to the list of candidates.
        candidate_options.append(candidate_name)

# Begin tracking the candidate's vote count
        candidate_votes[candidate_name] = 0

#Add a vote to that candidate's count
    candidate_votes[candidate_name] += 1

# Save the results to our text file.
txt_file = open(file_to_save, 'w')
#with open(file_to_save, "w") as txt_file:

election_results = ("\n"
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
         
print(election_results, end="")

# Save the final vote count to the text file.
txt_file.write(election_results)

    # #Iterate through the candidate list
for candidate_name in candidate_votes:

    # # Retreive vote count of a candidate.

        votes = candidate_votes[candidate_name]

    # calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

    # print(f"{candidate_name}: received {vote_percentage}% of the vote.")
    # print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print the winning candidates' results to the terminal.

    # winning_candidate_summary = (
    #     f"-------------------------\n"
    #     f"Winner: {winning_candidate}\n"
    #     f"Winning Vote Count: {winning_count:,}\n"
    #     f"Winning Percentage: {winning_percentage:.1f}%\n"
    #     f"-------------------------\n")
