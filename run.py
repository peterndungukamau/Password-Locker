#!/usr/bin/env python3.6
import os

import pyperclip
from credentials import Credentials

print("Hello! Welcome to Password Locker app where passwords are found")

# login in to password locker application with username and password
print("kindly enter your firstname as your username below and choose a password")
user_name = input()
print("Password")
password_locker = input()
print("You have successful created  an account")
print(f"Welcome {user_name} How may i help you?")

print("Do you have an existing account? Yes or No?")
have_account = input()


def generate_password(self):
        '''

         generate password
        '''

        return os.urandom(8)


if have_account == "Yes":
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
        if no_account == "No":
            proceed= False
        else:
            print("Enter Account Name")
            account_name = input()
            print("Enter Password")
            password = input()

    print("Create new Account")
    accept = input()
    if accept == "Yes":
        print("Enter Account Name")
        acc = input()
    print("Would You like us to generate a Password for you or input?Yes or No?")
    gen = input()
    if gen == "Yes":
        print(user_credentials)










