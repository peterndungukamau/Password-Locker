#!/usr/bin/env python3.6
import os

import pyperclip
from credentials import Credentials


def generate_password():
    '''

     generate password
    '''

    return os.urandom(8)

print("Hello! Welcome to Password Locker app where passwords are found")
print("****** Use Yes or No as shortcodes to navigate*****************")

# login in to password locker application with username and password
print("kindly enter your firstname as your username below and choose a password")
user_name = input()
print("Password")
password_locker = input()
print("You have successful created  an account Hurray! You have an account kindly proceed")
print(f"Welcome {user_name} How may i help you?")

print("Do you have an existing account? *****Reply Yes  *****")
have_account = input()
if have_account == "Yes":
    proceed =True
    print("***** Enter Your Account name and password *****")
    print("Enter Account Name")
    account_name = input()
    print("Enter Password")
    password = input()
    user_credentials = Credentials(account_name, password)
    Credentials.credential_list.append(user_credentials)
    print(user_credentials)
    while proceed:
        print("Do you have other accounts?***** Yes or No *****")
        no_account = input()
        if no_account == "No":
            proceed= False
        else:
            print("Enter Account Name")
            account_name = input()
            print("Enter Password")
            password = input()

    print("Create new Account and choose or Generate Password")
    accept = input()

    if accept == "Yes":
        print("Enter Account Name")
        acc = input()
    print("Would You like us to generate a Password for you or input?***** Yes or No? *****")
    gen = input()
    if gen == "Yes":
        gen_pass = str(generate_password())
        print("Password generated is " + gen_pass)
        # cred = Credentials(acc, gen_pass)
        # Credentials.credential_list.append(cred)

    print("********* Here are your accounts*****************")
    for list_accounts in Credentials.credential_list:
        print(list_accounts)

    print("Do You wish to delete account? Yes Or No")
    doaway = input()

    if doaway == "Yes":
     print("Enter account Name")
    goo = input()
    print(Credentials.credential_list.clear())

    print("You account has been deleted successfully")

    print("Copyright@2019. Thanks For Using Password-Locker APP.")










