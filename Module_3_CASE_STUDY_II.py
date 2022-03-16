
def telecalling():
    campaign_data = open('bank-data.csv','r')
    i = 1
    proflist=[]
    age=[]

    for data in campaign_data:
        data=data.split(',')
        if data[3]=='yes\n':
            age.append(data[0])
            if data[1] not in proflist:
                proflist.append(data[1])  
    campaign_data.close()

    proflist=set(proflist)
    age=set(age)

    print(" List of Jobs Eligible For Campaign:", proflist)
    print('Maximum age eligible for campaign:',max(age))
    print('Minimum age eligible for campaign:',min(age))
    
    client_prof = input('Enter client profession: ')

    if (client_prof in proflist):
        print ( "Go Ahead!!! Client is eligible and worthy for Tele Calling." )
    else:
        print("Skip !! *** Client Needs to be in one of these jobs",proflist) 
    
    
def main():
    print('''Welcome to tele calling.
             Please enter and key if u want to continue.
             If you wish to exit please Enter 'END'.''')
    s=input("Enter :")
    if s=='END':
        print("Thank you .Visit us Later.")
        exit()
    else:
        print('Welcome again!')
        telecalling()
        
while(1):
    main()
    
        
