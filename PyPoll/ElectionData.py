#to create file paths across operating systems
import os
# Module for reading CSV files
import csv

#Declare file location
csvpath = "PyPoll/Election Data.csv"

#Declare Variables
candidates = []
vote_numbers = []
vote_percentages = []
vote_total = 0
#open the csv file
with open(csvpath) as csvData:
    reader = csv.reader(csvData, delimiter=",")

    header = next(reader)
    for row in reader:
        #add vote counter
        vote_total +=1
        if row[2] not in candidates:
        #Append the candidates to the list
            candidates.append(row[2])
            index = candidates.index(row[2])
            vote_numbers.append(1)
        else:
            index = candidates.index(row[2])
            vote_numbers[index] += 1

    # to add a list for the vote percentages
    for votes in vote_numbers:
        #calculate the %
        percentage = (votes/vote_total)*100
        percentage = round(percentage)
        #format the %
        percentage ="%.3f%%" %percentage
        #append % to the list
        vote_percentages.append(percentage)


    # winning candidate
    winner= max(vote_numbers)
    index = vote_numbers.index(winner)
    winning_candidate = candidates[index]

#print results
print("Election Results")
print("-------------------")
print(f"Total Votes: {str(vote_total)}")
print("--------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(vote_percentages[i])} ({str(vote_numbers[i])})")
print("----------------------")
print(f"WINNER: {winning_candidate}")

#exporting text
output_file = open ("output.txt","w")
a = "Election Results"
b = "-----------------"
c = str(f"Total Votes: {str(vote_total)}")
d = "-----------------"
output_file.write('{}\n{}\n{}\n{}\n'.format(a,b,c,d))
for i in range (len(candidates)):
    e = str(f"{candidates[i]}: {str(vote_percentages[i])} ({str(vote_numbers[i])})")
    output_file.write('{}\n'.format(e))
f = "-------------------"
g = str(f"winner: {winning_candidate}")
h = "----------------------------------"
output_file.write('{}\n{}\n{}\n'.format(f,g,h))

