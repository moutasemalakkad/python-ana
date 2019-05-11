import csv
path = '/Users/moutasemakkad/Desktop/HomeWorks/python-challenge/budget_data.csv'

with open(path, 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
 
    header = next(csvreader)
    first_row = next(csvreader)
    totalMonth = 1
    totalProfitAndLoss = int(first_row[1])

    # Average Change
    totalChange = 0
    

    #The greatest increase in profits (date and amount) over the entire period
    greatestIncrease = 0

    #   The greatest decrease in losses (date and amount) over the entire period
    greatestDecrease = 100000000000

    
    # previous number
    previousnumber = int(first_row[1])

    # Max Month
    maxMonth = ''

    # Min Month 
    minMonth = ''

    #list
    listt = []


    for row in csvreader:
        totalMonth += 1
        totalProfitAndLoss += int(row[1])

        change = int(row[1]) - previousnumber
        totalChange += change
        listt.append(change)
        listtLength = len(listt)
        listtSum = sum(listt)
        

        if (int(row[1]) - previousnumber) > greatestIncrease:
            greatestIncrease = (int(row[1]) - previousnumber)
            maxMonth = row[0]

        if (int(row[1]) - previousnumber) < greatestDecrease:
            greatestDecrease = (int(row[1]) - previousnumber)
            minMonth = row[0]
        
        previousnumber = int(row[1])






    print("")
    print('total months:', ' ', totalMonth)
    print("")
    print('total Profit and Loss: ',totalProfitAndLoss)
    print("")
    print('Average Change', totalChange/listtLength * 100)
    #print('Average Change', listtSum/totalMonth * 100)
    print("")
    print('Greatest Decrease ',  f' ({minMonth})', greatestDecrease)
    print("")
    print('Greates Increase ', f' ({maxMonth})', greatestIncrease)
    print("")
        

 