import os
import csv
cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))


budgetdata_csv = "budget_data.csv"
totalMonth = 0
totalProfit_Losses = 0
previousProfit_Losses = 0
Profit_Losses_Change = 0
Profitloss_change_list = []
month_change = []
greatestIncrease = 0
greatestDecrease = 9999999999999999

with open(budgetdata_csv) as profit_lossData:
    reader = csv.DictReader(profit_lossData)
    # loop through the data 
    # At initial stage you should take previousProfit_Losses as first row
    # So skip the first row
    index = 0
    for row in reader :
        if (index==0):
            totalMonth+=1
            totalProfit_Losses = totalProfit_Losses + int(row["Profit/Losses"])
            previousProfit_Losses = int(row["Profit/Losses"])
            month_change = month_change + [row["Date"]]
            index+=1
            continue

        # the total number of months included in the dataset 

        totalMonth = totalMonth + 1

        # The net total amount of "Profit/Losses" over the entire period
        totalProfit_Losses = totalProfit_Losses +int(row["Profit/Losses"])
        Profit_Losses_Change = int(row["Profit/Losses"]) - previousProfit_Losses
        Profitloss_change_list.append(Profit_Losses_Change)
        previousProfit_Losses = int(row["Profit/Losses"])
        month_change = month_change + [row["Date"]]

        greatestDecrease = min(Profitloss_change_list)
        greatestIncrease = max(Profitloss_change_list)

        # We have to add 1 because month associated with change is the next month
        greatestDecrease_month = Profitloss_change_list.index(greatestDecrease) + 1
        greatestIncrease_month = Profitloss_change_list.index(greatestIncrease) + 1
        print("Finacial Analysis")

        print("----------------------")

        print(f"Total Months:{totalMonth}\n")

        print(f"Total Profit/Losses: ${totalProfit_Losses}\n")

        print(f"Average Change: ${round(sum(Profitloss_change_list)/len(Profitloss_change_list),2)}")

        print(f"Greatest Increase in Profits: {month_change[greatestIncrease_month]} (${(str(greatestIncrease))}")

        print(f"Greates Decrease in Profits: {month_change[greatestDecrease_month]} (${(str(greatestDecrease))}")

