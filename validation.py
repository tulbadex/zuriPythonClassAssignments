def account_number_validation(account_number):
    # check if account number is not empty
    # check if account number is 10 digits
    # check if the account number is an interger
    if account_number:
        
        try:
            int(account_number)

            if len(str(account_number)) == 10:
                return True

        except ValueError:
            # print("Account number should contains number only")
            return False
            
        except TypeError:
            return False

    return False

# def validate_registration_input(input):
    # check if it is a list
    # check each item in the list as the correct data type


""" if account_number:
        
        try:
            int(account_number)
            if len(str(account_number)) == 10:
                return True
            else:
                print("Account number can not be more or less than 10 digits")
                return False
        except ValueError:
            print("Account number should contains number only")
            return False
    else:
        print("Account number is a required field")
        return False """


""" if account_number:
        if len(str(account_number)) == 10:
            try:
                int(account_number)
                return True
            except ValueError:
                print("Account number should contains number only")
                return False
            except TypeError:
                print("Account number must be number only")
                return False
            return True
        else:
            # print("Account number can not be more or less than 10 digits")
            return False
        return True
    else:
        print("Account number is a required field")
        return False """