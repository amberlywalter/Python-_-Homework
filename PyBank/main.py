#import os module
import os

#import csv module
import csv

csvpath = "/Users/amberlywalter/Python_Homework/PyBank/Resources/budget_data.csv"
output_path = "/Users/amberlywalter/Python_Homework/PyBank/Analysis/budget_data_results.txt"


#variables list

Month_Count = 0
Net_Total = 0
Change_Average = 0
Profit_for_month = 0
Name_of_month = ""
Monthly_Changes = []
Max_Change = 0 
Min_Change = 0
Max_Change_Month = ""
Min_Change_Month = ""

#read header of first row
with open(csvpath) as budget_data           :
    csvreader = csv.reader(budget_data)
    #skip header row
    data_header = next(csvreader)
    
    #reads each row after header and loops
    for row in csvreader:
        Profit_for_month = int(row[1])
        Name_of_month = row[0]
        #calculates number of months
        Month_Count = Month_Count + 1
        #calculates total
        Net_Total = Net_Total + Profit_for_month
        #Calculates monthly change 
        if Month_Count > 1:
            Change = Profit_for_month - previous_month
            Monthly_Changes.append(Change)
            if Change > Max_Change:
                Max_Change = Change
                Max_Change_Month = Name_of_month
            if Change < Min_Change:
                Min_Change = Change
                Min_Change_Month = Name_of_month
        previous_month = Profit_for_month

#print(Monthly_Changes)
output = ""
output += "Financial Analysis\n"
output += "---------------------------------\n"
output += f"Total Months: {Month_Count}\n"
output += f"Total: ${Net_Total}\n"
output += f"Average Change: ${round(sum(Monthly_Changes)/len(Monthly_Changes),2)}\n"
output += f"Greatest Increase in Profits: {Max_Change_Month} (${Max_Change})\n"
output += f"Greatest Decrease in Profits: {Min_Change_Month} (${Min_Change})\n"
print (output)

#Create txt file
with open(output_path,mode="w") as budget_output:
    budget_output.write(output)
