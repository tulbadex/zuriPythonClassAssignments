import datetime
import random

database = {
    1232341234 : {
        'fname': 'ibrahim',
        'lname': 'ade',
        'password': 'passwordIbrahim',
        'balance': 5000
     },
     1232341233 : {
        'fname': 'mike',
        'lname': 'arin',
        'password': 'passwordMike',
        'balance': 5000
     },
     1232341235 : {
        'fname': 'tunde',
        'lname': 'akeke',
        'password': 'passwordTunde',
        'balance': 5000
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


def account_number_validation(account_number):
    # check if account number is not empty
    # check if account number is 10 digits
    # check if the account number is an interger
    if account_number:
        if len(str(account_number)) == 10:
            try:
                int(account_number)
                return True
            except ValueError:
                print("Account number should contains number only")
                return False
        else:
            print("Account number can not be more or less than 10 digits")
            return False
    else:
        print("Account number is a required field")
        return False


def register():
    # - username, password, email
    # - generate user id
    print("********** Register **********")
    fname = input("Enter your first name \n")
    lname = input("Enter your last name \n")
    password = input("Choose a password for yourself \n")

    accountNumber = generationAccountNumber()

    """ try:
        accountNumber = generationAccountNumber()
    except ValueError:
        print("Account failed due to internet connectivity")
        init() """

    database[accountNumber] = {
        'fname':fname, 
        'lname': lname, 
        'password': password,
        'balance': 0.0  
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
    is_valid_account_number = account_number_validation(accountNumberFromUser)
    if is_valid_account_number:
        password = input("Your password? \n")
    

    for accountNumber, userDetails in database.items():
        # print(accountNumber)
        # print(userDetails['password'])
        if(accountNumber == int(accountNumberFromUser)):
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
    if(withdraw and (withdraw > 0)):
        print('Take your cash')
    else:
        print('You can not withdraw a negative value of #%d' % withdraw)
    login()

def deposit(): 
    deposit = int(input('How much would you like to deposit? '))
    if(deposit and (deposit > 0)):
        print('Current balance is #%d' % deposit)
    else:
        print('You can not deposit a negative value of #%d' % deposit)
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

def set_current_balance(user, balance):
    user['balance'] = balance

def get_current_balance(user):
    return user['balance']


init()