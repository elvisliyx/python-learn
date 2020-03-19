# -*- coding:utf-8 -*-

import getpass

account = ['elvis','1234']
lock = []

count = 0
while count <3:
    user_name = input("Please enter your name:")
    if user_name in lock:
        print("Your account is locked!")
        break
    elif user_name in account:
        password = input("Please enter your password:")
        if password in account:
            print("Welcome to backup!")
            break
        else:
            print("password is error")
    else:
        print("Please enter the correct user!")
        break
    count +=1
    if count == 3:
        lock.append(user_name)
        countine_confirm = input("do you want to keep guessing..?")
        if countine_confirm != 'n':
            count = 0

# print(account[1])


