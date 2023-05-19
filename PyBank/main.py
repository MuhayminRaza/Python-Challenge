#import modules
import csv
import os

file_path = os.path.expanduser("~/Desktop/Python Challenge/PyBank/Resources/budget_data.csv")

# with open(file_path, 'r') as file:
#     csv_reader = csv.reader(file)
#     for row in csv_reader:
#         print(row)

#set the output of the text file
text_path = "output.txt"

#Set variables
total_months = 0
total_revenue = 0
revenue = []
previous_revenue = 0
month_of_change = []
revenue_change = 0
greatest_decrease = ["", 9999999]
greatest_increase = ["", 0]
revenue_change_list = []
revenue_average = 0

# Read Files
with open(os.path.expanduser("~/Desktop/Python Challenge/PyBank/Resources/budget_data.csv")) as csvfile:
    reader = csv.DictReader(csvfile)

    # loop through rows and add up the total months and profit losses 
    changes = []
    for row in reader:
        
        total_months = total_months + 1
        total_revenue = total_revenue + float(row["Profit/Losses"])
        # print(row)

         #Calculate the average change in revenue between months over the entire period
        revenue_change = float(row["Profit/Losses"]) - previous_revenue
        previous_revenue = float(row["Profit/Losses"])
        revenue_change_list += [revenue_change]
        month_of_change += [row["Date"]]
    
        changes += [revenue_change]

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
    
    # Show Output
    print("Financial Analysis")
    print("-------------------------------")
    print("Total Months: " + str(total_months))
    print(f"Total Months: {total_months}")
    print("Total : " + "$" + str(total_revenue))
    print("Average Change: " + "$" + str(round(average_change, 2)))
    print("Greatest Increase: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")") 
    print("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")
    

# Output Files
with open(os.path.expanduser("~/Desktop/Python Challenge/PyBank/Analysis/result.txt"), "w") as txt_file:
    txt_file.write("Total Months: " + str(total_months))
    txt_file.write("\n")
    txt_file.write("Total: " + "$" + str(total_revenue))
    txt_file.write("\n")
    txt_file.write("Average Change: " + "$" + str(round(sum(revenue_change_list) / len(revenue_change_list),2)))
    txt_file.write("\n")
    txt_file.write("Greatest Increase: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")") 
    txt_file.write("\n")
    txt_file.write("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")")
