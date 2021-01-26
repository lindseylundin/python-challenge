# import libraries
import csv, os
# read csv
csv_path = os.path.join("Resources", "budget_data.csv")
# open file to read, read in rows, break all rows up by columns using comma
with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
#Initialize List 
    date_list = []
    pl_list = []
# Loop through every list (row) starting at index 0 because that first value of each list (row) is all we want in our date_list
    for row in csvreader:
        date_list.append(row[0])   # every row at index 0, .append puts it in the date_list for us
        pl_list.append(int(row[1]))   # had to put int to make the answer an integer instead of string so we can add them
 
#Find month count, or total number of months  
    month_count = len(date_list)

# Net total    
    pl_sum = sum(pl_list)
       
# definte change_list as list
    change_list = []
    
    for x in range(1, len(pl_list)):
        
        change_list.append(int(pl_list[x] - pl_list[x-1]))
# calculate current row minus previous row to get the change value 
        
# total the values in change_list
    total_change = sum(change_list)
    
    
# find the average of those changes    
    average_change = round(total_change/(month_count-1),2)
    
# find the max value in change_list
    max_change = max(change_list)
    
# find the min value of the change_list
    min_change = min(change_list)

# Set index for calling the corresponding date for the min and max profit/loss change    
    date_max_change = change_list.index(max(change_list))+1
    date_min_change = change_list.index(min(change_list))+1
        
# Print Financial Analysis in script
    print('Financial Analysis')
    print('-------------------')
    print(f'Total Months: {month_count}')
    print(f'Total: ${pl_sum}')
    print(f'Average Change: ${average_change}')
    print(f'Greatest Increase in Profits: {date_list[date_max_change]} ${max_change}')

#tell computer where to create the new file
txtpath_out = os.path.join('analysis', 'budget_analysis.txt')
#what type the new file should be
with open(txtpath_out, 'w', newline='') as txtfile:
#we need to tell it  how to write on the file
    txtfile.write(f'Financial Analysis\n'
                  f'------------------\n'
                  f'Total Months: {month_count}\n' f'Total: ${pl_sum}\n' 
                  f'Average Change: ${average_change}\n' 
                  f'Greatest Increase in Profits: {date_list[date_max_change]} ${max_change}\n' 
                  f'Greatest Decrease in Profits: {date_list[date_min_change]} ${min_change}\n')