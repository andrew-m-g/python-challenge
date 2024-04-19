# import modules
import os
import csv
# read/write path
csvpath = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')
analysis_path = os.path.join('..', 'PyBank', 'analysis', 'analysis.txt')
#set up variables to store total dollars, number of months, changes, etc
total_dollars = 0
total_months = 0
previousDoller = 0
changes = []
decreaseChange = {
    'name': '',
    'value': float('inf')
}
increaseChange = {
    'name': '',
    'value': float('-inf')
}

with open(csvpath, 'r') as csvFile:
    readfile = csv.reader(csvFile)
    next(readfile)
        # for loop to count rows  and add up gaines/loses

    for row in readfile:
        total_months += 1
        dollers = int(row[1])
        total_dollars += dollers
        
        if total_months > 1:
            change = dollers - previousDoller
            changes.append(change)
        

            if change < decreaseChange['value']:
                decreaseChange['value'] = change
                decreaseChange['name'] = row[0]
            if change > increaseChange['value']:
                increaseChange['value'] = change
                increaseChange['name'] = row[0]

        previousDoller = dollers
aveDollchge = sum(changes)/len(changes)

# create variable to store print out of election results

analysis = "Financial Analysis\n"
analysis += "--------------------------\n"
analysis += f'Total Months: ${total_months}\n'
analysis += f'Total: ${total_dollars}\n'
analysis += f'Average Change: ${aveDollchge}\n'
analysis += f"Greatest Increase: ({increaseChange['name']}) ${increaseChange['value']}\n"
analysis += f"Greatest Decrease: ({decreaseChange['name']}) ${decreaseChange['value']}\n"


print(analysis)
# Create Text File with analysis

# export path
with open(analysis_path, 'w') as outputFile:
    outputFile.write(analysis)

