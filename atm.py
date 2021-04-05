import datetime

name = input("What is your name? \n")
allowedUsers = ['seyi', 'mike', 'tunde']
allowedPassword = ['passwordSeyi', 'passwordMike', 'passwordTunde']

        
if name in allowedUsers:
    password = input("Your password? \n")
    userId = allowedUsers.index(name)

    if password == allowedPassword[userId]:
        today = datetime.datetime.now()
        currentDate = today.strftime("%d %B, %Y")
        currentTime = today.strftime("%I:%M%p")
        print("\nDate and Time :", currentDate, currentTime)
        print('\nWelcome %s' % name)
        print('\nThese are the available options')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Complaint')

        selectedOption = int(input('Please select an option: '))

        if(selectedOption == 1):
            withdraw = int(input('How much would you like to withdraw? '))
            if(withdraw):
                print('Take your cash')
            pass
        elif(selectedOption == 2):
            deposit = int(input('How much would you like to deposit? '))
            if(deposit):
                print('Current balance is #%d' % deposit)
            pass
        elif(selectedOption == 3):
            complaint = input('What issue will you like to report? ')
            if(complaint):
                print('Thank you for contacting us')
            pass
        else:
            print('Invalid option selected, please try again! ')
    else:
        print('Incorrect password, please try again!')

else:
    print("Name not found, please try again!")
