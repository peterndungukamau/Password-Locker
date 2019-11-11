#!/usr/bin/env python3.6
from credentials import Credentials

print("Hello! Welcome to Password Locker app where passwords are found")

# login in to password locker application with username and password
print("Do you own an Account?If Yes kindly enter your username below")
user_name = input()
print("Password")
password_locker = input()
print("login successful")
print(f"Welcome {user_name} How may i help you?")

print("Do you have an existing account? Yes or No?")
have_account = input()
if have_account == "yes":
    proceed =True
    print("Enter Your Account name and password")
    print("Enter Account Name")
    account_name = input()
    print("Enter Password")
    password = input()
    user_credentials = Credentials(account_name, password)
    Credentials.credential_list.append(user_credentials)
    print(user_credentials)
    while proceed:
        print("Do you have other accounts?")
        no_account = input()
        if no_account == "no":
            proceed= False
        else:
            print("Enter Account Name")
            account_name = input()
            print("Enter Password")
            password = input()


    # account_name = input()
    # password = input()








