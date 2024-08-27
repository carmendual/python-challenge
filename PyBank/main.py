import os
import csv

# variables
total_months = 0
total_profit_loss = 0
previous_profit_loss = None  # Track changes
max_increase = float('-inf')  
min_decrease = float('inf')  
max_increase_date = None
min_decrease_date = None
previous_profit_loss = 0
changes = []
dates = []

# relative directory path
script_dir = os.path.dirname(__file__)

# Join the current directory with the relative directory
budget_csv = os.path.join(script_dir, '/Users/carmendee/Desktop/python-challenge/PyBank/Resources/budget_data.csv')

# Open the CSV file in read mode
with open(budget_csv, 'r') as csvfile:
    
# create CSV reader object
    csv_reader = csv.reader(csvfile)

# Skip the header row (if present)
    next(csv_reader)

# Process each row after skipping the header
    for row in csv_reader:
        current_profit_loss = float(row[1])
        
        # Calculate total months and profit/loss by counting each line item to get total months
        # and getting the sum of profit/loss in row[1] index
        total_months += 1
        total_profit_loss += current_profit_loss
        
        # Calculate changes in profits/losses   
        if previous_profit_loss != 0:
            change = int(row[1]) - previous_profit_loss
            changes.append(change)
            dates.append(row[0])
        previous_profit_loss = int(row[1])

# Find the greatest increase in profits 
max_increase = max(changes)

# Find the date corresponding to the greatest increase value
max_increase_date = dates[changes.index(max_increase)]

# Find the greatest decrease in profits
min_decrease = min(changes)

# Find the date corresponding to the greatest decrease value
min_decrease_date = dates[changes.index(min_decrease)]

# Calculate average change
average_change = sum(changes) / len(changes)

# Print out the results
print(f"-------------------------------------------------------------")
print(f"Financial Analysis")
print(f"-------------------------------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss:,.2f}")
print(f"Average Change: ${average_change:,.2f}")
print(f"Greatest Increase in Profits: {max_increase_date} (${max_increase:,.2f})")
print(f"Greatest Decrease in Profits: {min_decrease_date} (${min_decrease:,.2f})")
print(f"---------------------------------------------------------------")

# Set variables for output file
# Define the relative directory path
relative_output_dir = '/Users/carmendee/Desktop/python-challenge/PyBank/analysis'

# Join the current directory with the relative directory
analysis_output = os.path.join(script_dir, '/Users/carmendee/Desktop/python-challenge/PyBank/analysis')

# Write the results into the PyBank Financial Analysis.txt file
with open(analysis_output, "w") as output_csv_file:
    output_csv_file.write("Financial Analysis\n")
    output_csv_file.write("-------------------------------------------------------------\n")
    output_csv_file.write(f"Total Months: {total_months}\n")
    output_csv_file.write(f"Total: ${total_profit_loss:,.2f}\n")
    output_csv_file.write(f"Average Change: ${round(average_change,2)}\n")
    output_csv_file.write(f"Greatest Increase in Profits: {max_increase_date} (${max_increase:,.2f})\n")
    output_csv_file.write(f"Greatest Decrease in Profits: {min_decrease_date} (${min_decrease:,.2f})\n")
    output_csv_file.write("-------------------------------------------------------------\n")
