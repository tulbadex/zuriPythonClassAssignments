# create record
# update record
# read record
# delete record
# search for user

import os
import validation

user_db_path = "data/user_record/"

def create(user_account_number, fname, lname, email, password):
    # print("create a user record")
    prepared_user_detail = fname + "," + lname + "," + email + "," + password + "," + str(0.0)

    if account_number_exist(user_account_number):
        return False

    if dose_email_exist(email):
        print("User already exist")
        return False

    completion_status = False
    try:
        f = open(user_db_path+ str(user_account_number) + ".txt", "x")
    except FileExistsError:
        record_data = read(user_db_path+ str(user_account_number) + ".txt")
        if not record_data:
            delete(user_account_number)
        print("User already exist")
        # delete(account_number)
        return completion_status
    else:
        f.write(str(prepared_user_detail))
        completion_status = True
    finally:
        f.close()
        return completion_status
    


def update(user_account_number):
    print("Update user record")
    # find user with the account details
    # fetch the content of the file
    # update the content of the file
    # save the file
    # return true

def read(user_account_number):
    # print("View user record")
    is_valid_account_number = validation.account_number_validation(user_account_number)

    try:
        if is_valid_account_number:
            
            f = open(user_db_path+ str(user_account_number) + ".txt", "r")
        else:
            f = open(user_db_path+ user_account_number, "r")

    except FileNotFoundError:
        print("User not find")
    except FileExistsError:
        print("User doesn't exist")
    except TypeError:
        print("Invalid account number format")
    else:
        return f.readline()
    
    return False
    # find user with the account details
    # fetch the content of the file

def delete(user_account_number):
    # print("Delete user record")
    # find user with the account details
    # delete the user record(file)
    # return true

    is_delete_status = False
    if os.path.exists(user_db_path + str(user_account_number) + '.txt'):
        try:
            os.remove(user_db_path + str(user_account_number) + '.txt')
            is_delete_status = True
        except FileNotFoundError:
            print("User not found")
        finally:
            return is_delete_status

def dose_email_exist(email):
    all_users = os.listdir(user_db_path)
    for user in all_users:
        # print(user)
        # print(read(user))
        # print(str.split(read(user), ','))
        user_list = str.split(read(user), ',')
        if email in user_list:
            return True
    return False

def account_number_exist(account_number):
    all_users = os.listdir(user_db_path)
    for user in all_users:
        if user == str(account_number) + '.txt':
            return True
    return False


def authenicate_user(account_number, password):
    if account_number_exist(account_number):
        user = str.split(read(account_number), ',')
        if password == user[3]:
            return user
    return False

# create(3458712354, ['Ib', 'ade', 'ib@yahoo.com', 'password', 5000])
# delete(3458712354)
# print(read(2182466375))
dose_email_exist('ib@yahoo.com')