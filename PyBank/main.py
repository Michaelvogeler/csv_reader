import csv
import os

budget_csv = "Resources/budget_data.csv"
#budget_csv = os.path.join("..", "Resources", "budget_data.csv")
date_column = []
profit_column = []
profit_changes = []

row_counter = 0
total_profit = 0
average_change = 0
greatest_decrease_date = ""
greatest_decrease_profit = 0
greatest_increase_date = ""
greatest_increase_profit = 0

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    for row in csvreader:
        date_column.append(row[0])
        profit_column.append(row[1])

csvfile.close()

# Remove headers
date_column.pop(0)
profit_column.pop(0)

# Convert strings to integers
profit_column = [eval(i) for i in profit_column]

#Make calculations
total_months = len(date_column)
print(total_months)

total_profit = sum(profit_column)
print(total_profit)


#change = profit - previous_profit
#total_change += change
for i in range(1, len(profit_column)):
    change = profit_column[i] - profit_column[i-1]
    profit_changes.append(change)
print(profit_changes)
average_change = sum(profit_changes) / len(profit_changes)
print(average_change)
# average_change = total_profit/total_months
# print(average_change)

# print(date_column[0])
# print(profit_column[0])
# for element in date_column:
#     # print(element, end=" ")



# while(row_counter < len(date_column)):
#     print(f"{date_column[row_counter]} | {profit_column[row_counter]}")
#     row_counter += 1

# Finding the Greatest Increase and Greatest Decrease in Profits with Dates
for i in range(0, len(profit_column)-1):
    change = profit_column[i + 1] - profit_column[i]
    if change > greatest_increase_profit:
        greatest_increase_profit = change
        greatest_increase_date = date_column[i+1]
    elif change < greatest_decrease_profit:
        greatest_decrease_profit = change
        greatest_decrease_date = date_column[i+1]

print("Greatest increase in profits:", greatest_increase_date, greatest_increase_profit)
print("Greatest decrease in profits:", greatest_decrease_date, greatest_decrease_profit)



print(f"""
        Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_profit}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {greatest_increase_date} {greatest_increase_profit}
Greatest Decrease in Profits: {greatest_decrease_date} {greatest_decrease_profit}
      """)
