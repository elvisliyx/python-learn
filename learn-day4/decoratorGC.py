# -*- coding:utf-8 -*-

import time
user = "elvis"
passwd = "12345"

# def auth(func):
#     def wrapper(*args,**kwargs):
#         username = input("Username:").strip()
#         password = input("Password:").strip()
#         if user == username and passwd == password:
#             print("\033[32;1mUser has passwd authentication\033[0m")
#             # func(*args,**kwargs)
#             res = func(*args,**kwargs)
#             print("-----after authentication")
#             return res        #return func(*args,**kwargs)
#         else:
#
#             exit("\033[31;1mInvalid username or passwd\033[0m")
#     return wrapper

def auth(auth_type):
    print("auth func:",auth_type)
    def outer_wrapper(func):
        def wrapper(*args,**kwargs):
            print("wrapper func args:",*args,**kwargs)
            if auth_type == 'local':
                username = input("Username:").strip()
                password = input("Password:").strip()
                if user == username and passwd == password:
                    print("\033[32;1mUser has passwd authentication\033[0m")
                    # func(*args,**kwargs)
                    res = func(*args,**kwargs)
                    print("-----after authentication")
                    return res        #return func(*args,**kwargs)
                else:
                    exit("\033[31;1mInvalid username or passwd\033[0m")
            elif auth_type == 'ldap':
                print("over")
        return wrapper
    return outer_wrapper

# @auth
def index():
    print("welcome to index page")

@auth(auth_type="local")    #home = wrapper()
def home():
    print("welcome to home page")
    return "from home"

@auth(auth_type="ldap")
def bbs():
    print("welcome to bbs page")

index()
# home()
print(home())
bbs()

