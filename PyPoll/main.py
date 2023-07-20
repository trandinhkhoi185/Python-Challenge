import os
import csv
cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))



# Read the election data from the CSV file
with open('election_data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row

    total_votes = 0
    candidates = {}

    for row in reader:
        candidate = row[2]
        total_votes += 1
        candidates[candidate] = candidates.get(candidate, 0) + 1

# Calculate the percentage of votes each candidate won
results = []
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    results.append((candidate, percentage, votes))

# Find the winner based on popular vote
winner = max(results, key=lambda x: x[2])

# Print the analysis results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, percentage, votes in results:
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner[0]}")
print("-------------------------")
