# Python-Challenge

We were given 2 datasets: PyBank and PyPoll and instructed to write a Python script that outputs the following. 

For the PyBank: 
- The total number of months included in the dataset
- The net total amount of "Profit/Losses" over the entire period
- The changes in "Profit/Losses" over the entire period, and then the average of those changes
- The greatest increase in profits (date and amount) over the entire period
- The greatest decrease in profits (date and amount) over the entire period

For the PyPoll: 
- The total number of votes cast
- A complete list of candidates who received votes
- The percentage of votes each candidate won
- The total number of votes each candidate won
- The winner of the election based on popular vote

The following code was written with the help of TA's from office hours: 

winner = sorted(candidate_votes.items(), key=lambda x: -x[1])
print(winner)
#results
print("-------------------------")
print("Winner: " + str(winner[0][0]))
print("-------------------------")

 #The greatest increase in revenue (date and amount) over the entire period
        if revenue_change>greatest_increase[1]:
            greatest_increase[1]= revenue_change
            greatest_increase[0] = row['Date']

        #The greatest decrease in revenue (date and amount) over the entire period
        if revenue_change<greatest_decrease[1]:
            greatest_decrease[1]= revenue_change
            greatest_decrease[0] = row['Date']
    changes.pop(0)
    average_change = (sum(changes)) / (len(changes))
    
