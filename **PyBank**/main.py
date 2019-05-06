import csv


path = '/Users/moutasemakkad/Desktop/HomeWorks/python-challenge/budget_data.csv'


with open(path, 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
 

    header = next(csvreader)



    totalMonth = 0
    totalProfitAndLoss = 0

    # Average Change

    totalChange = 0
    

    #The greatest increase in profits (date and amount) over the entire period

    greatestIncrease = 0

    #   The greatest decrease in losses (date and amount) over the entire period


    greatesDecrease = 100000000000

    
    # previous number

    previousnumber = 0



    for row in csvreader:
        
        totalMonth += 1
        totalProfitAndLoss += int(row[1])
        change = int(row[1]) - previousnumber
        totalChange += change
        
        

        if (int(row[1]) - previousnumber) > greatestIncrease:
            greatestIncrease = (int(row[1]) - previousnumber)

        if (int(row[1]) - previousnumber) < greatesDecrease:
            greatesDecrease = (int(row[1]) - previousnumber)
        
        previousnumber = int(row[1])

    print('totalmonth:', ' ', totalMonth)
    print('total Profit and Loss: ',totalProfitAndLoss)
    print('Average', totalChange/totalMonth-1 * 100)
    print('Greatest Decrease ', greatesDecrease)
    print('Greates Increase ',greatestIncrease)
        

 