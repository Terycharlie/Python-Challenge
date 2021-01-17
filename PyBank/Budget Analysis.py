#to create file paths across operating systems
import os
# Module for reading CSV files
import csv

#Declare file location
csvpath = "PyBank/budget_data.csv"

#Declare Variables

profit = []
months = []
profit_change = []



#open the csv file
with open(csvpath) as csvData:
    reader = csv.reader(csvData, delimiter=",")
   
    # Skip header labels
    header = next(reader)

#loop through the rows
    for row in reader:
        #Append the total months and total PL to their corresponding lists
        months.append(row[0])
        profit.append(int(row[1])
    #iterate through profits to get monthly change
    #for row in reader:
        #Append the total months and total PL to their corresponding lists
        #months.append(row[0])
        #profit.append(int(row[1])
    #iterate through profits to get monthly change
    for i in range(len(profit)-1)
        #Take the difference beteen the months and append monthly profit change 
        profit_change.append(profit[i+1]-profit[i])    
    
#get max & min for the monthly profit change list
max_inc = max(profit_change)
max_dec = min(profit_change)

#correlate max and min to the proper month  
month_inc_max = profit_change.index(max(profit_change))+1
month_dec_max = profit_change.index(max(profit_change))+1

#iterate through the rows in the
for row in reader:
    #append the total months and total profit
    months.append(row[0])
    profit.append(int(row[1]))
    #iterate through the profits to get monthly change
for i in range(len(profit)-1):
 #Take the difference beteen the months and append monthly profit change 
        profit_change(profit[i+1]-profit[i])    
    
#get max & min for the monthly profit change list
max_inc = max(profit_change)
max_dec = min(profit_change)

#correlate max and min to the proper month  
#use +1 to for the next month
month_inc_max = profit_change.index(max(profit_change))+1
month_dec_max = profit_change.index(max(profit_change))+1

#printing
print("FINANCIAL ANALYSIS")
print("====================")
print(f"TOTAL MONTHS: {len(months)}")
print(f"TOTAL: ${sum(profit)}")
print(f"AVERAGE CHANGE: {round(sum(profit_change)/len(profit-change),2)}")
print(f"GREATEST INCREASE IN PROFITS: {months[month_inc_max]} (${str(max_inc))})")
print(f"GREATEST DECREASE IN PROFITS: {months[month_dec_max]} (${str(max_dec))})")
