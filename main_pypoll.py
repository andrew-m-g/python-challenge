# import os module
import os
# module to read csv
import csv
#read/ write path

csvpath = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')
analysis_path = os.path.join('..', 'PyPoll', 'analysis', 'analysis.txt')

#set variables to count votes and dictonaries to track canidates
total_votes = 0
canidates = {}

#for loop to open csv fil
with open(csvpath, 'r') as csvFile:
    readfile = csv.reader(csvFile)
    next(readfile)
    # for loop to count votes and intake canidate names
    for row in readfile:
        total_votes += 1


        try:
            canidates[row[2]] += 1
        except:
            canidates[row[2]] = 1
#set up dictionary to store winner
winner = {
    'name': '',
    'value': 0
}
# create variable to store print out of election results
analysis = "Election Result\n"
analysis += "--------------------------\n"
analysis += f'Total Votes: {total_votes}\n'
analysis += "--------------------------\n"
for name, total in canidates.items():
    if total > winner['value']:
        winner['value'] = total
        winner['name'] = name
    analysis += f"{name}: {round((total/total_votes)*100, 2)}% {total}\n"
analysis += "--------------------------\n"    
analysis += f"Winner: ({winner['name']})\n"
analysis += "--------------------------\n"


# Create Text File with analysis
print(analysis)
with open(analysis_path, 'w') as outputFile:
    outputFile.write(analysis)