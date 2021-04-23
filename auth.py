import random
import validation
import database
from getpass import getpass
# bank operation

# initializing the system


""" database = {
    3458712354:['Ib', 'ade', 'ib@yahoo.com', 'password', 5000]
} """ 

def init():

    ''' isValidOptionSelected = False
    print("Welcome to Bank HP")

    while isValidOptionSelected == False:
        haveAccount = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))
        if haveAccount == 1:
            isValidOptionSelected = True
            login()
        elif haveAccount == 2:
            isValidOptionSelected = True
            register()
        else:
            print("You have selected invalid option") '''
    
    print("Welcome to Bank HP")

    haveAccount = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))
    if haveAccount == 1:
        login()
    elif haveAccount == 2:
        register()
    else:
        print("You have selected invalid option")
        init()
        
def login():
    # username or email and password
    # print("Login to your account")
    print("******** Login ********")

    ''' isLoginSuccessful = False

    while isLoginSuccessful == False:
        accountNumberFromUser = int(input("Enter your account number \n"))
        password = input("Enter your password \n")

        for accountNumber, userDetails in database.items():
            if accountNumber == accountNumberFromUser:
                if userDetails[3] == password:
                    isLoginSuccessful = True
        
        print("Invalid account or password") '''


    account_number_from_user = int(input("Enter your account number \n"))
    is_valid_account_number = validation.account_number_validation(account_number_from_user)

    if is_valid_account_number:
        # password = input("Enter your password \n")
        password = getpass("Enter your password \n")

        user = database.authenicate_user(account_number_from_user, password)
        if user:
            bankOperation(user)


        """ for accountNumber, userDetails in database.items():
            if accountNumber == int(account_number_from_user):
                if userDetails[3] == password:
                    bankOperation(userDetails) """
    
        print("Invalid account or password") 
        login()
    else:
        print("Account number invalid, check to see if you have up to 10 digits number")
        init()


def register():
    # - username, password, email
    # - generate user id
    print("********** Register **********")
    email = input("Enter your email address \n")
    fname = input("Enter your first name \n")
    lname = input("Enter your last name \n")
    password = getpass("Choose a password for yourself \n")

    try:
        account_number = generationAccountNumber()
    except ValueError:
        print("Account failed due to internet connectivity")
        init()

    # database[accountNumber] = [fname, lname, email, password, 0.0]
    # is_user_created = database.create(account_number, [fname, lname, email, password, 0.0])
    # prepared_user_detail = fname + "," + lname + "," + email + "," + password + "," + str(0.0)
    is_user_created = database.create(account_number, fname, lname, email, password)

    if is_user_created:
        print("Account created successfully")
        print("== ==== ====== ====== ===== ===== ==")
        print("Your account number is %d" % account_number)
        print("Make sure you keep it safe")
        print("== ==== ====== ====== ===== ===== ==")
        login()
    else:
        print("Error while creating account. Please try again")
        register()

def bankOperation(user):
    print("Welcome %s %s " % (user[0], user[1]) )

    selectedOption = int(input("What will you like to do? \n (1) Deposit \n (2) Withdraw \n (3) Logout \n (4) Exit \n"))

    if (selectedOption == 1):
        deposit()
    elif (selectedOption == 2):
        withdrawal()
    elif (selectedOption == 3):
        login()
    elif (selectedOption == 4):
        exit()
    else:
        print("Invalid option selected")
        bankOperation(user)

def withdrawal(): 
    print("Withdrawal")
    # get current balance
    # get amount to withdraw
    # check if its greater than the amount to be withdrawn
    # deduct amount from current balance
    # display current balance 

def deposit(): 
    print("Deposit")
    # get current balance
    # get amount to deposit
    # add deposited amount to current balance
    # display current balance 

    # u can ask if they wanted to perfom another operation again

def generationAccountNumber():
    return random.randrange(1111111111, 9999999999)

def logout(): 
    login()


### Actual Banking System ###
# print(generationAccountNumber())
init()