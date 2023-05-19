import csv
import os

file_path = os.path.expanduser("~/Desktop/Python Challenge/PyPoll/Resources/election_data.csv")

# with open(file_path, 'r') as file:
#     csv_reader = csv.reader(file)
#     for row in csv_reader:
#         print(row)


votes = 0
winner_votes = 0
total_candidates = 0
greatest_votes = ["", 0]
candidate_options = []
candidate_votes = {}


with open(os.path.expanduser("~/Desktop/Python Challenge/PyPoll/Resources/election_data.csv")) as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        votes = votes + 1
        total_candidates = row["Candidate"]        

        if row["Candidate"] not in candidate_options:
            
            candidate_options.append(row["Candidate"])

            candidate_votes[row["Candidate"]] = 1
            
        else:
            candidate_votes[row["Candidate"]] = candidate_votes[row["Candidate"]] + 1

    # Determine the Winner:
    if (votes > winner_votes):
        greatest_votes[1] = candidate_votes
        greatest_votes[0] = row["Candidate"]
    
    
    print("Election Results")
    print("-------------------------")
    print("Total Votes " + str(votes))
    print("-------------------------")
#results
    for candidate in candidate_votes:
        print(candidate + " " + str((((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
        candidate_results = (candidate + " " + str((((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
    
candidate_votes

winner = sorted(candidate_votes.items(), key=lambda x: -x[1])
print(winner)
#results
print("-------------------------")
print("Winner: " + str(winner[0][0]))
print("-------------------------")



# Output Files
with open(os.path.expanduser("~/Desktop/Python Challenge/PyPoll/Analysis/result.txt"), "w") as txt_file:
    
    txt_file.write("Election Results")
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write(candidate + " " + str((((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")")
    txt_file.write(str(winner))
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write("Winner: " + str(winner[1]))
    txt_file.write("\n")
    txt_file.write("Total Votes " + str(votes))