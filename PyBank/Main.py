#to create file paths across operating systems
import os
## Module for reading CSV files
import csv

# Set path for file
csvpath = os.path.join(".","Resources","PyBank_budget_data.csv")
with open(csvpath) as revenueData:
    reader = csv.reader(revenueData, delimiter=",")
    for row in reader:
        print(row)