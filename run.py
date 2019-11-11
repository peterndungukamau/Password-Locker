#!/usr/bin/env python3.6
from credentials import Credentials

print("Hello! Welcome to Password Locker app where passwords are found")

# login in to password locker application with username and password
print("kindly enter your firstname as your username below and choose a password")
user_name = input()
print("Password")
password_locker = input()
print("login successful You have an account")
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
        print("Do you have other accounts?Yes or No")
        no_account = input()
        if no_account == "no":
            proceed= False
        else:
            print("Enter Account Name")
            account_name = input()
            print("Enter Password")
            password = input()









