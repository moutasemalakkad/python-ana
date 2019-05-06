import csv

csvpath = '/Users/moutasemakkad/Desktop/HomeWorks/python-challenge/election_data.csv'


with open(csvpath, 'r', newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    header = next(csvreader)

    # total number of vote casts
    totalVoteCast = 0

    # A complete list of candidates who received votes
    receivedVotes = {}
    #receivedVotes = [row[2] for row in csvreader if row[2] not in receivedVotes.keys()]
    



    

    for row in csvreader:
        totalVoteCast += 1

        if str(row[2]) not in receivedVotes:
            receivedVotes[row[2]] = 1

        else:
            receivedVotes[row[2]] += 1

    
    print("")
    print("                    Election Results:")
   
    

    print('-------------------------------------------------')
    print("")
    print("")
    print('Total Votes: ', totalVoteCast)
    print("")
    print("")
    print('-------------------------------------------------')


    print("")
    print("")
    #------------------------------------------------------#
    maxVotes = 0
    winner = ''

    for voter in receivedVotes.keys():
        print(voter, f'( {receivedVotes[voter]/totalVoteCast * 100}% )' , ' : ', receivedVotes[voter])

        if receivedVotes[voter] > maxVotes:
            maxVotes = receivedVotes[voter]
            winner = voter


    print("")
    print("")

    print('-------------------------------------------------')

    print("")

    print('The Winner is: ', winner, ' with ', maxVotes, ' votes.')

    print("")
    print("")

    #------------------------------------------------------#

    






 

