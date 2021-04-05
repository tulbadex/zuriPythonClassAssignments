''' voice = "Shout |"
print(voice * 5) '''

name = input("What is your name? \n")
allowedUsers = ['seyi', 'mike', 'tunde']
allowedPassword = ['passwordSeyi', 'passwordMike', 'passwordTunde']
# allowedPassword = "password"

""" if name in allowedUsers:
    password = input("Your password? \n")

    if password == allowedPassword:
        print('Welcome %s' % name)
    else:
        print('Incorrect password, please try again!')

else:
    print("Name not found, please try again!") """
        
if name in allowedUsers:
    password = input("Your password? \n")
    userId = allowedUsers.index(name)

    if password == allowedPassword[userId]:
        print('Welcome %s' % name)
        print('These are the available options')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Complaint')

        selectedOption = int(input('Please select an option: '))

        if(selectedOption == 1):
            print('You selected %d' % selectedOption)
            pass
        elif(selectedOption == 2):
            print('You selected %d' % selectedOption)
            pass
        elif(selectedOption == 3):
            print('You selected %d' % selectedOption)
            pass
        else:
            print('Invalid option selected, please try again! ')
    else:
        print('Incorrect password, please try again!')

else:
    print("Name not found, please try again!")
