import csv
import os

election_csv = "Resources/election_data.csv"
ballot_column = []
county_column = []
candidate_column = []
total_votes = 0

count_charles = 0
count_diana = 0
count_raymon = 0

charles_percent = 0
diana_percent = 0
raymon_percent = 0
winner = 0

with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    for row in csvreader:
        ballot_column.append(row[0])
        county_column.append(row[1])
        candidate_column.append(row[2])
csvfile.close()

# Remove headers
ballot_column.pop(0)
county_column.pop(0)
candidate_column.pop(0)

#Make calculations for total votes
total_votes = len(ballot_column)
print(total_votes)


#List of candidates that received votes
# Iterate all votes 
for i in range(0, len(candidate_column)-1):
    if candidate_column[i] == "Charles Casper Stockham":
        count_charles = count_charles + 1
    elif candidate_column[i] == "Diana DeGette":
        count_diana = count_diana + 1
    elif candidate_column[i] == "Raymon Anthony Doane":
        count_raymon = count_raymon + 1

charles_percent = count_charles / total_votes
diana_percent = count_diana / total_votes
raymon_percent = count_raymon / total_votes

if (count_charles > count_diana) and (count_charles > count_raymon):
    winner = "Charles Casper Stockham"
elif (count_diana > count_charles) and (count_diana > count_raymon):
    winner = "Diana DeGette"
elif (count_raymon > count_charles) and (count_raymon > count_diana):
    winner = "Raymon Anthony Doane"

result = f"""
        Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
Charles Casper Stockham: {charles_percent:.3%} ({count_charles})
Diana DeGette: {diana_percent:.3%} ({count_diana})
Raymon Anthony Doane: {raymon_percent:.3%} ({count_raymon})
-------------------------
Winner: {winner}
-------------------------
    """

print(result)

# Specify the file path
file_path = "analysis/output.txt"

# Open the file in write mode ('w')
with open(file_path, 'w') as file:
    # Write the string to the file
    file.write(result)

print("Text saved to", file_path)






