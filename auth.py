import random
# bank operation

# initializing the system


database = {} # dictionary

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


    accountNumberFromUser = int(input("Enter your account number \n"))
    password = input("Enter your password \n")

    for accountNumber, userDetails in database.items():
        if accountNumber == accountNumberFromUser:
            if userDetails[3] == password:
                bankOperation(userDetails)
    
    print("Invalid account or password") 

    login()

def register():
    # - username, password, email
    # - generate user id
    print("********** Register **********")
    email = input("Enter your email address \n")
    fname = input("Enter your first name \n")
    lname = input("Enter your last name \n")
    password = input("Choose a password for yourself \n")

    accountNumber = generationAccountNumber()
    database[accountNumber] = [fname, lname, email, password]

    # return database
    print("Account created successfully")
    print("== ==== ====== ====== ===== ===== ==")
    print("Your account number is %d" % accountNumber)
    print("Make sure you keep it safe")
    print("== ==== ====== ====== ===== ===== ==")
    login()

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

def deposit(): 
    print("Deposit")

def generationAccountNumber():
    return random.randrange(1111111111, 9999999999)

def logout(): 
    login()


### Actual Banking System ###
# print(generationAccountNumber())
init()