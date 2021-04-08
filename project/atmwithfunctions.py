import datetime
import random

database = {
    1232341234 : {
        'fname': 'ibrahim',
        'lname': 'ade',
        'password': 'passwordIbrahim'
     },
     1232341233 : {
        'fname': 'mike',
        'lname': 'arin',
        'password': 'passwordMike'
     },
     1232341235 : {
        'fname': 'tunde',
        'lname': 'akeke',
        'password': 'passwordTunde'
     },
} # dictionary

def init():
    
    print("Welcome to Bank HP")

    haveAccount = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))
    if haveAccount == 1:
        login()
    elif haveAccount == 2:
        register()
    else:
        print("You have selected invalid option")
        init()


def register():
    # - username, password, email
    # - generate user id
    print("********** Register **********")
    fname = input("Enter your first name \n")
    lname = input("Enter your last name \n")
    password = input("Choose a password for yourself \n")

    accountNumber = generationAccountNumber()
    database[accountNumber] = {
        'fname':fname, 
        'lname': lname, 
        'password': password
    }

    # return database
    print("Account created successfully")
    print("== ==== ====== ====== ===== ===== ==")
    print("Your account number is %d" % accountNumber)
    print("Make sure you keep it safe")
    print("== ==== ====== ====== ===== ===== ==")
    login()


def login():
    # username or email and password
    # print("Login to your account")
    print("******** Login ********")

    # name = input("What is your name? \n")
    accountNumberFromUser = int(input("Enter your account number \n"))
    password = input("Your password? \n")

    for accountNumber, userDetails in database.items():
        # print(accountNumber)
        # print(userDetails['password'])
        if(accountNumber == accountNumberFromUser):
            # print("This is ur account number ", accountNumber)
            if(userDetails['password'] == password):
                bankOperation(userDetails)
                # print(userDetails)
                # print(userDetails['password'])
    
    print("Invalid account or password") 

    login()

def bankOperation(user):
    print("\nWelcome %s %s " % (user['fname'], user['lname']) )
    today = datetime.datetime.now()
    currentDate = today.strftime("%d %B, %Y")
    currentTime = today.strftime("%I:%M%p")
    print("\nDate and Time :", currentDate, currentTime)

    selectedOption = int(input("\nWhat will you like to do? \n (1) Deposit \n (2) Withdraw \n (3) Complaint \n (4) Logout \n (5) Exit \n"))

    if (selectedOption == 1):
        deposit()
    elif (selectedOption == 2):
        withdrawal()
    elif (selectedOption == 3):
        complaint()
    elif (selectedOption == 4):
        login()
    elif (selectedOption == 5):
        exit()
    else:
        print("Invalid option selected")
        bankOperation(user)

def withdrawal(): 
    withdraw = int(input('How much would you like to withdraw? '))
    if(withdraw):
        print('Take your cash')
    login()

def deposit(): 
    deposit = int(input('How much would you like to deposit? '))
    if(deposit):
        print('Current balance is #%d' % deposit)
    login()
    

def complaint():
    complaint = input('What issue will you like to report? ')
    if(complaint):
        print('Thank you for contacting us')
    login()

def logout(): 
    login()

def generationAccountNumber():
    return random.randrange(1111111111, 9999999999)


init()