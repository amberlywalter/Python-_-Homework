
#import module
import os
#import csv module
import csv


csvpath = "/Users/amberlywalter/Python_Homework/Pypoll/Resources/election_data.csv"
output_path = "/Users/amberlywalter/Python_Homework/Pypoll/Analysis/Poll_data_results.txt"

#variable list
total_vote = 0
voters = {}

#read header of first row
with open(csvpath) as poll_data:
    csvreader = csv.reader(poll_data, delimiter=',')
    #skip header
    data_header = next(csvreader)
    data = list(csvreader)
    #Loop for total votes
    Vote_count = 0
    for row in data:
        Vote_count += 1
    total_vote = Vote_count
    list_of_candidates = []
    #loop for storing candidates names
    for row in data:
        if row[2].strip() not in list_of_candidates:
            list_of_candidates.append(row[2])
    voters = {}
    #loop for storing votes for each candidate
    for name in list_of_candidates:
        votes = 0
        for row in data:
            if row[2].strip() == name:
                votes +=1
        voters[name]=votes
    
    #prints data
    output = ""
    output += f"Election Results\n"
    output += f"-----------------------------\n"
    output += f"Total Votes: {total_vote}\n"
    output += f"-----------------------------\n"
    #loops for printing percentages with candidates
    for name, votes in voters.items():
        vote_percentage = ((votes) / (total_vote))*100
        name_and_votes = f'{name}: {vote_percentage:.3f}% ({votes})'
        output += f"{name_and_votes}\n"
    winner_vote = max(voters.values())
    winner = list(voters.keys())[list(voters.values()).index(winner_vote)]
    output += f"-----------------------------\n"
    output += f"Winner: {winner}\n"
    output += f"-----------------------------\n"
    print (output)

#create txt file
with open(output_path, mode="w") as poll_output:
    poll_output.write(output)
   
        