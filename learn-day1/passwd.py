# -*- coding:utf-8 -*-

import getpass    #隐藏用户输入的密码

_username = 'elvis'
_password = '1234'


username = input("username:")
# password = getpass.getpass("password:")
password = input("password:")

if _username == username and _password == password:
    print("Welcome user {name} login..".format(name=username))
else:
    print("Invalid username or password")


# print(username,password)



