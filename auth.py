import random
# bank operation

# initializing the system


database = {} # dictionary

def init():

    isValidOptionSelected = False
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
            print("You have selected invalid option")
        
def login():
    print("Login to your account")
    email = input("Enter your email address \n")
    password = input("Enter your password \n")
    bankOperation()

def register():
    print("********** Register **********")
    email = input("Enter your eamil address \n")
    fname = input("Enter your first name \n")
    lname = input("Enter your last name \n")
    password = input("Choose a password for yourself \n")

    accountNumber = generationAccountNumber()
    database[accountNumber] = [fname, lname, email, password]

    # return database
    print("Account created successfully")
    login()

def bankOperation():
    print("Some operations")

def generationAccountNumber():
    return random.randrange(1111111111, 9999999999)


### Actual Banking System ###
# print(generationAccountNumber())
init()